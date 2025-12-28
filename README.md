# Proyecto Final Capstone
# Clonar el proyecto
# instalar dependencias
    `pipenv shell`
# correr servidor Django
    `python manage.py runserver`

## Endpoints para prueba

### generar token proporcionando los siguientes datos:
password = contrasenadeprueba


username = prueba

http://127.0.0.1:8000/auth/token/login

#### edpoint para ver el menu del restaurante, ingresar el token en la pestana auth la opcion Bearer token y el prefijo Token
http://127.0.0.1:8000/restaurant/menu/

#### edpoint para ver las reservas hechas, ingresar el token en la pestana auth la opcion Bearer token y el prefijo Token
http://127.0.0.1:8000/restaurant/booking/


