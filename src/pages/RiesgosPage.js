// src/pages/RiesgosPage.js

import React, { useState, useEffect } from 'react';
import CrearRiesgo from '../components/CrearRiesgo';
import EliminarRiesgo from '../components/EliminarRiesgo';
import ActualizarRiesgo from '../components/ActualizarRiesgo';
import RiesgoList from '../components/RiesgoList';

function RiesgosPage() {
  const [riesgos, setRiesgos] = useState([]);
  const [actualizarId, setActualizarId] = useState(null);

  useEffect(() => {
    // Cargar la lista de riesgos al cargar la página
    // Puedes hacer una solicitud GET a tu API aquí
  }, []);

  const handleRiesgoCreado = (nuevoRiesgo) => {
    // Agregar el nuevo riesgo a la lista
    // Puedes hacer una solicitud POST a tu API aquí
  };

  const handleRiesgoEliminado = (id) => {
    // Eliminar el riesgo de la lista
    // Puedes hacer una solicitud DELETE a tu API aquí
  };

  const handleActualizarRiesgo = (id) => {
    // Guardar el ID del riesgo a actualizar y abrir el formulario de actualización
    setActualizarId(id);
  };

  const handleRiesgoActualizado = (id, nombre, descripcion) => {
    // Actualizar el riesgo en la lista
    // Puedes hacer una solicitud PUT a tu API aquí
    setActualizarId(null); // Cerrar el formulario de actualización
  };

  return (
    <div>
      <h1>Administración de Riesgos</h1>
      <CrearRiesgo onRiesgoCreado={handleRiesgoCreado} />
      <RiesgoList
        riesgos={riesgos}
        onRiesgoEliminado={handleRiesgoEliminado}
        onRiesgoActualizar={handleActualizarRiesgo}
      />
      {actualizarId && (
        <ActualizarRiesgo
          id={actualizarId}
          onRiesgoActualizado={handleRiesgoActualizado}
        />
      )}
    </div>
  );
}

export default RiesgosPage;
