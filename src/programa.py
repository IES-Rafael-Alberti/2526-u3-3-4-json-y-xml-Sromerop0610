import json
import shutil
from pathlib import Path

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
