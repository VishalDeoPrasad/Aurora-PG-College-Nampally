from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('register.html')

@app.route('/data')
def data():
    name = request.args.get('full_name')
    age = request.args.get('age')
    return f"{name}, {age}"

app.run(debug=True)