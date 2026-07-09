# Provectus Analytics: Approach & Findings

## 1. Architectural Approach
Para este reto, diseñé una arquitectura ligera y reproducible enfocada en la eficiencia y la facilidad de despliegue:
* **Almacenamiento Local (SQLite):** Elegido por su naturaleza embebida, permitiendo procesar y consultar miles de eventos de telemetría sin requerir infraestructura externa.
* **Procesamiento Eficiente (Pandas):** El script `ingest.py` lee el archivo JSONL línea por línea y enriquece los datos con el CSV de empleados, asegurando la conversión estricta de tipos de datos (ej. `cost_usd`).
* **Visualización (Streamlit):** Implementado por su rapidez para construir paneles interactivos. Se añadió `@st.cache_data` para evitar accesos redundantes a la base de datos y mejorar la experiencia del usuario.
* **Despliegue (Docker):** Toda la solución está contenerizada para garantizar que se ejecute con un solo comando (`docker compose up`), eliminando problemas de dependencias locales.
* **Agente IA (.cursorrules):** Se definió un entorno de agente estricto para asegurar que cualquier modificación futura respete la arquitectura y valide los tipos de datos.

## 2. Key Insights & Findings
Al analizar el dataset de telemetría, destacan los siguientes patrones de uso de Claude Code:
* **Volumen y Costo:** Se procesaron exitosamente casi 50,000 eventos, generando un costo simulado total de $652.18 durante el periodo analizado.
* **Distribución de Tareas:** La gran mayoría de los eventos corresponden al uso de herramientas (`tool_decision` y `tool_result`), lo que indica que los desarrolladores confían fuertemente en las capacidades autónomas del agente.
* **Estabilidad:** La tasa de eventos `api_error` es excepcionalmente baja en comparación con las peticiones exitosas, sugiriendo una alta confiabilidad en el entorno de los usuarios.