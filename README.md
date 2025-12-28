# 🚀 Proyecto Final Capstone – Backend con Django

Este proyecto corresponde al **Capstone Final**, desarrollado con **Django**, enfocado en la construcción de una API robusta, segura y escalable.  
Incluye autenticación mediante tokens y buenas prácticas de desarrollo backend.

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python**
- 🌐 **Django**
- 🔐 **Autenticación por Token**
- 📦 **Pipenv** para gestión de dependencias

---

## 📥 Clonar el proyecto

    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio

---

## 📦 Instalación de dependencias

Este proyecto usa **Pipenv**:

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

## 🎯 Objetivo del proyecto

- Implementar una API REST funcional
- Aplicar autenticación segura
- Demostrar buenas prácticas en Django
- Servir como proyecto de portafolio profesional

---

## 📌 Autor

👨‍💻 **Eduardo**  
Ingeniero | Backend Developer  
Apasionado por Django, APIs REST y buenas prácticas de software


