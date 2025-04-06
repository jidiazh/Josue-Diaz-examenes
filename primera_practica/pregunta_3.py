"""
Pregunta 3:
Profesor para este problema he considerado adecuado el
hacer este otro archivo que es una copia de mi ejercicio 2
para agregar el ultimo elemento de la lista
"""
# Creación de una lista vacía
trabajador_infor = []

#Usamos los valores del primer archivo
nombre = "Josue"
apellido = "Diaz"
salario = 920
edad = "20"
hijos = 0
compania = "Universidad Nacional Mayor de San Marcos"
bono_final = (salario ** 2) + (salario * 0.5)
cantidad_hijos = 2
# Variable para indicar si sigue trabajando (True o False)
trabajando = True
# Se modifica segun el estado del trabajador, en este caso es Verdadero

# Mostrar el tamaño de la lista antes de agregar los datos
print("Tamaño de la lista antes de agregar los datos:", len(trabajador_infor))
# Agregar datos a la lista
trabajador_infor.append(nombre)
trabajador_infor.append(apellido)
trabajador_infor.append(salario)
trabajador_infor.append(edad)
trabajador_infor.append(compania)
trabajador_infor.append(bono_final)
trabajador_infor.append(trabajando)
print("Lista de datos del trabajador sin la variable hijos:", trabajador_infor)
print("Tamaño de la lista actualizada:", len(trabajador_infor))
trabajador_infor.append(cantidad_hijos)


# Mostrar la lista en consola
print("Lista de datos actualizada del trabajador:", trabajador_infor)

# Mostrar el tamaño de la lista
print("Tamaño de la lista actualizada:", len(trabajador_infor))

# Verificar si está trabajando y mostrar el mensaje adecuado
if trabajando:
    print("El trabajador {} {} se encuentra trabajando actualmente en la compañía.".format(nombre,apellido))
else:
    print("El trabajador {} {} ya no se encuentra trabajando actualmente en la empresa.".format(nombre,apellido))


# Verificación si obtiene bono familiar
if cantidad_hijos > 0:
    bono_familiar = salario * 0.08  # 8% del sueldo
    trabajador_infor.append(bono_familiar)
    print("Obtiene el bono familiar el cual es de: {:.2f}".format(bono_familiar))
else:
    trabajador_infor.append("No cumple para obtener el bono familiar")
    print("No cumple para obtener el bono familiar")



