# Importaciones
from colorama import Fore # Importamos desdse colorama los colores
import pyfiglet

#convertir texto en arte ASCII
fuente = pyfiglet.figlet_format("Feliz Navidad")

print(Fore.RED, fuente)

print(Fore.GREEN, 'Les deseo que pasen una hermosa noche con todos los que aman 🌲')