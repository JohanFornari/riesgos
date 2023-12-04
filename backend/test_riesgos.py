from app import app, db, Usuario, Riesgo
import json

# Configurando la aplicación para pruebas
app.config['TESTING'] = True
client = app.test_client()

with app.app_context():
    db.create_all()

def login(username, password):
    response = client.post('/api/login', json={'username': username, 'password': password})
    return json.loads(response.data)['token']

def getid(username):
    token = login('admin', 'admin123')
    riesgos_usuario = Riesgo.query.filter_by(username=username).first().id
    return response.status_code == 200

def test_login():
    response = client.post('/api/login', json={'username': 'admin', 'password': 'admin123'})
    assert response.status_code == 200

def test_listar_riesgos():
    token = login('admin', 'admin123')
    response = client.get('/api/riesgos', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200

def test_crear_riesgo():
    token = login('admin', 'admin123')
    response = client.post('/api/riesgos', json={
        'nombre': 'Fallo en la seguridad del servidor test',
        'descripcion': 'Posible brecha de seguridad en el servidor test',
        'probabilidad': 'Alta test',
        'proveedor': 'Amazon Web Services test',
        'impacto': 'Alto test',
        'pais': 'Albania test'
    }, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200

# hay que ingresar el id del riesgo a actualizar
def test_actualizar_riesgo():
    token = login('admin', 'admin123')

    response = client.put(f'/api/riesgos/8', json={
        'nombre': 'Nuevo Nombre del Riesgo',
        'descripcion': 'Nueva descripción del riesgo',
        'probabilidad': 'Alta',
        'proveedor': 'Nuevo Proveedor',
        'impacto': 'Alto',
        'pais': 'Nuevo País'
    }, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200

# hay que ingresar el id del riesgo a actualizar
def test_eliminar_riesgo():
    token = login('admin', 'admin123')
    response = client.delete(f'/api/riesgos/8', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200


if __name__ == '__main__':
    import pytest
    pytest.main()
