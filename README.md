Se requiere tener instalado la ultima versión de python y node.js preferiblemente 
React: 
Descargamos el codigo fuente y lo guardamos en un directorio 

Ingresamos a la carpeta app_riesgos de la aplicación y abrimos la consola de comandos 

ejecutamos el siguiente comando: 

npm install

Flask:

Ahora en una nueva ventana ingresamos a la carpeta llamada backend y abrimos la consola de comandos del CMD 
donde ejecutamos los siguientes comandos en ese orden 
py -3 -m venv .venv
.venv\Scripts\activate

Luego procedemos a instalar los siguientes complementos de flask y python  ejecutándolos en la consola de comandos en orden: 

pip install Flask-SQLAlchemy psycopg2-binary
pip install Flask-SQLAlchemy
pip install Flask-JWT-Extended
pip install Flask
pip install Flask-Login
pip install request
pip install flask-cors
pip install PyJWT


Ahora procedemos a configurar la base de datos a la cual nos queremos conectar: 
Abrimos el archivo app.py y configuramos la conexión de base de datos, usuario y contraseña. En mi caso utilizo postgrest

# Configuración de la URL de conexión a la base de datos en PostgreSQL

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/gestion_riesgos'
![image](https://github.com/JohanFornari/riesgos/assets/25940586/17bd15be-ae27-4268-bd36-952d3904642e)

guardamos y en la consola cmd ejecutamos el siguiente script para la creación de los usuarios y algunos riesgos

![image](https://github.com/JohanFornari/riesgos/assets/25940586/40fd8249-7ae2-4757-926b-bf8736bdd8af)

despues procedemos a subir el servidor de flask de la siguiente manera 

en la consola de comandos ejecutamos el siguiente script
python app.py
![image](https://github.com/JohanFornari/riesgos/assets/25940586/3b3984a2-1828-4a2b-b5f2-caf69530603d)


Ahora nos devolvemos a la consola de comandos inicial de react, y procedemos a ejecutar el siguiente comando para subir el servidor 

npm start

![image](https://github.com/JohanFornari/riesgos/assets/25940586/f94e0915-94cb-4c14-bfd1-cdb0b0331bd7)


En este momento nuestra aplicación esta desplegada. 


para ejecutar las pruebas automaticas apagamos el servidor y ejecutamos el siguiente comando 
pytest
![image](https://github.com/JohanFornari/riesgos/assets/25940586/81097acb-ec3d-479c-b8c4-f6c3f99299b2)


Pagina de inicio del aplicativo

![image](https://github.com/JohanFornari/riesgos/assets/25940586/5aaa5de5-39ec-408a-96e0-e12ee1f594d1)

para acceder al servicio se tienen los usuarios por defecto: 
usuario: admin 
contraseña: admin123

usuario: user 
contraseña: user123

se pueden crear riesgos 
![image](https://github.com/JohanFornari/riesgos/assets/25940586/c7e101ef-c1e1-41a1-92f4-e3e49a0935cd)

ver riesgos, modificar y eliminar
![image](https://github.com/JohanFornari/riesgos/assets/25940586/0c366531-8186-4a87-ac46-ad25a96a3a19)

![image](https://github.com/JohanFornari/riesgos/assets/25940586/a30997d1-e71f-45ff-9a01-c4e1a3c1306e)

