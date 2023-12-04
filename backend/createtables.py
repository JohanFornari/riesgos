from app import app, db, Usuario, Riesgo
from werkzeug.security import generate_password_hash,check_password_hash
import json

app.app_context().push()

# Se crean las tablas de base de datos apartir del modelo de forma automatica, se requiere que exista la base de datos
db.create_all()

# Crear un usuario con una contraseña segura, guardándola en un hash
def create_user(username, password, es_admin=False):
    user = Usuario(username=username, es_admin=es_admin)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()  # ¡Asegúrate de hacer el commit!

# Crear usuarios
create_user('user', 'user123')
create_user('admin', 'admin123', es_admin=True)

with open('riesgos.json', 'r') as file:
    data = json.load(file)

for riesgo_data in data:
    print(riesgo_data)
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





# Guarda los cambios
db.session.commit()
