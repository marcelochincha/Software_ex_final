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

        if valor <= 0:
            return "Valor invalido"
    
        if self.saldo < valor:
            return "Saldo insuficiente"
        
        #obtener el destino
        if destino not in self.contactos:
            return "Contacto no existe"
        
        db_users[destino].saldo += valor
        self.saldo -= valor

        operation = Operation(self.numero,destino,valor, datetime.datetime.now())
        self.operaciones.append(operation)
        db_users[destino].operaciones.append(operation)

        return f"Realizado en {datetime.datetime.now()}"

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
            return "Usuario no existe"

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
            return "Usuario no existe"

        return user.transferir(numero_destino,valor)


    def historial(mi_numero):
        user = db_users.get(mi_numero,None)
        if not user:
            return "Usuario no existe"
        
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
    
#Guardando informacion en memoria
Billing_System.add_user("21345", "Arnaldo", 200, ["123", "456"])
Billing_System.add_user("123", "Luisa", 400, ["456"])
Billing_System.add_user("456", "Andrea", 300, ["21345"])
print("Data loaded!")

#Debug purposes
#print(db_users)