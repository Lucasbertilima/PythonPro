from flask import Flask, render_template,redirect,request

import sys
sys.path.append('C:/Users/900145/Documents/PythonPro/Aula37')

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

#


app.run(debug=True)