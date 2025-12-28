# 🚀 Proyecto Final Capstone – Little Lemon

Este proyecto corresponde al **Capstone Final**, desarrollado con **Django**, enfocado en la construcción de una **aplicación web + API** para el restaurante *Little Lemon*.  
Incluye autenticación mediante tokens, vistas HTML renderizadas en servidor y buenas prácticas de desarrollo backend.

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python**
- 🌐 **Django**
- 📄 **HTML**
- 🎨 **CSS**
- 🔐 **Autenticación por Token**
- 📦 **Pipenv** para gestión de dependencias
- 🧱 Patrón **Model–View–Template (MVT)**

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una **arquitectura modular**, separando claramente la configuración del proyecto, la lógica del negocio, la gestión de usuarios y la presentación.

### 📁 Estructura general del proyecto

- **LittleLemon/**  
  Configuración principal del proyecto Django (settings, urls, wsgi/asgi)
- **restaurant/**  
  Lógica del negocio relacionada con el restaurante
  - Modelos, vistas y rutas asociadas al menú y operaciones de menú
- **users/**  
  Gestión de usuarios
  - Autenticación y autorización (registro, login, perfil)
- **templates/**  
  Vistas HTML renderizadas por Django
- **static/**  
  Archivos estáticos (CSS)

---

## 🔄 Flujo de una petición

1. El cliente realiza una solicitud HTTP (API o vista web).  
2. Django resuelve la ruta mediante `urls.py`.  
3. La vista correspondiente procesa la solicitud.  
4. Si es una API, devuelve una respuesta en JSON.  
5. Si es una vista web, renderiza un template HTML.  
6. Si la ruta está protegida, se valida el token de autenticación antes de continuar. 1

---

## 📥 Clonar el proyecto

    git clone https://github.com/ECastro08/CapstoneLittleLemon.git
    cd CapstoneLittleLemon

---

## 📦 Instalación de dependencias

Este proyecto utiliza **Pipenv**:

    pipenv install
    pipenv shell

---

## ▶️ Ejecutar el servidor

    python manage.py runserver

El servidor estará disponible en:  
👉 http://127.0.0.1:8000/

---

## 🔑 Autenticación (Pruebas)

Para acceder a los endpoints protegidos, primero debes generar un **token de autenticación**.

### 📌 Credenciales de prueba

    username: prueba
    password: contrasenadeprueba

### 📌 Endpoint para generar token

    POST http://127.0.0.1:8000/auth/token/login

Incluye el token en los headers de tus solicitudes:

    Authorization: Token TU_TOKEN_AQUÍ

---

## 📊 Endpoints disponibles

### 🧑‍💻 Autenticación y usuarios

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/auth/token/login/` | Generar token de autenticación |
| `POST` | `/users/register/` | Registrar un nuevo usuario |
| `GET`  | `/users/profile/` | Ver datos de perfil del usuario autenticado |

---

### 🍽️ Restaurante / Menú

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET`  | `/restaurant/` | Listar elementos del restaurante |
| `GET`  | `/restaurant/<id>/` | Ver elemento específico del menú |
| `POST` | `/restaurant/create/` | Crear un nuevo elemento |
| `PUT`  | `/restaurant/update/<id>/` | Actualizar un elemento existente |
| `DELETE` | `/restaurant/delete/<id>/` | Eliminar un elemento del menú |

> 📌 Estos endpoints se derivan de las rutas definidas en tus archivos `urls.py` y vistas correspondientes dentro de la carpeta `restaurant`. 2

---

## 💻 Interfaz Web

El proyecto incluye una **interfaz web básica**:

- Templates HTML renderizados por Django
- Estilos CSS propios
- Formularios y vistas públicas para visualizar el menú y otras secciones
- Integración directa entre backend y frontend

Esto permite demostrar un enfoque **full-stack ligero**, sin depender de frameworks frontend externos.

---

## 🎯 Objetivos del proyecto

- Construir una API REST funcional con Django
- Implementar autenticación segura
- Integrar backend con vistas HTML
- Aplicar separación de responsabilidades
- Servir como proyecto de portafolio profesional

---

## 📌 Autor

👨‍💻 **Eduardo**  
Ingeniero | Backend Developer  
Apasionado por Django, APIs REST y desarrollo de aplicaciones web bien estructuradas


