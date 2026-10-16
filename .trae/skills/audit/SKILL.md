---
name: Audit
description: Use this skill when performing repository audits, consistency checks, structural reviews, governance validation, duplication analysis, readiness assessments, or any investigation whose goal is to identify issues without changing the repository.
---

## Instructions

This is an **audit-only task**.

### Forbidden Actions

Do **NOT** create:

* files in `reports/`
* markdown documents
* temporary documents
* analysis artifacts
* audit logs stored in the repository
* remediation files

Do **NOT** modify:

* repository content
* governance documents
* specifications
* source files
* configuration files

### Required Output

Return the complete audit report directly in the chat response.

The report should include:

1. Executive Summary
2. Findings
3. Anomalies Detected
4. Risk Assessment
5. Recommended Remediation Actions

### Remediation Policy

Repository modifications are forbidden during the audit phase.

If issues are identified:

1. Document the issue.
2. Explain the impact.
3. Recommend a remediation.
4. Wait for explicit user approval before making any repository changes.

### Success Criteria

* Repository remains unchanged.
* No files are created.
* No files are modified.
* All findings are reported in chat only.
* Clear remediation recommendations are provided when necessary.