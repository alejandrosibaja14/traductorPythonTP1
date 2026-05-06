#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 26/04/2026
#Ultima actualización: 06/05/2026
#Versión de python: 3.14
#Definición de funciones
def mostrarMenu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print("\nSistema de traducción de código")
    print("\n============== Menú ==============\n")
    print("1. Cargar tokens")
    print("2. Mostrar tokens")
    print("3. Agregar/modificar token")
    print("4. Guardar tokens")
    print("5. Traducir código")
    print("6. Generar CSV")
    print("7. Generar HTML")
    print("8. Bitácora")
    print("9. Salir")
    print("\n==================================\n")

def cargarTokens(pnombreArchivo, pseparador, plista):
    """
    Funcionamiento: Lee un archivo de texto que contiene tokens separados por un separador, 
    los valida, y los agrega o actualiza en la lista de tokens.
    Entradas: pnombreArchivo: nombre del archivo a leer.
            pseparador: string que separa la palabra original y su reemplazo.
            plista: lista actual de tokens.
    Salidas: Lista de tokens actualizada y una lista de mensajes de retroalimentación.
    """
    retroalimentacionUsuario=[]
    try:
        with open(pnombreArchivo, "r") as archivo:
            for linea in archivo:
                linea=linea.strip()
                if linea=="":
                    continue
                partes=linea.split(pseparador)
                if len(partes)!=2:
                    retroalimentacionUsuario.append("Línea no válida: "+linea)
                    continue
                palabraOriginal=partes[0].strip()
                reemplazoPalabra=partes[1].strip()
                token=(palabraOriginal, reemplazoPalabra)
                tokenDuplicado=False
                for i in range(len(plista)):
                    if plista[i][0]==palabraOriginal:
                        retroalimentacionUsuario.append("El token: "+palabraOriginal+" ha sido sobreescrito.")
                        plista[i]=token
                        tokenDuplicado=True
                        break
                if not tokenDuplicado:
                    plista.append(token)
    except FileNotFoundError:
        retroalimentacionUsuario.append("Error: el archivo solicitado no existe. Vuelva a intentarlo.")
    return plista, retroalimentacionUsuario                

def agregarModificarTokens(pentrada, pseparador, plista):
    """
    Funcionamiento: Procesa un string que contiene tokens separados por comas, los valida y los agrega o actualiza en la lista de tokens.
    Entradas: pentrada: tokens ingresados por el usuario.
            pseparador: string que separa la palabra original y su reemplazo.
            plista: lista actual de tokens.
    Salidas: Lista de tokens actualizada y una lista de mensajes de retroalimentación.
    """
    retroalimentacionUsuario=[]
    tokens=pentrada.split(",")
    for t in tokens:
        t=t.strip()
        partesToken=t.split(pseparador)
        if len(partesToken)!=2:
            retroalimentacionUsuario.append("Token inválido: "+t)
            continue
        palabraOriginal=partesToken[0].strip()
        reemplazoPalabra=partesToken[1].strip()
        tokenNuevo=(palabraOriginal, reemplazoPalabra)
        tokenDuplicado=False
        for i in range(len(plista)):
            if plista[i][0]==palabraOriginal:
                plista[i]=tokenNuevo
                tokenDuplicado=True
                retroalimentacionUsuario.append("El token: "+palabraOriginal+" ha sido sobreescrito.")
                break
        if not tokenDuplicado:
            plista.append(tokenNuevo)
            retroalimentacionUsuario.append("Token agregado existosamente: "+palabraOriginal)
    return plista, retroalimentacionUsuario

def main():
    """
    Funcionamiento: Controla la ejecución principal del programa, mostrando el menú de opciones de manera repetitiva.
    Entradas: NA
    Salidas: Resultado según la opción seleccionada por el usuario.
    """
    listaTokens=[]
    while True:
        mostrarMenu()
        opcion=input("Seleccione la opción que desee: ")
        if opcion=="1":
            archivo=input("Ingrese el nombre del archivo a usar: ")
            separador=input("Ingrese el método de separación usado dentro del archivo (por ejemplo: -> , =): ")
            listaTokens, retroalimentacionUsuario=cargarTokens(archivo, separador, listaTokens)
            for m in retroalimentacionUsuario:
                print(m)
        elif opcion=="2":
            print("Pendiente")
        elif opcion=="3":
            entrada=input("Ingrese los tokens que desea agregar: ")
            separador=input("Ingrese el método de separación usado dentro del archivo (por ejemplo: -> , =): ")
            listaTokens, retroalimentacionUsuario=agregarModificarTokens(entrada, separador, listaTokens)
            for mensaje in retroalimentacionUsuario:
                print(mensaje)
        elif opcion=="4":
            print("Pendiente")
        elif opcion=="5":
            print("Pendiente")
        elif opcion=="6":
            print("Pendiente")
        elif opcion=="7":
            print("Pendiente")
        elif opcion=="8":
            print("Pendiente")
        elif opcion=="9":
            print("Ha salido del sistema.")
            break
        else: print("\nLa opción ingresada no es válida.")

main()