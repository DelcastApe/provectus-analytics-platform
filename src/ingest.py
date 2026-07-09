import pandas as pd
import json
import sqlite3
from pathlib import Path

def ingest_data():
    # Rutas dinámicas basadas en la ubicación de este script
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / 'data'
    
    logs_file = data_dir / 'telemetry_logs.jsonl'
    employees_file = data_dir / 'employees.csv'
    db_file = data_dir / 'telemetry.db'

    # Validación preventiva
    if not logs_file.exists() or not employees_file.exists():
        print(f"Error: No se encuentran los archivos de datos en {data_dir}")
        print("Asegúrate de ejecutar 'generate_fake_data.py' primero.")
        return

    print("--- Iniciando proceso de ingesta ---")
    conn = None
    
    try:
        # 1. Cargar empleados
        df_emp = pd.read_csv(employees_file)

        # 2. Cargar logs línea por línea (eficiente para archivos grandes)
        logs = []
        with open(logs_file, 'r', encoding='utf-8') as f:
            for line in f:
                batch = json.loads(line)
                for event in batch.get('logEvents', []):
                    msg = json.loads(event['message'])
                    
                    flat_event = {
                        'timestamp': event.get('timestamp'),
                        'body': msg.get('body'),
                        'event_name': msg['attributes'].get('event.name'),
                        'user_email': msg['attributes'].get('user.email'),
                        'duration_ms': msg['attributes'].get('duration_ms'),
                        'cost_usd': msg['attributes'].get('cost_usd', 0.0)
                    }
                    logs.append(flat_event)

        df_logs = pd.DataFrame(logs)
        
        # Limpieza y conversión estricta de tipos de datos
        df_logs['cost_usd'] = pd.to_numeric(df_logs['cost_usd'], errors='coerce').fillna(0.0)
        df_logs['duration_ms'] = pd.to_numeric(df_logs['duration_ms'], errors='coerce').fillna(0)

        # 3. Enriquecimiento de datos (Merge)
        df_final = pd.merge(df_logs, df_emp, left_on='user_email', right_on='email', how='left')

        # 4. Persistencia en base de datos
        conn = sqlite3.connect(db_file)
        df_final.to_sql('telemetry', conn, if_exists='replace', index=False)
        
        print(f"--- Proceso terminado con éxito. Base de datos creada en: {db_file.name} ---")
        
    except Exception as e:
        print(f"Error crítico durante la ingesta de datos: {e}")
        
    finally:
        # Garantiza que la conexión se cierre incluso si el script falla
        if conn:
            conn.close()

if __name__ == "__main__":
    ingest_data()