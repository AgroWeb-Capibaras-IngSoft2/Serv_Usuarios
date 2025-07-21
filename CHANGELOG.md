# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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






