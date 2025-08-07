# Imagen base con Java 17
FROM openjdk:17-slim

# Establecer variables de entorno
ENV PYSPARK_PYTHON=python3

# Instalar Python y dependencias básicas
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer puerto si usás Flask o similar (opcional)
EXPOSE 5000

# Comando por defecto al correr el contenedor
CMD ["python3", "app.py"]
