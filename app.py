from flask import Flask
from flask_interface.routes import bp
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app, template_file="swagger/swagger.yaml")
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)