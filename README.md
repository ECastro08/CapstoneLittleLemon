# 🚀 Proyecto Final Capstone – Little Lemon

Este proyecto corresponde al **Capstone Final**, desarrollado con **Django y Django REST Framework**, enfocado en la construcción de una **API REST + vistas web** para el restaurante *Little Lemon*.  
Incluye autenticación mediante tokens, endpoints protegidos y buenas prácticas de desarrollo backend.

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python**
- 🌐 **Django**
- 🔁 **Django REST Framework**
- 🔐 **Autenticación por Token**
- 📄 **HTML**
- 🎨 **CSS**
- 📦 **Pipenv**
- 🧱 Patrón **Model–View–Template (MVT)**

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una **arquitectura modular y basada en capas**, separando configuración, lógica de negocio, autenticación y presentación.

### 📁 Estructura general

- **LittleLemon/**
  - Configuración global del proyecto Django
- **restaurant/**
  - Lógica del negocio
  - Endpoints del menú y reservas
- **users/**
  - Gestión de usuarios y autenticación
- **templates/**
  - Vistas HTML renderizadas por Django
- **static/**
  - Archivos CSS

---

## 🔄 Flujo de una petición

1. El cliente realiza una petición HTTP.
2. Django resuelve la ruta en `urls.py`.
3. La vista correspondiente procesa la solicitud.
4. Se valida autenticación (`IsAuthenticated`) si aplica.
5. El serializer transforma los datos.
6. Se devuelve la respuesta en JSON o HTML.

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

Servidor disponible en:  
👉 http://127.0.0.1:8000/

---

## 🔑 Autenticación (Pruebas)

Para acceder a los endpoints protegidos, debes generar un **token de autenticación**.

### 📌 Credenciales de prueba

    username: prueba
    password: contrasenadeprueba

### 📌 Generar token

    POST http://127.0.0.1:8000/auth/token/login

Agregar el token en los headers:

    Authorization: Token TU_TOKEN_AQUÍ

---

## 📊 Endpoints documentados

### 🌐 Vistas Web

| Método | Endpoint | Descripción |
|------|--------|-------------|
| GET | `/restaurant/index/` | Página principal |
| GET | `/restaurant/about/` | Página "About" |

---

### 🍽️ Menú (API REST)

> Protegidos con `IsAuthenticated`

| Método | Endpoint | Descripción |
|------|--------|-------------|
| GET | `/restaurant/menu/` | Listar ítems del menú |
| POST | `/restaurant/menu/` | Crear ítem del menú |
| GET | `/restaurant/menu/<int:pk>/` | Obtener ítem específico |
| PUT | `/restaurant/menu/<int:pk>/` | Actualizar ítem |
| DELETE | `/restaurant/menu/<int:pk>/` | Eliminar ítem |

📌 Implementado con:
- `ListCreateAPIView`
- `RetrieveUpdateDestroyAPIView`

---

### 📅 Reservas / Booking (API REST)

> Protegidos con `IsAuthenticated`

| Método | Endpoint | Descripción |
|------|--------|-------------|
| GET | `/restaurant/booking/` | Listar reservas |
| POST | `/restaurant/booking/` | Crear reserva |
| GET | `/restaurant/booking/<int:pk>` | Obtener reserva |
| PUT | `/restaurant/booking/<int:pk>` | Actualizar reserva |
| DELETE | `/restaurant/booking/<int:pk>` | Eliminar reserva |

---

## 🔐 Seguridad

- Autenticación basada en **Token**
- Uso de `IsAuthenticated` en endpoints sensibles
- Separación clara entre vistas públicas y API protegida

---

## 💻 Interfaz Web

El proyecto incluye una **interfaz web básica**:

- Templates HTML renderizados por Django
- Estilos CSS propios
- Integración directa con el backend
- Ideal para demostrar un enfoque **full-stack ligero**

---

## 🎯 Objetivos del proyecto

- Construir una API REST funcional
- Implementar autenticación segura
- Aplicar buenas prácticas con Django REST Framework
- Integrar backend y vistas web
- Servir como proyecto profesional de portafolio

---

## 📌 Autor

👨‍💻 **Eduardo**  
Ingeniero | Backend Developer  
Apasionado por Django, APIs REST y desarrollo backend profesional

