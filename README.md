[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

# tiendaOnlineDjango
Tienda online backend with Django

Setup de entorno local para desarrollo
-------------

### Crear el entorno virtual
    pyenv local 3.13.0
    python -m venv env


### Instalacion de requirements
    pip install -r requirements.txt


### Crear imagen y contenedor para la bd Postgress

Se requiere tener instalado docker 

```bash
docker build --build-arg USER_ID=1000 --build-arg GROUP_ID=1000 -t postgresbdimg .

docker volume create pgdbdatawebstore

docker run --name webstore-postgres --user 1000:1000 -v pgdbdatawebstore:/var/lib/postgresql/data -p 5432:5432 -d postgresbdimg
```

### Migrar la base de datos

```bash
python manage.py migrate
```
