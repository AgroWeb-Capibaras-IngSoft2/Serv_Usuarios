# Servicio de Usuarios para Agroweb

Este microservicio maneja las operaciones CRUD para perfiles de usuarios de la plataforma Agroweb. Utiliza MongoDB como base de datos y Flask como framework web.

## Características

- Registro de usuarios con validación de datos
- Autenticación de usuarios  
- Consulta de usuarios por documento o email
- Documentación Swagger automática
- Arquitectura hexagonal (Clean Architecture)

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


## Prerrequisitos

- Python 3.8 o superior
- MongoDB instalado y ejecutándose en localhost:27017
- Git (para clonar el repositorio)

## Configuración de MongoDB

### Instalación de MongoDB

#### Windows
1. **Descargar MongoDB Community Server**:
   - Visita [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
   - Selecciona "Windows" y descarga el archivo MSI
   - Ejecuta el instalador y sigue las instrucciones (acepta la configuración por defecto)

2. **Configurar MongoDB como servicio**:
   - Durante la instalación, asegúrate de marcar "Install MongoDB as a Service"
   - Esto permitirá que MongoDB se inicie automáticamente con Windows

3. **Verificar la instalación**:
   ```cmd
   mongod --version
   mongo --version
   ```

#### Linux (Ubuntu/Debian)
```bash
# Importar la clave pública GPG de MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Crear archivo de lista para MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Actualizar el índice de paquetes
sudo apt-get update

# Instalar MongoDB
sudo apt-get install -y mongodb-org

# Iniciar MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

#### macOS
```bash
# Instalar usando Homebrew
brew tap mongodb/brew
brew install mongodb-community

# Iniciar MongoDB
brew services start mongodb/brew/mongodb-community
```

### Configuración inicial de la base de datos

1. **Conectar a MongoDB**:
   ```bash
   mongo
   ```

2. **Crear la base de datos y colección** (opcional, se crea automáticamente):
   ```javascript
   use Serv_Usuarios
   db.createCollection("Usuarios")
   ```

3. **Verificar la conexión**:
   ```javascript
   show dbs
   use Serv_Usuarios
   show collections
   ```

### Configuración de MongoDB para desarrollo

#### Configuración básica (mongodb.conf)
Para una configuración más robusta, crear un archivo de configuración:

**Windows**: `C:\Program Files\MongoDB\Server\6.0\bin\mongod.cfg`
**Linux/macOS**: `/etc/mongod.conf`

```yaml
# Configuración básica para desarrollo
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true

systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

net:
  port: 27017
  bindIp: 127.0.0.1

processManagement:
  fork: true
  pidFilePath: /var/run/mongodb/mongod.pid
```

#### Iniciar MongoDB manualmente

**Windows**:
```cmd
# Desde la carpeta de instalación de MongoDB
mongod --dbpath "C:\data\db"
```

**Linux/macOS**:
```bash
# Con archivo de configuración
sudo mongod --config /etc/mongod.conf

# O manualmente especificando la ruta
mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --fork
```

### Verificación de la instalación

1. **Verificar que MongoDB esté ejecutándose**:
   ```bash
   # Verificar el proceso
   ps aux | grep mongod
   
   # Verificar el puerto
   netstat -tulpn | grep 27017
   ```

2. **Probar la conexión desde Python**:
   ```python
   from pymongo import MongoClient
   
   try:
       client = MongoClient('localhost', 27017)
       db = client['Serv_Usuarios']
       print("Conexión a MongoDB exitosa")
       client.close()
   except Exception as e:
       print(f"Error conectando a MongoDB: {e}")
   ```

### Solución de problemas comunes

#### MongoDB no inicia
- **Windows**: Verificar que el servicio MongoDB esté iniciado en "Servicios"
- **Linux**: `sudo systemctl status mongod` para verificar el estado
- Verificar que el directorio de datos tenga los permisos correctos

#### Error de conexión
- Verificar que MongoDB esté ejecutándose en el puerto 27017
- Comprobar que no haya firewall bloqueando la conexión
- Verificar la configuración de `bindIp` en el archivo de configuración

#### Espacio en disco insuficiente
- MongoDB requiere al menos 3GB de espacio libre para iniciar
- Verificar espacio disponible: `df -h` (Linux/macOS) o `dir` (Windows)

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd Serv_Usuarios
```

### 2. Crear entorno virtual

**En Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**En Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Iniciar MongoDB
Asegúrate de que MongoDB esté ejecutándose en tu sistema:
- **Windows**: Ejecuta `mongod` desde la línea de comandos o inicia el servicio MongoDB
- **Linux/macOS**: `sudo systemctl start mongod` o `brew services start mongodb/brew/mongodb-community`

## Ejecución

### Iniciar el servicio
```bash
python app.py
```

El servicio estará disponible en `http://localhost:5001`

### Ejecutar pruebas
```bash
python test_users.py
```

## Documentación Swagger

Para acceder a la documentación interactiva de la API:
[http://127.0.0.1:5001/apidocs](http://127.0.0.1:5001/apidocs)

## Endpoints Disponibles

- `POST /users/register` - Registrar nuevo usuario
- `GET /users/getById/<document>` - Obtener usuario por documento
- `GET /users/getByEmail/<email>` - Obtener usuario por email  
- `POST /users/autenticate/` - Autenticar usuario

## Estructura de la Base de Datos

El servicio utiliza MongoDB con la siguiente estructura:
- Base de datos: `Serv_Usuarios`
- Colección: `Usuarios`



