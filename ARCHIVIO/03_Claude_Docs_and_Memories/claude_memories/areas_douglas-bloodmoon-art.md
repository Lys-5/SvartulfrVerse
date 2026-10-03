---
name: douglas-bloodmoon-art
description: Character art generation for the Douglas-Bloodmoon werewolf kemonomimi family via PixAI — read for workflow, model settings, and character status
sources: [backfill]
aliases: [Douglas-Bloodmoon family]
---
- [stated] Creative worldbuilding project centered on a fictional family of werewolf kemonomimi characters, the Douglas-Bloodmoon family
- [stated] Produces character art for the family using the PixAI platform with a detailed, iterative technical workflow
- [stated] Prefers iterative testing before moving on to new characters
- [stated] Working toward a reusable fixed style block for generating family members consistently
Characters in focus
- [stated] Alyssa — female werewolf kemonomimi; prompt refinement completed
- [stated] Malachia — large, heavily scarred male werewolf with a stern presence and expressive wolf features; art recently begun
Technical workflow
- [stated] Uses Danbooru-style tag-based prompt structure (subject / pose / background / descriptors)
- [stated] Model stack: VXP_XL v2.2 Hyper with Niji semi realism LoRA (weight 0.75–0.85) and Add More Details LoRA (weight 0.3)
- [stated] Generation settings: CFG 1.6–2.0, Euler a sampler, 7–8 steps
- [stated] Uses Liquid9745VAE, chosen over SharpSpectrumVAEXL to avoid warm color casts
- [stated] Uses inpainting for edge artifact cleanup (denoising strength 0.5–0.7, steps 10–12) and for adding fine details like piercings
- [stated] Adds NSFW to the negative prompt when using certain tags
- [stated] Adds "feminine face, androgynous" to the negative prompt for male characters
- [stated] Tested the Niji6 Style-Mature Male LoRA for Malachia as an alternative to the semi realism LoRA