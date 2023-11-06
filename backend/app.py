from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_login import UserMixin, login_user, login_required, current_user, logout_user
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, get_jwt
from datetime import datetime, timedelta
from models import db,Usuario,Riesgo

app = Flask(__name__)

CORS(app, supports_credentials=True)
# Configuración de la URL de conexión a la base de datos en PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/gestion_riesgos'
db.init_app(app)

with app.app_context():
    db.create_all()

#Configuración de jwt
app.config['JWT_SECRET_KEY'] = 'clave_secreta'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# Inicio de sesión y creacción de token
@app.route('/api/login', methods=['POST','GET'])
def login():

    data = request.json
    username = data.get('username')
    password_hash = data.get('password')

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario and check_password_hash(usuario.password_hash, password_hash):
        # Generación token jwt
        token = create_access_token(identity=username)

        print('token:',token)
        return jsonify({'username': username, 'token': token}), 200
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401


@app.route('/api/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))

# Metodo para listar los riesgos
# Se valida el token jwt el cual se recibe del headers
@app.route('/api/riesgos', methods=['GET'])
@jwt_required()
def listar_riesgos():
    username = get_jwt_identity()
    riesgos_usuario = Riesgo.query.all()
    riesgos_usuario = [{'id': riesgo.id, 'nombre': riesgo.nombre, 'descripcion': riesgo.descripcion, 'proveedor': riesgo.proveedor, 'probabilidad': riesgo.probabilidad, 'impacto': riesgo.impacto, 'pais': riesgo.pais, 'usuario_id': Usuario.query.filter_by(id=riesgo.usuario_id).first().username} for riesgo in riesgos_usuario]
    print(riesgos_usuario)
    return jsonify({'riesgos': riesgos_usuario})


# Metodo para actualizar la información de un riesgo
@app.route('/api/riesgos/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_riesgo(id):

    riesgo = Riesgo.query.get(id)

    if riesgo:
        username = get_jwt_identity()
        usuario = Usuario.query.filter_by(username=username).first()
        # Verifica si el riesgo pertenece al usuario autenticado
        if riesgo.usuario_id == usuario.id:
            datos_actualizados = request.json
            # Actualiza los campos del riesgo
            riesgo.nombre = datos_actualizados.get('nombre')
            riesgo.descripcion = datos_actualizados.get('descripcion')
            riesgo.probabilidad = datos_actualizados.get('probabilidad')
            riesgo.proveedor = datos_actualizados.get('proveedor')
            riesgo.impacto = datos_actualizados.get('impacto')
            riesgo.pais = datos_actualizados.get('pais')

            db.session.commit()
            return jsonify({'mensaje': f'Riesgo con ID {id} actualizado correctamente'})
        else:
            return jsonify({'mensaje': f'No tienes permisos para actualizar este riesgo'}), 403
    else:
        return jsonify({'mensaje': f'Riesgo con ID {id} no encontrado'}), 404

# metodo para eliminar un riesgo
# Se valida el token jwt el cual se recibe del headers
@app.route('/api/riesgos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_riesgo(id):
    riesgo = Riesgo.query.get(id)

    if riesgo:
        username = get_jwt_identity()
        usuario = Usuario.query.filter_by(username=username).first()
        # Verifica si el riesgo pertenece al usuario autenticado
        if riesgo.usuario_id == usuario.id:
            db.session.delete(riesgo)
            db.session.commit()
            return jsonify({'mensaje': f'Riesgo con ID {id} eliminado correctamente'})
        else:
            return jsonify({'mensaje': f'No tienes permisos para eliminar este riesgo'}), 403
    else:
        return jsonify({'mensaje': f'Riesgo con ID {id} no encontrado'}), 404

# Se realiza la creación de un riesgo
# Se valida el token jwt el cual se recibe del headers
@app.route('/api/riesgos', methods=['POST'])
@jwt_required()
def crear_riesgo():
    username = get_jwt_identity()
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario:
        # Aquí procedes a crear el riesgo
        # Asegúrate de que los datos del riesgo estén en el cuerpo de la solicitud (request.json)
        nombre = request.json.get('nombre')
        descripcion = request.json.get('descripcion')
        pais = request.json.get('pais')
        probabilidad = request.json.get('probabilidad')
        proveedor = request.json.get('proveedor')
        impacto = request.json.get('impacto')

        print(usuario.id)

        nuevo_riesgo = Riesgo(
            nombre=nombre,
            descripcion=descripcion,
            proveedor=proveedor,
            probabilidad = probabilidad,
            impacto = impacto,
            pais=pais,
            usuario_id=usuario.id
        )

        db.session.add(nuevo_riesgo)
        db.session.commit()

        return jsonify({'mensaje': 'Riesgo creado exitosamente'}), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 401


if __name__ == '__main__':
    app.run(debug=True)
