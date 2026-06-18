# 1. Imagen base oficial de Python ligera
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Copiar el archivo de código fuente al contenedor
COPY app.py .

# 4. Comando por defecto para ejecutar la aplicación al arrancar
CMD ["python", "app.py"]
