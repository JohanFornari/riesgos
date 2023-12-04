import React, { useState,useEffect } from 'react';
import axios from 'axios';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showAlert, setShowAlert] = useState(false);

  useEffect(() => {

    axios.get('/api')
      .then(response => {
       console.log('hecho')
       console.log(response.data)
      })
      .catch(error => {
        console.error('Error ', error);
      });
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    
    axios.post('/api/login', {
      username: username,
      password: password
    }, {
      mode: 'cors'
    })
    .then(response => {
      const token = response.data.token;
      console.log(token)
      // Guardar el token en el localStorage
      localStorage.setItem('token', token);

      // Redireccionar a la página de dashboard
      window.location.href = '/dashboard';
    })
    .catch(error => {

      console.error('Error al iniciar sesión:', error);
      setShowAlert(true);
    });
  };

  return (
    <div  className="container ">
    {showAlert && (
        <div className="alert alert-danger" role="alert">
          Contraseña incorrecta. Por favor, inténtalo de nuevo.
        </div>
    )}
    <br />
    <div  className="card col-md-10">
      <h2 className="text-center">Login</h2>
      <form className="px-4 py-3" onSubmit={handleSubmit}>
      <div className="form-group">
      <input
      className="form-control"
        type="text"
        placeholder="Usuario"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        name="username" // Asegúrate de tener esto en tu campo de nombre de usuario
        required
      /><br />
      </div>
      <div className="form-group">
      <input
        className="form-control"
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        name="password" // Asegúrate de tener esto en tu campo de contraseña
        required
      />
      <br />
      </div>
        <button type="submit" className="btn btn-primary">Iniciar Sesión</button>
      </form>
    </div>
    </div>
  );





}

export default Login;
