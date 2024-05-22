# Segundo Parcial
## Programación Web III - MVC API RESTful

### Antes de Empezar:

1. Realiza un **Fork** de este repositorio:

![Repositorio del Segundo Parcial](https://live.staticflickr.com/65535/53738608284_706405e96e_z.jpg)

2. Si vas a trabajar en tu equipo local clona el nuevo repositorio resultado del **Fork** y ábrelo con **VSCode** o el editor de tu preferencia para trabajar tu solución. También puedes trabajar tu solución en **GitHub Codespaces**.

3. Completa tus datos personales en la siguiente tabla:
    | Nombre   | Apellido   | CI   |
    | -------- | ---------- | ---- |
    | `Ignacio` | `Condori` | `12704046` |

4. Realiza un commit de esta modificación y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "datos actualizados"
    git push origin main
    ```
5. En la terminal ejecuta el siguiente comando para instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Contexto:

Eres el **Back-End Developer** de una StarUp que esta desarrollando una aplicación de gestión de tareas de equipos de trabajo. Debes desarrollar una **API MVC RESTful** que permita administrar la información de las tareas de pendientes, en curso y completadas de un equipo de trabajo. 

Se debe almacenar en **Base de Datos** los siguientes datos de las **Tareas**:
- **id**: Identificador único de la tarea. De tipo **entero y autoincremental**.
- **title**: Título de la tarea. De tipo **cadena de texto**.
- **description**: Descripción de la tarea. De tipo **cadena de texto**.
- **status**: Estado de la tarea (pendiente, en curso, completada). De tipo **cadena de texto**.
- **created_at**: Fecha de creación de la tarea. De tipo **cadena de texto**.
- **assigned_to**: Nombre del usuario asignado a la tarea. De tipo **cadena de texto**.

Se debe almacenar en **Base de Datos** los siguientes datos de los **Usuarios**:
- **id**: Identificador único del usuario. De tipo **entero y autoincremental**.
- **name**: Nombre del usuario. De tipo **cadena de texto**.
- **email**: Correo electrónico del usuario. De tipo **cadena de texto**.
- **password**: Contraseña del usuario. De tipo **cadena de texto**.
- **role**: Rol del usuario (admin, member). De tipo **cadena de texto**.

Existe un usuario administrador (`admin`) del equipo que puede realizar las siguientes acciones:
- **Listar las tareas**: Listar todas las tareas del equipo.
- **Mostar una tarea**: Mostrar la información de una tarea específica.
- **Crear una tarea**: Crear una nueva tarea.
- **Actualizar una tarea**: Actualizar una tarea existente.
- **Eliminar una tarea**: Eliminar una tarea existente. 

Existe un usuario miembro (`member`) del equipo que puede realizar las siguientes acciones:
- **Listar las tareas**: Listar todas las tareas del equipo.
- **Mostar una tarea**: Mostrar la información de una tarea específica.

Los usuarios deben autenticarse en la API para poder realizar las acciones permitidas. Se debe utilizar **JWT** para la autenticación de los usuarios.

### Tareas:

Construye una **API MVC RESTful** documentada con **Swagger** que permita realizar las operaciones **CRUD** sobre las tareas del equipo de trabajo y los usuarios del sistema.

1. Crear un usuario administrador (`admin`) con los siguientes datos:
    - **name**: `Washington`
    - **email**: `gwash@gmail.com`
    - **password**: `admin`
    - **role**: `admin`
2. Crear un usuario miembro (`member`) con los siguientes datos:
    - **name**: `Hamilton`
    - **email**: `aham@gmail.com`
    - **password**: `member`
    - **role**: `member`
3. Crear una tarea con los siguientes datos:
    - **title**: `Desarrollar API RESTful`
    - **description**: `Desarrollar una API RESTful con Python y Flask`
    - **status**: `pendiente`
    - **assigned_to**: `Washington`
    - **created_at**: `22-05-2024`
4. Crear una tarea con los siguientes datos:
    - **title**: `Desplegar API RESTful`
    - **description**: `Desplegar una API RESTful en Heroku`
    - **status**: `en curso`
    - **assigned_to**: `Hamilton`
    - **created_at**: `23-05-2024`
5. Actualizar la tarea con `id=1` con los siguientes datos:
    - **status**: `en curso`
6. Eliminar la tarea con `id=2`.
7. Listar todas las tareas del equipo.
8. Mostrar la información de la tarea con `id=1`.
9. Levantar la documentación de la API con **Swagger** en la ruta `/api/docs`.

### Rutas y resultados esperados:
Revisa el documento [swagger.json](app/static/swagger.json) para conocer las rutas y los resultados esperados de la API.

### Restricciones:
1. Debes utilizar **Python** como lenguaje de programación.
2. Debes utilizar el framework **Flask** para el desarrollo de la API.
3. Debes utilizar **SQLAlchemy** como ORM para la conexión con la Base de Datos.
4. Debes utilizar **SQLite** como motor de Base de Datos.
5. Debes utilizar **Swagger** para documentar la API.
6. Debes utilizar **JWT** para la autenticación de los usuarios.
7. Las respuestas de la API deben ser en formato **JSON**.
8. Debes utilizar el patrón de diseño **MVC** para la estructura de tu proyecto.
9. Debes manejar los errores y excepciones que puedan ocurrir en la API con los códigos de estado HTTP correspondientes.

## Entrega:
1. La estructura de carpetas de tu solución debe estar dentro de la carpeta `app`
2. Una vez tengas tu solución debes realizar un **Commit** y un **Push** a tu repositorio en **GitHub** ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "Entrega Final"
    git push origin main
    ```
3. Una vez completado el paso anterior adjunta la **URL** de tu repositorio de **GitHub** en la tarea asignada en **Google Classroom**. 


### Restricciones:

Durante el examen solo puede consultar los siguientes recursos:
- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Documentación de SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Documentación de Flask Login](https://flask-login.readthedocs.io/en/latest/)
- [Documentación de JWT](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Documentación de SQLite](https://www.sqlite.org/docs.html)
- [Documentación de Swagger](https://swagger.io/docs/)
