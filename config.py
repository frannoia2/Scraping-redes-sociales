import json
import os


def config_func():

    res = []
    xpaths = []
    for file in os.listdir('.'):
        if os.path.isfile(os.path.join('.', file)):
            res.append(file)
    #pedimos el tipo de webdriver para lanzar el testeo
    print("Escriba el tipo de navegador para el test (Chrome o Firefox)")
    while True:
        try:
            input1 = str(input())
        except ValueError:
            continue
        if (input1 == "Chrome") or (input1 == "chrome"):
            input1 = "chrome"
            print("Ha elegido Chrome.\n")
            break
        elif (input1 == "Firefox") or (input1 == "firefox"):
            input1 = "firefox"
            print("Ha elegido Firefox.\n")
            break
        else:
            print("Entrada incorrecta, las opciones son Chrome o Firefox.")
            continue
    #pedimos el txt con las urls de los sitios a scrapear y miramos si esta en el directorio
    print("Indique el documento de donde leer las urls a scrapear")
    while True:
        try:
            input2 = str(input())
            esta = res.index(input2)
        except ValueError:
            print("Entrada incorrecta, el archivo no existe o no esta en el directorio.")
            continue
        if esta: 
            print("Archivo correcto en el directorio.\n")
            break
        else: 
            print("Entrada incorrecta, el archivo no existe o no esta en el directorio.")
            continue

    urlsFile = open(input2, "r")
    urls = urlsFile.readlines()
    count = 0
    print("Estas son las url en el documento")
    for url in urls:
        count +=1
        print ("{} - {}\n".format(url.strip(), count))
    #pedimos los xpath de los elementos a scrapear
    print("Añada el XPATH del elemento que desea scrapear")
    while True:
        try:
            input3 = str(input())
            print("XPATH recibido.")
            print(input3)
            answer = input("Es correcto este XPATH?\n")
        except ValueError:
            print("Entrada incorrecta, el formato del XPATH es incorrecto.")
            continue
        if answer.lower() in ["y", "yes", "s", "si"]:
            xpaths.append(input3)
            while True:
                try:
                    more = input("Desea añadir más XPATH para otras url en el documento?\n")   
                except ValueError:
                    print("Entrada incorrecta, el formato del XPATH es incorrecto.")
                    continue
                if more.lower() in ["n", "no"] :
                    break
                elif more.lower() in ["y", "yes", "s", "si"]:
                    print("Inserte otro XPATH")
                    input4 = str(input())
                    print("XPATH recibido.")
                    print(input4)
                    answer = input("Es correcto este XPATH?\n")
                    if answer.lower() in ["y", "yes", "s", "si"]:
                        xpaths.append(input4)
                        continue
                    elif answer.lower() in ["n", "no"]:
                        print("Inserte el XPATH correcto")
                        continue
                    continue
            break
        elif answer.lower() in ["n", "no"]:
            print("Inserte el XPATH correcto")
            continue
                
    #escribimos en formato json las especificaciones
    data = {
        "browsers": [
        {
        "browser": input1,
        "urls_doc": input2,
        "xpath": xpaths
        }
        ]
    }

    with open("configuracion.json", "w") as write_file:
        json.dump(data, write_file)