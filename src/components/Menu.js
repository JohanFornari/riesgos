import React from 'react';
import axios from 'axios';

function Menu({ onMenuClick }) {

  return (

    <div>
      <div className= "form-label">
      <div className="btn-group">
      <button className="btn btn-outline-primary" onClick={() => onMenuClick('crear')}>Crear Riesgo</button>
      <button className="btn btn-outline-success" onClick={() => onMenuClick('ver')}>Ver Riesgos</button>
      <button className="btn btn-outline-primary" onClick={() => onMenuClick('crearUsuario')}>Crear Usuario</button>
      <button className="btn btn-outline-dark" onClick={() => onMenuClick('cerrar')}>Cerrar Sesion</button>
    </div>
    </div>
    </div>
  );
}

export default Menu;
