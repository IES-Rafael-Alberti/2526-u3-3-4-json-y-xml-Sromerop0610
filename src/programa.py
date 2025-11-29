import json
import shutil
from pathlib import Path

# Limpiar pantalla:
def limpiar_consola():
    n=0
    while n < 50:
        print(" \n")
        n += 1

# Funcion auxiliar de pausa:
def pausar():
    """Pausa hasta que el usuario pulse una tecla."""
    input("\nPresione una tecla para continuar . . . ")

# Funciones principales:
def mostrar_datos(datos):
    """
    Recibe un diccionario (lo esperado: {'usuarios': [...]})
    y muestra el contenido de forma organizada.
    """
    if not isinstance(datos, dict): #Comprueba que datos sea un diccionario (dict)
        print("ERROR: Los datos proporcionados no tienen el formato esperado.")
        return

    usuarios = datos.get("usuarios") #Intenta sacar el valor de la clave "usuarios" del diccionario
    if not usuarios:
        print("ERROR El archivo JSON no contiene usuarios!")
        return

    print("Contenido Actual del JSON")
    for i in usuarios:
        id = i.get("id", "N/A")
        nombre = i.get("nombre", "N/A")
        edad = i.get("edad", "N/A")
        print(f"ID: {id}, Nombre: {nombre}, Edad: {edad}")
    print("Fin del Contenido")

def inicializar_datos(archivo_origen, archivo_destino):
    """
    Copia el contenido de archivo_origen a archivo_destino.
    Maneja errores: origen no existe o JSON inválido.
    """
    origen = Path(archivo_origen)
    destino = Path(archivo_destino)

    if not origen.exists():
        print(f"ERROR El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
        return False

    # Comprobar que el origen contiene JSON válido antes de copiar
    try:
        with origen.open('r', encoding='utf-8') as f:
            json.load(f)  # solo para validar
    except json.JSONDecodeError:
        print(f"ERROR El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")
        return False
    except Exception as e:
        print(f"ERROR al leer '{archivo_origen}': {e}")
        return False

    # Si todo bien, copiar (sobrescribe si existe)
    try:
        shutil.copyfile(origen, destino)
        print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")
        return True
    except Exception as e:
        print(f"ERROR al copiar el archivo: {e}")
        return False

# Funcion para cargar json y funcion para guardarlo:
def cargar_json(ruta):
    """Carga JSON desde un archivo y devuelve el diccionario (o None si error)."""
    path = Path(ruta)
    if not path.exists():
        print(f"ERROR: El archivo '{ruta}' no existe.")
        return None
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"ERROR: El archivo '{ruta}' tiene JSON inválido.")
        return None
    except Exception as e:
        print(f"ERROR al leer '{ruta}': {e}")
        return None
    
def guardar_json(ruta, datos):
    """Guarda el diccionario 'datos' como JSON en 'ruta'."""
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"ERROR al guardar en '{ruta}': {e}")
        return False

# Funciones para: actualizar edad, insertar usuario y eliminar usuario
def actualizar_edad(datos, id_usuario, nueva_edad):
    usuarios = datos.get("usuarios", [])
    for u in usuarios:
        if u.get("id") == id_usuario:
            u["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return True
    print(f"ERROR: Usuario con ID {id_usuario} no encontrado.")
    return False

def insertar_usuario(datos, nombre, edad):
    usuarios = datos.get("usuarios")
    if usuarios is None:
        usuarios = []
        datos["usuarios"] = usuarios
    # calcular nuevo id (1 + máximo id existente)
    max_id = 0
    for u in usuarios:
        try:
            if int(u.get("id", 0)) > max_id:
                max_id = int(u.get("id", 0))
        except Exception:
            pass
    nuevo_id = max_id + 1
    nuevo_usuario = {"id": nuevo_id, "nombre": nombre, "edad": edad}
    usuarios.append(nuevo_usuario)
    print(f"Usuario {nombre} añadido con éxito.")
    return True

def eliminar_usuario(datos, id_usuario):
    usuarios = datos.get("usuarios", [])
    nueva_lista = [u for u in usuarios if u.get("id") != id_usuario]
    if len(nueva_lista) == len(usuarios):
        print(f"ERROR: Usuario con ID {id_usuario} no encontrado.")
        return False
    datos["usuarios"] = nueva_lista
    print(f"Usuario con ID {id_usuario} eliminado.")
    return True

# Funcion Main

