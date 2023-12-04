from flask import Flask, request,jsonify
from flask_cors import CORS
from werkzeug.security import check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from models import db,Usuario,Riesgo
import json

app = Flask(__name__)

#CORS(app, supports_credentials=True)
CORS(app)
# Configuración de la URL de conexión a la base de datos en PostgreSQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/gestion_riesgos'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@172.21.0.2:5432/gestion_riesgos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@app_riesgos-db-1:5432/gestion_riesgos'
db.init_app(app)

with app.app_context():
    db.create_all()

#Configuración de jwt
app.config['JWT_SECRET_KEY'] = 'clave_secreta'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# Inicio 
@app.route('/api')
def iniciar():
    username = 'admin'
    usuario = Usuario.query.filter_by(username=username).first()
    crearRegistros() 
    if not usuario:
        create_user('user', 'user123')
        create_user('admin', 'admin123', es_admin=True)
        print('crea usuarios')    
        return jsonify({'inicio': 'crea usuarios'})
    else:
        print('usuarios creados') 
        return jsonify({'inicio': 'usuarios creados'})

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


def crearRegistros():
    with open('riesgos.json', 'r') as file:
        data = json.load(file)
    riesgos_usuario = Riesgo.query.all()
    if not riesgos_usuario:
        for riesgo_data in data:
            nuevo_riesgo = Riesgo(
                id=riesgo_data['id'],
                nombre=riesgo_data['nombre'],
                descripcion=riesgo_data['descripcion'],
                pais=riesgo_data['pais'],
                probabilidad=riesgo_data['probabilidad'],
                impacto=riesgo_data['impacto'],
                proveedor=riesgo_data['proveedor'],
                usuario_id=riesgo_data['id_usuario']
            )
            db.session.add(nuevo_riesgo)
        print('Riesgos creados') 
        db.session.commit()
        

@app.route('/api/logout')
@jwt_required()
def logout():
    username = get_jwt_identity()
    JWTManager.unauthorized_loader(identity=username)
    #revoked_token_loader(identity=username)
    return jsonify({'mensaje': f'Se ha cerrado sesion'})

# Metodo para listar los riesgos
@app.route('/api/riesgos', methods=['GET'])
@jwt_required()
def listar_riesgos():
    username = get_jwt_identity()
    riesgos_usuario = Riesgo.query.all()
    riesgos_usuario = [{'id': riesgo.id, 'nombre': riesgo.nombre, 'descripcion': riesgo.descripcion, 'proveedor': riesgo.proveedor, 'probabilidad': riesgo.probabilidad, 'impacto': riesgo.impacto, 'pais': riesgo.pais, 'usuario_id': Usuario.query.filter_by(id=riesgo.usuario_id).first().username} for riesgo in riesgos_usuario]
    return jsonify({'riesgos': riesgos_usuario})


# Metodo para actualizar la información de un riesgo
@app.route('/api/riesgos/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_riesgo(id):

    riesgo = Riesgo.query.get(id)

    if riesgo:
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
        return jsonify({'mensaje': f'Riesgo con ID {id} no encontrado'}), 404

# metodo para eliminar un riesgo
# Se valida el token jwt el cual se recibe del headers
@app.route('/api/riesgos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_riesgo(id):
    riesgo = Riesgo.query.get(id)
    if riesgo:
        db.session.delete(riesgo)
        db.session.commit()
        return jsonify({'mensaje': f'Riesgo con ID {id} eliminado correctamente'})
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
        nombre = request.json.get('nombre')
        descripcion = request.json.get('descripcion')
        pais = request.json.get('pais')
        probabilidad = request.json.get('probabilidad')
        proveedor = request.json.get('proveedor')
        impacto = request.json.get('impacto')

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

# Se realiza la creación del usuario
# Se valida el token jwt el cual se recibe del headers
@app.route('/api/crearusuario', methods=['POST'])
@jwt_required()
def crear_usuario():
    username = get_jwt_identity()
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario.es_admin == True:
        # creación usuario
        nombre_usuario = request.json.get('nombre')
        password = request.json.get('password')
        # Crear usuarios
        create_user(nombre_usuario, password)
        return jsonify({'mensaje': 'Usuario creado exitosamente'}), 200
    else:
        return jsonify({'message': 'No tiene permisos para crear usuario'}), 401

#Creación del usuario
@jwt_required()
def create_user(username, password, es_admin=False):
    user = Usuario(username=username, es_admin=es_admin)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)



# comando que hace todo 
# docker-compose up -d --build 


# crear requirements.txt
# python -m pip freeze >requirements.txt  

# Crear imagen docker
#docker build -t servicio .

#docker images 
#docker run -it -p 5000:5000 --name gestion_riesgos servicio

# crear una nueva red
# docker network create red_riesgos
# docker necworkresul: fdee0059bc389b5564ceea928b9ea71af7257d5c659bace6531c8615a89f024f

# visualizar redes 
# docker network ls


# se sube el servicio de docker con la red creada con elasticsearch
# docker run -d --net=postgresqldocker_default --name gestion_riesgos servicio 


# correr el contenedor 
# docker start gestion_riesgos

# conectar el contenedor a la red 
# docker exec -it gestion_riesgos bash

#root@cb79def45247
# psql postgres://postgres:123@localhost:5432/gestion_riesgos

# docker-compose up — build. 