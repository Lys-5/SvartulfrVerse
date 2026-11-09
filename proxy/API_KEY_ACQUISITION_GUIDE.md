# Svartúlfr Verse — Wyvern Failover Proxy API Key Audit & Acquisition Guide

**Target Component**: Local Failover Micro-Proxy (`proxy/free_tier_proxy.py`, `proxy/config_free_proxy.json`)  
**Architecture Version**: v1.6.0+ (Loopback `127.0.0.1:5005`, OpenAI-Compatible, 5-Phase Compactor)  
**Date**: November 2026  
**Status**: Production Roleplay Optimization  

---

## 1. Executive Summary & Configuration Audit

The Wyvern failover micro-proxy routes interactive roleplay requests through a multi-tier hierarchy of LLM providers. To prevent roleplay interruptions caused by rate limits (`HTTP 429`), temporary suspensions (`HTTP 403`), or depleted balances (`HTTP 402`), the proxy implements automatic circuit-breaker failover across 28+ model endpoints.

A comprehensive audit of local configuration files (`.env`, `proxy/config_free_proxy.json`, and runtime environment variables) was conducted. This guide provides a full inventory of active, missing, and depleted keys, accompanied by step-by-step instructions and direct developer console URLs to acquire all missing keys at **zero or minimal cost**.

### Key Findings Summary:
1. **Primary Fiat Pillars**:
   - **Google AI Studio**: Key configured and active, but Pro/Argon models are heavily constrained by free tier limits (2 RPM / 50 RPD). Adding 2–3 keys in an array solves this limitation.
   - **SambaNova Cloud**: Key configured and live-verified HTTP 200 on `gemma-4-31B-it`. Now wired directly into active upstream Priority 6.
   - **OpenRouter**: Two keys configured and active for `:free` models (including Gemma 4 and GLM 5.2/5.3).
   - **Zhipu AI (BigModel Direct)**: Currently blank. Adding a free trial key enables direct GLM 5.2/5.3 access with 25M free tokens.
2. **High-Value Missing RPG Providers**:
   - **DeepSeek Platform**: Missing. Grants 5M free tokens ($0.50–$1.00 credit); post-trial cost is the lowest worldwide ($0.14/1M tokens).
   - **Cerebras Cloud**: Missing. 100% free developer tier granting 1,000,000 tokens/day of Llama 3.3 70B at 2,000 tokens/sec.
   - **SiliconFlow (SiliconCloud)**: Missing. Grants 14–20 RMB free credit plus permanently free open-source models (0 deduction).
   - **Mistral AI**: Missing. Free developer tier (1 RPS / 60 RPM) for Mistral Large 2 and Mistral Nemo.
3. **Depleted / Deprecated Providers**:
   - **Chutes.ai**: Configured key has a negative balance ($-0.057), returning HTTP 402. Requires creating a new account or depositing a small balance.
   - **NVIDIA NIM & Cloudflare**: Model IDs updated to active non-deprecated slugs.
   - **GitHub Models**: Dormant key now wired into Priority 22 for Azure AI inference.

---

## 2. Master Key Audit & Status Matrix

