from flask import Flask
from flask_interface.routes import bp
from flasgger import Swagger


app = Flask(__name__)

template = {
    "swagger": "2.0",
    "info": {
        "title": "Servicio de usuarios API docs",
        "version": "1.0.0",
        "description": "API documentation for Flask Interface",
    },
    "schemes": ["http", "https"],
    "basePath": "/api/v1",
}

swagger = Swagger(app, template=template)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)