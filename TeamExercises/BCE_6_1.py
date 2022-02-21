# Team 1 BCE 6.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

from flask import Flask, flash, redirect, render_template, request, session, abort

# Initializing Flask app
app = Flask(__name__)

# Setting home to return 'Flask App!'
@app.route("/")
def index():
    return "Flask App!"

# Setting /hello/name to render test.html where there are headers, paragraphs, and an image
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
    'test.html',name=name)

# The Flask app is ran in the main function    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)