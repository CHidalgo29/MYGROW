# O1 · Casos comparables: proceso tradicional vs. AI-First

## Método

| | Proceso tradicional | Proceso AI-First |
|---|---|---|
| Proyecto | SiGes · Portal del Colaborador ([SIGE en Jira](https://soinlabs.atlassian.net/jira/software/c/projects/SIGE/issues)) | [AgentPlatform](https://github.com/CHidalgo29/AgentPlatform) |
| Período | Julio – noviembre 2025 | Agosto – septiembre 2026 |
| Stack | Next.js / React | Next.js / React + API Node |
| Fuente del tiempo | Campo Jira **Duración final** (horas reales registradas al cerrar la tarea) | Tiempo activo de sesiones de Claude Code en la rama del PR (`scripts/medir-tiempo-ia.py`, pausas >30 min excluidas) |
| Validación | Revisión funcional / QA del proyecto | CI obligatorio (11 checks: build, lint, type-check, unit, integración con base de datos, smoke) + tests nuevos en el PR |

**Regla de comparación**: se emparejan tareas del mismo tipo de trabajo (misma capa y naturaleza), donde el entregable con IA tiene alcance igual o mayor que el tradicional. Productividad = horas tradicionales ÷ horas con IA.

**Por qué es conservador**
- Los entregables con IA incluyen tests automatizados y, en algunos casos, backend; las tareas de SiGes eran solo UI.
- Se usa la *Duración final* real de SiGes, no la estimación inicial.

## Casos

| # | Tipo de trabajo | Tradicional (SiGes) | Con IA (AgentPlatform) | Productividad |
|---|---|---|---|---|
| 1 | Pantalla nueva con formulario | [SIGE-87](https://soinlabs.atlassian.net/browse/SIGE-87) Nueva pantalla Agregar horas · **24 h** | [#342](https://github.com/CHidalgo29/AgentPlatform/pull/342) Crear connection profile inline en el wizard de APIs · **3.1 h** · +1,981 líneas, 9 archivos de test | **7.7x** |
| 2 | Pantalla que consume servicios de la API | [SIGE-126](https://soinlabs.atlassian.net/browse/SIGE-126) Consumir servicios de la API para pantalla de Perfil · **24 h** (estimado 16 h) | [#386](https://github.com/CHidalgo29/AgentPlatform/pull/386) Pantalla de detalle de tool **+ la API de monitoreo** · **5.9 h** · +5,994 líneas, 19 archivos de test | **4.1x** |
| 3 | Actualización de UI en varias pantallas | [SIGE-355](https://soinlabs.atlassian.net/browse/SIGE-355) Actualización de diseño en diferentes pantallas · **32 h** | [#491](https://github.com/CHidalgo29/AgentPlatform/pull/491) Toolbar de filtros unificado y chips de estado en todos los catálogos · **5.4 h** · 100 archivos, 33 de test | **5.9x** |

Los tres PRs pasaron 11/11 checks de CI antes del merge.

## Referencia: velocidad tradicional en SiGes

64 tareas del Portal del Colaborador y SiGes V2 (julio – noviembre 2025) suman **311.5 h** de duración final
(293.5 h estimadas). Tareas grandes de referencia:

| Tarea | Duración final |
|---|---|
| SIGE-82 Migrar el app de Electron a Next.js | 16 h |
| SIGE-86 Nueva pantalla Reportar días | 24 h |
| SIGE-87 Nueva pantalla Agregar horas | 24 h |
| SIGE-100 Agregar traducciones | 24 h |
| SIGE-126 Consumir servicios de la API para pantalla de Perfil | 24 h |
| SIGE-142 Maqueteo de pantalla de solicitudes | 16 h |
| SIGE-275 Terminar gastos | 16 h |
| SIGE-355 Actualización de diseño en diferentes pantallas | 32 h |

## Pendiente para blindar la evidencia
- Que el líder técnico confirme que los pares son comparables (una línea de aprobación basta).
- Captura de los campos *Story Points* y *Duración final* de las tres tareas de Jira.
