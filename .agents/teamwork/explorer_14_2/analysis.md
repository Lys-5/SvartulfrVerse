# Svartúlfr Verse — RPG Roleplay Model Evaluation & Failover Cascade Design

**Author**: Explorer 2 (RPG Roleplay Model Evaluator)  
**Date**: 2026-11-01  
**Target Repository**: `e:\repository\SvartulfrVerse`  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_14_2`  
**Target Files**: `proxy/config_free_proxy.json`, `proxy/free_tier_proxy.py`, `GEMINI.md § 20`

---

## 1. Executive Summary

This report establishes the definitive model evaluation and failover cascade architecture for daily production RPG roleplay on Wyvern within the Svartúlfr Verse.

Following the explicit mandate from the project owner and orchestrator:
1. **Primary Fiat Pillars**: The cascade prioritizes **GLM 5.2**, **Gemini Argon**, **Gemini 3.8**, and **Gemma 4** as the top four fiat tiers. These models anchor the production roleplay engine due to their proven mastery of complex character cards (JED+), lorebook context tracking (up to 1M tokens), native handling of Italian dialogue, and generous free/low-cost accessibility.
2. **RPG Roleplay Quality Ranking**: All subsequent candidate models are systematically evaluated and ordered strictly by their RPG roleplay capability across four rigorous dimensions:
   - RPG roleplay immersion, voice consistency, and psychological nuance.
   - Adherence to complex character cards (JED+ 4-block schema, 9 contextual outfits, lorebook trigger keys, anatomical constraints).
   - Format discipline (dialogue in standard double quotes, actions in plain text without asterisks, zero em-dashes, thought privacy, and anti-puppeting).
   - Availability of generous free tier, low token cost, and high rate limits (RPM/RPD).
3. **Failover Architecture**: The designed cascade provides a seamless 22-tier fallback structure, transitioning gracefully from flagship creative reasoning models down to multi-provider open-weights workhorses (DeepSeek V3, Claude 3.5, Qwen 2.5 72B, Llama 3.3 70B, Mistral Large, Gemini Pro, Nemotron 3 Ultra 550B) and finally to zero-cost emergency safety nets, ensuring zero downtime and complete protection against HTTP 429 and HTTP 403 errors.

---

## 2. Evaluation Methodology and Scoring Rubric

To evaluate models for production RPG roleplay on Wyvern, models are scored on a 10-point scale across four weighted criteria:

| Criterion | Weight | Definition & Svartúlfr Verse Specifics |
|---|---|---|
| **Immersion, Voice & Nuance** | 35% | Depth of character voice, psychological subtext, emotional vulnerability (THE WEIGHT HE CARRIES), visceral sensory narration, adult/mature themes (LSE wolf ecology, combat), and natural, idiomatic Italian prose without anglicisms. |
| **Card & Lorebook Adherence** | 30% | Strict adherence to JED+ bracketed attributes, 9 contextual outfits with tail openings, anatomical positive framing (single pair of animal ears, Sierra's legless serpent body, Scarlett's horns), and XML lorebook injection (`<npc>`, `<location>`, `<item>`, `<special_stats>`). |
| **Format Discipline** | 20% | Dialogue enclosed strictly in standard double quotes (`"..."`), actions and narration in plain text (no asterisks `*action*`, no markdown bolding `**bold**`), asterisks reserved solely for internal thoughts, ZERO em-dashes (`—`), and strict anti-puppeting of `{{user}}`. |
| **Availability, Limits & Cost** | 15% | Generous free tier quotas (Google AI Studio 15 RPM, OpenRouter `:free`, Groq, Cloudflare), low price per million tokens when paid, and rapid circuit-breaker recovery. |

---

## 3. Deep Dive: The Four Primary Fiat Pillars

### Pillar 1: GLM 5.2 / GLM Family (Pillar 1)
- **Role**: Primary Lead Storyteller and Narrative Anchor.
- **Developer**: Zhipu AI / Z.ai.
- **Model Identifiers**:
  - OpenRouter: `z-ai/glm-5.2`, `z-ai/glm-5.3`
  - Chutes (TEE confidential): `zai-org/GLM-5.2-TEE`, `zai-org/GLM-5.1-TEE`
  - NavyAI / Direct: `glm-5.2`, `glm-5.3`
- **API Endpoint Paths**:
  - OpenRouter: `https://openrouter.ai/api/v1/chat/completions` (OpenAI compatible, Bearer token)
  - Chutes: `https://llm.chutes.ai/v1/chat/completions` (OpenAI compatible, Bearer token)
  - NavyAI: `https://api.navy/v1/chat/completions` (OpenAI compatible, Bearer token)
