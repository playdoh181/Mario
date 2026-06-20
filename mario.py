import random
import os

# Colores ANSI (Termux y algunas versiones de QPython3)
COLORES = [
    '\033[91m',  # Rojo
    '\033[92m',  # Verde
    '\033[93m',  # Amarillo
    '\033[94m',  # Azul
    '\033[95m',  # Magenta
    '\033[96m',  # Cian
]

RESET = '\033[0m'

def color():
    return random.choice(COLORES)

# Banner Mario estilo neón
def mostrar_banner():
    banner = r"""
███╗   ███╗ █████╗ ██████╗ ██╗ ██████╗
████╗ ████║██╔══██╗██╔══██╗██║██╔═══██╗
██╔████╔██║███████║██████╔╝██║██║   ██║
██║╚██╔╝██║██╔══██║██╔══██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝
"""
    print(color() + banner + RESET)

# Lista de nombres latinos
nombres_latinos = [
    "Juan", "Pedro", "Maria", "Luis", "Ana",
    "Carlos", "Laura", "Jorge", "Sofia",
    "Diego", "Mario"
]

def generar_combos(cantidad):
    combos = []

    for _ in range(cantidad):
        nombre = random.choice(nombres_latinos)
        numero = random.randint(100, 999)

        user = f"{nombre}{numero}"
        password = f"{nombre.lower()}{numero}"

        combos.append(f"{user}:{password}")

    return combos

def guardar_combos(combos):
    carpeta = "/sdcard/Combos"

    try:
        os.makedirs(carpeta, exist_ok=True)

        ruta = os.path.join(carpeta, "combos.txt")

        with open(ruta, "w", encoding="utf-8") as archivo:
            for combo in combos:
                archivo.write(combo + "\n")

        print(color() + f"\n✓ Combos guardados en:\n{ruta}" + RESET)

    except Exception as e:
        print(color() + f"\nError: {e}" + RESET)

if __name__ == "__main__":
    os.system("clear" if os.name != "nt" else "cls")

    mostrar_banner()

    try:
        cantidad = int(input(color() + "¿Cuántos combos deseas generar? " + RESET))

        combos = generar_combos(cantidad)

        print(color() + "\nPrimeros resultados:\n" + RESET)

        for combo in combos[:10]:
            print(color() + combo + RESET)

        guardar_combos(combos)

    except ValueError:
        print(color() + "Ingresa un número válido." + RESET)