from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Vishal'
    role = 'ML/AI Engineer'
    return render_template('home.html', name=name, role=role)

app.run(debug=True)