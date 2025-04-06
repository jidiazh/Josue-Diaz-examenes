
# Definir variables
nombre = "Josue Diaz"
salario = 920
edad = "20"  # Edad como string
compania = "Universidad Nacional Mayor de San Marcos"

# Convertir edad a entero
edad_entero = int(edad)

# Evaluar el bono según la edad
if edad_entero > 30:
    bono_porcentaje = 0.10
    mensaje_bono = "Usted tiene un bono de 10% en el mes de diciembre"
else:
    bono_porcentaje = 0.05
    mensaje_bono = "Usted tiene un bono del 5% en el mes de diciembre"

# Calcular bono final
bono_final = (salario ** 2) + (salario * bono_porcentaje)

# Mostrar resultados
print("El tipo de dato de la variable nombre es: {}.".format(type(nombre)))
print("El tipo de variable salario es: {}.".format(type(salario)))
print("El tipo de edad es: {}.".format(type(edad)))
print("El tipo de compañia es: {}.".format(type(compania)))
print(mensaje_bono)
print("El bono final es de : {}".format(bono_final))

