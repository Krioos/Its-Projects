from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def nome()-> str:
    return "<h3>Hello World!</h3>"

@app.route('/user/<string:username>')
def showusername(username: str)-> str:
    return f"Profilo di {username}"

with app.test_request_context():
    print(url_for('nome'))
    print(url_for('showusername', username= "Jhon Doe"))
    
# app.run(debug= True, port = 5001) se si usano i comnandi non serve usare questo
