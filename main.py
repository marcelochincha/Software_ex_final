import datetime
import flask
from chat import Chat

#Starting data
Chat.add_user("cpaz", "Christian", ["lmunoz", "mgrau"])
Chat.add_user("lmunoz", "Luisa", ["mgrau"])
Chat.add_user("mgrau", "iguel", ["cpaz"])

print(f"Users: {Chat.get_user("cpaz")}")
print("Data loaded!")



#Start flask server 
app = flask.Flask("chat")

#Send message
@app.route("/mensajeria/contactos", methods=["GET"])
def get_contacts():
    data = flask.request.args
    alias = data.get('mialias', None)
    if not alias:
        flask.abort(400, description = "Alias is required")
    return flask.jsonify(Chat.get_user(alias)['contactos'])

@app.route("/mensajeria/enviar", methods=["GET"])
def send_message():
    data = flask.request.args
    from_alias = data.get('mialias', None)
    to_alias = data.get('aliasdestino', None)
    texto = data.get('texto', None)

    #obtener feacha actual dia mes año
    fecha = datetime.datetime.now()
    Chat.add_message(from_alias, to_alias, texto, fecha)
    return f"Mensaje enviado {fecha}"

@app.route("/mensajeria/recibidos", methods=["GET"])
def get_messages():
    data = flask.request.args
    alias = data.get('mialias', None)
    return flask.jsonify(Chat.get_messages(alias))

if __name__ == "__main__":
    app.run(port=5000)
