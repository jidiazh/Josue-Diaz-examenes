"""3. (3 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas: - Al ejecutar el decorador mostrará un mensaje:
“El decorador está siendo ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará
 los elementos de la función que pasará como parámetro
 de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos."""

from datetime import datetime


def decorador_hora_suma(func):
    def wrapper(**kwargs):
        ahora = datetime.now()
        print(
            "El decorador está siendo ejecutado "
            "a las {} con {} minutos".format(ahora.hour, ahora.minute)
        )

        suma = sum(kwargs.values())
        print("La suma de los valores es: {}".format(suma))

        resultado = func(**kwargs)
        return resultado
    return wrapper


@decorador_hora_suma
def encontrar_mayor(**kwargs):
    mayor = max(kwargs.values())
    print("El mayor valor es: {}".format(mayor))
    return mayor


encontrar_mayor(a=9, b=8, c=19)
encontrar_mayor(x=24, y=3, z=7, w=14)
encontrar_mayor(n1=105, n2=84, n3=90, n4=30, n5=10, n6=280)
