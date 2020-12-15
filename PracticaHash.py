# Importación de la librería para generar las funciones Hash.
import hashlib
# Importación de una librería que me permite hacer un sleep o pausa del script de los segundos indicados.
import time
# Importación de una librería que, entre otras cosas, nos permite ver los ficheros de un directorio indicado.
import os

# Declaración de variables de colores
fcian = "\033[3;46m" # Fondo cian + negrita
fblanco = "\033[4;47m" # Fondo blanco + subrayado
frojo = "\033[4;41m" # Fondo rojo + subrayado
nnegro = "\033[1;30m" # Color negro en negrita
nverde = "\033[1;32m" # Color verde en negrita.
nmorado = "\033[1;35m" # Color morado en negrita.
nrojo = "\033[1;31m" # Color rojo en negrita.
nazul = "\033[1;34m" # Color azul en negrita.
namarillo = "\033[1;33m" # Color amarillo en negrita.
reset = "\033[0;m" # Reset de color

# Definición de una función qué, al llamarla me imprimirá el menú.
def menu():
    print(nnegro+fcian+"Selecciona una opción:"+reset)
    print("\t1 - Resumen "+nverde+"MD5"+reset+" de una"+nverde+" cadena"+reset)
    print("\t2 - Resumen "+nrojo+"MD5"+reset+" de un"+nrojo+" fichero"+reset)
    print("\t3 - Resumen "+nazul+"SHA1"+reset+" de una"+nazul+" cadena"+reset)
    print("\t4 - Resumen "+nmorado+"SHA1"+reset+" de un"+nmorado+" fichero"+reset)
    print("\t0 - Salir")

# Definición de una función que se ejecuta cuando elijamos la opción 1 del menú y que con ayuda de la librería
# hashlib en la que introducimos una cadena y a la hora de mostrarlo lo codifica, lo convierte un resumen en
# MD5 y luego en hexadecimal.
def cadenamd5():
    cadena = input("¿Sobre qué cadena quieres hacer un resumen MD5?: ")
    print("Resumen MD5: "+nverde+hashlib.md5(cadena.encode('utf-8')).hexdigest()+reset)
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Definición de una función que se ejecutará al elegir la opción 2
def ficheromd5():
    # Primero pintamos el siguiente texto.
    print(nnegro+frojo+"Ficheros del directorio actual:"+reset)
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
        print("Resumen MD5: ", nrojo, h.hexdigest(), reset)
    except:
        print(nnegro+fblanco+"El fichero NO existe o es un directorio."+reset)
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Definición de una función que se ejecuta cuando elijamos la opción 2 del menú y que con ayuda de la librería
# hashlib en la que introducimos una cadena y a la hora de mostrarlo lo codifica, lo convierte un resumen en
# SHA1 y luego en hexadecimal.
def cadenasha1():
    cadena = input("¿Sobre qué cadena quieres hacer un resumen SHA1?: ")
    print("Resumen SHA1: "+nazul+hashlib.sha1(cadena.encode('utf-8')).hexdigest()+reset)
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

def ficherosha1():
    # Primero pintamos el siguiente texto.
    print(nnegro+frojo+"Ficheros del directorio actual:"+reset)
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
        print("Resumen SHA1: "+nmorado+h.hexdigest()+reset)
    except:
        print("El fichero NO existe o es un directorio.")
    # Pausa de 1 segundo para poder visualizar tranquilamente el resumen.
    time.sleep(1)

# Defino una función para salir que simplemente pinta un texto y hace una pausa.
def salir():
    print(namarillo+"Saliendo..."+reset)
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