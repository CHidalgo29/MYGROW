# Mi Grow

Tablero personal para dar seguimiento a los objetivos y competencias del período, y guardar la evidencia de cada uno.

## Uso

1. Abrir `index.html` en el navegador (doble clic, no necesita servidor).
2. Hacer clic en una tarjeta para ver el detalle: tareas, indicador, tabla de registros, evidencias y notas.
3. Los cambios se guardan automáticamente en el navegador (localStorage).
4. Para dejarlos en el repo: **Exportar progreso.js** → reemplazar `progreso.js` en la raíz → commit.
   Al abrir `index.html` se usa la copia más reciente (la del repo o la del navegador).
5. Guardar archivos de evidencia (capturas, PDFs, logs) en `evidencias/<objetivo>/` y enlazarlos con su ruta relativa,
   por ejemplo `evidencias/o3-agentes-hexagon/health-check-agente1.png`.
6. **Vista reporte** → **Imprimir / PDF** genera el documento para presentar cuando lo pidan.

El período (inicio / fin) se edita en el encabezado; la fecha límite de la línea base de O4 se calcula como inicio + 14 días.

## Estructura

```
index.html      Tablero (HTML + CSS + JS en un solo archivo)
progreso.js     Datos exportados del tablero (window.GROW_DATA)
evidencias/     Archivos de respaldo, una carpeta por objetivo / competencia
```

## Análisis de objetivos

Cada meta se descompone en **tareas** (checklist) y un **indicador medible**. El avance de cada tarjeta es el promedio entre ambos; se marca *Completado* solo cuando todas las tareas están hechas y el indicador está en meta.

| # | Meta | Indicador que la cierra | Evidencia esperada |
|---|------|-------------------------|--------------------|
| O1 | Modelo AI-First | ≥3 casos comparables con productividad ≥3x y validados técnicamente | Tabla de casos (tiempo tradicional estimado vs. real con IA), PRs, cómo se validó |
| O2 | Tiempo productivo | Promedio ≥70% según registros oficiales | Captura mensual del registro oficial |
| O3 | Agentes Hexagon | ≥2 agentes desplegados en dev + health check OK + 1 solicitud real E2E; runbook documentado | Link al despliegue, log del health check, traza E2E, runbook |
| O4 | Medición de generación de agentes | Segmentos definidos y línea base de ≥3 agentes (baja/media/alta) en las primeras 2 semanas; registro todo el semestre | Documento de segmentos, tabla de tiempos por agente |
| C1 | Revisión automática de PRs con IA | Activa en AgentPlatform y Boilerplate cubriendo estándares, defectos y calidad | Workflow/config en ambos repos, PRs con comentarios de la IA |
| C2 | Git, PRs y diffs IA | 100% de cambios hechos con IA revisados antes del merge | Registro de PRs, historial de branches/commits |
| C3 | Agentic software engineering | Uso de subagentes, MCP, herramientas, automatizaciones y flujo planning → implementation → testing → review | Definiciones de agentes, config MCP, hooks, tarea real con el flujo |
| C4 | Prácticas avanzadas con líder técnico | ≥3 entregables reales validados por el líder | PRs/features + aprobación o nota del líder |

### Puntos de atención

- **O4 es urgente por fecha**: la línea base debe quedar dentro de las primeras 2 semanas del período.
- **O1 depende de un método de comparación** defendible (histórico, story points o estimación previa). Definirlo antes de registrar casos.
- **O3 y O4 se alimentan entre sí**: cada agente de Hexagon generado puede registrarse también en la medición de O4.
- **C1 y C2 se refuerzan**: la revisión automática de PRs sirve como evidencia de que los diffs con IA se revisan.
- **C3 y C4 comparten evidencia** con O1: los mismos entregables pueden mostrar prácticas agénticas y validación del líder.
