from flask import Flask
from flask import render_template
from flask import request
import os
app = Flask(__name__,template_folder='template')
IMG = os.path.join("static",'img')
app.config['IMG_FOLDER'] = IMG

@app.route("/")
def start():
    print( request.args.get("paramgit"))
    x = 2
    return str(x)


@app.route("/<name>")
def files(name):
    pass


if __name__ == "__main__":
    app.run()