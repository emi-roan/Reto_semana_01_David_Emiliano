# Reto 1: Calculadora de Sumas
Proyecto de Programación para Ciencia de Datos - ESCOM.
## Desarrollo Técnico del Proyecto

### 1. Limpieza y Normalización de Datos (Preprocessing)
El principal reto fue procesar entradas "sucias". Implementamos una lógica de filtrado utilizando el método `.strip()` para eliminar espacios en blanco residuales y una estructura de control que permite ignorar caracteres alfabéticos. Esto asegura que solo los componentes numéricos (`0-9`), el punto decimal (`.`) y el signo negativo (`-`) lleguen a la etapa de conversión.

### 2. Lógica de Truncado vs. Redondeo
A diferencia de una calculadora estándar que redondea al entero más cercano, este desarrollo aplica un **truncado estricto**. 
* **Implementación:** Se utiliza la conversión directa a `int()` tras la validación del flujo.
* **Impacto:** Si la entrada es `19.99`, el sistema procesa `19`. Esto es fundamental en análisis de datos donde se requiere la parte entera exacta para indexación o conteo de ciclos completos.

### 3. Gestión de Robustez (Error Handling)
Para evitar que el programa "truene" ante entradas vacías o caracteres especiales imprevistos, se implementó un bloque `try-except`. 
* **ValueError:** Captura cualquier intento de conversión fallida (por ejemplo, si el usuario ingresa solo letras o símbolos raros).
* **Flujo Continuo:** En lugar de detener la ejecución, el programa notifica el error de forma silenciosa o lo ignora para continuar con la siguiente línea del flujo de datos, garantizando la integridad del proceso hasta el final del archivo.

### 4. Flujos de Entrada Estándar (Standard Streams)
Se optó por el uso de la librería `sys` para manejar `sys.stdin`. Esto permite que el script sea parte de un **pipeline** de comandos en la terminal, facilitando la automatización:
```bash
cat datos.txt | python main.py
