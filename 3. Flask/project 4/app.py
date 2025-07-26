from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/data', methods=['POST'])
def data():
    # course = request.args.get('course')
    course = request.form['course']
    return course

app.run(debug=True)