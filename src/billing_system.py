import datetime

db_users = {}

class Operation:
    def __init__(self, origen, destino, valor, date):
        self.origen = origen
        self.destino = destino
        self.valor = valor
        self.fecha = date
    
class User:
    def __init__(self, numero, nombre,saldo,contactos = []):
        self.nombre = nombre
        self.numero = numero
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

    def historial_operaciones(self):
        return self.operaciones
    
    def transferir(self,destino,valor):
        valor = int(valor)
        #Verificar que el saldo sea suficiente
        if self.saldo < valor:
            print("Saldo insuficiente")
            return
        
        #obtener el destino
        if destino not in self.contactos:
            print("Contacto no existe")
            return
        
        db_users[destino].saldo += valor
        self.saldo -= valor

        operation = Operation(self.numero,destino,valor, datetime.datetime.now())
        self.operaciones.append(operation)
        db_users[destino].operaciones.append(operation)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Saldo: {self.saldo}, Contactos: {self.contactos}"




class Billing_System:
    def __init__(self):
        pass
    
    def add_user(numero,nombre,saldo,contactos = []):
        user = User(numero,nombre,saldo,contactos)
        db_users[numero] = user

    def contactos(numero):
        user = db_users.get(numero,None)
        if not user:
            print("Usuario no existe")
            return

        contactos = user.contactos
        datos_contactos = {}
        for numero_contacto in contactos:
            contacto = db_users.get(numero_contacto,None)
            if contacto:
                datos_contactos[numero_contacto] = contacto.nombre

        return datos_contactos
    

    def pagar(mi_numero,numero_destino,valor):
        user = db_users.get(mi_numero,None)
        if not user:
            print("Usuario no existe")
            return

        user.transferir(numero_destino,valor)

        return f"Realizado en {datetime.datetime.now()}"

    def historial(mi_numero):
        user = db_users.get(mi_numero,None)
        if not user:
            print("Usuario no existe")
            return
        
        print(user)
        
        datos_historial = user.historial_operaciones()
        #format data
        message = f"Saldo de {user.nombre}: {user.saldo}\n"

        #recorrer lista de fin a inicio
        for operation in datos_historial[::-1]:
            if operation.origen == mi_numero:
                user_destino = db_users[operation.destino]
                message += f"Pago realizado de {operation.valor} a {user_destino.nombre} \n"
            else:
                user_origen = db_users[operation.origen]
                message += f"Pago recibido de {operation.valor} de {user_origen.nombre}\n"


        return message


"""
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

    def h(alias):
        return Chat.db_users.get(alias, None)
    
    def get_all_users():
        return list(Chat.db_users.keys())
"""