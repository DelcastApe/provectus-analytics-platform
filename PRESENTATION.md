# Provectus Analytics: Approach & Findings

## 1. Architectural Approach
For this assignment, I designed a lightweight, reproducible architecture focused on efficiency and ease of deployment:
* **Local Storage (SQLite):** Chosen for its embedded nature, allowing the processing and querying of thousands of telemetry events without requiring external infrastructure or complex setups.
* **Efficient Processing (Pandas):** The `ingest.py` script reads the JSONL file line by line and enriches the data with the employee CSV, ensuring strict data type conversion (e.g., `cost_usd`).
* **Visualization (Streamlit):** Implemented for its rapid development of interactive dashboards. The `@st.cache_data` decorator was added to prevent redundant database queries and significantly improve user experience.
* **Deployment (Docker):** The entire solution is containerized to ensure it runs with a single command (`docker compose up`), eliminating local dependency issues.
* **AI Agent (.cursorrules):** A strict agent environment was defined to ensure that any future modifications respect the decoupled architecture and enforce data type validations.

## 2. Key Insights & Findings
Analyzing the telemetry dataset revealed the following usage patterns for Claude Code:
* **Volume & Cost:** Successfully processed nearly 50,000 events, generating an estimated total simulated cost of $652.18 during the analyzed period.
* **Task Distribution:** The vast majority of events correspond to tool usage (`tool_decision` and `tool_result`), indicating that developers heavily rely on the agent's autonomous capabilities and tool-calling features.
* **Stability:** The rate of `api_error` events is exceptionally low compared to successful requests, suggesting high reliability and stability in the users' working environment.