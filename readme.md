# Examen final - Ingeniería de Software

Billetera virtual tipo yape o plin.

## Integrantes:
- Marcelo Andres Chincha León
- David Herencia Galván

---
## Pregunta 3
Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a
transferir por día.
Qué cambiaría en el código (Clases / Métodos) - No realizar la implementación, sólo
descripción.
Qué casos de prueba nuevos serían necesarios?
Los casos de prueba existentes garantizan que no se introduzcan errores en la funcionalidad
existente?

### Respuesta
Cambios: Se añade una variable en la clase de User (Cuentas) registra el valor total de los montos tranferidos en el día, y se añade un método que verifica si el monto a transferir no supera los 200 soles. Esta variable se incrementa cada vez que se realiza una transferencia y se reinicia al final del día.

Casos de prueba:
- Caso 1:  (Validando el monto máximo diario de transferencia)
    Precondiciones: 
        - Montos transferidos en el día del user 123: 0 soles
    Data: 
        numero de origen: 123 (Luisa)
        numero de destino: 456 (Andrea)
        monto a transferir 1: 160 soles
        monto a transferir 2: 100 soles
    Resultado esperado: Transferencia 1 exitosa, Transferencia 2 fallida

- Caso 2: (Reiniciar el monto total de transferencia al final del día)
    Precondiciones: 
        - Montos transferidos en el día 1 del user 123: 200 soles
        - Estar en el dia 2 (dia siguiente)

    Data: 
        numero de origen: 123 (Luisa)
        numero de destino: 456 (Andrea)
        monto a transferir 1: 100 soles
    Resultado esperado: Transferencia 1 exitosa


Estos casos de prueba existentes garantizan que no se introduzcan errores, ya que abarcan la mayoria de los escenario donde podrian ocurrir errores. Sin embargo, se puede hacer pruebas más exhaustivas para casos atipicos o extremos.