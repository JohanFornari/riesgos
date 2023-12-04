from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()

# modelos de datos de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Usuario {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# modelos de datos de Riesgos
class Riesgo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    probabilidad = db.Column(db.String(255), nullable=False)
    impacto = db.Column(db.String(255), nullable=False)
    proveedor = db.Column(db.String(255), nullable=False)
    pais = db.Column(db.String(80), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __repr__(self):
        return '<Riesgo %r>' % self.nombre
