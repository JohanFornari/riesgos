import React, { useState } from 'react';

function SeleccionarPais({ paises, onPaisSeleccionado }) {
  const [paisSeleccionado, setPaisSeleccionado] = useState('');

  const handleChange = (e) => {
    setPaisSeleccionado(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onPaisSeleccionado(paisSeleccionado);
  };

  return (
  
  );
}

export default SeleccionarPais;
