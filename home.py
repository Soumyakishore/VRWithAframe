from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/class1')
def class1():
    return render_template("class1-click.html")

@app.route('/class2')
def class2():
    return render_template("class2-animation.html")

@app.route('/class3')
def class3():
    return render_template("class3-models.html")

@app.route('/class4')
def class4():
    return render_template("class4-physics.html")
@app.route('/class5')
def class5():
    return render_template("class5-grabbable.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
