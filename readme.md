# Proyecto API con Django y Nuxt.js

Este proyecto consiste en un backend desarrollado con Django que expone una API para obtener una lista de productos, y un frontend desarrollado con Nuxt.js que consume y muestra esos datos.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Configuración del Proyecto](#configuración-del-proyecto)
- [Backend (Django)](#backend-django)
- [Frontend (Nuxt.js)](#frontend-nuxtjs)
- [Uso](#uso)
- [Solución de Problemas](#solución-de-problemas)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Requisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- Python 3.8 o superior
- Node.js (versión 14 o superior)
- npm (incluido con Node.js)
- Git (opcional, para clonar el proyecto)

## Configuración del Proyecto

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <DIRECTORIO_DEL_REPOSITORIO>
   ```

2. Crea un archivo `.env` en la raíz del proyecto y configura las variables de entorno necesarias (si es aplicable).

## Backend (Django)

### Configuración del Entorno Virtual

1. Crea y activa un entorno virtual:

   **En macOS/Linux:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   **En Windows:**
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Configuración de la Base de Datos

1. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

2. (Opcional) Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

### Ejecución del Servidor de Desarrollo

```bash
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000/api/products/`.

## Frontend (Nuxt.js)

1. Navega al directorio del frontend:
   ```bash
   cd frontend
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```

El frontend estará disponible en `http://localhost:3000/`.

## Uso

1. Asegúrate de que tanto el backend como el frontend estén en ejecución.
2. Abre un navegador y visita `http://localhost:3000/` para ver la lista de productos.
3. Para acceder al panel de administración de Django, visita `http://localhost:8000/admin/` (necesitarás las credenciales de superusuario).

## Solución de Problemas

- **Problemas de CORS:** Verifica que `django-cors-headers` esté correctamente configurado en `settings.py`:
  ```python
  INSTALLED_APPS = [
      # ...
      'corsheaders',
  ]

  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
      # ...
  ]

  CORS_ALLOWED_ORIGINS = [
      "http://localhost:3000",
  ]
  ```

- **Errores de dependencias:** Asegúrate de que todas las dependencias estén instaladas y actualizadas:
  ```bash
  pip install -r requirements.txt
  npm install
  ```