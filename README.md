# 🗂️ Sistema de Gestión de Tareas (API Flask + SQLite)

Este proyecto consiste en una API RESTful desarrollada con Flask para gestionar usuarios y tareas, con almacenamiento en SQLite y contraseñas protegidas mediante hashing.

La API está desplegada en **Render** y cuenta con HTTPS habilitado automáticamente.

---

## 🌐 Servidor

La API está hosteada en Render en esta URL:

👉 **https://gestion-de-tareas-pfo2.onrender.com**  


---

## ⚙️ Funcionalidades de la API

### 1. Registro de usuarios
- **Endpoint:** `POST /registro`
- **Cuerpo JSON:**  
json
{
  "usuario": "ejemplo",
  "contraseña": "1234"
}


### 2. Inicio de sesión
- **Endpoint:** `POST /login`
- **Verifica credenciales del usuario**

### 3. Ver tareas
- **Endpoint:** `GET /tareas`
- **Autenticación requerida:** básica (usuario y contraseña en el encabezado)
- **Respuesta:** HTML de bienvenida

---

## 💻 Cliente de Consola (`cliente.py`)

Este cliente permite interactuar con la API desde la terminal.

### 📥 Requisitos

- Python 3.x
- requests (`pip install requests`)

### ▶️ Cómo usar el cliente

1. Cloná el repositorio o descargá los archivos.
2. Asegurate de tener `cliente.py`.
3. Ejecutá el cliente:
bash
python cliente.py


4. Elegí una de las opciones:
text
1. Registrar usuario
2. Iniciar sesión y ver tareas
3. Salir


> 🛡️ El inicio de sesión utiliza autenticación básica para acceder a la vista HTML `/tareas`.

---

## 📦 Archivos importantes

| Archivo         | Descripción                                     |
|-----------------|-------------------------------------------------|
| `servidor.py`   | Código del servidor Flask con la API            |
| `cliente.py`    | Cliente de consola para interactuar con la API  |
| `requirements.txt` | Dependencias necesarias                      |

---

## 🚀 ¿Cómo desplegar tu propia API en Render?

1. Creá una cuenta en [https://render.com](https://render.com)
2. Subí tu proyecto a GitHub
3. En Render, elegí **"New Web Service"**
4. Usá `python servidor.py` como comando de inicio
5. Render activará HTTPS automáticamente

---

## 🔐 Seguridad

- Las contraseñas se almacenan **hasheadas** (no en texto plano)
- La API se accede solo por **HTTPS** (gracias a Render)
- El endpoint `/tareas` requiere **autenticación básica**

---

### ¿Por qué hashear contraseñas?

Para proteger las contraseñas en caso de robo de la base de datos. El hash es irreversible y evita que un atacante conozca la contraseña original.

---

### Ventajas de usar SQLite en este proyecto

- No requiere instalación ni configuración.
- Viene con Python (`sqlite3`).
- Ideal para proyectos pequeños y prototipos.
- Guarda datos de forma persistente en un archivo local.



## 🧑‍💻 Autor

Proyecto desarrollado por Javier Rodríguez para la materia "Programación sobre redes" con Flask y SQLite.
