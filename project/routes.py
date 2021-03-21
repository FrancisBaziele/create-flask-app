from project import app 
from flask import render_template
from project.forms import RegistrationForm

@app.route( '/', methods=['GET', 'POST'])
@app.route( '/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title='Home')
    