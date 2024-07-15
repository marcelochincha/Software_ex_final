import time

USER_TPL = {
    'alias' : '',
    'nombre' : '',
    'contactos' : [],
}
MSG_TPL = {
    'from_alias' : '',
    'to_alias': '',
    'fecha': 0,
    'texto' : '',
}
class Chat:
    db_users = {}
    db_messages = []

    def __init__(self):
        pass

    def add_user(alias, nombre, contactos=[]):
        user = USER_TPL.copy()
        user['alias'] = alias
        user['nombre'] = nombre
        user['contactos'] = contactos
        Chat.db_users[alias] = user

    def add_message(from_alias, to_alias, texto, fecha):
        message = MSG_TPL.copy()
        #check if to_alias exists
        if to_alias not in Chat.get_all_users():
            print(f"User {to_alias} does not exist")
            return
        message['from_alias'] = from_alias
        message['to_alias'] = to_alias
        message['fecha'] = fecha
        message['texto'] = texto
        Chat.db_messages.append(message)

    def get_messages(alias):
        messages = []
        for message in Chat.db_messages:
            if message['to_alias'] == alias:
                messages.append(message)
        return messages

    def get_user(alias):
        return Chat.db_users.get(alias, None)
    
    def get_all_users():
        return list(Chat.db_users.keys())