| # | Provider Platform | Target Models | Env Variable Name | Local Config Status | Live Probe Status | Action Required |
|---|---|---|---|---|---|---|
| **1** | **Google AI Studio** | Gemini 4 Argon, Gemini 3.8 Flash, 3.1 Pro | `GOOGLE_AI_STUDIO_API_KEY` | Configured | **HTTP 200 OK** (Flash) / 429 (Pro) | Recommended: Add 2-3 keys for multi-key pooling |
| **2** | **Zhipu AI (BigModel)** | GLM 5.2, GLM 5.3, GLM-4-Plus, GLM-4-Flash | `ZHIPU_API_KEY` | **BLANK / MISSING** | Not configured | Obtain free 25M token trial key |
| **3** | **SambaNova Cloud** | Gemma 4 31B, Llama 3.3 70B, Qwen 2.5 72B | `SAMBANOVA_API_KEY` | Configured | **HTTP 200 OK** on `gemma-4-31B-it` | Key active; wired to active upstreams |
| **4** | **OpenRouter** | GLM 5.2/5.3, Gemma 4, Nemotron 3 Ultra, 14+ Free | `OPENROUTER_API_KEY` | Configured (2 keys) | **HTTP 200 OK** (Both keys active) | Fully operational |
| **5** | **DeepSeek Platform** | DeepSeek-V3 (671B MoE), DeepSeek-R1 | `DEEPSEEK_API_KEY` | **BLANK / MISSING** | Not configured | Obtain 5M free token trial key |
| **6** | **Groq Cloud** | Qwen 3.8 27B, GPT-OSS 120B, Llama 3.3 70B | `GROQ_API_KEY` | Configured | **HTTP 200 OK** on active models | Fully operational |
| **7** | **Cerebras Cloud** | Llama 3.3 70B (Wafer-Scale 2,000 t/s) | `CEREBRAS_API_KEY` | **BLANK / MISSING** | Not configured | Obtain 100% free 1M tokens/day key |
| **8** | **SiliconFlow** | DeepSeek-V3, Qwen 2.5 72B, GLM-4-9B (Free) | `SILICONFLOW_API_KEY` | **BLANK / MISSING** | Not configured | Obtain 14-20 RMB signup credit key |
| **9** | **Mistral AI** | Mistral Large 2, Mistral Small 3, Mistral Nemo | `MISTRAL_API_KEY` | **BLANK / MISSING** | Not configured | Obtain free developer experimentation key |
| **10** | **Chutes.ai** | GLM 5.2 TEE, Gemma 4 Turbo TEE, Qwen 3.8 TEE | `CHUTES_API_KEY` | Configured | **HTTP 402** (Depleted balance) | Create new account or deposit balance |
| **11** | **NVIDIA NIM** | Nemotron 3 Ultra 550B, Llama 3.1 Nemotron 70B | `NVIDIA_API_KEY` | Configured | **HTTP 200 OK** on catalog | Model slugs updated to active models |
| **12** | **Cloudflare Workers AI** | Llama 3.3 70B FP8 Fast, Qwen 2.5 72B | `CLOUDFLARE_API_KEY` | Configured | **HTTP 200 OK** on active models | Model slugs updated to active models |
| **13** | **GitHub Models** | GPT-4o, GPT-4o-mini, Llama 3.3 70B | `GITHUB_API_KEY` / `GITHUB_TOKEN` | Configured | Ready (DNS dependent) | Wired to Priority 22 upstream |
| **14** | **DeepInfra** | Llama 3.3 70B, Qwen 2.5 72B | `DEEPINFRA_API_KEY` | Configured | **HTTP 402** (Zero balance) | Optional backup |
| **15** | **Hugging Face** | Open-source inference backups | `HUGGINGFACE_API_KEY` | Configured | Standby | Optional backup |

---

## 3. Step-by-Step Acquisition Guide (Zero or Minimal Cost)

---

### 1. Zhipu AI / BigModel Open Platform (GLM 5.2 / GLM 5.3 Direct)
*The lead fiat storyteller. Renowned for rich literary prose, psychological depth, and complex lorebook tracking.*

