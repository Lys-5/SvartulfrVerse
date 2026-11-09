# Style Guide — Database Record

---

## Migration Metadata

| Field | Value |
|-------|-------|
| Source | d:\Progetti\database\assets\style_guide.md |
| Authority | Visual Authority |
| Migration Date | 2026-06-08 (Updated 2026-10-16 — Argon/Gemini Standard) |
| Status | Active Canonical Standard |

---

## Purpose

Reusable prompt templates, anatomical guardrails, and outfit series formulas for generating SvartúlfrVerse character portraits and *Appearance & Outfits* galleries via **Gemini / Argon**.

Reference sessions:
- [Gemini Session 1 — Douglas Family & Outfits](https://gemini.google.com/app/699ca946550ec63b)
- [Gemini Session 2 — Wulfnic Bloodmoon & Variants](https://gemini.google.com/app/cacb36df583d0db9)

---

## 1. Master Character Portrait Formula (Partial Shift — Wolf Ears & Tail)

```text
A detailed anime/manhwa style illustration, cowboy shot, of a [AGE/BUILD DESCRIPTION, e.g., tall, muscular young man with broad shoulders and defined abs]. He has [HAIR DESCRIPTION, e.g., messy shoulder-length jet-black hair with strands framing his face and covering the sides of his head] and [EYE DESCRIPTION, e.g., piercing glowing golden-amber eyes / bright emerald-green eyes]. He has a single pair of [COLOR] wolf ears on top of his head (only one pair of ears, no human ears) and a thick, bushy [COLOR] wolf tail visible behind him. [TATTOOS / SCARS / FACIAL HAIR]. He is wearing [OUTFIT DESCRIPTION]. Background of [SETTING DESCRIPTION, e.g., a luxury modern terrace overlooking Blackwood City with palm trees against a warm golden-orange sunset sky]. Dramatic warm sunset rim lighting, rich shading, high-end Korean manhwa / semi-realistic anime digital painting.
```

---

## 2. Master Character Portrait Formula (Human Form — Public / School / Suit)

```text
Keep the exact same character, face, hair, eye color, build, tattoos, and art style from the previous image, but in fully human form (remove the wolf ears and wolf tail, normal human ears partially hidden by hair). Change his outfit and background: he is wearing [OUTFIT DESCRIPTION] in [SETTING DESCRIPTION]. Maintain the same warm dramatic lighting and detailed manhwa/anime illustration style.
```

---

## 3. Master Full Wolf Form Formula (`Wolf`)

```text
Keep the exact same art style and lighting, transforming the character into his full majestic giant wolf form (Svartúlfr / Lycanthrope beast form): a massive, powerful [FUR COLOR] dire wolf with [EYE COLOR] glowing eyes, [DISTINCTIVE SCARS/MARKINGS], standing in [SETTING DESCRIPTION] under dramatic lighting.
```

---

## 4. Standard *Appearance & Outfits* Series (Wyvern Character Cards & Personas)

Every primary Character Card and User Persona should be equipped with a cohesive set of contextual outfits following this nomenclature:

| Outfit Name | Form State | Typical Attire & Context |
|-------------|------------|--------------------------|
| `Default` | Partial Shift (or Human) | Signature iconic look against Blackwood City sunset / estate backdrop |
| `Night` | Partial Shift | Dark nocturnal streetwear, leather jacket, or moonlit rooftop/balcony vibe |
| `Suit` | Human Form (or Partial) | Bespoke three-piece suit, gala/executive attire, luxury lounge or penthouse |
| `Swimwear` | Partial Shift | Beach/poolside boardshorts or bikini, wet skin, coastal California sunset |
| `Underwear` | Partial Shift | Relaxed bedroom/morning loungewear, boxer briefs or lingerie/Calvin Klein set |
| `Sport` / `Boxe` | Partial Shift | MMA hand wraps, gym shorts, compression gear, or basketball/track attire |
| `School` / `Campus` | Human Form | SUCC college streetwear, varsity jacket, backpack/headphones on campus |
| `Casual` / `Relax` | Partial Shift | Cozy home hoodie, flannel, sweatpants, gaming setup or living room |
| `Wolf` | Full Wolf Form | Giant dire wolf transformation (`Svartúlfr`) |

---

## 5. Canonical Proportions & Scale Reference in Group Compositions

When portraying or describing the Douglas-Bloodmoon family members together in group compositions, visual prompts, or scene staging, maintain strict anatomical proportions and height deltas:
- Alyssa: 155 cm (5' 1")
- Jasper: 193 cm (6' 4")
- Noah: 197 cm (6' 5.6")
- Malachia: 208 cm (6' 9.9")
- Erik: 213 cm (6' 11.9")
- Wulfnic: 220 cm (7' 2.6")

Direct Proportional Scale References:
- Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).
- Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.
- Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno).

---

## Authority

Established by: Visual Authority Layer & User Direction (16 October 2026)
Full Prompt Catalog: [argon_gemini_prompts_reference.md](./argon_gemini_prompts_reference.md)

