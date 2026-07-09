import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

# 1. Configuración principal de la página
st.set_page_config(page_title="Claude Code Analytics", page_icon="📊", layout="wide")

# 2. Caché para evitar consultas repetitivas a la base de datos
@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent.parent
    db_file = base_dir / 'data' / 'telemetry.db'
    
    # Validar que la base de datos exista antes de intentar conectar
    if not db_file.exists():
        return None
        
    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql_query("SELECT * FROM telemetry", conn)
        # Limpieza de datos numéricos
        df['cost_usd'] = pd.to_numeric(df['cost_usd'], errors='coerce').fillna(0.0)
        return df
    except Exception as e:
        st.error(f"Error al cargar la base de datos: {e}")
        return None
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    st.title("📊 Claude Code Telemetry Dashboard")
    
    df = load_data()
    
    if df is None or df.empty:
        st.warning("⚠️ No se encontró la base de datos. Por favor, ejecuta 'python3 src/ingest.py' primero.")
        return

    # 3. Sidebar interactivo para filtros
    st.sidebar.header("Filtros del Dashboard")
    if 'practice' in df.columns:
        practice_filter = st.sidebar.multiselect(
            "Filtrar por Departamento:", 
            options=df['practice'].dropna().unique(),
            default=df['practice'].dropna().unique()
        )
        # Aplicar el filtro
        df_filtered = df[df['practice'].isin(practice_filter)]
    else:
        df_filtered = df

    # 4. Métricas rápidas actualizadas según el filtro
    st.subheader("Métricas Generales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Eventos Totales", f"{len(df_filtered):,}")
    col2.metric("Usuarios Únicos", df_filtered['user_email'].nunique())
    
    total_cost = df_filtered['cost_usd'].sum()
    col3.metric("Costo Total Est.", f"${total_cost:.2f}")

    # 5. Gráficos distribuidos en columnas para mejor uso del espacio
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Distribución de Eventos")
        event_counts = df_filtered['event_name'].value_counts()
        st.bar_chart(event_counts)
        
    with col_chart2:
        st.subheader("Costo por Tipo de Evento")
        cost_by_event = df_filtered.groupby('event_name')['cost_usd'].sum().sort_values(ascending=False)
        st.bar_chart(cost_by_event)

    # 6. Tabla interactiva
    st.subheader("Detalle de Eventos")
    st.dataframe(df_filtered.head(100), use_container_width=True)

if __name__ == "__main__":
    main()