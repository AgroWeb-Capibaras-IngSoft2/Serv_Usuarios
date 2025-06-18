from flask import Flask
from flask_interface.routes import bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app,origins=["http://localhost:5173"])

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True,port=5001)