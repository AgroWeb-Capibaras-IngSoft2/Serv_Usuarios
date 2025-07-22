"""
Script de demostración para observabilidad de AgroWeb
Genera tráfico realista hacia el API de productos para demostrar las métricas
de Prometheus.

Métricas demostradas:
- Contador de peticiones por endpoint
- Latencia/tiempo de respuesta 
- Errores HTTP por código de estado
"""
import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor

def call_endpoint(url, delay=0):
    """Realiza una petición HTTP con delay opcional para simular carga"""
    try:
        if delay > 0:
            time.sleep(delay)
        response = requests.get(url, timeout=5)
        status = "✅" if response.status_code < 400 else "❌"
        print(f"{status} {url} -> {response.status_code} ({response.elapsed.total_seconds():.3f}s)")
        return response.status_code
    except Exception as e:
        print(f"❌ {url} -> Error: {str(e)[:50]}")
        return 500

def generate_usuarios_traffic():
    """Genera patrones de tráfico realistas para demostrar observabilidad en Serv_Usuarios"""
    print("🚀 Iniciando demostración de observabilidad...")
    print("📊 Monitorea las métricas en tiempo real:")
    print("   - Prometheus: http://localhost:5001/metrics")
    print()
    # Endpoints del API de usuarios para generar diferentes métricas
    endpoints = [
        "http://localhost:5001/users/register",         # Registro de usuario (POST, pero aquí solo GET para demo)
        "http://localhost:5001/users/getById/1234567890", # Consulta usuario existente
        "http://localhost:5001/users/getById/9999999999", # Usuario inexistente (404)
        "http://localhost:5001/users/getByEmail/test@email.com", # Consulta por email
        "http://localhost:5001/health",                 # Health check
        "http://localhost:5001/metrics",                # Métricas Prometheus
        "http://localhost:5001/nonexistent",            # Endpoint inexistente (404)
    ]
    # Patrones de tráfico para simular diferentes escenarios
    patterns = [
        {"name": "🌱 Tráfico normal", "requests": 30, "delay": 0.5, "concurrent": 2},
        {"name": "🚀 Pico de tráfico", "requests": 60, "delay": 0.1, "concurrent": 5},
        {"name": "🐌 Tráfico lento", "requests": 15, "delay": 2.0, "concurrent": 1},
        {"name": "📈 Carga mixta", "requests": 40, "delay": 0.3, "concurrent": 3},
    ]
    for pattern in patterns:
        print(f"🔄 Patrón: {pattern['name']} ({pattern['requests']} requests, {pattern['concurrent']} concurrent)")
        with ThreadPoolExecutor(max_workers=pattern['concurrent']) as executor:
            futures = []
            for i in range(pattern['requests']):
                endpoint = random.choice(endpoints)
                delay = random.uniform(0, pattern['delay'])
                future = executor.submit(call_endpoint, endpoint, delay)
                futures.append(future)
            for future in futures:
                future.result()
        print(f"✅ {pattern['name']} completado\n")
        time.sleep(3)  # Pausa entre patrones
    print("🎉 Demostración completada!")
    print("📈 Revisa las métricas generadas en http://localhost:5001/metrics")

def test_connectivity():
    """Verifica que el API de usuarios esté disponible antes de generar tráfico"""
    print("🔍 Verificando conectividad del API de usuarios...")
    try:
        response = requests.get("http://localhost:5001/health", timeout=5)
        if response.status_code == 200:
            print("✅ API de usuarios disponible")
            return True
        else:
            print(f"❌ API responde con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ No se puede conectar al API: {e}")
        print("💡 Asegúrate de ejecutar primero:")
        print("   1. python app.py")
        return False

if __name__ == "__main__":
    print("📊 DEMO DE OBSERVABILIDAD - AGROWEB - SERVICIO DE USUARIOS")
    print("=" * 40)
    if test_connectivity():
        print()
        input("Presiona Enter para comenzar la demostración...")
        generate_usuarios_traffic()
    else:
        print("\n🛑 No se puede generar tráfico sin el API activo")