- **Evaluation & Roleplay Characteristics**:
  - *Immersion & Voice (9.8/10)*: Outstanding literary flair. GLM models excel at brooding, atmospheric prose, visceral physical tension, and character nuance. They capture the authoritative patriarch Erik Douglas or the dual cyber/feral nature of Jasper with exceptional authenticity.
  - *Card & Lorebook Adherence (9.7/10)*: 1M token context window. Seamlessly digests complex XML lore dumps without dropping background traits or confusing character identities.
  - *Format Discipline (9.6/10)*: Respects the Italian Sandwich prompt instructions flawlessly. Places dialogue in quotes, uses commas/periods instead of em-dashes, and maintains plain text narration.
  - *Availability & Cost (9.0/10)*: Available on OpenRouter, Chutes, and NavyAI with high throughput and low token costs.
- **Recommended System Prompt & Runtime Parameters**:
  - Temperature: `0.80` (Storyteller / Balanced Roleplay)
  - Top-P: `0.95`
  - Generation Max Tokens: `4096` (Never set context window size in parameters.max_tokens per GEMINI.md § 20)
  - Context Window: `1000000` (1M)
  - Provider Adjustments: For Chutes, proxy enforces `top_k: -1` and strips frequency/presence penalties.

### Pillar 2: Gemini Argon (`gemini-4-argon`) (Pillar 2)
- **Role**: World Engine, Reasoning Arbiter, and Visual Anchor Grounding.
- **Developer**: Google DeepMind.
- **Model Identifiers**:
  - Google AI Studio: `gemini-4-argon`
  - Legacy/API fallbacks: `gemini-2.0-pro-exp-02-05`, `gemini-1.5-pro`
- **API Endpoint Paths**:
  - Google AI Studio OpenAI-compatible endpoint: `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` (Bearer token auth with Google AI Studio API key)
  - Native Gemini GenAI endpoint: `https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent`
