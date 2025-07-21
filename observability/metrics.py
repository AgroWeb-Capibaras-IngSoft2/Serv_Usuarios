from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter('usuarios_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('usuarios_request_duration_seconds', 'Request latency')
ERROR_COUNT = Counter('usuarios_errors_total', 'Total errors', ['endpoint'])