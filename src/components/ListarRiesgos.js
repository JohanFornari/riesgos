
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ActualizarRiesgo from './ActualizarRiesgo';

function RiesgoList() {
  const [riesgos, setRiesgos] = useState([]);
  const [riesgoSeleccionado, setRiesgoSeleccionado] = useState(null);
  const [filtro, setFiltro] = useState('');

  useEffect(() => {

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
    axios.get('/api/riesgos',config)
      .then(response => {
        setRiesgos(response.data.riesgos);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleEliminarRiesgo = (id) => {

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

    axios.delete(`/api/riesgos/${id}`,config)
      .then(response => {
        setRiesgos(riesgos.filter(riesgo => riesgo.id !== id));
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleRiesgoActualizado = (nuevoRiesgo) => {
    setRiesgos(riesgos.map(riesgo =>
      riesgo.id === nuevoRiesgo.id ? nuevoRiesgo : riesgo
    ));
    setRiesgoSeleccionado(null);
  };

  const handleModificarRiesgo = (riesgo) => {
    setRiesgoSeleccionado(riesgo);
  };

  const handleFiltrarRiesgos = () => {
    return riesgos.filter(riesgo =>
      riesgo.nombre.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.descripcion.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.impacto.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.probabilidad.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.proveedor.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.pais.toLowerCase().includes(filtro.toLowerCase()) ||
      riesgo.id.toString().includes(filtro.toString())
    );
  };


  return (
    <div className="container mt-4">
      <h2>Listado de Riesgos</h2>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Filtrar ..."
        value={filtro}
        onChange={(e) => setFiltro(e.target.value)}
      />
      <table className="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Nombre</th>
          <th scope="col">Descripción</th>
          <th scope="col">proveedor</th>
          <th scope="col">Probabilidad</th>
          <th scope="col">Impacto</th>
          <th scope="col">Usuario</th>
          <th scope="col">País</th>
          <th scope="col">Acciones</th>
        </tr>
      </thead>
        <tbody>
          {handleFiltrarRiesgos().map(riesgo => (
            <tr key={riesgo.id}>

                  <th scope="row">{riesgo.id}</th>
                  <td>{riesgo.nombre}</td>
                  <td>{riesgo.descripcion}</td>
                  <td>{riesgo.proveedor}</td>
                  <td>{riesgo.probabilidad}</td>
                  <td>{riesgo.impacto}</td>
                  <td>{riesgo.usuario_id}</td>
                  <td>{riesgo.pais}</td>

              <td>
                <button className="btn btn-primary" onClick={() => handleModificarRiesgo(riesgo)}>Modificar</button>
                <button className="btn btn-danger" onClick={() => handleEliminarRiesgo(riesgo.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {riesgoSeleccionado && <ActualizarRiesgo riesgo={riesgoSeleccionado}  onRiesgoModificado={handleRiesgoActualizado} />} {/* Muestra ActualizarRiesgo si hay un riesgo seleccionado */}
    </div>
  );
}

export default RiesgoList;
