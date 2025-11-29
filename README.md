# Práctica 3.4: JSON y XML

Apóyate en los siguientes recursos para realizar la práctica:

* [U3: JSON](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica004/)
* [U3: XML](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica005/)

---

# Título de la Actividad

**Práctica 3.4 — Gestión de Usuarios con JSON y XML**

---

# Identificación de la Actividad

* **ID de la Actividad:** P3.4
* **Módulo:** PROG
* **Unidad de Trabajo:** Unidad 3 — Manejo de Ficheros (JSON y XML)
* **Fecha de Creación:** *28/11/2025*
* **Fecha de Entrega:** *29/11/2025*
* **Alumno:**

  * **Nombre y Apellidos:** *Sara Romero Peralta*
  * **Correo electrónico:** *sromper0610@g.educaand.es*
  * **Iniciales:** *SRP*

---

# Descripción de la Actividad

En esta práctica se desarrollan dos programas independientes, **json.py** y **xml.py**, que implementan una miniaplicación de gestión de usuarios utilizando los formatos de almacenamiento **JSON** y **XML**.

Ambos programas deben:

* Leer datos desde un archivo origen (`datos_usuarios_orig.*`)
* Copiarlo a un archivo destino (`datos_usuarios.*`)
* Mostrar los datos en consola
* Permitir:

  * Actualizar la edad de un usuario
  * Insertar un nuevo usuario
  * Eliminar un usuario existente
* Guardar los cambios en el archivo destino
* Manejar todos los errores solicitados en el enunciado

Además, deben utilizar funciones auxiliares de limpieza de consola y pausa, y seguir exactamente los mensajes y el flujo marcado en el enunciado.

---

# Instrucciones de Compilación y Ejecución

## 1. Requisitos Previos

* **Lenguaje:** Python 3.10+
* **Entorno recomendado:** VS Code / PyCharm / Terminal
* **Librerías estándar usadas:**

  * `json`
  * `xml.etree.ElementTree`
  * `os`, `shutil`, `pathlib`

No es necesario instalar nada adicional.

---

## 2. Ejecutar los programas

### Ejecutar el programa de JSON:

```bash
python src/json.py
```

### Ejecutar el programa de XML:

```bash
python src/xml.py
```

# Desarrollo de la Actividad

## Descripción del Desarrollo

Se han desarrollado dos programas estructurados de forma modular, cada uno centrado en un formato de datos distinto: **JSON** y **XML**.

### JSON

En `json.py` se implementaron las funciones:

* `mostrar_datos()`: imprime los usuarios del archivo JSON
* `inicializar_datos()`: copia el archivo origen al destino con manejo de errores
* `cargar_json()` y `guardar_json()`
* Operaciones de gestión:

  * `actualizar_usuario()`
  * `insertar_usuario()`
  * `eliminar_usuario()`

El `main()` ejecuta las operaciones en el orden pedido.

### XML

En `xml.py` se implementaron:

* `mostrar_datos()`: imprime los nodos `<usuario>`
* `inicializar_datos()`: copia el XML origen al destino
* `crear_arbol()`: genera un árbol vacío si el archivo está corrupto o no existe
* `actualizar_edad()`, `insertar_usuario()`, `eliminar_usuario()`

También se añade carga segura mediante `cargar_xml()`.

Se siguió exactamente el flujo solicitado:

1. Limpiar consola
2. Inicializar datos
3. Cargar archivo
4. Mostrar contenido
5. Actualizar usuario
6. Insertar usuario
7. Eliminar usuario
8. Guardar archivo

### Enlaces al código

> Los enlaces deben pegarse cuando subas tu repositorio:

Ejemplo:

```
src/json.py  
src/xml.py  
tests/test_json.py  
tests/test_xml.py  
```

---

# Ejemplos de Ejecución

### Ejemplo JSON (resumen)

```
Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---
```

### Ejemplo XML (resumen)

```
Datos inicializados desde 'datos_usuarios_orig.xml' a 'datos_usuarios.xml'.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---
```

---

# Resultados de Pruebas

Se han verificado los siguientes casos:

* Archivo origen inexistente → muestra error correcto
* Archivo con formato inválido → error correcto
* Inserción de usuarios → ID autoincremental
* Eliminación de usuarios → nodo eliminado correctamente
* Actualización de edad → modifica valor dentro del archivo
* Archivo destino vacío o corrupto → se recrea en XML con `crear_arbol()`

Las pruebas unitarias incluidas en la carpeta `tests` validan varias funciones clave.

---

# Documentación Adicional

* **Manual de Usuario:** No aplica (la ejecución es directa desde terminal).
* **Permisos del Repositorio:** Se debe otorgar acceso de lectura al profesor.

---

# Conclusiones

Esta práctica ha permitido comprender:

* Cómo manejar archivos JSON de forma segura en Python.
* Cómo parsear, modificar y guardar árboles XML con `ElementTree`.
* La importancia del manejo de errores en lectura y escritura de archivos.
* La estructura modular de programas con funciones auxiliares.
* El flujo completo de un CRUD básico para usuarios en distintos formatos de datos.

Como mejora futura, podría añadirse:

* Interfaz por menús
* Validación de entradas del usuario
* Comprobación de duplicados
* Integración con bases de datos reales

---

# Referencias y Fuentes

* Documentación oficial de Python:
  [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
  [https://docs.python.org/3/library/xml.etree.elementtree.html](https://docs.python.org/3/library/xml.etree.elementtree.html)
* Recursos de clase U3 JSON y XML
* Ejemplos revisados en el aula virtual

---

# Notas Adicionales

1. **Estructura del repositorio** (ejemplo):

```
src/
 ├── json.py
 ├── xml.py
tests/
 ├── test_json.py
 ├── test_xml.py
datos_usuarios.json
datos_usuarios_orig.json
datos_usuarios.xml
datos_usuarios_orig.xml
README.md
```

2. **Nombres del repositorio:**
   Formato recomendado:
   `PROG-P3.4-INICIALES`

3. **Entrega:**
   Subir únicamente el enlace al repositorio al aula virtual.

