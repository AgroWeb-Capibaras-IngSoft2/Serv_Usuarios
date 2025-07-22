# Changelog

## [1.1.0] - 2025-07-22
### Added
- Endpoint `/users/` para consultar todos los usuarios.

## [1.1.0] - 2025-07-21
### Added
- **Observabilidad Prometheus:** Se implementó la exposición de métricas Prometheus en el endpoint `/metrics` para monitoreo y análisis del servicio de usuarios.
- **Script de demo de observabilidad:** Añadido `observability/generate_observability_demo.py` para simular tráfico y visualizar métricas en tiempo real.
- **Tests de observabilidad:** Añadido `observability/test_observability.py` para validar el correcto funcionamiento de los endpoints `/health` y `/metrics`.

### Changed
- **Documentación mejorada:**
  - Swagger actualizado para documentar los endpoints `/metrics` y `/health`.
  - README y ejemplos de uso ampliados para reflejar la integración de observabilidad y los nuevos endpoints.

## [1.0.4] - 2025-07-14
### Changed
- Mejorada documentación del README con instrucciones detalladas para Windows y MongoDB
- Agregados comentarios explicativos en el código para mejor mantenibilidad

### Fixed
- Corregida documentación Swagger para usar el puerto correcto (5001)
- Validaciones mejoradas en el modelo de usuario

## [1.0.3] - 2025-07-04
### Changed
- Nueva base de datos en MongoDB

## [1.0.2] - 2025-06-13
### Added
- Documentación Swagger para todos los endpoints de usuario.

## [1.0.1] - 2025-06-11
### Added
- Endpoint `/users/autenticate/` para autenticación de usuario.
- Validación de datos y manejo de errores en los endpoints.

## [1.0.0] - 2025-06-09
### Added
- Estructura inicial del microservicio de usuarios para Agroweb.
- Endpoint `/users/register` para registrar nuevos usuarios.
- Endpoint `/users/getById/<document>` para consultar usuario por documento.
- Endpoint `/users/getByEmail/<email>` para consultar usuario por email.






