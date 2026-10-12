# Piloto 1 — Bitácora (2026-10-12)

Ambiente: https://hexagon-dev.soincloud.com · Agente: **Pokedex Assistant** (`agent-000053`, `/agents/1444`) · Caso: consultas de Pokémon contra PokeAPI.

Horas locales (UTC-6).

## Resultado

| Criterio de O3 | Resultado | Evidencia |
|---|---|---|
| Desplegado en dev | Sí — `v1.0.0`, estado "Desplegado · Working" | PR https://github.com/SoinLabs/KolbiTappAgents/pull/400 (mergeado 13:56:46) |
| Health check OK | Sí — panel *Diagnosis* del detalle del agente | `health-diagnostico.jpg` |
| Solicitud real E2E | Sí — "¿Qué tipo es Pikachu y cuáles son sus habilidades?" | `e2e-conversacion.jpg`, sesión `bbb396a4-1223-48ef-80e8-cb0b6ee33134` en Monitoring |

Respuesta del agente: Pikachu, tipo eléctrico, habilidades static y lightning-rod (oculta), altura 0.4 m, peso 6 kg (coincide con PokeAPI y con la regla de conversión de unidades de la knowledge base). La métrica personalizada `Pokemon consultados` registró 1 evento, lo que confirma que se llamó a la tool `Get Pokemon`.

## Segmentos (para O4)

| # | Segmento | Inicio | Fin | Duración | Notas |
|---|---|---|---|---|---|
| 1 | Definición | 12:46:42 | 12:48:43 | ≈2 min | Navegación del app, plan y aprobación. No incluye el login ni la conversación previa |
| 2 | Configuración en AgentPlatform | 12:48:46 | 13:00:13 | ≈11.5 min | Connection profile, API, tool, knowledge base y wizard del agente (10 pasos) |
| 3 | Publicación (PR) | 13:55:16 | 13:56:46 | ≈1.5 min | PR abierto y mergeado automáticamente. Entre 13:00 y 13:55 se esperó la aprobación y el clic en *Deploy* (tiempo humano, no cuenta) |
| 4 | Despliegue dev + health | 13:56:46 | ≤14:04:31 | ≤7.75 min | Cota superior: es la hora en que se verificó, no la hora exacta en que quedó *Working* |
| 5 | Prueba E2E | 14:04:49 | 14:05:12 | ≈0.4 min | Un solo mensaje, respuesta en 4 s |

Total activo ≈ 23 min (≈0.39 h). Con la espera de aprobación, de 12:46 a 14:05 ≈ 1 h 19 min.

## Recursos creados

| Hora local | Recurso | Código / URL | Notas |
|---|---|---|---|
| 12:49:36 | Connection profile `PokeAPI Profile` | `connprof-000041` · /apis/connection-profiles/581 | Base URL `https://pokeapi.co`, sin autenticación, nodo `pokeapi.co:443`, ruta `kolbi-route-connprof-000041-dev` publicada (201) |
| ≈12:50 | API `PokeAPI` v2.0 | /apis/862 | OpenAPI 3.0.3 pegada con "Paste code" (`pokeapi-openapi.json`), 1 operación `GET /api/v2/pokemon/{name}`, sin categoría |
| 12:51:48 | Tool `Get Pokemon` | `tool-000122` · /tools/1307 | Parámetro `name` + 8 propiedades de respuesta, descripciones para el agente, sin confirmación de usuario (solo lectura) |
| ≈12:54 | Knowledge base `Pokedex Rules` | `kb-000010` · /knowledge-base/202 | Categoría "Prueba", `MULTILINGUAL_E5_SMALL`, chunk 180 palabras, overlap 15%. `pokedex-reglas.txt` → Ready, 1,250 caracteres, 2 chunks. Documento con categoría "Recursos Humanos" y tipo "Manual" (únicas opciones razonables; corregir si hay otra) |
| 13:00 | Agente `Pokedex Assistant` | `agent-000053` · /agents/1444 | Tipo Agent, categoría Prueba, For conversation. Tool `Get Pokemon`; métrica `Pokemon consultados` (Counter, cualquier 2xx); prompt por capas (Rol, Contexto, Tarea, Cómo trabaja, Formato, Tono, Boundaries ×2 = 7/10 capas); memoria dentro y entre conversaciones; KB `Pokedex Rules`; sin canales; OpenAI GPT-5.4 Mini |
| 13:55:16 | PR `Agent: agent-000053@1.0.0` | SoinLabs/KolbiTappAgents#400 | Mergeado 13:56:46, commit `464399d` |

## Propiedades ejercitadas

Prompt por capas ✔ · Tool contra API (vía connection profile) ✔ · Métricas personalizadas ✔ · Memoria (dentro y entre conversaciones) ✔ · Knowledge base (RAG) ✔ · Modelo LLM ✔ · Seguridad: sin canales · Pendientes (opcionales): Examples y Guardrails de entrada/salida, Profile (Expediente), A2A.

## Observaciones sobre el app (para el runbook)

- Los wizards (connection profile 4 pasos, API 3 pasos, tool 5 pasos, agente 10 pasos) se pueden recorrer sin guardar borrador.
- El selector de profile en el wizard de API queda parcialmente tapado por la barra inferior; la opción existe aunque solo se vea "+ Create profile".
- La API pública no requiere autenticación: plantilla "No Authentication".
- En el paso 4 de la tool todas las propiedades exigen "Description for agent".
- Crear una knowledge base falló la primera vez con `ORA-20005: La extension "tif" esta en la ruta de OCR pero no en los tipos permitidos`. Solución: agregar TIF y TIFF a *Allowed types*.
- El diálogo *Upload documents* exige categoría de documento y tipo (Otro, Reporte, Contrato, Manual, Política); solo existen las categorías de documento "Recursos Humanos" y "Campaign manager".
- Tras subir un documento aparece un aviso transitorio "failed —" aunque el documento queda `Ready`; al recargar desaparece.
- Wizard de agente, paso Prompt: las capas con lista (Boundaries) solo cuentan como definidas con "Add" (catálogo o texto propio + categoría). Las capas de texto se confirman al abrir otra capa.
- Wizard de agente: Security acepta cero canales; Profile (Expediente) en Memory requiere definir campos.
- Wizard de agente: Metrics exige tool disparadora y condición de éxito (por defecto cualquier 2xx).
- Tras *Deploy* el PR se abre y se mergea solo (≈1.5 min). El detalle del agente muestra *Desplegado · Working*, *View PR*, *Diagnosis* y *Test agent*.
- *Diagnosis* muestra: versión en ejecución, LLM Gateway, credencial de ejecución, Tool Gateway (aparece "Reachable (401)": el gateway responde, el 401 es el sondeo sin credencial), memoria de corto y largo plazo.
- El PR incluye `tools.generated/arithmeticCalculator.js` además del tool REST de PokeAPI: es código base del generador: `agent-definition.generated.json` lista únicamente `tool-000122` (`Get Pokemon`).
- Monitoring marcó 1 de 4 solicitudes con error (25%) en el periodo; no se investigó la causa (el costo por categoría muestra "Health checks" aparte).
