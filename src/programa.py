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
# Funciones que te pide:
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

# Funciones extras para estructurar el codigo:
