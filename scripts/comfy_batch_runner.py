import io
import json
import os
import random
import sys
import time
import urllib.parse
import requests

sys.stdout.reconfigure(encoding="utf-8")

COMFY_URL = "http://127.0.0.1:8188"
DEFAULT_CHECKPOINT = "CyberRealistic_PonySemi_V5.safetensors"
SEMIREAL_CHECKPOINT = "CyberRealistic_PonySemi_V5.safetensors"
ANIME_CHECKPOINT = "waiNSFWIllustrious_v150.safetensors"

STYLE_WESTERN_SEMIREAL_POS = (
    "score_9, score_8_up, score_7_up, semi-realistic, western digital painting, "
    "detailed painterly shading, realistic facial proportions, warm cinematic golden hour lighting, "
    "rich skin texture, expressive eyes, detailed hair, depth of field"
)

DEFAULT_NEGATIVE = (
    "score_6, score_5, score_4, worst quality, low quality, lowres, bad anatomy, bad hands, extra digits, "
    "fewer digits, extra arms, extra legs, fused fingers, mutated hands, deformed, blurry, watermark, signature, "
    "text, logo, censored, jpeg artifacts, rating_explicit, source_pony, source_anime, source_cartoon, "
    "anime, moe, big anime eyes, chibi, flat 2d, cel shading, cartoon, sketchy"
)


def _round_to_8(value: float) -> int:
    """Round pixel dimension to the nearest multiple of 8 required by SDXL VAEs."""
    return max(64, int(round(value / 8.0)) * 8)


