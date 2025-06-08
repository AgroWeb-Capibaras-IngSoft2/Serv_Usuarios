from flask import Flask
app=Flask(__name__)
@app.route("usuarios/<id>",method=["GET"])
def getUserById(id):
    pass