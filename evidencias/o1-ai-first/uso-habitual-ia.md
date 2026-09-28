# O1 · Evidencia de modelo de trabajo AI-First

Repositorio: [CHidalgo29/AgentPlatform](https://github.com/CHidalgo29/AgentPlatform)
Corte: 2026-09-28

## Resumen de uso

| Indicador | Valor | Fuente |
|---|---|---|
| Sesiones de Claude Code en AgentPlatform | 359 (9 en agosto, 350 en septiembre) | `~/.claude/projects/-Users-chidalgo-Documents-AgentPlatform*` |
| Commits propios | 334 (132 en agosto, 201 en septiembre) | `git log --author=CHidalgo29` |
| PRs propios | 89 (86 merged) | `gh pr list --author @me` |
| PRs con CI completo en verde | 75 de 78 con checks | GitHub Actions `ci.yml` |
| Propuestas OpenSpec (análisis previo) | 141 activas + 44 archivadas, 18 specs | `openspec/` |
| Equipo agéntico del repo | tech-lead, full-stack-developer (+ Codex), code-reviewer, security-engineer, qa-engineer | `.claude/agents/` |

## Uso por actividad

### Análisis de código
- Cada funcionalidad arranca con una propuesta OpenSpec generada con IA: `proposal.md`, `design.md`, `tasks.md` y el delta de specs.
  Ejemplos: `openspec/changes/duplicate-agent-from-catalog`, `add-tool-field-transformations`, `retire-deployed-agents`.
- `openspec/exploration.md`, y la skill `grill-me` para cuestionar requerimientos antes de implementar.

### Desarrollo
- El 100% de las funcionalidades del período se implementaron con Claude Code: 89 PRs y 334 commits.
- Casos con tiempo medido contra el proceso tradicional: [comparacion-3x.md](comparacion-3x.md).

### Debugging
- Correcciones hechas con IA, por ejemplo #443 (esquemas vacíos en tools), #457 (estado de despliegue de agentes), #477 (respuestas oneOf/anyOf escalares) y #489 (paginación server-side).

### Pruebas
- Agente `qa-engineer`. Los tests se generan junto con cada feature: #402 incluye 85 archivos de test, #392 incluye 31.
- En CI corren unit, integración con base de datos (en shards), smoke de API y de UI, y type-check.

### Documentación
- 18 specs vivas en `openspec/specs`, `CHANGELOG.md`, `docs/` y descripciones de PR detalladas (plantilla `.github/pull_request_template.md`).

## Control y validación técnica
- **CI obligatorio**: build, lint, type-check, unit, integración con base de datos y smoke. Los 5 PRs candidatos pasan 11/11 checks.
- **Revisión por agentes**: `code-reviewer` y `security-engineer`, con reportes por ciclo en `.agent-history/` (ej. `REQ-20260804-001/.../code-review/cycle-1.json`).
- **Revisión propia del diff** antes de cada merge.
- Punto débil: solo 1 de los 86 PRs merged tiene revisión humana registrada en GitHub (jcquesadaSOIN).

## Cómo reproducir la medición de tiempo con IA

```bash
python3 scripts/medir-tiempo-ia.py AgentPlatform
```
