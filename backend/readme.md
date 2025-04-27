# Proyecto Backend - Documentación

## Clonación del Repositorio

Para clonar este proyecto, ejecuta el siguiente comando en tu terminal:

```bash
git clone https://github.com/EBlanco17/prueba_tecnica_fullstack.git
cd backend
```

## Configuración del Entorno Virtual

Antes de instalar las dependencias, configura un entorno virtual. Sigue los pasos según tu sistema operativo:

### En Windows

1. Crea un entorno virtual:
   ```bash
   python -m venv env
   ```
2. Activa el entorno virtual:
   ```bash
   .\env\Scripts\activate
   ```

### En Linux o macOS

1. Crea un entorno virtual:
   ```bash
   python3 -m venv env
   ```
2. Activa el entorno virtual:
   ```bash
   source env/bin/activate
   ```
   Deberia verse de esta forma:
   ```
   (env) user-notebook:~/Documents/prueba_tecnica_fullstack/backend$
   ```

## Instalación de Dependencias

## Instala `wkhtmltopdf` desde [wkhtmltopdf.org](https://wkhtmltopdf.org/), ya que es necesario para la generación de PDFs ya sea para Windows o alguna versión de linux o Mac.

Una vez configurado el entorno virtual, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Para comprobar que se instaló correctamente deberia haber una carpeta llamada `env/lib/python3.12/site-packages` y dentro todas las dependencias.

## Configuración del Archivo `.env`

Crea un archivo `.env` en la raíz del proyecto basado en el archivo `.env.example`. Asegúrate de completar las variables de entorno requeridas.

```bash
DB_HOST=localhost
DB_PORT=3306
DB_USER=user
DB_PASSWORD=password
DB_NAME=ordenesdb
```

Edita el archivo `.env` con los valores correspondientes.

## Ejecución del Servidor

Antes de llenar la tabla de productos, asegúrate de que el servidor esté en ejecución. Para ello, utiliza el siguiente comando:

```bash
uvicorn app.main:app --reload
```

## Llenado de la Tabla de Productos

Con el servidor en ejecución, ejecuta el siguiente script para llenar la tabla de productos:

```bash
python app/scripts/cargar_productos.py
```

Este script cargará datos iniciales en la base de datos, modifique si lo desea por sus propios productos.

## Pruebas en Swagger

Puedes probar los endpoints del proyecto utilizando Swagger. Una vez que el servidor esté en ejecución, accede a la documentación interactiva en:

```
http://localhost:<PUERTO>/docs
http://127.0.0.1:8000/docs
```

## Pruebas Automatizadas con Pytest

Desde el directorio raíz del proyecto, ejecuta las pruebas automatizadas con el siguiente comando:

```bash
pytest
```

Tener en cuenta que si se ejecutan las pruebas sin haber ejecutado el proyecto, se generará un error de conexión a la base de datos. Para evitar esto, asegúrate de ejecutar el servidor por lo menos una vez antes.

⚠️**Advertencia:** La base de datos se limpiara completamente al finalizar los tests.

## Estructura de Carpetas

La estructura principal del proyecto es la siguiente:

```
backend/
├── .env.example               # Archivo de ejemplo para variables de entorno
├── .gitignore                 # Archivos y carpetas ignorados por Git
├── pytest.ini                 # Configuración de pytest
├── requirements.txt           # Dependencias del proyecto
├── schema.sql                 # Script SQL para crear la base de datos
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada del servidor FastAPI
│   ├── init_db.py             # Inicialización de la base de datos
│   ├── api/                   # Endpoints de la API
│   │   ├── ordenes.py
│   │   ├── productos.py
│   ├── core/                  # Configuración y base de datos
│   │   ├── config.py
│   │   ├── database.py
│   ├── models/                # Modelos de SQLAlchemy
│   ├── schemas/               # Esquemas de Pydantic
│   ├── pdf/                   # Generación de reportes PDF
│   │   ├── generate_pdf.py
│   │   ├── templates/
│   │       ├── report.html    # Plantilla HTML para el reporte PDF
│   ├── scripts/               # Scripts adicionales
│       ├── cargar_productos.py
├── tests/                     # Pruebas del proyecto
│   ├── test_ordenes.py
│   ├── test_productos.py
```

Cada carpeta y archivo tiene un propósito específico:

- `app/`: Contiene la lógica principal del proyecto.
- `scripts/`: Scripts auxiliares como el de carga de productos.
- `tests/`: Pruebas automatizadas para garantizar el correcto funcionamiento.
- `main.py`: Punto de entrada de la aplicación.
- `.env.example`: Archivo de ejemplo para configuración de variables de entorno.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.
- `readme.md`: Documentación del proyecto.
  readme.md
  Mostrando readme.md.
