from flask import Flask
from flask_interface.routes import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)