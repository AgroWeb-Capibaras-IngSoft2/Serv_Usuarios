

# 👤 Servicio de Gestión de Usuarios - AgroWeb

## 📖 Descripción General

Microservicio para la gestión de usuarios de la plataforma AgroWeb, con **observabilidad integrada** y arquitectura limpia. Permite registrar, autenticar y consultar usuarios, exponiendo métricas en tiempo real para monitoreo y análisis.

## 🗂️ Estructura del Proyecto

```
Serv_Usuarios/
├── app.py                          # Aplicación Flask con instrumentación
├── requirements.txt                # Dependencias
├── test_users.py                   # Pruebas automatizadas
├── application/                    # Casos de uso del negocio
├── domain/                         # Entidades y repositorios
├── Infrastructure/                 # Adaptadores de BD
├── flask_interface/                # Endpoints HTTP
├── observability/                  # Scripts de observabilidad
│   ├── generate_observability_demo.py
│   └── test_observability.py
├── swagger/                        # Documentación API
└── README.md
```

## ✅ Requisitos

- **Runtime:** Python 3.8+ (recomendado: 3.11)
- **Base de Datos:** MongoDB 6.0+ (local en `localhost:27017`)
- **Dependencias Python:** Flask, prometheus_client, flasgger, pymongo

## 🚀 Instalación y Ejecución Paso a Paso

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd Serv_Usuarios
```

### 2. Crear entorno virtual
**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```
**Linux/macOS:**
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
- **Windows:** Ejecuta `mongod` o inicia el servicio MongoDB
- **Linux/macOS:** `sudo systemctl start mongod` o `brew services start mongodb/brew/mongodb-community`

### 5. Iniciar el servicio
```bash
python app.py
```
El servicio estará disponible en [http://localhost:5001](http://localhost:5001)

### 6. Ejecutar pruebas
```bash
python test_users.py
```

## 📄 Documentación API

Swagger UI disponible en: [http://localhost:5001/apidocs](http://localhost:5001/apidocs)

## 📡 Endpoints de la API

- `POST /users/register` - Registrar nuevo usuario
- `GET /users/getById/<document>` - Obtener usuario por documento
- `GET /users/getByEmail/<email>` - Obtener usuario por email
- `POST /users/autenticate/` - Autenticar usuario
- `GET /health` - Estado del servicio (health check)
- `GET /metrics` - Métricas Prometheus para observabilidad

## 📊 Observabilidad y Métricas

La **observabilidad** permite monitorear el estado y rendimiento del servicio en tiempo real. Este microservicio expone métricas Prometheus en `/metrics` y un endpoint de salud en `/health`.

### 🔍 Prometheus - Recolección de Métricas
- **`usuarios_requests_total`** - Contador de peticiones HTTP por endpoint y método
- **`usuarios_request_duration_seconds`** - Latencia de peticiones por endpoint
- **`usuarios_errors_total`** - Contador de errores por endpoint
- **Métricas del sistema Python** - Uso de memoria, CPU, GC

### Demo de Observabilidad
```bash
python observability/generate_observability_demo.py
```
El script genera tráfico para visualizar métricas en tiempo real en `/metrics`.

### Tests de Observabilidad
```bash
python observability/test_observability.py
```
Valida que los endpoints `/health` y `/metrics` funcionen correctamente.

## 🧪 Ejemplos de Uso

```bash
# Verificar estado del servicio
curl http://localhost:5001/health

# Ver métricas de observabilidad
curl http://localhost:5001/metrics

# Registrar usuario
curl -X POST http://localhost:5001/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "document": "12345678",
    "email": "usuario@agroweb.com",
    "name": "Juan Pérez",
    "password": "secreto123"
  }'

# Obtener usuario por documento
curl http://localhost:5001/users/getById/12345678

# Obtener usuario por email
curl http://localhost:5001/users/getByEmail/usuario@agroweb.com

# Autenticar usuario
curl -X POST http://localhost:5001/users/autenticate/ \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@agroweb.com", "password": "secreto123"}'
```

## 🔧 Troubleshooting

| Problema | Solución |
|----------|----------|
| **API no responde** | Verificar que MongoDB esté ejecutándose y `python app.py` activo |
| **Error de conexión a MongoDB** | Revisar puerto 27017 y permisos de carpeta de datos |
| **Métricas no aparecen** | Acceder a `/metrics` y generar tráfico con el script demo |
| **Dependencias faltantes** | Ejecutar `pip install -r requirements.txt` en entorno virtual |
| **Puerto 5001 ocupado** | Cambiar puerto en `app.py` o cerrar proceso conflictivo |

## 📝 Notas Técnicas

- **Base de Datos:** MongoDB, base `Serv_Usuarios`, colección `Usuarios`
- **IDs:** El campo `document` es el identificador principal del usuario
- **Observabilidad:** Métricas estándar de Prometheus integradas
- **Arquitectura:** Hexagonal (Clean Architecture) para escalabilidad y mantenibilidad
- **Swagger:** Documentación interactiva en `/apidocs`
- **Integración:** Otros servicios (como productos) validan usuarios mediante `GET /users/getById/<document>`

---
AgroWeb - Gestión de Usuarios | Observabilidad y monitoreo nativos | 2025