* **Direct Console URL**: [https://open.bigmodel.cn/usercenter/apikeys](https://open.bigmodel.cn/usercenter/apikeys)
* **Zero/Minimal Cost Details**:
  * **Signup Bonus**: New registered accounts receive **25,000,000 free tokens** (25M tokens) or 20–50 RMB trial credit valid for 1 month upon phone verification.
  * **Permanently Free Model**: `glm-4-flash` is **100% free with unlimited total tokens** and up to 100 RPM concurrency.
  * **Post-Trial Cost**: Extremely economical (~$0.014 to $0.10 per 1M tokens).
* **Quotas & Limits**: 60–100 RPM, 1,000,000 TPM.
* **Signup Instructions**:
  1. Open [https://open.bigmodel.cn/](https://open.bigmodel.cn/) and click **Sign Up / Register**.
  2. Verify with SMS (supports international numbers).
  3. Navigate to **User Center > API Keys** ([https://open.bigmodel.cn/usercenter/apikeys](https://open.bigmodel.cn/usercenter/apikeys)).
  4. Click **Create API Key**, copy the key, and paste into `.env` as `ZHIPU_API_KEY=` or in `proxy/config_free_proxy.json` under `"keys.zhipu"`.

---

### 2. DeepSeek Open Platform (DeepSeek-V3 & DeepSeek-R1 Direct)
*The community standard for uncensored, immersive multi-turn roleplay and emotional nuance.*

* **Direct Console URL**: [https://platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
* **Zero/Minimal Cost Details**:
  * **Signup Bonus**: **5,000,000 free tokens** (approx. $0.50–$1.00 credit) valid for 30 days upon registration.
  * **Post-Trial Cost**: The most affordable frontier model in existence:
    * Input (Cache Hit): **$0.07 per 1M tokens**
    * Input (Cache Miss): **$0.14 per 1M tokens**
    * Output: **$0.28 per 1M tokens**
    * A $2.00 deposit provides over 10 million tokens of elite roleplay!
* **Quotas & Limits**: 60 RPM, 100,000 TPM.
* **Signup Instructions**:
  1. Open [https://platform.deepseek.com/](https://platform.deepseek.com/) and create an account with email or Google.
  2. Complete email verification.
  3. Navigate to **API Keys** and click **Create new secret key**.
  4. Copy the generated key (`sk-...`) and save as `DEEPSEEK_API_KEY=` in `.env`.

---

### 3. Cerebras Cloud (Ultra-Fast Llama 3.3 70B & DeepSeek R1 Distill)
*World's fastest inference engine powered by Wafer-Scale Engines (2,000+ tokens/sec). Delivers instantaneous roleplay replies.*

* **Direct Console URL**: [https://cloud.cerebras.ai/platform/](https://cloud.cerebras.ai/platform/)
* **Zero/Minimal Cost Details**:
  * **Cost**: **100% FREE Developer Tier** (no credit card required).
  * **Daily Token Allowance**: **1,000,000 tokens per day (1M TPD)** completely free.
  * **Rate Limits**: **30 RPM**, 60,000 TPM.
* **Signup Instructions**:
  1. Go to [https://cloud.cerebras.ai/platform/](https://cloud.cerebras.ai/platform/).
  2. Click **Sign in with GitHub** or **Sign in with Google**.
  3. Accept terms of service.
  4. Click **API Keys** on the left navigation bar, then click **+ Create API Key**.
  5. Copy the key (`csk-...`) and save as `CEREBRAS_API_KEY=` in `.env`.

---

### 4. SiliconFlow / SiliconCloud (硅基流动)
*Multi-model inference hub hosting DeepSeek-V3, Qwen 2.5 72B, and dedicated permanently free open-source models.*

* **Direct Console URL**: [https://cloud.siliconflow.cn/account/ak](https://cloud.siliconflow.cn/account/ak)
* **Zero/Minimal Cost Details**:
  * **Signup Bonus**: **14 to 20 RMB** (~$2.00–$2.80 USD) in free credits upon registration.
  * **Permanently Free Models** (0 balance deduction):
    * `THUDM/glm-4-9b-chat`
    * `Qwen/Qwen2.5-7B-Instruct`
    * `internlm/internlm2_5-7b-chat`
    * `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
  * **Paid Models**: DeepSeek-V3 and Qwen 2.5 72B at very competitive pricing (~1–2 RMB per 1M tokens).
* **Quotas & Limits**: 100–300 RPM on free tier.
* **Signup Instructions**:
  1. Open [https://cloud.siliconflow.cn/](https://cloud.siliconflow.cn/) and click **Sign Up**.
  2. Sign in with GitHub or register with mobile/email.
  3. Go to **API Keys** ([https://cloud.siliconflow.cn/account/ak](https://cloud.siliconflow.cn/account/ak)) and click **Create New Key**.
  4. Copy key (`sk-...`) and save as `SILICONFLOW_API_KEY=` in `.env`.

---

### 5. Mistral AI ("La Plateforme")
*European multilingual powerhouse. Masters sophisticated dialogue, subtle emotional subtext, and gritty atmospheres.*

* **Direct Console URL**: [https://console.mistral.ai/api-keys/](https://console.mistral.ai/api-keys/)
* **Zero/Minimal Cost Details**:
  * **Cost**: **Free Experimentation Tier** available for developers (no credit card required).
  * **Quotas**: **1 RPS** (60 RPM), 500,000 TPM.
  * **Models Accessible**: `mistral-large-latest`, `mistral-small-latest`, `open-mistral-nemo`.
* **Signup Instructions**:
  1. Visit [https://console.mistral.ai/](https://console.mistral.ai/) and register an account.
  2. Verify your email and phone number to unlock the Experimentation tier.
  3. Navigate to **API Keys** on the left menu.
  4. Click **Create new key**, name it `WyvernProxy`, copy the token, and save as `MISTRAL_API_KEY=` in `.env`.

---

### 6. SambaNova Cloud (Gemma 4 31B, Llama 3.3 70B)
*Hardware-accelerated RDU inference with native support for Gemma 4 31B (Pillar 4).*

* **Direct Console URL**: [https://cloud.sambanova.ai/apis](https://cloud.sambanova.ai/apis)
* **Zero/Minimal Cost Details**:
  * **Cost**: **100% FREE Developer Tier** (no credit card required).
  * **Quotas**: 10–20 RPM, ample for interactive chat turns.
  * **Active Models**: Verified live: `gemma-4-31B-it`, `Meta-Llama-3.3-70B-Instruct`, `Qwen2.5-72B-Instruct`.
* **Current Repository Status**:
  * **Already active in repository configuration!** The key `5b29a236-820a-465e-a576-431ad7922d43` is live and wired to Priority 6, Priority 12, and Priority 16.

---

### 7. Google AI Studio (Multi-Key Optimization)
*World Engine and visual grounding flagship with up to 1,000,000–2,000,000 token context window.*

* **Direct Console URL**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
* **Zero/Minimal Cost Details**:
  * **Cost**: 100% FREE without credit card.
  * **Quotas**:
    * `gemini-3.8-flash` / `gemini-3.1-flash-lite`: **15 RPM**, 1,000,000 TPM, **1,500 RPD**.
    * `gemini-4-argon` / `gemini-2.5-pro` / `gemini-3.1-pro-preview`: **2 RPM**, 32,000 TPM, **50 RPD**.
* **Multi-Key Pooling Strategy (Bypassing 2 RPM / 50 RPD Limits)**:
  * Google allows creating multiple Google Cloud projects under different Google accounts or within the same Google workspace.
  * Generate a separate API key in 2 or 3 distinct Google projects.
  * In `proxy/config_free_proxy.json`, configure the `"google_ai_studio"` entry as a list of strings:
    ```json
    "google_ai_studio": [
      "AIzaSyKey1...",
      "AIzaSyKey2...",
      "AIzaSyKey3..."
    ]
    ```
  * The proxy automatically rotates across these keys. If Key 1 hits the 2 RPM rate limit, the proxy immediately routes the next request through Key 2 without triggering a delay or cooldown on Key 2!

---

### 8. OpenRouter (Multi-Model Hub & Free Tier Safety Net)
*Aggregator providing access to GLM 5.2, Gemma 4, Nemotron 3 Ultra, Claude 3.5, and 14+ daily zero-cost models.*

* **Direct Console URL**: [https://openrouter.ai/keys](https://openrouter.ai/keys)
* **Zero/Minimal Cost Details**:
  * **Cost**: 100% Free for all models ending in `:free`.
  * **Quotas**: 20 RPM, 200 RPD per key base.
  * **Current Repository Status**: Two active keys configured (`sk-or-v1-c407...` and `sk-or-v1-ee90...`), providing a combined 400 RPD on free models.

---

### 9. Groq Cloud (Ultra-Fast Inference)
*LPU-powered inference providing 300–500 tokens/sec on Qwen 3.8 27B and Llama 3.3 70B.*

* **Direct Console URL**: [https://console.groq.com/keys](https://console.groq.com/keys)
* **Zero/Minimal Cost Details**:
  * **Cost**: 100% FREE developer tier (no credit card needed).
  * **Quotas**: **30 RPM**, 1,000 RPD for 70B models, 14,400 RPD for 8B models.
  * **Current Repository Status**: Key active (`gsk_t9xp...`) and operational.

---

### 10. Chutes.ai (Confidential Compute TEE)
*Hosts confidential TEE instances of GLM 5.2, Gemma 4 Turbo, and Qwen 3.8.*

* **Direct Console URL**: [https://app.chutes.ai/](https://app.chutes.ai/)
* **Zero/Minimal Cost Details**:
  * **Signup Credit**: $5.00 in free trial balance upon account creation.
  * **Current Account Note**: The configured key (`cpk_d535...`) has a depleted balance (`-$0.057`), returning HTTP 402. To re-enable:
    1. Sign up for a fresh Chutes.ai account at [https://app.chutes.ai/](https://app.chutes.ai/) with an alternate email to receive a fresh $5.00 credit.
    2. Alternatively, deposit $2.00–$5.00 on the existing account to reactivate access.
    3. Update `CHUTES_API_KEY=` in `.env`.

---

### 11. NVIDIA NIM (API Catalog)
*Enterprise-grade inference for Nemotron 3 Ultra 550B and Llama models.*

* **Direct Console URL**: [https://build.nvidia.com/](https://build.nvidia.com/)
* **Zero/Minimal Cost Details**:
  * **Signup Credit**: 1,000 free API credits upon signup with email/NVIDIA account.
  * **Quotas**: Generous rate limits across the NIM catalog.
  * **Current Repository Status**: Key active (`nvapi-lOwZ...`). Model slugs updated in `config_free_proxy.json` to active endpoints (`qwen/qwen2.5-72b-instruct`).

---

### 12. Cloudflare Workers AI
*Edge AI network hosting Llama 3.3 70B and Qwen models.*

* **Direct Console URL**: [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)
* **Zero/Minimal Cost Details**:
  * **Free Daily Allowance**: **10,000 Neurons per day** free on all Cloudflare accounts.
  * **Quotas**: Up to 50 RPM on free tier.
  * **Current Repository Status**: Token active (`cfat_DlTy...`). Model slugs updated in `config_free_proxy.json` to `@cf/meta/llama-3.3-70b-instruct-fp8-fast`.

---

### 13. GitHub Models (Azure AI Inference)
*Free frontier model access for all GitHub accounts.*

* **Direct Console URL**: [https://github.com/settings/tokens](https://github.com/settings/tokens)
* **Zero/Minimal Cost Details**:
  * **Cost**: 100% Free with standard GitHub Personal Access Token (classic or fine-grained).
  * **Quotas**: 15 RPM, 150 RPD for GPT-4o and Llama 3.3 70B.
  * **Current Repository Status**: Key configured (`ghp_mHXn...`) and wired to active upstream Priority 22.

---

## 4. How to Configure Keys in the Repository

There are two equally supported methods to supply API keys to the proxy:

### Method A: Environment File (`.env`) — Recommended
1. Copy `.env.example` to `.env` at the repository root:
   ```powershell
   copy .env.example .env
   ```
2. Open `.env` in any text editor and paste your keys:
   ```bash
   ZHIPU_API_KEY=your_zhipu_key_here
   DEEPSEEK_API_KEY=your_deepseek_key_here
   CEREBRAS_API_KEY=your_cerebras_key_here
   SILICONFLOW_API_KEY=your_siliconflow_key_here
   MISTRAL_API_KEY=your_mistral_key_here
   ```
3. The proxy automatically loads `.env` on startup via `python-dotenv`.

### Method B: Directly in `proxy/config_free_proxy.json`
1. Open `proxy/config_free_proxy.json`.
2. Locate the `"keys"` block at the top of the file:
   ```json
   "keys": {
     "zhipu": "your_zhipu_key_here",
     "deepseek": "your_deepseek_key_here",
     "cerebras": "your_cerebras_key_here",
     "siliconflow": "your_siliconflow_key_here",
     "mistral": "your_mistral_key_here"
   }
   ```
3. Save the file. The proxy's built-in hot-reload mechanism (`mtime` tracking) applies changes instantly without restarting the server!

---

## 5. Verification & Health Monitoring

To verify that all keys are resolving correctly and upstreams are healthy:

### Check Health Endpoint
Run in PowerShell:
```powershell
python -c "import urllib.request, json; print(json.dumps(json.loads(urllib.request.urlopen('http://127.0.0.1:5005/health').read()), indent=2))"
```

### Inspect Cooldowns & Active Routing
Inspect the debug log file:
```powershell
Get-Content proxy/proxy_debug.log -Tail 30
```
