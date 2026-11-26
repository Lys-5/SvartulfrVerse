# Repository Configuration

**Date:** 2026-06-08
**Authority:** Migration Architect
**Status:** ACTIVE

---

## Workspace Structure

```text
Workspace
├── SvartulfrVerse      (ACTIVE CANON)
└── Progetti            (SECONDARY ARCHIVE — read-only)
```

---

## Repository Roles

### SvartulfrVerse

| Property | Value |
|----------|-------|
| Role | Primary Repository |
| Status | ACTIVE CANON |
| Access | Read/Write |
| Authority | Single Source of Truth |
| URL | (local) |

**Rules:**
- Only canonical repository
- All migrations target this repository
- All authority records live here
- All governance documents live here


---

### Progetti

| Property | Value |
|----------|-------|
| Role | Secondary Archive |
| Status | READ-ONLY |
| Access | Read-only |
| Authority | Supplementary evidence |
| URL | (local) D:\Progetti |

**Rules:**
- Historical archive reference
- Supplementary materials only
- No modifications allowed

---

## Evidence Priority

When sources conflict:

```text
SvartulfrVerse (canon) > Progetti
```

---

## Import Workflow

All information from external repositories must follow:

```text
1. Research
   - Query Progetti
   - Extract evidence summary

2. Audit
   - Verify against existing canon
   - Identify conflicts

3. Architecture Review
   - Assess impact on existing structure
   - Determine authority ownership

4. Authority Decision
   - Governance approval required
   - Document decision in ADR

5. Import
   - Create database record in appropriate domain subdirectory
   - Source attribution preserved in record metadata
```

---

## Workspace Configuration

### VS Code Multi-Root Workspace (Optional)

> **Note:** `Progetti` are external research archives. They are NOT included in the local repository. To use them as additional workspace folders, clone them manually first, then add them to the workspace configuration.

Create file: `SvartulfrVerse.code-workspace`

```json
{
  "folders": [
    {
      "path": "d:/SvartulfrVerse",
      "name": "SvartulfrVerse (CANON)"
    },
    {
      "path": "d:/Progetti",
      "name": "Progetti (ARCHIVE)"
    }
  ],
  "settings": {
    "files.readonlyInclude": {
      "**/Progetti/**": true
    }
  }
}
```

### Git Clone Commands (Optional — for research only)

```bash
cd d:\
git clone https://github.com/Alys5/Svartulfr_LA.git  # Research archive only — no canonical authority
git clone https://github.com/Alys5/Progetti.git
```

---

## Agent Instructions

When operating in this workspace:

```text
Repository Configuration

Primary Repository:
- SvartulfrVerse

Historical Archive:
- Progetti (read-only)

Rules:

- SvartulfrVerse is the active canonical repository.
- Progetti are evidence repositories only.
- No direct imports from external repositories.
- All imported information must follow:
  Research → Audit → Architecture Review → Authority Decision → Import.

When migration sources are missing in SvartulfrVerse:

1. Search Progetti second.
2. Produce evidence summary.
3. Ask for approval.
4. Import only after approval.
```

---

## Authority

**Document Type:** Repository Configuration
**Date:** 2026-06-08
**Authority:** Migration Architect
**Status:** ACTIVE
