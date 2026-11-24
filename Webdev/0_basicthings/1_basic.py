from flask import Flask, request
from markupsafe import escape
app=Flask(__name__)
@app.route("/") # this is for route 

def hello():
    return "hello"

@app.route("/hello")
def name_hello ():
    name=request.args.get("name","flask")
    return f"hello {escape(name)}"
