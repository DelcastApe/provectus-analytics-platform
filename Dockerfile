# Usamos una imagen ligera de Python 3.12 (la misma versión que usas localmente)
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requerimientos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del proyecto
COPY . .

# Exponemos el puerto de Streamlit
EXPOSE 8501

# Comando dual: primero ingesta los datos, luego levanta el dashboard
CMD python src/ingest.py && streamlit run src/dashboard.py --server.port=8501 --server.address=0.0.0.0