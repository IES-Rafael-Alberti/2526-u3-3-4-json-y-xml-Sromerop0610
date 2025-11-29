import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

# Funciones limpiar y pausa
def limpiar_consola():
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    """Pausa la ejecución hasta que el usuario pulse una tecla."""
    input("Presione una tecla para continuar . . . ")

# Funciones mostrar datos y inicializarlos
def mostrar_datos(root):
    """
    Muestra los datos de los usuarios de forma organizada.
    """
    print("\n--- Contenido Actual del XML ---")

    usuarios = root.findall("usuario")

    if not usuarios:
        print("ERROR No hay usuarios en el archivo XML.")
        print("--- Fin del Contenido ---\n")
        return

    for usuario in usuarios:
        id_ = usuario.find("id").text
        nombre = usuario.find("nombre").text
        edad = usuario.find("edad").text
        print(f"ID: {id_}, Nombre: {nombre}, Edad: {edad}")

    print("--- Fin del Contenido ---\n")


def inicializar_datos(archivo_origen, archivo_destino):
    """
    Copia el archivo origen al destino manejando errores.
    """
    origen = Path(archivo_origen)

    # Error: archivo origen no existe
    if not origen.exists():
        print(f"ERROR El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
        return

    # Error: formato XML inválido
    try:
        ET.parse(archivo_origen)
    except ET.ParseError:
        print(f"ERROR El archivo origen '{archivo_origen}' tiene un formato XML inválido.")
        return

    # Copia correcta
    shutil.copy(archivo_origen, archivo_destino)
    print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")

# Funciones cargar y guardar y crear
def cargar_xml(archivo):
    """
    Carga un archivo XML. Si hay errores, devuelve (None, None).
    """
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        return tree, root
    except (FileNotFoundError, ET.ParseError):
        return None, None


def guardar_xml(arbol, archivo):
    """
    Guarda el árbol XML en el archivo indicado.
    """
    arbol.write(archivo, encoding="utf-8", xml_declaration=True)

def crear_arbol(nombre_raiz):
    """
    Crea un nuevo árbol XML con un nodo raíz dado.
    """
    raiz = ET.Element(nombre_raiz)
    return ET.ElementTree(raiz)


