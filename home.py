from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/class1')
def projects():
    return render_template("index.html", title = 'Projects')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
