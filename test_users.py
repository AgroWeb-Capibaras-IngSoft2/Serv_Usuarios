"""
Pruebas de integración para el servicio de usuarios
Ejecuta pruebas completas de todos los endpoints disponibles
Asegúrate de que el servicio esté ejecutándose en http://127.0.0.1:5001
"""

import requests

BASE_URL = "http://127.0.0.1:5001"

# Datos de prueba para registrar usuarios
users = [
    {
        "firstName": "Juan",
        "middleName": "Carlos",
        "surName1": "Pérez",
        "surName2": "Gómez",
        "userType": "seller",
        "bornDate": "1990-05-10",
        "department": "Cundinamarca",
        "municipality": "Bogotá",
        "trail": "urbano",
        "email": "juan.perez@hotmail.com",
        "typeDocument": "CC",
        "numberDocument": "100000001",
        "phoneNumber": "3001234567",
        "hashPassword": "password123",
        "username": "juanperez"
    },
    {
        "firstName": "Ana",
        "middleName": "María",
        "surName1": "Rodríguez",
        "surName2": "López",
        "userType": "buyer",
        "bornDate": "1985-08-20",
        "department": "Antioquia",
        "municipality": "Medellín",
        "trail": "rural",
        "email": "ana.rodriguez@hotmail.com",
        "typeDocument": "CC",
        "numberDocument": "100000002",
        "phoneNumber": "3012345678",
        "hashPassword": "password456",
        "username": "anarodriguez"
    }
]

def test_register_users():
    """Prueba el registro de usuarios con datos válidos"""
    print("Testing user registration...")
    for user in users:
        resp = requests.post(f"{BASE_URL}/users/register", json=user)
        print(f"POST /users/register {user['email']} ->", resp.status_code, resp.json())

def test_get_all_users():
    """Prueba de la consulta de todos los usuarios"""
    print("Testing get all users...")
    resp = requests.get(f"{BASE_URL}/users")
    print(f"GET /users/", resp.status_code, resp.json())


def test_get_user_by_id():
    """Prueba la consulta de usuarios por número de documento"""
    print("\nTesting get user by document...")
    for user in users:
        doc = user["numberDocument"]
        resp = requests.get(f"{BASE_URL}/users/getById/{doc}")
        print(f"GET /users/getById/{doc} ->", resp.status_code, resp.json())

def test_get_user_by_email():
    """Prueba la consulta de usuarios por dirección de email"""
    print("\nTesting get user by email...")
    for user in users:
        email = user["email"]
        resp = requests.get(f"{BASE_URL}/users/getByEmail/{email}")
        print(f"GET /users/getByEmail/{email} ->", resp.status_code, resp.json())

def test_authenticate_users():
    """Prueba la autenticación de usuarios con credenciales válidas"""
    print("\nTesting user authentication...")
    for user in users:
        data = {
            "email": user["email"],
            "hashPassword": user["hashPassword"]
        }
        resp = requests.post(f"{BASE_URL}/users/autenticate/", json=data)
        print(f"POST /users/autenticate {user['email']} ->", resp.status_code, resp.json())

def test_user_not_found():
    """Prueba casos de error: usuarios no encontrados y credenciales incorrectas"""
    print("\nTesting user not found cases...")
    resp = requests.get(f"{BASE_URL}/users/getById/999999999")
    print("GET /users/getById/999999999 ->", resp.status_code, resp.json())
    resp = requests.get(f"{BASE_URL}/users/getByEmail/noexiste@example.com")
    print("GET /users/getByEmail/noexiste@example.com ->", resp.status_code, resp.json())
    data = {"email": "juan.perez@example.com", "hashPassword": "wrongpass"}
    resp = requests.post(f"{BASE_URL}/users/autenticate/", json=data)
    print("POST /users/autenticate (wrong password) ->", resp.status_code, resp.json())
    data = {"email": "juan.perez@hotmail.com", "hashPassword": "wrongpass"}
    resp = requests.post(f"{BASE_URL}/users/autenticate/", json=data)
    print("POST /users/autenticate (wrong password) ->", resp.status_code, resp.json())

def cleanup_test_users():
    """
    Limpia los usuarios de prueba de la base de datos
    Elimina los usuarios creados durante las pruebas para mantener la base de datos limpia
    """
    print("\nCleaning up test users...")
    
    # Note: Since there's no delete endpoint in the current API,
    # we'll need to use MongoDB directly for cleanup
    try:
        from pymongo import MongoClient
        
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['Serv_Usuarios']
        collection = db['Usuarios']
        
        # Delete test users by their document numbers
        test_documents = ["100000001", "100000002"]
        deleted_count = 0
        
        for doc_num in test_documents:
            result = collection.delete_one({"numberDocument": doc_num})
            deleted_count += result.deleted_count
            if result.deleted_count > 0:
                print(f"Deleted user with document: {doc_num}")
        
        client.close()
        print(f"Cleanup completed. Deleted {deleted_count} test users.")
        
    except Exception as e:
        print(f"Error during cleanup: {e}")
        print("Test users may still exist in the database.")

if __name__ == "__main__":
    """
    Ejecuta todas las pruebas de integración del servicio de usuarios
    Asegúrate de que el servicio esté ejecutándose antes de ejecutar estas pruebas
    """
    print("=== INICIANDO PRUEBAS DEL SERVICIO DE USUARIOS ===")
    print("Servicio esperado en:", BASE_URL)
    print("=" * 50)
    
    try:
        test_register_users()
        test_get_user_by_id()
        test_get_user_by_email()
        test_get_all_users()
        test_authenticate_users()
        test_user_not_found()
        
        print("\n" + "=" * 50)
        print("=== PRUEBAS COMPLETADAS EXITOSAMENTE ===")
        
    except Exception as e:
        print(f"\nError durante las pruebas: {e}")
        
    finally:
        # Always cleanup test users, even if tests fail
        print("\n" + "=" * 50)
        cleanup_test_users()
        print("=" * 50)
        print("=== PRUEBAS Y LIMPIEZA FINALIZADAS ===")
