"""3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas: - El programa deberá considerar 2 cuentas bancarias para el
constructor: 1 en soles y otra en dólares. Considerar el nombre y
apellido del titular - Deberá tener un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas. - Tendrá otro método para retirar dinero, esto debe actualizar ambas
cuentas y mostrar en pantalla los montos actualizados, a su vez
validar si tiene fondos suficientes o no para el retiro, mostrar un
mensaje que indique no tiene suficientes en caso fuera el caso. - Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados. """

class Billetera:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares

    def transferir(self, cantidad, desde, hacia, tipo_cambio):
        if desde == "soles" and hacia == "dolares":
            if self.saldo_soles >= cantidad:
                self.saldo_soles = self.saldo_soles - cantidad
                self.saldo_dolares = self.saldo_dolares + (cantidad / tipo_cambio)
                print("Transferencia de {} soles a dólares exitosa.".format(cantidad))
            else:
                print("No tienes suficientes soles para hacer la transferencia.")
                return
        elif desde == "dolares" and hacia == "soles":
            if self.saldo_dolares >= cantidad:
                self.saldo_dolares = self.saldo_dolares - cantidad
                self.saldo_soles = self.saldo_soles + (cantidad * tipo_cambio)
                print("Transferencia de {} dólares a soles exitosa.".format(cantidad))
            else:
                print("No tienes suficientes dólares para hacer la transferencia.")
                return
        # Muestro ambos saldos siempre
        print("Saldos actuales -> Soles: {:.2f}, Dólares: {:.2f}".format(self.saldo_soles, self.saldo_dolares))

    def retirar(self, cantidad, moneda):
        if moneda == "soles":
            if self.saldo_soles >= cantidad:
                self.saldo_soles = self.saldo_soles - cantidad
                print("Retiro de {} soles exitoso.".format(cantidad))
            else:
                print("No tienes suficientes soles para hacer el retiro.")
                return
        elif moneda == "dolares":
            if self.saldo_dolares >= cantidad:
                self.saldo_dolares = self.saldo_dolares - cantidad
                print("Retiro de {} dólares exitoso.".format(cantidad))
            else:
                print("No tienes suficientes dólares para hacer el retiro.")
                return
        # Muestro ambos saldos tras el retiro
        print("Saldos actuales -> Soles: {:.2f}, Dólares: {:.2f}".format(self.saldo_soles, self.saldo_dolares))


billetera1 = Billetera("Diego", "González", 1000.0, 300.0)

# 3 transferencias distintas
billetera1.transferir(200, "soles", "dolares", 3.5)
billetera1.transferir(50,  "dolares", "soles",  3.5)
billetera1.transferir(100, "soles", "dolares", 3.5)

# 2 retiros para probar el otro metodo
billetera1.retirar(150, "soles")
billetera1.retirar(30,  "dolares")
