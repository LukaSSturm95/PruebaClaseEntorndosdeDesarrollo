'''
    Programa agenda V2.0
    Prueba para DAM1 "Entornos de desarrollo" Realizado en clases.
    13/11/2025
    Lucas Ezequiel Andrés Griego
'''

################ DEFINICION DE FUNCIONES ################

def imprimeBienvenida():
    print("Programa agenda V1.0 por Lucas Ezequiel Andrés Griego")

def muestraMenu():
    print("selecciona una opcion:")
    print("1. -Insertar clientes")
    print("2. -Ver lista clientes")
    print("3. -Actualizar clientes")
    print("4. -Eliminar clientes")

def insertarCliente():
    global clientes    #Solucion global para la variable "clientes" dentro de las otras funciones esa variable no existe, sin esta solucion fea, no funcionaria el codigo.
    nombre = input("Dime el nuevo nombre del cliente: ")
    clientes += nombre+","

def listadoClientes():
    global clientes
    print("Tus clientes son: ")
    print(clientes)

def actualizaClientes():
    global clientes
    print("Tus clientes son: ")
    print(clientes)
    print("¿Quienes quieres que sean?")
    clientes = input("Introduce los nuevos clientes: ")

def borraClientes():
    global clientes
    clientes = ""
    print("Tus clientes han sido eliminados")

################ DEFINICION DE VARIABLES GLOBALES ################

clientes = ""   #clientes = a nada.

################ BUCLE PRINCIPAL ################

imprimeBienvenida()

while True:     #"while True" sirve para hacer "bucle infinito"
    muestraMenu()
    opcion = input("Elige tu opcion ")
    opcion = int(opcion)

    if opcion == 1:
        insertarCliente()
    elif opcion == 2:
       listadoClientes()
    elif opcion == 3:
       actualizaClientes()
    elif opcion == 4:
        borraClientes()
'''
En la version V2.0 vemos que la diferencia esta en la deficion de los bloques de codigo,
en bloques de funciones reutlizables,
y tambien aplicamos la solucion global, con la variable "clientes",
Por ultimo tambien hacemos que el menu de opciones se muestre en el bucle,
en cada vez que se ejecute una opcion
'''
