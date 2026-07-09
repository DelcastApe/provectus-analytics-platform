```markdown
# Claude Code Usage Analytics Platform

Plataforma de ingeniería de datos diseñada para procesar telemetría de uso de Claude Code y extraer insights accionables sobre el comportamiento del desarrollador.

## Arquitectura del Proyecto
La solución sigue un flujo de procesamiento de datos robusto y modular:
* **Ingesta (ETL):** Un script de Python (`src/ingest.py`) procesa los logs crudos en formato JSONL y los enriquece con metadatos de empleados desde un CSV[cite: 2].
* **Almacenamiento:** Se utiliza **SQLite** como motor de base de datos embebido, garantizando velocidad de consulta y portabilidad sin necesidad de servidores externos[cite: 2].
* **Visualización:** **Streamlit** se emplea para crear un dashboard interactivo que permite filtrar y analizar métricas de productividad, costos y errores en tiempo real[cite: 2].

## Instrucciones de Reproducción

### Requisitos previos
- Python 3.10+
- Entorno virtual configurado

### Comandos de ejecución
1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt

```

2. **Ejecutar Ingesta (Procesar datos):**
```bash
python3 src/ingest.py

```


3. **Iniciar el Dashboard:**
```bash
streamlit run src/dashboard.py

```



## Decisiones Técnicas

* **Agentes de IA:** El desarrollo se realizó utilizando un entorno configurado con `.cursorrules` para asegurar la calidad del código y la consistencia en el manejo de tipos de datos.


* **Manejo de Errores:** Se implementó validación explícita de tipos (especialmente en columnas numéricas como `cost_usd`) para asegurar la resiliencia del dashboard ante datos inconsistentes.


* **Escalabilidad:** La elección de SQLite y Pandas permite manejar volúmenes de datos significativos de manera eficiente en entornos locales y contenedores.



## Configuración del Agente

El proyecto incluye un archivo `.cursorrules` que define las reglas de estilo y las habilidades personalizadas (custom skills) para la IA, permitiendo que cualquier desarrollador o agente mantenga la integridad de la base de datos al realizar nuevas consultas o visualizaciones.

```

---

### Un consejo final para tu entrega:
Ya tienes todo listo. Para "bordar" la entrega, te sugiero crear un pequeño archivo llamado `requirements.txt` para que ellos puedan instalar todo automáticamente:

```bash
pip freeze > requirements.txt

```