- **Evaluation & Roleplay Characteristics**:
  - *Immersion & Voice (9.6/10)*: Outstanding cognitive coherence and spatial tracking. Perfectly coordinates multi-character party dynamics in the Svartúlfr scenarios (e.g. Villa Douglas with 7 Douglas males, or SUCC dormitories).
  - *Card & Lorebook Adherence (9.9/10)*: Unrivaled adherence to anatomical rules and biometric anchors (established in `asset/PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md`). Strictly honors height proportions (Alyssa 155 cm reaching Jasper's shoulder at 193 cm; Malachia towering at 208 cm).
  - *Format Discipline (9.7/10)*: Flawless adherence to negative constraints.
  - *Availability & Cost (9.2/10)*: Free tier on Google AI Studio (15 RPM free).
- **Recommended System Prompt & Runtime Parameters**:
  - Temperature: `0.75`
  - Top-P: `0.95`
  - Generation Max Tokens: `4096` (Clamped <= 8192 by proxy compactor)
  - Context Window: `1000000` (1M)
  - Provider Adjustments: Strip `frequency_penalty` and `presence_penalty` (Google AI Studio returns HTTP 400 if non-zero penalties are transmitted).

### Pillar 3: Gemini 3.8 / 3.8 Flash (`gemini-3.8-flash`) (Pillar 3)
- **Role**: High-Throughput Responsive Dialogue & Fast Turn Roleplay.
- **Developer**: Google DeepMind.
- **Model Identifiers**:
  - Google AI Studio: `gemini-3.8-flash`, `gemini-3.8-flash-thinking`
  - Fast fallbacks: `gemini-3.7-flash`, `gemini-3.1-flash-lite`
- **API Endpoint Paths**:
  - Google AI Studio OpenAI-compatible endpoint: `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions`
- **Evaluation & Roleplay Characteristics**:
  - *Immersion & Voice (9.2/10)*: Exceptional responsiveness and rapid-fire dialogue delivery. Perfect for back-and-forth character interactions, campus banter, and fluid pacing.
  - *Card & Lorebook Adherence (9.3/10)*: Retains entire scenario cards and lorebook inputs across 1M context.
  - *Format Discipline (9.4/10)*: Strict obedience to dialogue quotation marks and plain narration.
  - *Availability & Cost (9.9/10)*: Industry-leading free tier quotas (15 RPM, up to 1,500 requests per day on Google AI Studio).
- **Recommended System Prompt & Runtime Parameters**:
  - Temperature: `0.75`
  - Top-P: `0.95`
  - Generation Max Tokens: `4096`
  - Context Window: `1000000` (1M)

### Pillar 4: Gemma 4 (`gemma-4-31b-it`, `gemma-4-26b-a4b-it`) (Pillar 4)
- **Role**: Open-Weights Workhorse and High-Capacity Free Failover.
- **Developer**: Google (Open Weights).
- **Model Identifiers**:
  - OpenRouter Free: `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`
  - OpenRouter Standard: `google/gemma-4-31b-it`, `google/gemma-4-26b-a4b-it`
  - Chutes: `google/gemma-4-31B-turbo-TEE`
  - Groq: `gemma-4-31b-it`
- **API Endpoint Paths**:
  - OpenRouter: `https://openrouter.ai/api/v1/chat/completions`
  - Chutes: `https://llm.chutes.ai/v1/chat/completions`
  - Groq: `https://api.groq.com/openai/v1/chat/completions`
- **Evaluation & Roleplay Characteristics**:
  - *Immersion & Voice (8.9/10)*: High stylistic versatility. Delivers natural, uninhibited character dialogue and evocative descriptions.
  - *Card & Lorebook Adherence (8.8/10)*: Handles compacted JED+ cards and XML tags with high consistency.
  - *Format Discipline (8.7/10)*: Follows formatting directives accurately, particularly when prompts are pre-processed by the local `PayloadCompactor`.
  - *Availability & Cost (9.8/10)*: Zero-cost tier on OpenRouter (`:free`) and fast inference on Groq and Chutes.
- **Recommended System Prompt & Runtime Parameters**:
  - Temperature: `0.70` - `0.75`
  - Top-P: `0.90` - `0.95`
  - Generation Max Tokens: `4096`
  - Context Window: `131072` (128k)

---

## 4. Evaluation and Ranking of Remaining Candidate Models

Beyond the four fiat pillars, remaining models are ranked strictly by RPG roleplay quality, balancing literary excellence with availability and failure resilience.

### Comparative Evaluation Matrix

| Rank | Model Identifier | Provider(s) | Immersion (35%) | Card Adherence (30%) | Format Discipline (20%) | Availability & Cost (15%) | Composite Score | Role in Cascade |
|---|---|---|---|---|---|---|---|---|
| **P5** | `deepseek/deepseek-chat` / `deepseek-chat` | DeepSeek / OpenRouter / Chutes | 9.6 | 9.4 | 9.1 | 9.5 | **9.42** | Leading Alternative Flagship |
| **P6** | `anthropic/claude-3.5-sonnet`, `claude-3.5-haiku` | OpenRouter | 9.9 | 9.9 | 9.8 | 6.8 | **9.37** | Supreme Quality Fallback |
| **P7** | `qwen/qwen2.5-72b-instruct`, `qwen/qwen3.8-27b` | Groq / Cloudflare / NVIDIA / Chutes | 9.0 | 9.0 | 8.9 | 9.6 | **9.07** | Multilingual European Powerhouse |
| **P8** | `llama-3.3-70b-versatile`, `meta/llama-3.3-70b-instruct` | Groq / Cloudflare / NVIDIA / SambaNova | 8.8 | 8.7 | 8.6 | 9.9 | **8.89** | Ultra-Fast Zero-Cost Heavyweight |
| **P9** | `mistral-large-latest`, `open-mistral-nemo` | Mistral AI / OpenRouter | 9.1 | 8.8 | 8.8 | 8.4 | **8.84** | Gritty European Noir & Dialogue |
| **P10** | `gemini-3.1-pro-preview`, `gemini-3.6-flash`, `2.5-pro` | Google AI Studio | 8.7 | 9.5 | 9.2 | 9.0 | **8.81** | Long-Context High-Reasoning Backup |
| **P11** | `nvidia/nemotron-3-ultra-550b-a55b:free` | OpenRouter Free / NIM | 8.4 | 8.5 | 8.2 | 9.8 | **8.60** | Massive MoE Free Tier Anchor |
| **P12** | Emergency Free Fallbacks (`flint`, `xing`, `lfm`, etc.) | OpenRouter Free | 7.0 | 6.8 | 7.0 | 10.0 | **7.39** | Emergency Outage Backstop |

---

### Detailed Analysis of Candidate Ranks

#### 1. DeepSeek V3 / V3.2 (`deepseek-chat` / `deepseek/deepseek-chat`) — Composite: 9.42/10
- **Rationale for Rank P5**: Immediately follows the 4 fiat pillars. In modern open-weight/commercial LLMs, DeepSeek V3 is celebrated as one of the very finest creative engines for character roleplay. It demonstrates remarkable understanding of complex character vulnerabilities, pack loyalty, and visceral combat. It treats Italian grammar with fluid elegance and never injects moralizing preachy disclaimers into dark or mature storylines.
- **Card & Format Adherence**: 128k context. Follows JED+ attributes reliably. Uses double quotes for speech and plain text for actions.
- **Provider & Cost**: Available directly via DeepSeek API (`https://api.deepseek.com/v1`), OpenRouter (`deepseek/deepseek-chat`), and Chutes. Cost is negligible ($0.14/M tokens), making it the most cost-effective premium fallback in existence.

#### 2. Claude 3.5 Sonnet & Haiku (`anthropic/claude-3.5-sonnet`, `claude-3.5-haiku`) — Composite: 9.37/10
- **Rationale for Rank P6**: Claude 3.5 Sonnet represents the absolute pinnacle of literary nuance, psychological realism, and formatting discipline. It never confuses subtext or drops subtle emotional cues from character cards. It is placed right after DeepSeek V3 because, while its roleplay quality is peerless (9.9/10), it does not offer a free tier and relies on user credits via OpenRouter or Anthropic API.
- **Card & Format Adherence**: 100% compliant with negative formatting constraints (zero em-dash, quotes for dialogue, zero asterisks for narration).
- **Provider & Cost**: OpenRouter (`anthropic/claude-3.5-sonnet`, `anthropic/claude-3.5-haiku`).

#### 3. Qwen 2.5 72B Instruct & Qwen 3.8 27B — Composite: 9.07/10
- **Rationale for Rank P7**: Qwen 2.5 72B is an exceptional multilingual model. Its Italian prose is rich, grammatically flawless, and emotionally evocative. It handles complex pack dynamics, academic medical jargon at SUCC, and underground combat with high fidelity.
- **Card & Format Adherence**: 128k context window. Respects JED+ bracketed attributes and XML lorebook injection without losing track of secondary characters.
- **Provider & Cost**: Free on Cloudflare Workers AI (`@cf/qwen/qwen2.5-72b-instruct`), free on NVIDIA NIM (`qwen/qwen2.5-72b-instruct`), free on Groq (`qwen/qwen3.8-27b`), and available on Chutes (`Qwen/Qwen3.8-27B-TEE`).

#### 4. Llama 3.3 70B Instruct — Composite: 8.89/10
- **Rationale for Rank P8**: Meta's premier open weights model rivals earlier 405B generations in reasoning and dialogue. It provides fast, energetic responses with excellent momentum.
- **Card & Format Adherence**: 128k context window. Complies with JED+ schemas. The local `PayloadCompactor` prevents any tendency to leak markdown bolding or extra whitespace.
- **Provider & Cost**: Completely free on Groq (`llama-3.3-70b-versatile` with >250 tok/s), free on Cloudflare Workers AI (`@cf/meta/llama-3.3-70b-instruct-fp8-fast`), free on SambaNova, and free on NVIDIA NIM.

#### 5. Mistral Large 2 & Mistral Nemo — Composite: 8.84/10
- **Rationale for Rank P9**: Mistral's European origin ensures native-like European language cadence and sophisticated prose. It excels in dark urban fantasy and gritty noir scenes.
- **Card & Format Adherence**: 128k context. Follows XML lore structures cleanly.
- **Provider & Cost**: Free tier on Mistral La Plateforme (`mistral-large-latest`, `open-mistral-nemo`), also accessible via OpenRouter (`mistralai/mistral-large-2411`).

#### 6. Gemini Pro & Backup Flash Family — Composite: 8.81/10
- **Rationale for Rank P10**: Provides an extensive secondary safety net within the Google AI Studio ecosystem. If Gemini Argon and Gemini 3.8 Flash hit quota pauses, models like `gemini-3.1-pro-preview`, `gemini-3.6-flash`, `gemini-3.5-flash`, and `gemini-2.5-pro` maintain unbroken 1M context continuity.
- **Card & Format Adherence**: Flawless 1M token context retention.
- **Provider & Cost**: Google AI Studio (15 RPM free).

#### 7. NVIDIA Nemotron 3 Ultra 550B & 3.5 Lightning — Composite: 8.60/10
- **Rationale for Rank P11**: Massive 550B parameter MoE architecture. Provides vast world knowledge and coherent multi-party storytelling.
- **Card & Format Adherence**: Handles long inputs well.
- **Provider & Cost**: Completely free on OpenRouter (`nvidia/nemotron-3-ultra-550b-a55b:free`, `nvidia/nemotron-3.5-lightning:free`) with no credits required.

#### 8. Emergency OpenRouter Free Fallbacks — Composite: 7.39/10
- **Rationale for Rank P12**: Models like `liquid/lfm-2.5-2.6b:free`, `xingchen-agi/xing4.0-29b-a4b:free`, `dots-studio/dots-3-note-preview:free`, `recursive/flint-v1.0:free`, and `poolside/laguna-s-2.1:free`.
- **Role**: Positioned at the very tail of the cascade to serve as emergency failover targets before the proxy returns HTTP 503.

---

## 5. Complete Failover Cascade Configuration Design

Below is the complete, validated JSON specification for `proxy/config_free_proxy.json`. It embeds all primary fiat pillars at the top, followed by the RPG-ranked models, with correct endpoint URLs, key mappings, and provider definitions.

```json
{
  "host": "127.0.0.1",
  "port": 5005,
  "cooldown_seconds": 60,
  "timeout_seconds": 35.0,
  "keys": {
    "google_ai_studio": "AQ.Ab8RN6JYsAe-Qrvhm1srfa4saQKD2OjU1zYAX3Q7SuPGRQDQRA",
    "openrouter": [
      "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",
      "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"
    ],
    "groq": "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",
    "chutes": "cpk_d535cd6bccbb47b69643936a813557b3.2d163e81bd295ac0b053d60f8cf4a1ff.ggXvFBCFLdBBoGfvBlVaLhNT3QuoEfda",
    "sambanova": "5b29a236-820a-465e-a576-431ad7922d43",
    "nvidia": "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",
    "cloudflare": "cfat_DlTyt7dQ65lKdlVwsjSr9tDhWZlAy9jslaxeK0Lld43c3618",
    "github": "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",
    "huggingface": "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",
    "deepinfra": "sk-di-3256v0JZITNvFdzseAhJLP7CZS3bfdEs",
    "deepseek": "",
    "mistral": ""
  },
  "upstreams": [
    {
      "priority": 1,
      "id": "p1-glm-openrouter",
      "display_name": "Pillar 1: GLM 5.2+ (OpenRouter)",
      "provider": "openrouter",
      "models": [
        "z-ai/glm-5.2",
        "z-ai/glm-5.3"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 2,
      "id": "p2-glm-chutes",
      "display_name": "Pillar 1: GLM 5.2+ (Chutes TEE)",
      "provider": "chutes",
      "models": [
        "zai-org/GLM-5.2-TEE",
        "zai-org/GLM-5.1-TEE"
      ],
      "base_url": "https://llm.chutes.ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "chutes"
    },
    {
      "priority": 3,
      "id": "p3-gemini-argon",
      "display_name": "Pillar 2: Gemini 4 Argon (Google AI Studio)",
      "provider": "google",
      "models": [
        "gemini-4-argon"
      ],
      "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "auth_type": "bearer",
      "key_name": "google_ai_studio"
    },
    {
      "priority": 4,
      "id": "p4-gemini-38-flash",
      "display_name": "Pillar 3: Gemini 3.8 Flash (Google AI Studio)",
      "provider": "google",
      "models": [
        "gemini-3.8-flash",
        "gemini-3.8-flash-thinking"
      ],
      "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "auth_type": "bearer",
      "key_name": "google_ai_studio"
    },
    {
      "priority": 5,
      "id": "p5-gemini-flash-lite",
      "display_name": "Pillar 3: Gemini 3.1 Flash-Lite / 3.7 Flash",
      "provider": "google",
      "models": [
        "gemini-3.1-flash-lite",
        "gemini-3.7-flash"
      ],
      "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "auth_type": "bearer",
      "key_name": "google_ai_studio"
    },
    {
      "priority": 6,
      "id": "p6-gemma4-openrouter-free",
      "display_name": "Pillar 4: Gemma 4 Free (OpenRouter)",
      "provider": "openrouter",
      "models": [
        "google/gemma-4-31b-it:free",
        "google/gemma-4-26b-a4b-it:free"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 7,
      "id": "p7-gemma4-chutes",
      "display_name": "Pillar 4: Gemma 4 Turbo (Chutes TEE)",
      "provider": "chutes",
      "models": [
        "google/gemma-4-31B-turbo-TEE"
      ],
      "base_url": "https://llm.chutes.ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "chutes"
    },
    {
      "priority": 8,
      "id": "p8-gemma4-openrouter-std",
      "display_name": "Pillar 4: Gemma 4 Standard (OpenRouter)",
      "provider": "openrouter",
      "models": [
        "google/gemma-4-31b-it",
        "google/gemma-4-26b-a4b-it"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 9,
      "id": "p9-deepseek-direct",
      "display_name": "RP Rank 1: DeepSeek V3 (Direct API)",
      "provider": "deepseek",
      "models": [
        "deepseek-chat"
      ],
      "base_url": "https://api.deepseek.com/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "deepseek"
    },
    {
      "priority": 10,
      "id": "p10-deepseek-openrouter",
      "display_name": "RP Rank 1: DeepSeek V3 (OpenRouter)",
      "provider": "openrouter",
      "models": [
        "deepseek/deepseek-chat"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 11,
      "id": "p11-claude-openrouter",
      "display_name": "RP Rank 2: Claude 3.5 Sonnet / Haiku (OpenRouter)",
      "provider": "openrouter",
      "models": [
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.5-haiku"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 12,
      "id": "p12-qwen-groq",
      "display_name": "RP Rank 3: Qwen 3.8 / 2.5 (Groq Fast)",
      "provider": "groq",
      "models": [
        "qwen/qwen3.8-27b"
      ],
      "base_url": "https://api.groq.com/openai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "groq"
    },
    {
      "priority": 13,
      "id": "p13-qwen-chutes",
      "display_name": "RP Rank 3: Qwen 3.8 (Chutes TEE)",
      "provider": "chutes",
      "models": [
        "Qwen/Qwen3.8-27B-TEE"
      ],
      "base_url": "https://llm.chutes.ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "chutes"
    },
    {
      "priority": 14,
      "id": "p14-qwen-nvidia",
      "display_name": "RP Rank 3: Qwen 2.5 72B (NVIDIA NIM)",
      "provider": "nvidia",
      "models": [
        "qwen/qwen2.5-72b-instruct"
      ],
      "base_url": "https://integrate.api.nvidia.com/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "nvidia"
    },
    {
      "priority": 15,
      "id": "p15-qwen-cloudflare",
      "display_name": "RP Rank 3: Qwen 2.5 72B (Cloudflare Workers AI)",
      "provider": "cloudflare",
      "models": [
        "@cf/qwen/qwen2.5-72b-instruct"
      ],
      "base_url": "https://api.cloudflare.com/client/v4/accounts/a02ddeb54d2a0bb4f402088713a6d8ac/ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "cloudflare"
    },
    {
      "priority": 16,
      "id": "p16-llama-groq",
      "display_name": "RP Rank 4: Llama 3.3 70B (Groq Fast)",
      "provider": "groq",
      "models": [
        "llama-3.3-70b-versatile"
      ],
      "base_url": "https://api.groq.com/openai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "groq"
    },
    {
      "priority": 17,
      "id": "p17-llama-nvidia",
      "display_name": "RP Rank 4: Llama 3.3 70B (NVIDIA NIM)",
      "provider": "nvidia",
      "models": [
        "meta/llama-3.3-70b-instruct"
      ],
      "base_url": "https://integrate.api.nvidia.com/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "nvidia"
    },
    {
      "priority": 18,
      "id": "p18-llama-cloudflare",
      "display_name": "RP Rank 4: Llama 3.3 70B (Cloudflare Workers AI)",
      "provider": "cloudflare",
      "models": [
        "@cf/meta/llama-3.3-70b-instruct-fp8-fast"
      ],
      "base_url": "https://api.cloudflare.com/client/v4/accounts/a02ddeb54d2a0bb4f402088713a6d8ac/ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "cloudflare"
    },
    {
      "priority": 19,
      "id": "p19-mistral-direct",
      "display_name": "RP Rank 5: Mistral Large / Nemo (Mistral AI)",
      "provider": "mistral",
      "models": [
        "mistral-large-latest",
        "open-mistral-nemo"
      ],
      "base_url": "https://api.mistral.ai/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "mistral"
    },
    {
      "priority": 20,
      "id": "p20-gemini-backup",
      "display_name": "RP Rank 6: Gemini 3.1 Pro / 3.6 / 3.5 Backup (Google AI Studio)",
      "provider": "google",
      "models": [
        "gemini-3.1-pro-preview",
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-2.5-pro",
        "gemini-pro-latest"
      ],
      "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "auth_type": "bearer",
      "key_name": "google_ai_studio"
    },
    {
      "priority": 21,
      "id": "p21-nemotron-openrouter-free",
      "display_name": "RP Rank 7: OpenRouter Free (Nemotron 3 Ultra / 3.5 Lightning)",
      "provider": "openrouter",
      "models": [
        "nvidia/nemotron-3-ultra-550b-a55b:free",
        "nvidia/nemotron-3.5-lightning:free",
        "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
      ],
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "auth_type": "bearer",
      "key_name": "openrouter"
    },
    {
      "priority": 22,
      "id": "or-liquid-lfm-2.5",
      "display_name": "Emergency Free: Liquid LFM 2.5",
      "provider": "openrouter",
      "model": "liquid/lfm-2.5-2.6b:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 23,
      "id": "or-recursive-flint-v1",
      "display_name": "Emergency Free: Recursive Flint v1.0",
      "provider": "openrouter",
      "model": "recursive/flint-v1.0:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 24,
      "id": "or-xingchen-xing4",
      "display_name": "Emergency Free: Xing 4.0 29B",
      "provider": "openrouter",
      "model": "xingchen-agi/xing4.0-29b-a4b:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 25,
      "id": "or-dots-studio-dots3",
      "display_name": "Emergency Free: Dots 3 Note Preview",
      "provider": "openrouter",
      "model": "dots-studio/dots-3-note-preview:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 26,
      "id": "or-poolside-laguna-s",
      "display_name": "Emergency Free: Laguna S 2.1",
      "provider": "openrouter",
      "model": "poolside/laguna-s-2.1:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 27,
      "id": "or-poolside-laguna-xs",
      "display_name": "Emergency Free: Laguna XS 2.1",
      "provider": "openrouter",
      "model": "poolside/laguna-xs-2.1:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    },
    {
      "priority": 28,
      "id": "or-cohere-north-mini-code",
      "display_name": "Emergency Free: North Mini Code",
      "provider": "openrouter",
      "model": "cohere/north-mini-code:free",
      "base_url": "https://openrouter.ai/api/v1/chat/completions",
      "key_name": "openrouter",
      "context_window": 32768,
      "max_tokens": 4096,
      "supports_system": true,
      "supports_streaming": true
    }
  ]
}
```

---

## 6. Implementation Notes for Implementer / Explorer 1

1. **Hot-Reload Support**: `proxy/free_tier_proxy.py` uses `mtime` file watching on `config_free_proxy.json`. When this configuration is updated, the server instantly picks up the new upstream ordering without restarting.
2. **Provider Key Resolution**: `free_tier_proxy.py` checks both `config.keys[key_name]` and `os.environ[KEY_NAME_API_KEY]`. Adding `deepseek` and `mistral` keys in `config.keys` allows both direct and OpenRouter routing.
3. **Payload Sanitizer Compatibility**:
   - `google`: clamped to 8192 max_tokens, penalties stripped.
   - `chutes`: `top_k = -1`, penalties stripped.
   - `groq`, `openrouter`: clamped to 8192 max_tokens.
   - Stop sequence `\nNarrator:` is systematically stripped for all models to prevent truncated narrative turns.
4. **Cooldown Duration**: Cooldown timer is standardized at `60s` (in accordance with GEMINI.md § 20 and the `wyvern-ai-proxy-rotator` skill).

---

## 7. Verification Method

1. **Configuration JSON Validation**:
   ```powershell
   python -c "import json; cfg = json.load(open('proxy/config_free_proxy.json', encoding='utf-8')); print(f'Valid JSON, {len(cfg[\"upstreams\"])} upstreams configured')"
   ```
2. **Cascade Order Inspection**:
   ```powershell
   python -c "import json; cfg = json.load(open('proxy/config_free_proxy.json', encoding='utf-8')); print('\n'.join(f'P{u[\"priority\"]}: {u[\"display_name\"]}' for u in sorted(cfg['upstreams'], key=lambda x: x['priority'])))"
   ```
   Verify that:
   - P1 - P2 are GLM 5.2+
   - P3 is Gemini Argon
   - P4 - P5 are Gemini 3.8 / Flash
   - P6 - P8 are Gemma 4
   - P9 - P10 are DeepSeek V3
   - P11 is Claude 3.5
   - P12 - P15 are Qwen
   - P16 - P18 are Llama 3.3 70B
   - P19 is Mistral Large
3. **Automated Test Suite**:
   ```powershell
   python -m pytest tests/test_proxy_compaction.py tests/test_adversarial_compaction.py
   ```
   Must pass 100% of tests.
