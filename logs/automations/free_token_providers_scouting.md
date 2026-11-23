# Report Quotidiano Scouting — Provider & Token Free Tier

**Data Scansione:** 2026-11-22 09:01:53  
**Target:** Modelli Prioritari (GLM 5.2+, Gemini 3.8+, Gemma 4+)  
**Stato Pipeline:** Stage 1B (Automazione Master Quotidiana)

---

## 1. Modelli Free Rilevati su OpenRouter (`:free`)
| Modello | Nome Visualizzato | Context Window | Endpoint |
| :--- | :--- | :--- | :--- |
| `google/gemma-4-26b-a4b-it:free` | Google: Gemma 4 26B A4B  (free) | 262144 | `https://openrouter.ai/api/v1/chat/completions` |
| `google/gemma-4-31b-it:free` | Google: Gemma 4 31B (free) | 262144 | `https://openrouter.ai/api/v1/chat/completions` |

---

## 2. Panoramica Provider con Token Free / Programmi Sviluppatori
| Provider | Offerta Free Tier | Modelli Chiave Supportati | Stato Chiave nel Proxy |
| :--- | :--- | :--- | :--- |
| **Google AI Studio** | Free Tier (RPM / RPD quotas without credit card) | `gemini-3.5-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `gemma-4-31b-it` | Active (4 keys in pool) |
| **Zhipu AI (Z.ai / BigModel)** | Developer Free Quota / Startup Grant Program | `glm-4-flash`, `glm-5.3-flash`, `glm-zero-preview` | Active (Key configured) |
| **SiliconFlow (SiliconCloud)** | Free Registration Tokens (Millions of initial free tokens) | `GLM-5.3-Flash`, `DeepSeek-V3`, `Qwen3.8` | Available for registration (Free token grant on signup) |
| **Cloudflare Workers AI** | Free Tier (10,000 Neurons / day free allowance) | `@cf/google/gemma-7b-it`, `GLM partner endpoints` | Active (Token configured) |

---

## 3. Opportunità di Espansione Limiti
- **SiliconFlow:** Registrando un account gratuito su `siliconflow.cn` si ottiene un pacchetto di benvenuto con milioni di token gratuiti per modelli GLM e DeepSeek via API OpenAI-compatible. Basta incollare la chiave in `config_free_proxy.json` sotto `"siliconflow"`.
- **Zhipu AI Startup / Dev Grant:** Per progetti open e TTRPG, il programma developer `z.ai` rilascia token gratuiti dedicati a sviluppatori.
- **Google AI Studio Key Pool:** È possibile creare ulteriori chiavi su account Google secondari per ampliare ulteriormente il round-robin a 5+ chiavi.

---