from project import app 

@app.route( '/', methods=['GET', 'POST'])
@app.route( '/home', methods=['GET', 'POST'])
def home():
    return '<h1>Hi there </h1>'