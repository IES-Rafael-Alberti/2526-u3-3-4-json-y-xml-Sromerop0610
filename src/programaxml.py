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

