# Mis representantes

## Objetivo
Obtener información sistemática, ordenada y accesible de nuestros 
representantes en México.

- Senadores (WIP)
- Diputados
- ???

## Proyecto (django)
El proyecto está montando en:
- `Django 3.2`
- `Python 3.10`
- `pipenv 2022.5.2`

El objetivo es tener scrappers que obtegan la información directo de las 
fuentes y guarden en data en la base de datos, luego que dicha información 
sea accesible a través de un portal web y/o un API.

### Instalación
1. Instalar python 3.10
```
https://www.python.org/downloads/
```
2. instalar pipenv
```
python -m pip install pipenv
```
3. O actualizar pipenv
```
python -m pip install pipenv --upgrade
```
4. Installar dependencias
```
pipenv sync --dev
```

### Aplicar migraciones
```
pipenv run manage.py migrate
```

### Instalar el dump de la base de datos
```
pipenv run manage.py ...
```

### Lanzar django
1. Lanzar django
```
pipenv run manage.py runserver
```
2. Visitar http://127.0.0.1:8080 

### Pruebas unitarias

## Herramientas

### Scrappers


## Contribuciones
¿Te gustaría añadir funcionalidad? ¿Corregir un bug?