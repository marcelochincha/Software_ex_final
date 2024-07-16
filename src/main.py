import datetime
import flask
from billing_system import Billing_System, db_users

#Start flask server 
app = flask.Flask("chat")

#Send message
@app.route("/billetera/contactos", methods=["GET"])
def get_contacts():
    data = flask.request.args
    numero = data.get('minumero', None)
    if not numero:
        flask.abort(400, description = "Se requiere un numero")
    return flask.jsonify(Billing_System.contactos(numero))

@app.route("/billetera/pagar", methods=["GET"])
def pay():
    data = flask.request.args
    from_numero = data.get('minumero', None)
    to_numero = data.get('numerodestino', None)
    texto = data.get('valor', None)

    #obtener feacha actual dia mes año
    msg = Billing_System.pagar(from_numero, to_numero, texto)
    return msg

@app.route("/billetera/historial", methods=["GET"])
def get_historial():
    data = flask.request.args
    numero = data.get('minumero', None)
    msg = Billing_System.historial(numero)
    return msg

if __name__ == "__main__":
    app.run(port=5000)