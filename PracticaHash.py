# Importación de la librería para generar las funciones Hash.
import hashlib
# Importación de una librería que me permite hacer un sleep o pausa del script de los segundos indicados.
import time
# Importación de una librería que, entre otras cosas, nos permite ver los ficheros de un directorio indicado.
import os

# Definición de una función qué, al llamarla me imprimirá el menú.
def menu():
    print("Selecciona una opción")
    print("\t1 - Resumen MD5 de una cadena")
    print("\t2 - Resumen MD5 de un fichero")
    print("\t3 - Resumen SHA1 de una cadena")
    print("\t4 - Resumen SHA1 de un fichero")
    print("\t0 - salir")

# Definición de una función que se ejecuta cuando elijamos la opción 1 del menú y que con ayuda de la librería
# hashlib en la que introducimos una cadena y a la hora de mostrarlo lo codifica, lo convierte un resumen en
# MD5 y luego en hexadecimal.
def cadenamd5():
    cadena = input("¿Sobre qué cadena quieres hacer un resumen MD5?: ")
    print("Resumen MD5: ", hashlib.md5(cadena.encode('utf-8')).hexdigest())
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Definición de una función que se ejecutará al elegir la opción 2
def ficheromd5():
    # Primero pintamos el siguiente texto.
    print("Ficheros del directorio actual:")
    print("")
    # Con ayuda de la librería 'os' mostramos los ficheros que tenemos, en este caso, en el directorio donde
    # estamos trabajando.
    diractual = os.getcwd()
    dir = os.listdir(diractual)
    for fichero in dir:
            print(fichero)
    print("")
    # En esta parte elegimos el nombre de uno de los fichero mostrados anteriormente. Si existe, hará el proceso
    # para darnos la funcion Hash en MD5 del fichero, si no existe el fichero definido, nos muestra un error
    # y volvemos al menú.
    cadena = input("Elige el fichero sobre el que sacar el resumen MD5: ")
    try:
        f = open(cadena)
        lineas = f.readlines()
        h = hashlib.new('md5')
        for linea in lineas:
            linea = str.encode(linea)
            h.update(linea)
        print("Resumen MD5: ", h.hexdigest())
    except:
        print("El fichero NO existe.")
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Definición de una función que se ejecuta cuando elijamos la opción 2 del menú y que con ayuda de la librería
# hashlib en la que introducimos una cadena y a la hora de mostrarlo lo codifica, lo convierte un resumen en
# SHA1 y luego en hexadecimal.
def cadenasha1():
    cadena = input("¿Sobre qué cadena quieres hacer un resumen SHA1?: ")
    print("Resumen SHA1: ", hashlib.sha1(cadena.encode('utf-8')).hexdigest())
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

def ficherosha1():
    # Primero pintamos el siguiente texto.
    print("Ficheros del directorio actual:")
    print("")
    # Con ayuda de la librería 'os' mostramos los ficheros que tenemos, en este caso, en el directorio donde
    # estamos trabajando.
    diractual = os.getcwd()
    dir = os.listdir(diractual)
    for fichero in dir:
        print(fichero)
    print("")
    # En esta parte elegimos el nombre de uno de los fichero mostrados anteriormente. Si existe, hará el proceso
    # para darnos la funcion Hash en MD5 del fichero, si no existe el fichero definido, nos muestra un error
    # y volvemos al menú.
    cadena = input("Elige el fichero sobre el que sacar el resumen SHA1: ")
    try:
        f = open(cadena)
        lineas = f.readlines()
        h = hashlib.new('sha1')
        for linea in lineas:
            linea = str.encode(linea)
            h.update(linea)
        print("Resumen SHA1: ", h.hexdigest())
    except:
        print("El fichero NO existe.")
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Defino una función para salir que simplemente pinta un texto y hace una pausa.
def salir():
    print("Saliendo...")
    time.sleep(1)

# Hacemos un bucle infinito del cuál sólo podremos salir con un break.
while True:
    print("")

    # Mostramos el menú
    menu()

    # Elegimos una opción
    opcion = input("Opción elegida: ")

    print("")

    # Creamos un condicional el cuál llama a las funciones dependiendo de la opción elegida añadiendo un
    # break en la opción de salir.
    if opcion == "1":
        cadenamd5()
    elif opcion == "2":
        ficheromd5()
    elif opcion == "3":
        cadenasha1()
    elif opcion == "4":
        ficherosha1()
    elif opcion == "0":
        salir()
        break
    else:
        input("No has pulsado una opción correcta... pulsa una tecla para continuar.")