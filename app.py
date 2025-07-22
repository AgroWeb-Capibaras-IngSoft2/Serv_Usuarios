from flask import Flask
from flask_interface.routes import bp
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5174"])  # Allow CORS for the specified origin
swagger = Swagger(app, template_file="swagger/swagger.yaml")
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Run on port 5001 for Serv_Usuarios