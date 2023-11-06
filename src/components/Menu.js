import React from 'react';

function Menu({ onMenuClick }) {
  return (

    <div>
      <div className= "form-label">
      <div className="btn-group">
      <button className="btn btn-outline-primary" onClick={() => onMenuClick('crear')}>Crear Riesgo</button>
      <button className="btn btn-outline-success" onClick={() => onMenuClick('ver')}>Ver Riesgos</button>
    </div>
    </div>
    </div>
  );
}

export default Menu;
