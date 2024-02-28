from flask import Flask, jsonify #La primera linea de codigo estoy importando el Flask y el Jsonify

app = Flask(__name__)

@app.route('/')    #CREACION DE RUTA PREDETERMINADA
def index():
    return 'Hola, Soy Sebastian Vargas'


Personas = ["Juan","Sebastian","Freddy","Luisa","Carlos","Daniela"] #CREACION DE LA LISTA CON NOMBRE DE PERSONAS
@app.route('/personas')     #ESTABLECIENDO EL ENDPOINT /PERSONAS
def persona():              #CREACION DE LA FUNCION PERSONA LA CUAL SE VA EJECUTAR CUANDO SE ACCEDA AL ENDPOINT PERSONA
    return jsonify(Personas) #RETORNAR LA LISTA PERSONA USANDO LA FUNCION JSONIFY PARA CONVERTIR LA LISTA PERSONA EN FORMATO JSON

if __name__ == '__main__':
    app.run(debug=True)