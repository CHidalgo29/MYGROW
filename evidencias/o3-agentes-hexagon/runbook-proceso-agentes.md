# Runbook: generación de un agente en Hexagon (de principio a fin)

> Documento vivo. Se actualiza después de cada corrida de un agente piloto (ver *Historial de cambios*).
> Los pasos marcados **(por confirmar)** se completan en la primera corrida. La corrida 1 (2026-10-12) resolvió los de despliegue y health check; ver `piloto1-2026-10-12/bitacora.md`.

## Propósito

Recorrer el proceso estandarizado de Hexagon con agentes piloto para:
1. Validar que el proceso funciona de principio a fin en el ambiente de desarrollo (O3).
2. Medir cuánto dura cada segmento del proceso y cómo cambia con cada funcionalidad nueva de la plataforma (O4).

## Agentes piloto

Confirmado con el líder del grow: el objetivo son **2 agentes nuevos, creados de inicio a fin en Hexagon**, cada uno
configurado con cada una de las propiedades (capacidades) del agente. El proceso es **iterativo**.
Por ahora se crea **1 agente** y se guarda la evidencia; el segundo se crea en la siguiente iteración.

| Piloto | Qué ejercita | Código |
|---|---|---|
| Piloto 1 (primero) | Todas las propiedades disponibles hoy: prompt por capas, tool contra API (PokeAPI), métrica personalizada, memoria, knowledge base **(por confirmar la lista exacta con el líder)** | `agent-000053` — Pokedex Assistant (corrida 1: 2026-10-12, v1.0.0) |
| Piloto 2 (siguiente iteración) | Igual que el piloto 1, con un caso de uso distinto | (por asignar) |

Cada vez que sale una funcionalidad relevante de la plataforma (ej. memoria larga, gateways, guardrails),
se vuelve a recorrer el proceso para que las corridas sean comparables entre sí.

## Cuándo correr los pilotos

- **Ahora**: Piloto 1 de inicio a fin, con evidencia completa.
- **Siguiente iteración**: Piloto 2, hasta tener los 2 agentes desplegados en dev.
- **Después de cada hito de plataforma** que cambie lo que un agente puede hacer o cómo se genera.
  Anotar el hito (PR / release de AgentPlatform) en la corrida.

## Segmentos medidos

Registrar hora de inicio y fin de cada segmento. Las horas van al tablero (O4 → *Registro por corrida*).

| # | Segmento | Empieza | Termina |
|---|---|---|---|
| 1 | Definición | Se toma el requerimiento del piloto | Prompt, tools y datos de prueba definidos |
| 2 | Configuración en AgentPlatform | Se abre el wizard del agente | Agente guardado, listo para publicar |
| 3 | Publicación (PR) | Se publica el agente | PR `Agent: agent-XXXXXX@x.y.z` merged en el repo del tenant |
| 4 | Despliegue dev + health | Merge del PR | Workload corriendo en dev y health check OK |
| 5 | Prueba E2E | Primera solicitud real | Solicitud completada correctamente y verificada en el monitoreo |

Si un segmento se repite por un error (ej. volver a publicar), el tiempo se suma al mismo segmento y se anota la causa.

## Procedimiento

### 1. Definición
- [ ] Elegir el piloto y el caso de uso real que va a resolver.
- [ ] Definir las capas del prompt, las tools y la knowledge base que necesita.
- [ ] Definir la solicitud real de prueba y el resultado esperado.

### 2. Configuración en AgentPlatform
- [ ] Crear el agente con el wizard (ambiente dev).
- [ ] Configurar el prompt por capas desde el catálogo de prompts.
- [ ] Asociar las tools (y su connection profile / autenticación si aplica).
- [ ] Asociar la knowledge base (si aplica) y verificar que sus documentos estén procesados.
- [ ] Guardar y anotar el código `agent-XXXXXX`.

### 3. Publicación
- [ ] Publicar el agente desde AgentPlatform.
- [ ] Verificar que `snap-code-generator` abrió el PR en el repo del tenant (ej. `SoinLabs/KolbiTappAgents`).
- [ ] Revisar el diff generado y hacer merge. Guardar el link del PR.

### 4. Despliegue en dev y health check
- [ ] Verificar el despliegue desde la UI, sin acceso al cluster: en el detalle del agente debe aparecer *Desplegado · Working* con la versión (ej. `v1.0.0`).
- [ ] Abrir **Diagnosis** en el detalle del agente (es el health check): versión en ejecución, LLM Gateway OK, credencial de ejecución entregada, Tool Gateway alcanzable, memoria de corto y largo plazo habilitadas. Guardar la captura. (El Tool Gateway puede mostrar "Reachable (401)": responde, el 401 es el sondeo sin credencial.)

### 5. Prueba E2E
- [ ] Enviar la solicitud real definida en el paso 1 desde el botón **Test agent** del detalle del agente.
- [ ] Verificar la respuesta y las llamadas a tools en la pestaña **Monitoring** del agente (sesión con trazas y métrica personalizada incrementada).
- [ ] Guardar la captura o el link de la conversación.

### Cierre de la corrida
- [ ] Registrar la corrida en el tablero: O3 (casillas + evidencia) y O4 (horas por segmento).
- [ ] Guardar la evidencia en `evidencias/o3-agentes-hexagon/<piloto>-<fecha>/`.
- [ ] Anotar problemas encontrados y actualizar este runbook.

## Evidencia por corrida

| Evidencia | Dónde |
|---|---|
| PR del agente | Repo del tenant |
| Health check OK | Captura / log |
| Solicitud real E2E | Captura o link del monitoreo de AgentPlatform |
| Tiempos por segmento | Tablero (O4) |

## Problemas conocidos y soluciones

| Fecha | Problema | Solución |
|---|---|---|
| 2026-10-12 | Crear knowledge base falla con `ORA-20005: La extension "tif" esta en la ruta de OCR pero no en los tipos permitidos` | Agregar TIF y TIFF a *Allowed types* (el control es un `select` múltiple) |
| 2026-10-12 | El diálogo de subir documentos exige categoría y tipo, y solo existen las categorías de documento "Recursos Humanos" y "Campaign manager" | Usar la más genérica y tipo "Manual"; pendiente definir si hay una categoría adecuada |
| 2026-10-12 | En el paso Prompt, escribir en el textarea de Boundaries no lo registra | Usar *Add* con una sugerencia del catálogo o texto propio con categoría |
| 2026-10-12 | Aviso transitorio "failed —" tras subir un documento | Recargar la página: el documento queda `Ready` |

## Historial de cambios

| Fecha | Cambio | Corrida |
|---|---|---|
| 2026-09-28 | Versión inicial del runbook (plantilla) | — |
| 2026-10-12 | Resueltos los "por confirmar" de despliegue (UI) y health check (*Diagnosis*); agregados problemas conocidos y pilotos (ahora 2 agentes, iterativo) | Corrida 1 — `agent-000053` v1.0.0, PR KolbiTappAgents#400 |
