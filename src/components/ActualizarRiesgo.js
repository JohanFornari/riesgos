import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ActualizarRiesgo({ riesgo, onRiesgoModificado }) {
  const [nombre, setNombre] = useState(riesgo.nombre);
  const [descripcion, setDescripcion] = useState(riesgo.descripcion);
  const [impacto, setImpacto] = useState(riesgo.impacto);
  const [probabilidad, setProbabilidad] = useState(riesgo.probabilidad);
  const [pais, setPais] = useState(riesgo.pais);
  const [usuario, setUsuario] = useState(riesgo.usuario);
  const [proveedor, setProveedor] = useState(riesgo.proveedor);
  const [paises, setPaises] = useState([]);

  useEffect(() => {
    // Aquí se realiza la solicitud a la API de países
    axios.get('https://restcountries.com/v3.1/independent?status=true')
      .then(response => {
        const nombresPaises = response.data.map(pais => pais.name.common);
        setPaises(nombresPaises);
      })
      .catch(error => {
        console.error('Error al obtener la lista de países:', error);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const token = localStorage.getItem('token');
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

    axios.put(`/api/riesgos/${riesgo.id}`, {
      nombre: nombre,
      descripcion: descripcion,
      pais: pais,
      impacto: impacto,
      probabilidad: probabilidad,
      proveedor: proveedor

    },config)
    .then(response => {
      console.log(response.data.mensaje);
      onRiesgoModificado({
        id: riesgo.id,
        nombre: nombre,
        descripcion: descripcion,
        pais: pais,
        usuario: riesgo.usuario,
        proveedor: proveedor,
        impacto: impacto,
        probabilidad: probabilidad
      });
    })
    .catch(error => {
      console.error('Error al modificar el riesgo:', error);
    });
  };

  return (
    <div className="container mt-4">
      <h2>Modificar Riesgo</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="nombre" className="form-label">Nombre:</label>
          <input
            type="text"
            id="nombre"
            className="form-control"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="descripcion" className="form-label">Descripción:</label>
          <input
            type="text"
            id="descripcion"
            className="form-control"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="Proveedor" className="form-label">Proveedor:</label>
          <input
            type="text"
            id="descripcion"
            className="form-control"
            value={proveedor}
            onChange={(e) => setProveedor(e.target.value)}
          />
        </div>
          <div>
            <label htmlFor="Impacto" className="form-label" >Impacto:</label>
            <input
              type="text"
              id="Impacto"
              className="form-control"
              value={impacto}
              onChange={(e) => setImpacto(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor="Probabilidad" className="form-label" >Probabilidad:</label>
            <input
              type="text"
              id="Probabilidad"
              className="form-control"
              value={probabilidad}
              onChange={(e) => setProbabilidad(e.target.value)}
            />
          </div>

        <div className="mb-3">
          <label htmlFor="pais" className="form-label">País:</label>
          <select className="form-select"
            id="pais"
            value={pais}
            onChange={(e) => setPais(e.target.value)}
          >
            <option value="">Selecciona un país</option>
            {paises.map((nombrePais, index) => (
              <option key={index} value={nombrePais}>
                {nombrePais}
              </option>
            ))}
          </select>
        </div>
        <button className="btn btn-primary" type="submit">Modificar Riesgo</button>
      </form>
    </div>
  );
}

export default ActualizarRiesgo;
