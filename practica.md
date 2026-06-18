# Guía Teórico-Práctica: Introducción a Docker y Contenedorización

**Duración Estimada:** 3 horas (Sesión de Laboratorio)

---

## 1. Objetivo General

Al finalizar esta guía, el estudiante estará en la capacidad de:

- Explicar qué es Docker, identificando su utilidad y ventajas competitivas frente a la instalación tradicional de aplicaciones y la virtualización de hardware.
- Comprender e interrelacionar los conceptos fundamentales del ecosistema Docker: Imagen, Contenedor, Dockerfile, Repositorio, Volumen y Red.
- Construir, empaquetar y ejecutar aplicaciones multiplataforma (Python y Java) dentro de contenedores aislados.

---

## 2. Contenido Teórico

### Introducción a la Virtualización y la Contenedorización

Tradicionalmente, para desplegar una aplicación se requería instalar el sistema operativo, las dependencias, librerías y configuraciones directamente sobre el hardware (servidor) o dentro de una Máquina Virtual (VM). Esto solía causar el clásico problema: *"En mi máquina funciona, pero en producción no"*.

Docker surge para resolver esto mediante la **contenedorización**. Es una tecnología de código abierto que automatiza el despliegue de aplicaciones dentro de entornos aislados llamados contenedores. A diferencia de las máquinas virtuales, los contenedores comparten el kernel del sistema operativo del host, lo que los hace extremadamente ligeros y rápidos.

---

### Arquitectura de Docker

Docker utiliza una arquitectura **Cliente-Servidor**:

- **Docker Client:** La interfaz de línea de comandos (`docker` CLI) que utiliza el usuario para interactuar con Docker.
- **Docker Host (Daemon - `dockerd`):** El servicio en segundo plano que escucha las peticiones de la API de Docker y gestiona los objetos (imágenes, contenedores, redes y volúmenes).
- **Docker Registry (Hub):** El lugar (público o privado) donde se almacenan y distribuyen las imágenes de Docker.

```
[ Docker Client ]  --->  [ Docker Daemon (Host) ]  --->  [ Docker Hub ]
   (run, build)            (Gestiona Contenedores)        (Descarga Imágenes)
```

---

### Diferencias: Máquinas Virtuales vs. Contenedores

| Característica   | Máquinas Virtuales (VMs)                     | Contenedores (Docker)                        |
|------------------|----------------------------------------------|----------------------------------------------|
| Arquitectura     | Incluyen un SO completo por VM.              | Comparten el Kernel del SO Host.             |
| Peso / Tamaño    | Pesadas (Gigabytes - GB).                    | Ligeras (Megabytes - MB).                    |
| Tiempo de Inicio | Minutos (debe arrancar todo el SO).          | Segundos o milisegundos.                     |
| Rendimiento      | Menor, debido a la sobrecarga del Hipervisor.| Casi nativo, ejecución directa en el kernel. |
| Aislamiento      | Aislamiento completo a nivel de hardware.    | Aislamiento a nivel de procesos del SO.      |

---

### Conceptos Clave

| Concepto       | Descripción |
|----------------|-------------|
| **Dockerfile** | Archivo de texto plano con instrucciones secuenciales para construir una imagen. |
| **Imagen**     | Plantilla de solo lectura que contiene el código, entorno de ejecución, librerías y configuraciones necesarias. |
| **Contenedor** | Una instancia ejecutable y viva de una imagen. |
| **Volumen**    | Mecanismo de almacenamiento persistente para guardar datos fuera del ciclo de vida del contenedor. |
| **Red (Network)** | Canal virtual que permite la comunicación entre contenedores o con el mundo exterior. |

---

### Casos de Uso en la Industria

- **Microservicios:** Aislar componentes de software independientes de forma masiva.
- **CI/CD:** Garantizar que el entorno de pruebas sea exactamente idéntico al de producción.
- **Portabilidad Local:** Configurar bases de datos complejas (PostgreSQL, Redis) en segundos para desarrollo local sin ensuciar el SO del desarrollador.

---

