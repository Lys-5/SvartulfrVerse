## 2026-11-01T20:56:21Z
You are Worker 1 (teamwork_worker).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_14_1
Read ORIGINAL_REQUEST.md at: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
Read SCOPE.md at: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_14\SCOPE.md
Read GEMINI.md § 20 at: e:\repository\SvartulfrVerse\GEMINI.md
Read the domain skill wyvern-ai-proxy-rotator at: e:\repository\SvartulfrVerse\.agents\skills\wyvern-ai-proxy-rotator\SKILL.md

Read the synthesis and exploration reports:
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_14\SYNTHESIS.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_14_1\analysis.md and handoff.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_14_2\analysis.md and handoff.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_14_3\analysis.md and handoff.md

Write Ownership:
You exclusively own and may edit or create these files:
- `proxy/config_free_proxy.json`
- `proxy/free_tier_proxy.py`
- `proxy/API_KEY_ACQUISITION_GUIDE.md`
- `.env.example`

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Tasks to Implement:
1. Update `proxy/config_free_proxy.json`:
   - Enforce the failover cascade prioritizing the primary fiat models:
     * Pillar 1 (Priorities 1-2): GLM 5.2 / 5.3 (Zhipu BigModel direct, OpenRouter, Chutes).
     * Pillar 2 (Priority 3): Gemini 4 Argon (`gemini-4-argon`, `gemini-2.5-pro` via Google AI Studio).
     * Pillar 3 (Priorities 4-5): Gemini 3.8 Flash (`gemini-3.8-flash`, `gemini-3.8-flash-thinking`, `gemini-3.1-flash-lite` via Google AI Studio).
     * Pillar 4 (Priorities 6-8): Gemma 4 (`gemma-4-31B-it` via SambaNova [working live!], OpenRouter `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, Chutes `google/gemma-4-31B-turbo-TEE`).
   - Arrange remaining models ordered strictly by RPG roleplay quality:
     * Priorities 9-10: DeepSeek V3 / V3.2 (`deepseek-chat` direct, `deepseek/deepseek-chat` OpenRouter).
     * Priority 11: Claude 3.5 Sonnet & Haiku via OpenRouter.
     * Priorities 12-15: Qwen 2.5 72B & Qwen 3.8 27B (SambaNova, Groq `qwen/qwen3.8-27b`, Chutes, NVIDIA NIM, Cloudflare).
     * Priorities 16-18: Llama 3.3 70B (SambaNova, Groq, NVIDIA NIM, Cloudflare).
     * Priority 19: Mistral Large 2 & Mistral Nemo (Mistral direct / OpenRouter).
     * Priority 20: Gemini Pro / Flash Backup Family.
     * Priority 21: NVIDIA Nemotron 3 Ultra 550B & 3.5 Lightning (OpenRouter Free).
     * Priorities 22+: Clean Emergency Free Safety Net (purge content moderation models like `nemotron-3.5-content-safety` and code-only models like `north-mini-code`).
   - Wire dormant keys (`sambanova`, `github`) into active `upstreams`.
   - Update model IDs for Groq, NVIDIA, and Cloudflare to active non-deprecated models.
   - Maintain valid JSON formatting with all required provider fields, endpoint paths, headers, and parameter controls.

2. Update `proxy/free_tier_proxy.py`:
   - Add `load_dotenv()` support (gracefully checking if python-dotenv is present and loading `.env` if exists).
   - In `sanitize_parameters`, ensure providers like `zhipu`, `github`, `cerebras`, `mistral`, `sambanova` properly strip unsupported parameters (such as `frequency_penalty`, `presence_penalty`).
   - Ensure seamless fallback, circuit-breaker cooldown handling, and parameter pass-through.

3. Create `proxy/API_KEY_ACQUISITION_GUIDE.md`:
   - Comprehensive audit of missing, unconfigured, or blank API keys in local configuration files.
   - Direct provider console URLs and acquisition instructions for zero/minimal cost for:
     * Zhipu AI / BigModel (`ZHIPU_API_KEY`)
     * DeepSeek Platform (`DEEPSEEK_API_KEY`)
     * Cerebras Cloud (`CEREBRAS_API_KEY`)
     * SiliconFlow (`SILICONFLOW_API_KEY`)
     * Mistral AI (`MISTRAL_API_KEY`)
     * SambaNova Cloud (`SAMBANOVA_API_KEY`)
     * Google AI Studio (`GOOGLE_AI_STUDIO_API_KEY` / multi-key setup)
     * OpenRouter (`OPENROUTER_API_KEY`)
     * Groq Cloud (`GROQ_API_KEY`)
     * Chutes AI (`CHUTES_API_KEY` - balance reset/free endpoints)
     * NVIDIA NIM (`NVIDIA_API_KEY`)
     * Cloudflare Workers AI (`CLOUDFLARE_API_KEY` + Account ID)
     * GitHub Models (`GITHUB_TOKEN` / Azure AI)
   - Detail free tier quotas (RPM, TPM, RPD), free token credits, and signup instructions.

4. Create `.env.example`:
   - Clear, clean template at project root detailing all environment variables for the proxy.

5. Verification:
   - Run the full test suite:
     `python -m pytest tests/test_proxy_compaction.py tests/test_adversarial_compaction.py -v`
   - Verify `proxy/config_free_proxy.json` parses cleanly in Python with `json.load`.
   - Verify that all 28+ unit tests pass without errors.
   - Document commands, outputs, and results in your handoff report.
