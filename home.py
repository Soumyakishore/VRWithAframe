from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/projects')
def projects():
    return render_template("index.html", title = 'Projects')

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
