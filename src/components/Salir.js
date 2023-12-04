import React, { useEffect } from 'react';
import axios from 'axios';

function Salir() {

  
  useEffect(() => {
    
    sessionStorage.removeItem('token')
    window.location.href = '/';
    
    axios.post('/api/logout')
    .then(response => {
     console.log('Cerrar Sesión')
     console.log(response.data)
      // Redireccionar a la página de dashboard
      window.location.href = '/';
    })
    .catch(error => {
      console.error('Error Cierre', error);
      window.location.href = '/';
    });
   
  });

 
}

export default Salir;
