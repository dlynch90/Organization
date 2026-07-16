# AGENTS.md — dlynch90/Organization

Canonical governance pointer for this repository: platform organization governance, templates, and reusable workflows for the dlynch90 fleet.

## 1. Instruction precedence (narrower wins, never weakens higher policy)

1. Security, privacy, legal, production-safety constraints.
2. `dlynch90/developer-platform` → `standards/AGENTS.md` (platform canonical governance contract).
3. This file.
4. The nearest directory-level `AGENTS.md`, governance contract, or runbook in this repository.
5. The immediate task request.

When instructions conflict, stop the conflicting edit and record the conflict. Do not silently pick the least restrictive interpretation.

## 2. Fail-closed routing

- Structured-file parse/read/edit resolves through the platform tool-routing contract (`contracts/tool-routing.yaml` in `dlynch90/developer-platform`). Never invent ad-hoc parsers when a routed vendor CLI exists (JSON → jq, YAML → yq).
- GitHub mutations go through authenticated `gh api` — no console clicks for anything reproducible.
- Missing tools, credentials, or approvals are recorded as gaps with an owner layer and the next deterministic gate. Absence is never reported as success.

## 3. External-source provenance

Any file, template, or workflow imported from an external source records provenance (`source_key`, `official_url`, `retrieved_at`, `used_for`) per the platform external-source provenance rule before it lands here.
