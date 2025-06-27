from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'tareas.db'


def crear_tabla_usuarios():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            )
        ''')


@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    hash_contraseña = generate_password_hash(contraseña)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, hash_contraseña))
            conn.commit()
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409


@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado and check_password_hash(resultado[0], contraseña):
            return jsonify({"mensaje": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales inválidas"}), 401


@app.route('/tareas', methods=['GET'])
def tareas():
    auth = request.authorization
    if not auth:
        return make_response("Se requiere autenticación básica", 401, {"WWW-Authenticate": "Basic realm='Login'"})

    usuario = auth.username
    contraseña = auth.password

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado and check_password_hash(resultado[0], contraseña):
            html = f"""
                <html>
                    <body>
                        <h1>Bienvenido, {usuario}</h1>
                        <p>Aquí puedes gestionar tus tareas.</p>
                    </body>
                </html>
            """
            return html
        else:
            return make_response("Credenciales inválidas", 401, {"WWW-Authenticate": "Basic realm='Login'"})


if __name__ == '__main__':
    crear_tabla_usuarios()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
