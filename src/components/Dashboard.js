import React, { useState } from 'react';
import CrearRiesgo from './CrearRiesgo';
import RiesgoList from './ListarRiesgos';
import ActualizarRiesgo from './ActualizarRiesgo';
import CrearUsuario from './CrearUsuario';
import Salir from './Salir';
import Menu from './Menu';

function Dashboard() {
  const [opcionMenu, setOpcionMenu] = useState(null);

  const handleMenuClick = (opcion) => {
    setOpcionMenu(opcion);
  };



  let contenido;

  switch (opcionMenu) {
    case 'crear':
      contenido = <CrearRiesgo onRiesgoCreado={nuevoRiesgo => {}} />;
      break;
    case 'modificar':
      contenido = <ActualizarRiesgo onRiesgoActualizado={nuevoRiesgo => {}} />;
      break;
    case 'ver':
      contenido = <RiesgoList />;
      break;
    case 'crearUsuario':
        contenido = <CrearUsuario />;
        break;
    case 'cerrar':
        contenido = <Salir />;
        break;
    default:
      contenido = null;
    
  
  
  }

  return (
    <div className="App">
      <div  className="container">
      <h1 className="display-2">Administración de Riesgos</h1>
      <Menu onMenuClick={handleMenuClick} />
      {contenido}
      </div>
    </div>
  );
}

export default Dashboard;
