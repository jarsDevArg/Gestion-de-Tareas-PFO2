import requests
from getpass import getpass

# Cambiá esta URL luego de subirlo a Render:
BASE_URL = "https://tu-api.onrender.com"

def registrar():
    try:
        usuario = input("Nombre de usuario: ")
        contraseña = getpass("Contraseña: ")
        datos = {"usuario": usuario, "contraseña": contraseña}
        r = requests.post(f"{BASE_URL}/registro", json=datos, timeout=5)
        r.raise_for_status()  # lanza error si hay código 4xx/5xx
        print(r.json())
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar con el servidor.")
    except requests.exceptions.Timeout:
        print("⏱️ Error: Tiempo de espera agotado.")
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error HTTP: {err.response.status_code} - {err.response.text}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def iniciar_sesion():
    try:
        usuario = input("Usuario: ")
        contraseña = getpass("Contraseña: ")
        r = requests.get(f"{BASE_URL}/tareas", auth=(usuario, contraseña), timeout=5)
        r.raise_for_status()
        print("\nRespuesta del servidor:")
        print(r.text)
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar con el servidor.")
    except requests.exceptions.Timeout:
        print("⏱️ Error: Tiempo de espera agotado.")
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error HTTP: {err.response.status_code} - {err.response.text}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión y ver tareas")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
