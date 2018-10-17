from flask import Flask
from flask import render_template

app = Flask('app')

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('home.html')
    
app.run(host='0.0.0.0', port=8080)
