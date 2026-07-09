# Claude Code Usage Analytics Platform

An end-to-end data engineering and analytics platform designed to process Claude Code telemetry data, extract insights, and present actionable metrics through an interactive dashboard[cite: 2].

## 🏗️ Architectural Overview
The solution follows a robust, decoupled data processing pipeline:
* **Data Ingestion (ETL):** A Python script (`src/ingest.py`) processes raw telemetry logs in JSONL format, enriches them with user metadata from a CSV, and enforces strict data type casting (e.g., parsing `cost_usd` safely).
* **Storage:** **SQLite** is used as an embedded database. It ensures high-speed querying and perfect portability without requiring external server configurations.
* **Visualization:** **Streamlit** powers the interactive dashboard (`src/dashboard.py`). It utilizes `@st.cache_data` to minimize database hits and provides real-time filtering and metrics calculation.

## 🚀 How to Run (Single Command Execution)
The entire application is containerized to ensure full reproducibility across any environment without local dependency conflicts. The solution starts with a single documented command[cite: 2].

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Execution
1. Unzip/Clone this repository and navigate to the root directory.
2. Run the following command to build and start the platform:
   ```bash
   docker compose up --build
3. Open your web browser and navigate to: http://localhost:8501

*Note: The Docker container will automatically execute the data ingestion script first, generate the SQLite database locally, and then spin up the Streamlit dashboard.*

## 🧠 Agent Setup & Tuning

This project was developed using **Cursor** as the primary agentic IDE.
The repository includes a `.cursorrules` file that acts as the core instruction set for the AI agent, fulfilling the requirement to commit the complete agent setup to the repository. This setup ensures that the LLM:

1. Understands the decoupled architecture (ingest vs. dashboard).
2. Consistently applies strict data type conversions before database operations.
3. Uses Streamlit best practices for any new UI components.
4. Operates efficiently within the local `data/` directory constraints.

## 🤖 LLM Usage Documentation

As per the assignment requirements, AI-assisted development was utilized to accelerate and optimize the build, and the documentation of LLM usage and generated components is provided below:

* **Data Processing (`src/ingest.py`):** The LLM was used to optimize the JSONL line-by-line parsing logic (to handle large files efficiently without memory bottlenecks) and to generate the Pandas merging logic.
* **Dashboard (`src/dashboard.py`):** AI assisted in structuring the Streamlit layout (columns, metrics, charts) and implementing data caching (`@st.cache_data`) to improve UI responsiveness.
* **Infrastructure (`Dockerfile` & `docker-compose.yml`):** The containerization configuration was generated and refined through agentic prompts to satisfy the "single documented command" requirement seamlessly.



## 📁 Project Structure

* `src/ingest.py`: ETL pipeline script.
* `src/dashboard.py`: Streamlit frontend application.
* `data/`: Directory containing source data (`telemetry_logs.jsonl`, `employees.csv`) and the generated `telemetry.db` file.
* `.cursorrules`: Custom skills, rules, and context for the AI agent.


* `.env.example`: Template for environment variables (security best practice).


* `docker-compose.yml` & `Dockerfile`: Containerization and orchestration setup.
* `PRESENTATION.md`: Summary of analytical findings, insights, and technical decisions.


* `requirements.txt`: Python dependencies for alternative local execution.