def is_comfy_alive() -> bool:
    try:
        r = requests.get(f"{COMFY_URL}/system_stats", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def upload_reference_image(local_path: str) -> str:
    """Upload a local reference image to ComfyUI's input folder."""
    fname = os.path.basename(local_path)
    ext = os.path.splitext(fname)[1].lower()
    mime = "image/png" if ext == ".png" else "image/webp" if ext == ".webp" else "image/jpeg"
    with open(local_path, "rb") as f:
        r = requests.post(
            f"{COMFY_URL}/upload/image",
            files={"image": (fname, f, mime)},
            data={"overwrite": "true"},
            timeout=30,
        )
    r.raise_for_status()
    return r.json()["name"]


def build_workflow(
    positive: str,
    negative: str = DEFAULT_NEGATIVE,
    checkpoint: str = DEFAULT_CHECKPOINT,
    width: int = 832,
    height: int = 1216,
    steps: int = 30,
    cfg: float = 5.5,
    sampler_name: str = "dpmpp_2m_sde",
    scheduler: str = "karras",
    seed: int | None = None,
    clip_skip: int | None = -2,
    ref_image_names: list[str] | str | None = None,
    ipadapter_weight: float = 0.65,
    ipadapter_weight_type: str = "linear",
    ipadapter_start_at: float = 0.0,
    ipadapter_end_at: float = 0.85,
    ipadapter_embeds_scaling: str = "K+V",
    ipadapter_combine_embeds: str = "average",
    ipadapter_preset: str = "PLUS FACE (portraits)",
    ipadapter_mode: str = "standard",
    ipadapter_crop_position: str = "top",
    faceid_lora_strength: float = 0.6,
    faceid_weight_v2: float = 0.8,
    faceid_provider: str = "CPU",
    hires_upscaler: str | None = "4x_NickelbackFS_72000_G.pth",
    hires_scale: float = 1.5,
    hires_steps: int = 16,
    hires_cfg: float = 4.0,
    hires_denoise: float = 0.25,
    hires_use_ipadapter: bool = False,
    enable_face_detailer: bool = True,
    face_detailer_denoise: float = 0.35,
    enable_wrist_rune_detailer: bool = False,
    wrist_rune_image_name: str | None = None,
    wrist_rune_prompt: str | None = None,
    wrist_rune_weight: float = 0.35,
    wrist_rune_denoise: float = 0.35,
    wrist_rune_left_only: bool = True,
    lora_name: str | None = None,
    lora_strength_model: float = 0.80,
    lora_strength_clip: float = 0.80,
    style_ref_image_name: str | None = None,
    style_ref_image_names: list[str] | str | None = None,
    style_transfer_weight: float = 0.70,
    style_transfer_boost: float = 1.0,
    style_transfer_start_at: float = 0.0,
    style_transfer_end_at: float = 0.90,
    style_transfer_embeds_scaling: str = "V only",
    filename_prefix: str = "svartulfr",
    vae_name: str | None = None,
) -> dict:
    """Build a ComfyUI API workflow with optional LoRA, standard/FaceID IPAdapter, optional PreciseStyleTransfer, tiled Hires Fix, FaceDetailer, and optional Left-Wrist Rune Detailer."""
    if seed is None:
        seed = random.randint(1, 2**32 - 1)

    refs = [ref_image_names] if isinstance(ref_image_names, str) else list(ref_image_names or [])
    if style_ref_image_names:
        style_refs = (
            [style_ref_image_names]
            if isinstance(style_ref_image_names, str)
            else list(style_ref_image_names)
        )
    elif style_ref_image_name:
        style_refs = [style_ref_image_name]
    else:
        style_refs = []

    ckpt_model_ref = ["1l", 0] if lora_name else ["1", 0]
    ckpt_clip_ref = ["1l", 1] if lora_name else ["1", 1]
    base_model_ref = ["12", 0] if refs else ckpt_model_ref
    model_ref = ["18", 0] if style_refs else base_model_ref
    vae_ref = ["1v", 0] if vae_name else ["1", 2]
    clip_ref = ["2", 0] if clip_skip is not None else ckpt_clip_ref

    wf = {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": checkpoint},
        },
        **(
            {
                "1l": {
                    "class_type": "LoraLoader",
                    "inputs": {
                        "model": ["1", 0],
                        "clip": ["1", 1],
                        "lora_name": lora_name,
                        "strength_model": lora_strength_model,
                        "strength_clip": lora_strength_clip,
                    },
                }
            }
            if lora_name
            else {}
        ),
        **(
            {"1v": {"class_type": "VAELoader", "inputs": {"vae_name": vae_name}}}
            if vae_name
            else {}
        ),
        **(
            {
                "2": {
                    "class_type": "CLIPSetLastLayer",
                    "inputs": {"clip": ckpt_clip_ref, "stop_at_clip_layer": clip_skip},
                }
            }
            if clip_skip is not None
            else {}
        ),
        "3": {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": clip_ref, "text": positive},
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": clip_ref, "text": negative},
        },
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1},
        },
        "6": {
            "class_type": "KSampler",
            "inputs": {
                "model": model_ref,
                "positive": ["3", 0],
                "negative": ["4", 0],
                "latent_image": ["5", 0],
                "seed": seed,
                "steps": steps,
                "cfg": cfg,
                "sampler_name": sampler_name,
                "scheduler": scheduler,
                "denoise": 1.0,
            },
        },
    }

    if refs:
        if ipadapter_mode == "faceid":
            if len(refs) == 1:
                wf["10"] = {"class_type": "LoadImage", "inputs": {"image": refs[0]}}
                ip_img_ref = ["10", 0]
            else:
                wf["10"] = {"class_type": "LoadImage", "inputs": {"image": refs[0]}}
                wf["10b"] = {"class_type": "LoadImage", "inputs": {"image": refs[1]}}
                wf["14"] = {
                    "class_type": "ImageBatch",
                    "inputs": {"image1": ["10", 0], "image2": ["10b", 0]},
                }
                ip_img_ref = ["14", 0]

            faceid_preset = ipadapter_preset if "FACEID" in ipadapter_preset.upper() else "FACEID PLUS V2"
            wf["11"] = {
                "class_type": "IPAdapterUnifiedLoaderFaceID",
                "inputs": {
                    "model": ckpt_model_ref,
                    "preset": faceid_preset,
                    "lora_strength": faceid_lora_strength,
                    "provider": faceid_provider,
                },
            }
            wf["12"] = {
                "class_type": "IPAdapterFaceID",
                "inputs": {
                    "model": ["11", 0],
                    "ipadapter": ["11", 1],
                    "image": ip_img_ref,
                    "weight": ipadapter_weight,
                    "weight_faceidv2": faceid_weight_v2,
                    "weight_type": ipadapter_weight_type,
                    "combine_embeds": ipadapter_combine_embeds,
                    "start_at": ipadapter_start_at,
                    "end_at": ipadapter_end_at,
                    "embeds_scaling": ipadapter_embeds_scaling,
                },
            }
        else:
            if len(refs) == 1:
                wf["10"] = {"class_type": "LoadImage", "inputs": {"image": refs[0]}}
                wf["13"] = {
                    "class_type": "PrepImageForClipVision",
                    "inputs": {
                        "image": ["10", 0],
                        "interpolation": "LANCZOS",
                        "crop_position": ipadapter_crop_position,
                        "sharpening": 0.05,
                    },
                }
                ip_img_ref = ["13", 0]
            else:
                wf["10"] = {"class_type": "LoadImage", "inputs": {"image": refs[0]}}
                wf["10b"] = {"class_type": "LoadImage", "inputs": {"image": refs[1]}}
                wf["13a"] = {
                    "class_type": "PrepImageForClipVision",
                    "inputs": {
                        "image": ["10", 0],
                        "interpolation": "LANCZOS",
                        "crop_position": ipadapter_crop_position,
                        "sharpening": 0.05,
                    },
                }
                wf["13b"] = {
                    "class_type": "PrepImageForClipVision",
                    "inputs": {
                        "image": ["10b", 0],
                        "interpolation": "LANCZOS",
                        "crop_position": ipadapter_crop_position,
                        "sharpening": 0.05,
                    },
                }
                wf["14"] = {
                    "class_type": "ImageBatch",
                    "inputs": {"image1": ["13a", 0], "image2": ["13b", 0]},
                }
                ip_img_ref = ["14", 0]

            wf["11"] = {
                "class_type": "IPAdapterUnifiedLoader",
                "inputs": {
                    "model": ckpt_model_ref,
                    "preset": ipadapter_preset,
                },
            }
            wf["12"] = {
                "class_type": "IPAdapterAdvanced",
                "inputs": {
                    "model": ["11", 0],
                    "ipadapter": ["11", 1],
                    "image": ip_img_ref,
                    "weight": ipadapter_weight,
                    "weight_type": ipadapter_weight_type,
                    "combine_embeds": ipadapter_combine_embeds,
                    "start_at": ipadapter_start_at,
                    "end_at": ipadapter_end_at,
                    "embeds_scaling": ipadapter_embeds_scaling,
                },
            }

    if style_refs:
        for idx, sname in enumerate(style_refs):
            wf[f"15_{idx}"] = {
                "class_type": "LoadImage",
                "inputs": {"image": sname},
            }
            wf[f"16_{idx}"] = {
                "class_type": "PrepImageForClipVision",
                "inputs": {
                    "image": [f"15_{idx}", 0],
                    "interpolation": "LANCZOS",
                    "crop_position": "center",
                    "sharpening": 0.05,
                },
            }
        style_img_ref = ["16_0", 0]
        for idx in range(1, len(style_refs)):
            batch_id = f"16b_{idx}"
            wf[batch_id] = {
                "class_type": "ImageBatch",
                "inputs": {"image1": style_img_ref, "image2": [f"16_{idx}", 0]},
            }
            style_img_ref = [batch_id, 0]
        loader_17_inputs = {
            "model": base_model_ref,
            "preset": "PLUS (high strength)",
        }
        if refs:
            loader_17_inputs["ipadapter"] = ["11", 1]
        wf["17"] = {
            "class_type": "IPAdapterUnifiedLoader",
            "inputs": loader_17_inputs,
        }
        wf["18"] = {
            "class_type": "IPAdapterPreciseStyleTransfer",
            "inputs": {
                "model": ["17", 0],
                "ipadapter": ["17", 1],
                "image": style_img_ref,
                "weight": style_transfer_weight,
                "style_boost": style_transfer_boost,
                "combine_embeds": "average",
                "start_at": style_transfer_start_at,
                "end_at": style_transfer_end_at,
                "embeds_scaling": style_transfer_embeds_scaling,
            },
        }

    if hires_upscaler:
        target_w = _round_to_8(width * hires_scale)
        target_h = _round_to_8(height * hires_scale)
        wf["7"] = {
            "class_type": "VAEDecodeTiled",
            "inputs": {
                "samples": ["6", 0],
                "vae": vae_ref,
                "tile_size": 512,
                "overlap": 64,
                "temporal_size": 64,
                "temporal_overlap": 8,
            },
        }
        wf["20"] = {
            "class_type": "UpscaleModelLoader",
            "inputs": {"model_name": hires_upscaler},
        }
        wf["21"] = {
            "class_type": "ImageUpscaleWithModel",
            "inputs": {
                "upscale_model": ["20", 0],
                "image": ["7", 0],
            },
        }
        wf["22"] = {
            "class_type": "ImageScale",
            "inputs": {
                "image": ["21", 0],
                "upscale_method": "lanczos",
                "width": target_w,
                "height": target_h,
                "crop": "disabled",
            },
        }
        wf["23"] = {
            "class_type": "VAEEncodeTiled",
            "inputs": {
                "pixels": ["22", 0],
                "vae": vae_ref,
                "tile_size": 512,
                "overlap": 64,
                "temporal_size": 64,
                "temporal_overlap": 8,
            },
        }
        wf["24"] = {
            "class_type": "KSampler",
            "inputs": {
                "model": model_ref if hires_use_ipadapter else ckpt_model_ref,
                "positive": ["3", 0],
                "negative": ["4", 0],
                "latent_image": ["23", 0],
                "seed": seed,
                "steps": hires_steps,
                "cfg": hires_cfg,
                "sampler_name": sampler_name,
                "scheduler": scheduler,
                "denoise": hires_denoise,
            },
        }
        wf["25"] = {
            "class_type": "VAEDecodeTiled",
            "inputs": {
                "samples": ["24", 0],
                "vae": vae_ref,
                "tile_size": 512,
                "overlap": 64,
                "temporal_size": 64,
                "temporal_overlap": 8,
            },
        }
        final_image_ref = ["25", 0]
    else:
        wf["7"] = {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["6", 0], "vae": vae_ref},
        }
        final_image_ref = ["7", 0]

    if enable_face_detailer:
        wf["30"] = {
            "class_type": "UltralyticsDetectorProvider",
            "inputs": {"model_name": "bbox/face_yolov8m.pt"},
        }
        wf["31"] = {
            "class_type": "SAMLoader",
            "inputs": {
                "model_name": "sam_vit_b_01ec64.pth",
                "device_mode": "AUTO",
            },
        }
        wf["32"] = {
            "class_type": "FaceDetailer",
            "inputs": {
                "image": final_image_ref,
                "model": model_ref,
                "clip": clip_ref,
                "vae": vae_ref,
                "guide_size": 512,
                "guide_size_for": True,
                "max_size": 1024,
                "seed": seed,
                "steps": 18,
                "cfg": 4.0,
                "sampler_name": sampler_name,
                "scheduler": scheduler,
                "positive": ["3", 0],
                "negative": ["4", 0],
                "denoise": face_detailer_denoise,
                "feather": 5,
                "noise_mask": True,
                "force_inpaint": True,
                "bbox_threshold": 0.5,
                "bbox_dilation": 10,
                "bbox_crop_factor": 3.0,
                "sam_detection_hint": "center-1",
                "sam_dilation": 0,
                "sam_threshold": 0.93,
                "sam_bbox_expansion": 0,
                "sam_mask_hint_threshold": 0.7,
                "sam_mask_hint_use_negative": "False",
                "drop_size": 10,
                "bbox_detector": ["30", 0],
                "sam_model_opt": ["31", 0],
                "wildcard": "",
                "cycle": 1,
            },
        }
        final_image_ref = ["32", 0]

    if enable_wrist_rune_detailer and wrist_rune_image_name:
        if "31" not in wf:
            wf["31"] = {
                "class_type": "SAMLoader",
                "inputs": {
                    "model_name": "sam_vit_b_01ec64.pth",
                    "device_mode": "AUTO",
                },
            }
        default_rune_prompt = (
            "macro detailed anatomical human hand and inner wrist skin, "
            "small crisp dark charcoal cold-iron ink Elder Futhark rune tattoo neatly inscribed on the inner left wrist, "
            "natural fair matte skin texture, soft studio lighting, five natural fingers"
        )
        wf["40"] = {
            "class_type": "LoadImage",
            "inputs": {"image": wrist_rune_image_name},
        }
        wf["41"] = {
            "class_type": "PrepImageForClipVision",
            "inputs": {
                "image": ["40", 0],
                "interpolation": "LANCZOS",
                "crop_position": "pad",
                "sharpening": 0.1,
            },
        }
        loader_42_inputs = {
            "model": ckpt_model_ref,
            "preset": "PLUS (high strength)",
        }
        if style_refs:
            loader_42_inputs["ipadapter"] = ["17", 1]
        elif refs:
            loader_42_inputs["ipadapter"] = ["11", 1]
        wf["42"] = {
            "class_type": "IPAdapterUnifiedLoader",
            "inputs": loader_42_inputs,
        }
        wf["43"] = {
            "class_type": "IPAdapterAdvanced",
            "inputs": {
                "model": ["42", 0],
                "ipadapter": ["42", 1],
                "image": ["41", 0],
                "weight": wrist_rune_weight,
                "weight_type": "weak input",
                "combine_embeds": "average",
                "start_at": 0.0,
                "end_at": 0.65,
                "embeds_scaling": "V only",
            },
        }
        wf["44"] = {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": clip_ref, "text": wrist_rune_prompt or default_rune_prompt},
        }
        wf["45"] = {
            "class_type": "UltralyticsDetectorProvider",
            "inputs": {"model_name": "bbox/hand_yolov8s.pt"},
        }
        if wrist_rune_left_only:
            wf["46"] = {
                "class_type": "SEGSOrderedFilterDetailerHookProvider",
                "inputs": {
                    "target": "x1",
                    "order": True,
                    "take_start": 0,
                    "take_count": 1,
                },
            }
        fd_wrist_inputs = {
            "image": final_image_ref,
            "model": ["43", 0],
            "clip": clip_ref,
            "vae": vae_ref,
            "guide_size": 512,
            "guide_size_for": True,
            "max_size": 1024,
            "seed": seed,
            "steps": 18,
            "cfg": 4.5,
            "sampler_name": sampler_name,
            "scheduler": scheduler,
            "positive": ["44", 0],
            "negative": ["4", 0],
            "denoise": wrist_rune_denoise,
            "feather": 8,
            "noise_mask": True,
            "force_inpaint": True,
            "bbox_threshold": 0.4,
            "bbox_dilation": 44,
            "bbox_crop_factor": 2.5,
            "sam_detection_hint": "center-1",
            "sam_dilation": 16,
            "sam_threshold": 0.90,
            "sam_bbox_expansion": 32,
            "sam_mask_hint_threshold": 0.7,
            "sam_mask_hint_use_negative": "False",
            "drop_size": 10,
            "bbox_detector": ["45", 0],
            "sam_model_opt": ["31", 0],
            "wildcard": "",
            "cycle": 1,
        }
        if wrist_rune_left_only:
            fd_wrist_inputs["detailer_hook"] = ["46", 0]
        wf["47"] = {
            "class_type": "FaceDetailer",
            "inputs": fd_wrist_inputs,
        }
        final_image_ref = ["47", 0]

    wf["8"] = {
        "class_type": "SaveImage",
        "inputs": {"images": final_image_ref, "filename_prefix": filename_prefix},
    }

    return wf


