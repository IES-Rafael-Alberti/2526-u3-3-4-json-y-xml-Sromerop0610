# Práctica 3.4: JSON y XML

Apóyate en los siguientes recursos para realizar la práctica:

* U3: JSON
* U3: XML

---

# Título de la Actividad

Práctica 3.4 — Gestión de Usuarios con JSON y XML

---

# Identificación de la Actividad

* **ID de la Actividad:** P3.4
* **Módulo:** PROG
* **Unidad de Trabajo:** Unidad 3 — Manejo de Ficheros (JSON y XML)
* **Fecha de Creación:** 28/11/2025
* **Fecha de Entrega:** 29/11/2025

**Alumno:**

* **Nombre y Apellidos:** Sara Romero Peralta
* **Correo electrónico:** [sromper0610@g.educaand.es](mailto:sromper0610@g.educaand.es)
* **Iniciales:** SRP

---

# Descripción de la Actividad

Esta práctica está compuesta por tres ejercicios independientes:

### **Ejercicio 1 — json.py**

Miniaplicación que gestiona usuarios almacenados en un fichero JSON. Debe copiar un archivo origen, mostrar los datos, modificar usuarios, insertar nuevos, eliminar existentes y guardar los cambios.

### **Ejercicio 2 — xml.py**

Miniaplicación equivalente al ejercicio JSON, pero trabajando con archivos XML y gestionando nodos mediante `xml.etree.ElementTree`.

### **Ejercicio 3 — examen.py**

Programa sencillo indicado verbalmente por el profesor. Contiene un diccionario con datos de una persona y realiza:

1. Mostrar datos actuales
2. Modificar valores del diccionario
3. Añadir claves nuevas
4. Eliminar claves
5. Volver a mostrar el diccionario resultante

Los tres programas deben funcionar de forma independiente y cumplir el flujo de ejecución solicitado.

---

# Instrucciones de Compilación y Ejecución

## Requisitos Previos

* Python 3.10+
* Editor recomendado: VS Code o PyCharm
* No requiere librerías externas.

## Ejecutar cada ejercicio

### Ejecutar JSON:

```
python src/json.py
```

### Ejecutar XML:

```
python src/xml.py
```

### Ejecutar el Ejercicio 3:

```
python src/json_a_xml.py
```

---

# Desarrollo de la Actividad

## Descripción del Desarrollo

Los tres programas se han desarrollado en Python utilizando estructura modular y funciones claramente diferenciadas.

---

## Ejercicio 1: json.py

Se implementaron funciones para:

* `inicializar_datos()`: copia el archivo original y gestiona errores
* `cargar_json()` y `guardar_json()`: lectura y escritura del fichero
* `mostrar_datos()`: muestra todos los usuarios
* Gestión de usuarios:

  * `actualizar_usuario()`
  * `insertar_usuario()`
  * `eliminar_usuario()`

El `main()` realiza todas las operaciones en el orden pedido por el profesor.

---

## Ejercicio 2: xml.py

Funciones desarrolladas:

* `inicializar_datos()`: copia el XML origen
* `cargar_xml()`: lectura segura, detecta corrupción
* `crear_arbol()`: genera estructura válida si el archivo está dañado
* `mostrar_datos()`: imprime nodos `<usuario>`
* Gestión mediante ElementTree:

  * `actualizar_edad()`
  * `insertar_usuario()`
  * `eliminar_usuario()`

Se reprodujo el flujo indicado en el enunciado, incluyendo limpieza de consola y pausas.

---

## Ejercicio 3: examen.py

Este ejercicio contiene un diccionario denominado `persona = {"nombre": "...", "edad": ..., "curso": "..."}`.

El programa implementa:

* Mostrar los datos iniciales
* Cambiar valores de claves existentes
* Añadir nuevas claves
* Eliminar claves
* Mostrar el diccionario final

Es un programa directo, sin uso de archivos, pero forma parte oficial de la entrega.

---

# Enlaces al Código
[Ejercicios](src)
---

# Ejemplos de Ejecución

## JSON (resumen)

```
Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---
```

## XML (resumen)

```
Datos inicializados desde 'datos_usuarios_orig.xml' a 'datos_usuarios.xml'.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---
```

## Ejercicio 3 (resumen)

```
Datos actuales:
{'nombre': 'Sara', 'edad': 19, 'curso': '1ºDAM'}

Modificando edad...
Añadiendo clave nueva...

Diccionario final:
{'nombre': 'Sara', 'edad': 20, 'curso': '1ºDAM', 'telefono': '123456789'}
```

---

# Resultados de Pruebas

Las pruebas realizadas verifican:

* Manejo de errores en archivos inexistentes
* Detección de JSON o XML corruptos
* Actualización correcta de datos
* Inserción con ID correcto
* Eliminación segura de entradas
* Recreación de XML vacío cuando corresponde

---

# Documentación Adicional

* Manual de usuario: No necesario
* El profesor debe tener permisos de lectura en el repositorio

---

# Conclusiones

La práctica ha permitido comprender:

* Lectura y escritura de datos en JSON
* Manipulación de árboles XML con ElementTree
* Diseño modular usando funciones
* Aplicación de flujos de trabajo típicos de CRUD
* Manejo de excepciones y archivos corruptos

Se podrían implementar mejoras como menús interactivos, validación adicional y persistencia avanzada.

---

# Referencias y Fuentes

* Documentación oficial de Python:
  json
  xml.etree.ElementTree
* Material de clase
* Ejemplos mostrados en el aula

