# Prueba Técnica – Desarrollador Fullstack

## 📝 Contexto

Este proyecto simula el desarrollo de un sistema web diseñado para gestionar compras e inventarios. La finalidad es evaluar habilidades clave como la implementación de lógica de negocio, manejo de bases de datos relacionales y creación de interfaces de usuario intuitivas y funcionales.

---

## 🎯 Objetivo

El objetivo principal es desarrollar una funcionalidad que permita registrar órdenes de compra con múltiples productos. Esto incluye:

- Seleccionar productos desde un catálogo.
- Calcular automáticamente subtotales y totales de las órdenes.
- Registrar las órdenes en una base de datos mediante una API RESTful.
- Consultar y visualizar las órdenes previamente registradas.

---

## 📌 Requisitos funcionales

### 📋 Formulario para registrar órdenes de compra

- Permitir la selección de uno o más productos desde un listado.
- Cada producto debe incluir su nombre, cantidad (número entero positivo) y precio unitario (número decimal positivo).
- Calcular automáticamente el subtotal por producto y el total general de la orden.
- Posibilidad de eliminar productos antes de registrar la orden.
- Validación los datos tanto en el frontend como en el backend.

### 🌐 API RESTful

- Endpoints principales:
  - `POST /ordenes`: Crear una nueva orden de compra.
  - `GET /ordenes`: Listar todas las órdenes registradas.
  - `GET /ordenes/{id}`: Consultar los detalles de una orden específica.
  - `PUT /ordenes/{id}`: Actualizar una orden existente.
  - `DELETE /ordenes/{id}`: Eliminar una orden.
  - `GET /Productos/top3`: Obtener los tres productos más comprados.
  - Generar un reporte en PDF con el top 3 de productos más vendidos.

### 🛢️ Base de datos

- Modelo relacional que incluye:
  - Tabla para órdenes de compra.
  - Tabla para detalles de las órdenes.
  - Tabla para productos.
- Uso de claves primarias, foráneas, restricciones e índices básicos.

---

## 📂 Estructura del proyecto

El proyecto está organizado en las siguientes carpetas principales:

- **Frontend**: Contiene la interfaz de usuario que permite interactuar con el sistema.
- **Backend**: Incluye la lógica de negocio, la API RESTful y la conexión con la base de datos.
- **Docs**: Contiene documentación adicional, como diagramas UML y requisitos.

---

## 🚀 Clonación del repositorio

Para obtener una copia local del proyecto, ejecuta el siguiente comando:

```bash
git clone https://github.com/EBlanco17/prueba_tecnica_fullstack.git
```

---

## 📦 Instalación

1. Clona el repositorio en tu máquina local.
2. Configura las variables de entorno en un archivo `.env` basado en el ejemplo proporcionado (`.env.example`).
3. Sigue las instrucciones específicas en las carpetas `frontend/` y `backend/` para instalar las dependencias y ejecutar el proyecto.

---

## 🛠️ Tecnologías utilizadas

- **Frontend**: React, Vite, Tailwind CSS, Typedoc.
- **Backend**: Python, FastApi, uvicorn,
  sqlalchemy, pymysql, python-dotenv, jinja2, pdfkit.
- **Base de datos**: MySql.
- **Pruebas**: pytest.
- **Documentación**: Swagger para la API RESTful y **TypeDoc para el frontend con TypeScript**.
- **Control de versiones**: Git y GitHub para el manejo del código fuente.
- **Entorno de desarrollo**: Visual Studio Code.
- **Sistema de gestión de base de datos**: MySQL Workbench para la administración de la base de datos.

---

## 🧪 Pruebas

El backend incluye pruebas automatizadas para garantizar la funcionalidad de los endpoints. Para ejecutarlas, sigue las instrucciones en la carpeta `backend/`.