### Buenas Prácticas de Uso

- **Un proceso por contenedor:** Cada contenedor debe cumplir una única función (Principio de Responsabilidad Única).
- **Contenedores efímeros:** Deben poder destruirse y recrearse sin pérdida de datos (usando volúmenes para la persistencia).
- **Usar imágenes base oficiales y ligeras:** Preferir versiones `alpine` o `slim` para reducir el tamaño y los vectores de vulnerabilidad.
- **Aprovechar la caché de capas:** Colocar las instrucciones que menos cambian (como la instalación de dependencias) al principio del Dockerfile.

---

## 3. Práctica Guiada Paso a Paso

### Instalación de Docker

#### A. Windows

1. Descargue Docker Desktop desde el sitio web oficial.
2. Asegúrese de tener habilitado **WSL 2** (Windows Subsystem for Linux) en su sistema.
3. Ejecute el instalador, complete el asistente y reinicie la computadora.

#### B. macOS

1. Descargue el instalador de Docker Desktop (elija la versión Intel o Apple Silicon según su procesador).
2. Arrastre Docker a la carpeta de Aplicaciones y ejecútelo.

---

### Verificación de la Instalación

Abra una terminal (PowerShell, Bash o Zsh) y ejecute:

```bash
docker --version
```

> Muestra la versión actual de Docker instalada en el sistema para confirmar que el cliente CLI está disponible.

---

### Comandos Esenciales de Docker

| Comando                    | Propósito |
|----------------------------|-----------|
| `docker pull <imagen>`     | Descarga una imagen desde Docker Hub al equipo local sin ejecutarla. |
| `docker images`            | Lista todas las imágenes de Docker guardadas localmente. |
| `docker run <opciones> <imagen>` | Crea y arranca un nuevo contenedor basado en una imagen específica. |
| `docker ps`                | Lista únicamente los contenedores en ejecución. |
| `docker ps -a`             | Lista todos los contenedores (activos, pausados y detenidos). |
| `docker stop <id_o_nombre>`| Envía una señal de parada segura a un contenedor activo. |
| `docker start <id_o_nombre>`| Vuelve a iniciar un contenedor detenido. |
| `docker rm <id_o_nombre>`  | Elimina de forma permanente un contenedor detenido. |
| `docker rmi <id_imagen>`   | Elimina una imagen local (no debe tener contenedores asociados). |

---

### Ejercicio de Calentamiento: Hola Mundo

```bash
docker run hello-world
```

> Docker buscará la imagen localmente; si no la encuentra, la descargará de Docker Hub, creará el contenedor, imprimirá un mensaje de éxito y detendrá el proceso de forma inmediata.

---

## 4. Ejercicio Práctico Principal: Cálculo de Potencia

Para aplicar estos conceptos, crearemos un programa que calcula la potencia de un número mediante la fórmula:

$$P = b^e$$

Donde:
- **b** = Base (número real o entero)
- **e** = Exponente (número entero positivo o cero)

### Algoritmo

1. Solicitar al usuario ingresar la base.
2. Solicitar al usuario ingresar el exponente.
3. Validar que el exponente sea un número entero no negativo.
4. Calcular la potencia.
5. Imprimir el resultado.

### Diagrama de Flujo

```
[Inicio]
   │
   ▼
[Leer Base (b)]
   │
   ▼
[Leer Exponente (e)]
   │
   ▼
¿e es válido? ──(No)──> [Mostrar Error y Terminar]
   │ (Sí)
   ▼
[Calcular P = b ^ e]
   │
   ▼
[Mostrar "Resultado: P"]
   │
   ▼
[Fin]
```

---

## 5. Implementación en Python

### Paso 1: Crear el archivo `app.py`

Cree una carpeta llamada `docker-python` y guarde el siguiente código en `app.py`:

