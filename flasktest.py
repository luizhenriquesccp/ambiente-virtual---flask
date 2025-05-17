from flask import Flask 
app = Flask(__name__) 

@app.route("/") 
def hello(): 
    return "Hello, World!" 

@app.route("/soma/<int:a>/<int:b>") 
def soma(a, b): 
    R = a + b 
    return f"A soma de {a} e {b} é {R}" 

if __name__ == "__main__": 
    app.run()