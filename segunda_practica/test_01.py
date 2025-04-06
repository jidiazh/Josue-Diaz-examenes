"""-  Crear una clase llamada Empleado donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana, tendrá un método para solicitar su
nombre y otro para solicitar su edad.  - Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona. - Crear la instancia de la clase Persona y usar su nuevo método
aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que: “En
el año 2025 tendrá XX años”, el año se ingresará por parámetro y la edad
es la edad que ya se ingresó (Mostrar por pantalla este valor)"""


class Empleado:

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.sueldo = 0.0
        self.nacionalidad = "Peruana"

    # Metodo para solicitar nombre
    def solicita_nombre(self):
        self.nombre = input("Ingrese el nombre: ")

    # Metodo para solicitar edad
    def solicitar_edad(self):
        self.edad = int(input("Ingrese la edad: "))

    # Metodo que aumenta +1 en la edad
    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumento_sueldo(self):
        self.sueldo = (self.sueldo + (self.sueldo * 0.3))
        return self.sueldo

    def edad_en(self, año_futuro):
        # Ahora calculamos la edad futura basándonos en el año 2025.
        edad_futura = self.edad + (año_futuro - 2025)
        return f"En el año {año_futuro} tendrá {edad_futura} años."

# Creando las instancias
empleado1 = Empleado()
empleado1.solicita_nombre()
empleado1.solicitar_edad()
empleado1.sueldo = float(input("Ingrese el sueldo actual del empleado 1: "))
nuevo_sueldo1 = empleado1.aumento_sueldo()

print("El empleado {} cuenta con un aumento: S/ {:.2f}".format(empleado1.nombre,nuevo_sueldo1))
anio1 = int(input("Ingrese el año para calcular la edad futura del empleado 1: "))
print(empleado1.edad_en(anio1))

# Segunda instancia de empleado
empleado2 = Empleado()
empleado2.solicita_nombre()
empleado2.solicitar_edad()
empleado2.sueldo = float(input("Ingrese el sueldo actual del empleado 2: "))
nuevo_sueldo2 = empleado2.aumento_sueldo()

print("El empleado {} cuenta con un aumento: S/. {:.2f}".format(empleado2.nombre,nuevo_sueldo2))
anio2 = int(input("Ingrese el año para calcular la edad futura del empleado 2: "))
print(empleado2.edad_en(anio2))
