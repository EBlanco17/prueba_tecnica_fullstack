# Frontend - Proyecto Fullstack

Este documento detalla las instrucciones para clonar, instalar y ejecutar el proyecto frontend, así como la estructura de carpetas, los requisitos necesarios y las tecnologías utilizadas.

## Requisitos

- **Node.js**: Versión 22 o superior.
- **NPM**: Incluido con Node.js.

## Tecnologías Utilizadas

- **Vite**: Herramienta de construcción rápida para proyectos frontend.
- **Tailwind CSS**: Framework de utilidades CSS para un diseño rápido y eficiente.

## Clonación del Repositorio

```bash
git clone https://github.com/EBlanco17/prueba_tecnica_fullstack.git
cd frontend
```

## Instalación de Dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
npm install
```

## Ejecución del Proyecto

Para iniciar el servidor de desarrollo, utiliza:

```bash
npm start
o npm run dev
```

El proyecto estará disponible en `http://localhost:3000`.

## Estructura de Carpetas

```plaintext
├── public/          # Archivos estáticos
├── src/
│   ├── components/  # Componentes reutilizables
│   ├── pages/       # Páginas principales
│   ├── assets/      # Recursos como imágenes y estilos
│   ├── utils/       # Funciones auxiliares
│   ├── App.js       # Componente principal
│   ├── services/    # Servicios para la comunicación con la API
│   ├── index.js     # Punto de entrada
├── package.json     # Configuración del proyecto
```

## Documentación

- **TypeDoc**: Genera documentación para el código TypeScript. Puedes ejecutarlo con:

```bash
npm run doc
```

Se generará la documentación en la carpeta `docs`.
Y puedes abrir el archivo `index.html` en un navegador para ver la documentación generada.

## Notas Adicionales

- Asegúrate de tener instalada la versión correcta de Node.js antes de comenzar.
- Si encuentras problemas, verifica las dependencias en el archivo `package.json`.
- Este proyecto utiliza **Vite** para un entorno de desarrollo rápido y **Tailwind CSS** para estilos personalizados.
- Consulta la documentación oficial de Vite y Tailwind CSS si necesitas más información.
