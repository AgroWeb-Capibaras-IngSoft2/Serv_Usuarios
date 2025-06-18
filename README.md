# Servicio de usuario para el proyecto Agroweb

Este servicio se especializa en operaciones CRUD, en torno a perfiles de usuarios que se inscriben a la plataforma agroweb. 

## Estructura del servicio

```bash
├── application
│   ├── __init__.py
│   └── useCases
│       ├── __init__.py
│       ├── AuthenticationService.py
│       ├── GetUserEmailService.py
│       ├── GetUserIdService.py
│       └── RegisterUserService.py
├── domain
│   ├── entidades
│   │   ├── __init__.py
│   │   └── user_model.py
│   ├── __init__.py
│   └── repositorio
│       ├── __init__.py
│       └── user_repo.py
├── flask_interface
│   ├── __init__.py
│   └── routes.py
├── Infrastructure
│   ├── adapterUserRepo.py
│   ├── DB.py
│   ├── __init__.py
├── app.py
├── __init__.py
├── README.md
└── requirements.txt
```


## Documentación Swagger

Para la documentación ingresar al siguiente link:
[[http://127.0.0.1:5001/apidocs]]

## Como contribuir?

Descarga el repositorio, y crea un python enviroment con el siguiente comando:
```bash
python3 -m venv .venv
```
Luego activa el enviroment.

```bash
source .venv/bin/activate
```
Por último, ejecuta el siguiente comando para instalar las dependencias.

```bash
pip install -r requirements.txt
```



