import requests

BASE_URL = "http://127.0.0.1:5000"

users = [
    {
        "firstName": "Juan",
        "middleName": "Carlos",
        "surName1": "Pérez",
        "surName2": "Gómez",
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
    print("Testing user registration...")
    for user in users:
        resp = requests.post(f"{BASE_URL}/users/register", json=user)
        print(f"POST /users/register {user['email']} ->", resp.status_code, resp.json())

def test_get_user_by_id():
    print("\nTesting get user by document...")
    for user in users:
        doc = user["numberDocument"]
        resp = requests.get(f"{BASE_URL}/users/getById/{doc}")
        print(f"GET /users/getById/{doc} ->", resp.status_code, resp.json())

def test_get_user_by_email():
    print("\nTesting get user by email...")
    for user in users:
        email = user["email"]
        resp = requests.get(f"{BASE_URL}/users/getByEmail/{email}")
        print(f"GET /users/getByEmail/{email} ->", resp.status_code, resp.json())

def test_authenticate_users():
    print("\nTesting user authentication...")
    for user in users:
        data = {
            "email": user["email"],
            "hashPassword": user["hashPassword"]
        }
        resp = requests.post(f"{BASE_URL}/users/autenticate/", json=data)
        print(f"POST /users/autenticate {user['email']} ->", resp.status_code, resp.json())

def test_user_not_found():
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

if __name__ == "__main__":
    test_register_users()
    test_get_user_by_id()
    test_get_user_by_email()
    test_authenticate_users()
    test_user_not_found()