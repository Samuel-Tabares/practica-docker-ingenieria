# 1. Imagen base que incluye el JDK para compilar y ejecutar
# Nota: openjdk:17-slim fue descontinuada en Docker Hub; usamos el reemplazo oficial (Adoptium Temurin).
FROM eclipse-temurin:17-jdk

# 2. Directorio dentro del contenedor
WORKDIR /app

# 3. Copiar el código fuente de la máquina host
COPY Potencia.java .

# 4. Compilar el archivo Java para generar el bytecode (.class)
RUN javac Potencia.java

# 5. Ejecutar la clase compilada al iniciar el contenedor
CMD ["java", "Potencia"]
