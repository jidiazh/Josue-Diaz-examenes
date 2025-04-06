
# Creación de una lista vacía
trabajador_infor = []

#Usamos los valores del primer archivo
nombre = "Josue"
apellido = "Diaz"
salario = 920
edad = "20"
compania = "Universidad Nacional Mayor de San Marcos"
bono_final = (salario ** 2) + (salario * 0.5)

# Mostrar el tamaño de la lista antes de agregar los datos
print("Tamaño de la lista antes de agregar los datos:", len(trabajador_infor))

# Agregar datos a la lista
trabajador_infor.append(nombre)
trabajador_infor.append(apellido)
trabajador_infor.append(salario)
trabajador_infor.append(edad)
trabajador_infor.append(compania)
trabajador_infor.append(bono_final)

# Variable para indicar si sigue trabajando (True o False)
trabajando = True  # Se modifica segun el estado del trabajador, en este caso es Verdadero

# Agregamos la variable a la lista
trabajador_infor.append(trabajando)

# Mostrar la lista en consola
print("Lista de datos del trabajador:", trabajador_infor)

# Mostrar el tamaño de la lista
print("Tamaño de la lista:", len(trabajador_infor))

# Verificar si está trabajando y mostrar el mensaje adecuado
if trabajando:
    print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañía.")
else:
    print(f"El trabajador {nombre} {apellido} ya no se encuentra trabajando actualmente en la empresa.")
