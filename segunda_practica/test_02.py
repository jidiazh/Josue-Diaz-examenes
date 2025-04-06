"""Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear el siguiente programa (3 ptos):
Reglas: - Crear una clase llamada Persona (Que heredará de la anterior Clase) y
agregar un atributo sueldo a esta clase (ejercicio anterior). - Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada - El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en
su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
una transferencia y con dos personas."""


class Empleado:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.sueldo = 0.0
        self.nacionalidad = "Peruana"
        self.saldo = 0.0  # Atributo de saldo

    def solicita_nombre(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

    def solicitar_edad(self):
        self.edad = int(input("Ingrese la edad: "))

    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumento_sueldo(self):
        self.sueldo = self.sueldo + (self.sueldo * 0.30)
        return self.sueldo

    def edad_en(self, año_futuro):
        edad_futura = self.edad + (año_futuro - 2025)
        return "En el año {} tendrá {} años.".format(año_futuro,edad_futura)

    def transferencia(self, monto, empleado_destino):
        if self.saldo >= monto:
            self.saldo -= monto
            empleado_destino.saldo += monto
            print("Transferencia realizada de S/. {} a {}. Saldo actual: S/. {}".format(monto,empleado_destino.nombre,self.saldo))
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print("El saldo actual de {} es: S/. {}".format(self.nombre,self.saldo))


#  Instancia de la clase:Empleado 1
empleado1 = Empleado()
empleado1.solicita_nombre()
empleado1.solicitar_edad()
anio1 = int(input("Ingrese el año para calcular la edad futura del empleado 1: "))
print(empleado1.edad_en(anio1))
empleado1.sueldo = float(input("Ingrese el sueldo actual del empleado 1: "))
empleado1.saldo = float(input("Ingrese el saldo del empleado 1: "))
nuevo_sueldo1 = empleado1.aumento_sueldo()

print("El empleado {} cuenta con un aumento: S/. {:.2f}".format(empleado1.nombre, nuevo_sueldo1))

# Instancia de la clase:Empleado 2
empleado2 = Empleado()
empleado2.solicita_nombre()
empleado2.solicitar_edad()
anio2 = int(input("Ingrese el año para calcular la edad futura del empleado 2: "))
print(empleado2.edad_en(anio2))
empleado2.sueldo = float(input("Ingrese el sueldo actual del empleado 2: "))
empleado2.saldo = float(input("Ingrese el saldo del empleado 2: "))
nuevo_sueldo2 = empleado2.aumento_sueldo()

print("El empleado {} cuenta con un aumento: S/. {:.2f}".format(empleado2.nombre, nuevo_sueldo2))

empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

monto_transferir = float(input("Ingrese el monto a transferir de {} a {}: ".format(empleado1.nombre, empleado2.nombre)))
empleado1.transferencia(monto_transferir, empleado2)

empleado1.mostrar_saldo()
empleado2.mostrar_saldo()
