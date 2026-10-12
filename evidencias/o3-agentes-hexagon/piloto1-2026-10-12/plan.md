# Piloto 1 — Plan (2026-10-12)

Ambiente: https://hexagon-dev.soincloud.com (login con usuario de prueba "Test").

## Hallazgos de la navegación

- Home: 4 secciones — Agents, Tools, Knowledge Base, Monitoring.
- Catálogo de agentes: botón *Create agent* (`/agents/new`), agrupado por categoría.
- **Wizard de agente: 10 pasos** — Identity (detail) → Type → Tools → Metrics → Prompt → Memory → RAG → Security → LLM → Review.
  - Paso 1 pide: Name*, Description, Objective, Category*, Subcategory, Tags, *For conversation*, *Publish over A2A*. El código `agent-XXXXXX` se asigna al guardar.
  - Se puede guardar como borrador en cada paso.
- **Wizard de tool: 5 pasos** — General → API → Operation → Field labels → Confirm. Una tool se apoya en una API del catálogo.
- Catálogo de APIs (`/apis`, *Create API*), tools (`/tools`) y knowledge bases (`/knowledge-base`, *Create knowledge base*) existen con categorías.
- Ya existen categorías de prueba; para el piloto se crea una propia para no mezclar datos.

## Caso de uso

**Asistente Pokédex**: responde preguntas sobre Pokémon usando PokeAPI (https://pokeapi.co/, API pública de prueba).

Solicitud real E2E: "¿Qué tipo es Pikachu y cuáles son sus habilidades?" → debe llamar a la tool y responder con datos de PokeAPI (type: electric; abilities: static, lightning-rod).

## Plan por propiedad (paso del wizard)

| Paso | Qué se configura |
|---|---|
| Identity | Nombre "Pokedex Assistant", categoría propia, For conversation activo |
| Type | Según opciones que ofrezca el app (por confirmar al llegar) |
| Tools | Tool `Get Pokemon` → `GET https://pokeapi.co/api/v2/pokemon/{name}` (creada antes: API + tool) |
| Metrics | Sin métricas personalizadas, salvo que sean obligatorias |
| Prompt | Prompt por capas: rol, reglas de uso de la tool, formato de respuesta |
| Memory | Activar memoria si el app lo permite (por confirmar) |
| RAG | Knowledge base con un documento corto de reglas de la Pokédex (generado por mí) |
| Security | Guardrails por defecto |
| LLM | Modelo por defecto del ambiente dev |
| Review | Revisar y guardar |

## Orden de implementación

1. Crear categoría propia (si el app lo permite) → **connection profile** `PokeAPI` (4 pasos: identificación, ruta `https://pokeapi.co/api/v2`, autenticación ninguna, confirmar) → **API** PokeAPI (3 pasos: info, connection profile, spec) → tool `Get Pokemon` (5 pasos).
2. Crear knowledge base con 1 documento y esperar a que se procese.
3. Crear el agente con el wizard (10 pasos), guardar y anotar el código `agent-XXXXXX`.
4. **Publicar** (genera PR automático en el repo del tenant; merge automático) — requiere aprobación explícita antes de hacerlo.
5. Verificar en el detalle del agente: estado *desplegado* y health check.
6. Enviar la solicitud real E2E y capturar la conversación en Monitoring.
7. Llenar runbook, tablero (O3 y O4) y `progreso.js`.

## Registro de tiempos por segmento

Ver `bitacora.md` (sección *Segmentos*), con las horas reales de la corrida.

> Nota: el plan original contemplaba memoria, métricas por defecto y RAG; en la corrida se añadió además una métrica personalizada (`Pokemon consultados`) y el connection profile se creó antes de la API, como exige el app.
