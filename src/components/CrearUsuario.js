import React, { useState } from 'react';
import axios from 'axios';

function CrearUsuario() {
  const [nombre, setNombre] = useState('');
  const [password, setPassword] = useState('');
  const [showAlert, setShowAlert] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Obtener el token de localStorage si está disponible
    const token = localStorage.getItem('token');
    console.log('token react: ' + token)
    if (!token) {
      // Si el usuario no está autenticado, redirigir a la página de inicio de sesión
      window.location.href = '/'; // Cambia la URL según tu configuración
      return;
    }
    const config = {
        headers: {
          'Accept': '*/*',
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
    };

    axios.post('/api/crearusuario', {
      nombre: nombre,
      password: password
    }, config
    )
    .then(response => {
      console.log(response.data.mensaje);
      // Limpia los campos después de crear el riesgo
      setNombre('');
      setPassword('');

    })
    .catch(error => {
      console.error('Error al crear el usuario:', error);
      setShowAlert(true);
    });
  };

  return (
    <div className="container mt-4">
    {showAlert && (
      <div className="alert alert-danger" role="alert">
        No tiene permisos para crear usuarios.
      </div>
    )}
      <h2>Crear Usuario</h2>
      <form onSubmit={handleSubmit}>
        < div className="mb-3">
          <label htmlFor="nombre" className="form-label">Nombre:</label>
          <input
            type="text"
            id="nombre"
            className="form-control"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="descripcion" className="form-label" >Contraseña:</label>
          <input
            id="descripcion"
            type="password"
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <br />
        <button className="btn btn-primary" type="submit">Crear Usuario</button>
      </form>
    </div>
  );
}

export default CrearUsuario;
