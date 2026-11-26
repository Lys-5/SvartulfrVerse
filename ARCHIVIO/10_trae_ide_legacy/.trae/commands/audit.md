---
name: audit
description: Run a repository audit using the Audit skill.
---

# Audit Command

Use the **Audit** skill.

Determine the audit scope from the user's request.

Possible audit targets include:

* repository structure
* governance
* ADR consistency
* rules
* specifications
* exports
* engines
* documentation
* migration residue

Follow all requirements defined by the Audit skill.

Return findings in chat only.

Do not create files.

Do not modify repository content unless explicitly requested in a separate remediation task.
