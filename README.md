# Proyecto Web con Django

Proyecto web dinamico, requiere Django y Pillow para funcionar.

## Tabla de Contenidos

- [Instalación](#instalación)
  - [Requisitos Previos](#requisitos-previos)
  - [Instalación](#instalación)

## Instalación

Instrucciones para instalar y configurar el proyecto localmente.

### Requisitos Previos

Lista de lo que necesitas instalar con anterioridad.

- Python 3.x
- Django
- Pillow

### Instalación

Inicializar el proyecto:

```bash
# Crear un entorno virtual
python -m venv mi_entorno

# Activar el entorno virtual
mi_entorno\Scripts\activate

# Instalar Django y Pillow
pip install django pillow

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Iniciar el servidor
python manage.py runserver

# Conectarse
http://127.0.0.1:8000/usuario/index