```python
import sys

def calcular_potencia():
    print("=== CALCULADORA DE POTENCIA EN DOCKER (PYTHON) ===")
    try:
        base = float(input("Ingrese la base (b): "))
        exponente = int(input("Ingrese el exponente entero (e): "))

        if exponente < 0:
            print("Error: El exponente debe ser un entero no negativo.")
            return

        resultado = base ** exponente
        print(f"\nResultado Exitoso: {base} elevado a la {exponente} es = {resultado}")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    calcular_potencia()
```

### Paso 2: Explicación del código

- `input()`: Pausa el programa para leer los datos que el usuario tipea.
- `base ** exponente`: Operador aritmético nativo de Python para potencias.
- `try-except`: Captura entradas inválidas (texto en lugar de números) sin cerrar abruptamente el programa.

### Paso 3: Crear el `Dockerfile`

En la misma carpeta, cree un archivo llamado exactamente `Dockerfile` (sin extensión):

```dockerfile
# 1. Imagen base oficial de Python ligera
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Copiar el archivo de código fuente al contenedor
COPY app.py .

# 4. Comando por defecto para ejecutar la aplicación al arrancar
CMD ["python", "app.py"]
```

### Paso 4: Construir la imagen y ejecutar el contenedor

Desde la carpeta `docker-python`:

```bash
# Construir la imagen asignándole el tag 'potencia-py'
docker build -t potencia-py .

# Ejecutar el contenedor interactivo
docker run -it --name contenedor-py potencia-py
```

> **Nota:** El flag `-it` es obligatorio porque la aplicación requiere interactividad para capturar las entradas del teclado.

**Salida esperada:**

```
=== CALCULADORA DE POTENCIA EN DOCKER (PYTHON) ===
Ingrese la base (b): 5
Ingrese el exponente entero (e): 3

Resultado Exitoso: 5.0 elevado a la 3 es = 125.0
```

---

## 6. Implementación en Java

### Paso 1: Crear la clase `Potencia.java`

Cree una carpeta independiente llamada `docker-java` y dentro de ella genere el archivo `Potencia.java`:

```java
import java.util.Scanner;

public class Potencia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== CALCULADORA DE POTENCIA EN DOCKER (JAVA) ===");

        try {
            System.out.print("Ingrese la base (b): ");
            double base = scanner.nextDouble();

            System.out.print("Ingrese el exponente entero (e): ");
            int exponente = scanner.nextInt();

            if (exponente < 0) {
                System.out.println("Error: El exponente debe ser no negativo.");
                return;
            }

            double resultado = Math.pow(base, exponente);
            System.out.printf("\nResultado Exitoso: %.2f elevado a la %d es = %.2f\n", base, exponente, resultado);

        } catch (Exception e) {
            System.out.println("Error: Entrada inválida. Intente de nuevo.");
        } finally {
            scanner.close();
        }
    }
}
```

### Paso 2: Explicación del código

- `Scanner scanner`: Lee y procesa flujos de entrada estándar (consola).
- `Math.pow(base, exponente)`: Función de `java.lang` que retorna la potencia en formato `double`.
- `scanner.close()`: Libera el recurso de lectura al finalizar.

### Paso 3: Crear el `Dockerfile`

Dentro de la carpeta `docker-java`:

```dockerfile
# 1. Imagen base que incluye el JDK para compilar y ejecutar
FROM openjdk:17-slim

# 2. Directorio dentro del contenedor
WORKDIR /app

# 3. Copiar el código fuente de la máquina host
COPY Potencia.java .

# 4. Compilar el archivo Java para generar el bytecode (.class)
RUN javac Potencia.java

# 5. Ejecutar la clase compilada al iniciar el contenedor
CMD ["java", "Potencia"]
```

### Paso 4: Construir la imagen y ejecutar el contenedor

Desde la carpeta `docker-java`:

```bash
# Construir la imagen de Java
docker build -t potencia-java .

# Ejecutar el contenedor de Java de forma interactiva
docker run -it --name contenedor-java potencia-java
```

**Salida esperada:**

```
=== CALCULADORA DE POTENCIA EN DOCKER (JAVA) ===
Ingrese la base (b): 2
Ingrese el exponente entero (e): 8

Resultado Exitoso: 2,00 elevado a la 8 es = 256,00
```