def generate_image(
    out_path: str,
    positive: str,
    negative: str = DEFAULT_NEGATIVE,
    checkpoint: str = DEFAULT_CHECKPOINT,
    ref_image_path: list[str] | str | None = None,
    ipadapter_weight: float = 0.65,
    ipadapter_weight_type: str = "linear",
    ipadapter_start_at: float = 0.0,
    ipadapter_end_at: float = 0.85,
    ipadapter_embeds_scaling: str = "K+V",
    ipadapter_combine_embeds: str = "average",
    ipadapter_preset: str = "PLUS FACE (portraits)",
    ipadapter_mode: str = "standard",
    ipadapter_crop_position: str = "top",
    faceid_lora_strength: float = 0.6,
    faceid_weight_v2: float = 0.8,
    faceid_provider: str = "CPU",
    width: int = 832,
    height: int = 1216,
    steps: int = 30,
    cfg: float = 5.5,
    sampler_name: str = "dpmpp_2m_sde",
    scheduler: str = "karras",
    hires_upscaler: str | None = "4x_NickelbackFS_72000_G.pth",
    hires_scale: float = 1.5,
    hires_steps: int = 16,
    hires_cfg: float = 4.0,
    hires_denoise: float = 0.25,
    hires_use_ipadapter: bool = False,
    enable_face_detailer: bool = True,
    face_detailer_denoise: float = 0.35,
    enable_wrist_rune_detailer: bool = False,
    wrist_rune_image_name: str | None = None,
    wrist_rune_image_path: str | None = None,
    wrist_rune_prompt: str | None = None,
    wrist_rune_weight: float = 0.35,
    wrist_rune_denoise: float = 0.35,
    wrist_rune_left_only: bool = True,
    lora_name: str | None = None,
    lora_strength_model: float = 0.80,
    lora_strength_clip: float = 0.80,
    style_ref_image_name: str | None = None,
    style_ref_image_path: str | None = None,
    style_ref_image_names: list[str] | str | None = None,
    style_ref_image_paths: list[str] | str | None = None,
    style_transfer_weight: float = 0.70,
    style_transfer_boost: float = 1.0,
    style_transfer_start_at: float = 0.0,
    style_transfer_end_at: float = 0.90,
    style_transfer_embeds_scaling: str = "V only",
    seed: int | None = None,
    clip_skip: int | None = -2,
    vae_name: str | None = None,
    timeout_s: int = 600,
) -> str:
    """Queue a ComfyUI generation and save the final output image to out_path."""
    if isinstance(ref_image_path, list):
        ref_names = [upload_reference_image(p) for p in ref_image_path]
    elif ref_image_path:
        ref_names = [upload_reference_image(ref_image_path)]
    else:
        ref_names = None
    resolved_wrist_rune_name = wrist_rune_image_name
    if wrist_rune_image_path:
        resolved_wrist_rune_name = upload_reference_image(wrist_rune_image_path)
    if style_ref_image_paths:
        paths = (
            [style_ref_image_paths]
            if isinstance(style_ref_image_paths, str)
            else list(style_ref_image_paths)
        )
        resolved_style_names = [upload_reference_image(p) for p in paths]
    elif style_ref_image_path:
        resolved_style_names = [upload_reference_image(style_ref_image_path)]
    elif style_ref_image_names:
        resolved_style_names = (
            [style_ref_image_names]
            if isinstance(style_ref_image_names, str)
            else list(style_ref_image_names)
        )
    elif style_ref_image_name:
        resolved_style_names = [style_ref_image_name]
    else:
        resolved_style_names = None
    wf = build_workflow(
        positive=positive,
        negative=negative,
        checkpoint=checkpoint,
        width=width,
        height=height,
        steps=steps,
        cfg=cfg,
        sampler_name=sampler_name,
        scheduler=scheduler,
        seed=seed,
        clip_skip=clip_skip,
        vae_name=vae_name,
        lora_name=lora_name,
        lora_strength_model=lora_strength_model,
        lora_strength_clip=lora_strength_clip,
        ref_image_names=ref_names,
        ipadapter_weight=ipadapter_weight,
        ipadapter_weight_type=ipadapter_weight_type,
        ipadapter_start_at=ipadapter_start_at,
        ipadapter_end_at=ipadapter_end_at,
        ipadapter_embeds_scaling=ipadapter_embeds_scaling,
        ipadapter_combine_embeds=ipadapter_combine_embeds,
        ipadapter_preset=ipadapter_preset,
        ipadapter_mode=ipadapter_mode,
        ipadapter_crop_position=ipadapter_crop_position,
        faceid_lora_strength=faceid_lora_strength,
        faceid_weight_v2=faceid_weight_v2,
        faceid_provider=faceid_provider,
        hires_upscaler=hires_upscaler,
        hires_scale=hires_scale,
        hires_steps=hires_steps,
        hires_cfg=hires_cfg,
        hires_denoise=hires_denoise,
        hires_use_ipadapter=hires_use_ipadapter,
        enable_face_detailer=enable_face_detailer,
        face_detailer_denoise=face_detailer_denoise,
        enable_wrist_rune_detailer=enable_wrist_rune_detailer,
        wrist_rune_image_name=resolved_wrist_rune_name,
        wrist_rune_prompt=wrist_rune_prompt,
        wrist_rune_weight=wrist_rune_weight,
        wrist_rune_denoise=wrist_rune_denoise,
        wrist_rune_left_only=wrist_rune_left_only,
        style_ref_image_names=resolved_style_names,
        style_transfer_weight=style_transfer_weight,
        style_transfer_boost=style_transfer_boost,
        style_transfer_start_at=style_transfer_start_at,
        style_transfer_end_at=style_transfer_end_at,
        style_transfer_embeds_scaling=style_transfer_embeds_scaling,
        filename_prefix=os.path.splitext(os.path.basename(out_path))[0],
    )
    r = requests.post(f"{COMFY_URL}/prompt", json={"prompt": wf}, timeout=30)
    if not r.ok:
        raise RuntimeError(f"ComfyUI /prompt error {r.status_code}: {r.text[:500]}")
    prompt_id = r.json()["prompt_id"]

    t0 = time.time()
    while time.time() - t0 < timeout_s:
        hr = requests.get(f"{COMFY_URL}/history/{prompt_id}", timeout=15)
        if hr.ok and prompt_id in hr.json():
            entry = hr.json()[prompt_id]
            status_info = entry.get("status", {})
            if status_info.get("status_str") == "error":
                raise RuntimeError(f"ComfyUI workflow error for {prompt_id}: {status_info}")
            outputs = entry.get("outputs", {})
            for node_out in outputs.values():
                imgs = node_out.get("images", [])
                if imgs:
                    img_info = imgs[0]
                    params = urllib.parse.urlencode(
                        {
                            "filename": img_info["filename"],
                            "subfolder": img_info.get("subfolder", ""),
                            "type": img_info.get("type", "output"),
                        }
                    )
                    ir = requests.get(f"{COMFY_URL}/view?{params}", timeout=30)
                    ir.raise_for_status()
                    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
                    with open(out_path, "wb") as f:
                        f.write(ir.content)
                    return out_path
        time.sleep(1.5)

    raise TimeoutError(f"Timed out waiting for ComfyUI prompt {prompt_id}")


if __name__ == "__main__":
    print("ComfyUI alive:", is_comfy_alive())
