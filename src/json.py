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

# Funciones principalesa implementar:
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

# Funciones ya dadas (cargar y guardar)
def cargar_json(nombre_fichero: str) -> dict:
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent=4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")

# Funciones para: actualizar edad, insertar usuario y eliminar usuario (ya dadas)
def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"\nUsuario con ID {id_usuario} actualizado.")
            return
    print(f"\nUsuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    datos["usuarios"].append(nuevo_usuario)
    print(f"\nUsuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"\nUsuario con ID {id_usuario} eliminado.")
            return
    print(f"\nUsuario con ID {id_usuario} no encontrado.")


# Funcion Main
def main():
    limpiar_consola()

    archivo_origen = "src/otros/datos_usuarios_orig.json"
    archivo_destino = "src/otros/datos_usuarios.json"

    # 1. Inicializar datos
    inicializar_datos(archivo_origen, archivo_destino)

    # 2. Cargar datos
    datos = cargar_json(archivo_destino)
    if datos is None:
        datos = {"usuarios": []}

    # 3. Mostrar contenido inicial
    mostrar_datos(datos)
    pausar()

    # 4. ACTUALIZAR USUARIO
    actualizar_usuario(datos, id_usuario=1, nueva_edad=31)
    mostrar_datos(datos)
    pausar()

    # 5. INSERTAR USUARIO
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)
    mostrar_datos(datos)
    pausar()

    # 6. ELIMINAR USUARIO
    eliminar_usuario(datos, id_usuario=2)
    mostrar_datos(datos)
    pausar()

    # 7. GUARDAR CAMBIOS
    guardar_json(archivo_destino, datos)

    print("\nOperaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()