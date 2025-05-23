from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados en memoria (como si fuera una "base de datos")
usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "María"},
]

# Ruta de inicio (página de bienvenida)
@app.route('/')
def inicio():
    return "API REST básica en Flask"

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Obtener un usuario por su ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nuevo = request.get_json()
    if not nuevo or 'nombre' not in nuevo:
        return jsonify({"mensaje": "Datos inválidos"}), 400
    
    nuevo['id'] = usuarios[-1]['id'] + 1 if usuarios else 1
    usuarios.append(nuevo)
    return jsonify(nuevo), 201

# Ejecutar la app solo si se llama directamente (no al importar)
if __name__ == '__main__':
    app.run(debug=True)
