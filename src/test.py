import unittest
from billing_system import Billing_System

class TestBillingSystem():
    #Casos de error
    def test_saldo_insuficiente():
        responde = Billing_System.pagar("123","456",50000000)
        if responde == "Saldo insuficiente":
            print("TEST SALDO INSUFICIENTE PASSED")
        else:
            print("TEST SALDO INSUFICIENTE FAILED")

    def test_valor_de_pago_invalido():
        response = Billing_System.pagar("123","456",-5000)
        if response == "Valor invalido":
            print("TEST VALOR DE PAGO INVALIDO PASSED")
        else:
            print("TEST VALOR DE PAGO INVALIDO FAILED")

    def test_contacto_no_existe():
        response = Billing_System.pagar("123","2222",40)
        if response == "Contacto no existe":
            print("TEST CONTACTO NO EXISTE PASSED")
        else:
            print("TEST CONTACTO NO EXISTE FAILED")

    #Casos de exito
    def test_pago_exitoso():
        response = Billing_System.pagar("123","456",40)
        if response[:len("Realizado")] == "Realizado":
            print("TEST PAGO EXITOSO PASSED")
        else:
            print("TEST PAGO EXITOSO FAILED")

    def test_historial():
        response = Billing_System.historial("1234")
        if response != "Usuario no existe":
            print("TEST HISTORIAL PASSED")
        else:
            print("TEST HISTORIAL FAILED")

if __name__ == '__main__':
    #3 Casos error
    TestBillingSystem.test_saldo_insuficiente()
    TestBillingSystem.test_valor_de_pago_invalido()
    TestBillingSystem.test_contacto_no_existe()
    
    #2 Casos exito
    TestBillingSystem.test_historial()
    TestBillingSystem.test_pago_exitoso()

