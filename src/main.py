import datetime
import flask
from billing_system import Billing_System, db_users

#Guardando informacion en memoria
Billing_System.add_user("21345", "Arnaldo", 200, ["123", "456"])
Billing_System.add_user("123", "Luisa", 400, ["456"])
Billing_System.add_user("456", "Andrea", 300, ["21345"])
print("Data loaded!")

#Debug purposes
print(db_users)


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
def send_message():
    data = flask.request.args
    from_numero = data.get('minumero', None)
    to_numero = data.get('numerodestino', None)
    texto = data.get('valor', None)

    #obtener feacha actual dia mes año
    msg = Billing_System.pagar(from_numero, to_numero, texto)
    print(db_users)
    return msg

@app.route("/billetera/historial", methods=["GET"])
def get_messages():
    data = flask.request.args
    numero = data.get('minumero', None)
    msg = Billing_System.historial(numero)
    return msg

if __name__ == "__main__":
    app.run(port=5000)