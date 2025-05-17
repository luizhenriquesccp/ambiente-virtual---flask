from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/") 
def hello(): 
    return "Hello, World!" 

@app.route('/dia')
def dia_atual():
    hoje = datetime.datetime.now().strftime('%d/%m/%Y')
    return f"Hoje é: {hoje}"

@app.route('/hora')
def hora_atual():
    hora = datetime.datetime.now().strftime('%H:%M:%S')
    return f"A hora atual é: {hora}"

if __name__ == '__main__':
    app.run(debug=True)