---

## 7. Actividades para el Estudiante

### Preguntas de Análisis

1. ¿Qué sucede con el archivo `.class` generado en la compilación de Java cuando el contenedor se detiene y destruye?
2. Si ejecuta `docker run` sin el parámetro `-it`, ¿qué comportamiento observa en la consola y por qué ocurre esto?

### Actividades de Experimentación

1. Ejecute `docker ps -a` y documente cuántos contenedores permanecen almacenados en el disco duro.
2. Utilice `docker inspect <id_contenedor>` para averiguar cuál es la dirección IP interna asignada a su contenedor de Python.

### Retos de Dificultad Media

1. **Modificación del código:** Modifique `app.py` para que, en lugar de terminar tras dar el resultado, use un ciclo `while True` que pregunte si desea realizar otro cálculo o salir escribiendo `salir`.
2. **Actualización de imagen:** Tras cambiar el código, intente arrancar el contenedor con `docker start -i contenedor-py`. ¿Se ven reflejados los cambios? Explique el procedimiento correcto para actualizar una aplicación contenerizada.

---

## 8. Evaluación — Cuestionario (10 Preguntas)

**1. ¿Cuál es la función principal del Docker Daemon?**
> Escuchar las solicitudes de la API de Docker y gestionar los objetos del sistema como contenedores, imágenes, volúmenes y redes.

**2. ¿Qué comando se utiliza para descargar una imagen de Docker Hub sin iniciarla?**
> `docker pull <nombre_imagen>`

**3. ¿Cuál es la diferencia técnica fundamental entre un Dockerfile y una Imagen?**
> El Dockerfile es el archivo de recetas en texto plano; la Imagen es la plantilla binaria empaquetada resultante de compilar dicho Dockerfile.

**4. ¿Para qué sirve el parámetro `-it` al ejecutar un contenedor?**
> Habilita una TTY simulada y mantiene abierta la entrada estándar (`stdin`) para interactuar con la consola de la aplicación en tiempo real.

**5. ¿Qué comando muestra todos los contenedores, incluidos los que ya finalizaron su ejecución?**
> `docker ps -a`

**6. Si borras un contenedor con `docker rm`, ¿se borra también su imagen base?**
> No. El contenedor es una instancia independiente. La imagen permanece intacta hasta que se use explícitamente `docker rmi`.

**7. ¿Por qué los contenedores pesan considerablemente menos que una máquina virtual tradicional?**
> Porque no incluyen un sistema operativo completo huésped; utilizan y comparten el kernel del sistema operativo del host.

**8. ¿Qué instrucción del Dockerfile define el comando por defecto que se dispara al iniciar el contenedor?**
> La instrucción `CMD`.

**9. ¿Qué comando se debe utilizar para eliminar una imagen local específica?**
> `docker rmi <id_o_nombre_imagen>`

**10. ¿Qué sucede si ejecutas `docker run` con una imagen que no ha sido descargada previamente?**
> Docker detecta automáticamente su ausencia local, realiza un `pull` automático desde Docker Hub y luego procede a iniciar el contenedor de forma normal.

---

## 9. Conclusiones y Recomendaciones

### Resumen de Conceptos Clave

- La contenedorización permite aislar software con sus dependencias exactas, garantizando portabilidad e inmutabilidad en cualquier servidor compatible.
- El ciclo básico en Docker: **Escribir código → Configurar Dockerfile → Construir imagen (`build`) → Lanzar contenedor (`run`)**.
- El uso de flags interactivos (`-it`) abre un puente directo entre el usuario y la aplicación distribuida interna.

### Recomendaciones para Continuar Aprendiendo

- **Docker Compose:** Permite coordinar múltiples contenedores (app + base de datos + otros servicios) mediante un único archivo YAML.
- **Multi-stage builds:** Patrón avanzado para crear imágenes de producción con el menor tamaño posible.
- **Docker Hub:** Explore imágenes oficiales de Nginx, MySQL, MongoDB y Node.js para experimentar con despliegues rápidos.
