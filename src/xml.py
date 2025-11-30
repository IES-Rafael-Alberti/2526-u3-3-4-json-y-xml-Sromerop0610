import shutil
import xml.etree.ElementTree as ET

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

# Funciones mostrar datos y inicializarlos
def mostrar_datos(raiz: ET.Element):
    """
    Muestra el contenido del XML de forma organizada.
    """
    print("\n--- Contenido Actual del XML ---")

    usuarios = raiz.findall("usuario")

    if len(usuarios) == 0:
        print("ERROR No hay usuarios en el archivo XML.")
        print("--- Fin del Contenido ---")
        return

    for usuario in usuarios:
        id_u = usuario.find("id").text
        nombre = usuario.find("nombre").text
        edad = usuario.find("edad").text
        print(f"ID: {id_u}, Nombre: {nombre}, Edad: {edad}")

    print("--- Fin del Contenido ---")


def inicializar_datos(archivo_origen: str, archivo_destino: str):
    """
    Copia el archivo origen al destino.
    Maneja errores de no existe o XML inválido.
    """

    # 1. Si no existe → error
    if not os.path.exists(archivo_origen):
        print(f"ERROR El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
        return

    # 2. Comprobar formato XML válido
    try:
        ET.parse(archivo_origen)
    except ET.ParseError:
        print(f"ERROR El archivo origen '{archivo_origen}' tiene un formato XML inválido.")
        return

    # 3. Copiar archivo
    shutil.copy(archivo_origen, archivo_destino)

    print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")


def crear_arbol(nombre_raiz: str) -> ET.ElementTree:
    """
    Genera un XML vacío con un nodo raíz.
    """
    raiz = ET.Element(nombre_raiz)
    return ET.ElementTree(raiz)

# Funciones cargar y guardar y crear (ya dadas)
def cargar_xml(nombre_fichero: str) -> ET.ElementTree:
    try:
        return ET.parse(nombre_fichero)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except ET.ParseError:
        print("*ERROR* El archivo XML tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar el XML: {e}")

    return None


def guardar_xml(arbol: ET.ElementTree, nombre_fichero: str) -> bool:
    try:
        arbol.write(nombre_fichero, encoding="utf-8", xml_declaration=True)
        return True

    except FileNotFoundError:
        print(f"*ERROR* La ruta especificada '{nombre_fichero}' no existe.")

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar el archivo XML: {e}")

    return False

# Funciones para modificar datos (ya dadas)
def actualizar_usuario(raiz: ET.Element, id_usuario: int, nueva_edad: int):
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            usuario.find("edad").text = str(nueva_edad)
            print(f"\nUsuario con ID {id_usuario} actualizado.")
            return
    print(f"\nUsuario con ID {id_usuario} no encontrado.")


def insertar_usuario(raiz: ET.Element, nuevo_usuario: dict):
    usuario = ET.SubElement(raiz, "usuario")
    ET.SubElement(usuario, "id").text = str(nuevo_usuario["id"])
    ET.SubElement(usuario, "nombre").text = nuevo_usuario["nombre"]
    ET.SubElement(usuario, "edad").text = str(nuevo_usuario["edad"])
    print(f"\nUsuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(raiz: ET.Element, id_usuario: int):
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            raiz.remove(usuario)
            print(f"\nUsuario con ID {id_usuario} eliminado.")
            return
    print(f"\nUsuario con ID {id_usuario} no encontrado.")

# Funcion Main
def main():
    limpiar_consola()

    archivo_origen = "src/otros/datos_usuarios_orig.xml"
    archivo_destino = "src/otros/datos_usuarios.xml"

    # 1) Inicializar datos
    inicializar_datos(archivo_origen, archivo_destino)

    # 2) Cargar XML
    arbol = cargar_xml(archivo_destino)

    # Si falla → crear árbol vacío
    if arbol is None:
        arbol = crear_arbol("usuarios")

    raiz = arbol.getroot()

    # 3) Mostrar datos iniciales
    mostrar_datos(raiz)
    pausar()

    # 4) Actualizar usuario
    actualizar_usuario(raiz, id_usuario=1, nueva_edad=31)
    mostrar_datos(raiz)
    pausar()

    # 5) Insertar usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(raiz, nuevo_usuario)
    mostrar_datos(raiz)
    pausar()

    # 6) Eliminar usuario
    eliminar_usuario(raiz, id_usuario=2)
    mostrar_datos(raiz)
    pausar()

    # 7) Guardar cambios
    guardar_xml(arbol, archivo_destino)

    print("\nOperaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()