from config import *
from modelo import Carro
from flask import render_template


@app.route("/")
def inicio():
    carros = db.session.query(Carro).all()

    carros_em_json = [ x.json() for x in carros ]

    return render_template('listar-carros.html',listagem=carros_em_json)

@app.route("/listar_carros")
def listar_carros():
    carros = db.session.query(Carro).all()
    
    carros_em_json = [ x.json() for x in carros ]

    resposta = jsonify(carros_em_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta    

app.run(debug=True)    
