import xml.etree.ElementTree as ET

def json_a_xml(datos: dict) -> ET.Element:
    """
    Convierte un diccionario JSON en un nodo XML <usuario>.
    """
    usuario = ET.Element("usuario")

    # Nombre
    nombre = ET.SubElement(usuario, "nombre")
    nombre.text = datos["nombre"]

    # Edad
    edad = ET.SubElement(usuario, "edad")
    edad.text = str(datos["edad"])

    # Habilidades (lista)
    habilidades = ET.SubElement(usuario, "habilidades")
    for hab in datos["habilidades"]:
        nodo_hab = ET.SubElement(habilidades, "habilidad")
        nodo_hab.text = hab

    # Activo (booleano → true/false en minúsculas)
    activo = ET.SubElement(usuario, "activo")
    activo.text = "true" if datos["activo"] else "false"

    return usuario


def main():
    # Diccionario dado por el profesor
    datos = {
        "nombre": "Ana",
        "edad": 25,
        "habilidades": ["HTML", "CSS"],
        "activo": False
    }

    # Convertimos JSON → XML
    nodo_usuario = json_a_xml(datos)

    # Mostrar XML resultante por pantalla
    xml_str = ET.tostring(nodo_usuario, encoding="unicode")
    print(xml_str)


if __name__ == "__main__":
    main()
