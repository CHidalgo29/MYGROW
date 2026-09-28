# Runbook: generación de un agente en Hexagon (de principio a fin)

> Documento vivo. Se actualiza después de cada corrida de un agente piloto (ver *Historial de cambios*).
> Los pasos marcados **(por confirmar)** se completan en la primera corrida.

## Propósito

Recorrer el proceso estandarizado de Hexagon con agentes piloto para:
1. Validar que el proceso funciona de principio a fin en el ambiente de desarrollo (O3).
2. Medir cuánto dura cada segmento del proceso y cómo cambia con cada funcionalidad nueva de la plataforma (O4).

## Agentes piloto

| Piloto | Complejidad | Qué ejercita | Código |
|---|---|---|---|
| Piloto 1 | Baja | Solo prompt (sin tools ni knowledge base) | (por asignar) |
| Piloto 2 | Media | Prompt por capas + 1–2 tools contra una API | (por asignar) |
| Piloto 3 | Alta | Tools + knowledge base (RAG) + memoria | (por asignar) |

Los mismos pilotos se vuelven a correr cada vez que sale una funcionalidad relevante (ej. memoria larga, gateways, guardrails),
para que las corridas sean comparables entre sí.

## Cuándo correr los pilotos

- **Línea base**: primeras 2 semanas del período, con los 3 pilotos.
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
- [ ] Verificar el despliegue del workload (Deployment, Service, Ingress) en el namespace de agentes del tenant **(por confirmar: comando o pantalla)**.
- [ ] Ver el estado *desplegado* del agente en AgentPlatform.
- [ ] Ejecutar el health check **(por confirmar: endpoint)** y guardar la respuesta.

### 5. Prueba E2E
- [ ] Enviar la solicitud real definida en el paso 1.
- [ ] Verificar la respuesta y las llamadas a tools en el monitoreo de conversaciones.
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
| | | |

## Historial de cambios

| Fecha | Cambio | Corrida |
|---|---|---|
| 2026-09-28 | Versión inicial del runbook (plantilla) | — |
