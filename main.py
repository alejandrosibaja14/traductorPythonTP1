def mostrarMenu():
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

def cargarTokens(parchivo, pseparador, plista):
    print("Archivo utilizado:", parchivo)
    print("Separador utilizado:", pseparador)
    return plista
    #Función sin terminar

def main():
    listaTokens=[]
    while True:
        mostrarMenu()
        opcion=input("Seleccione la opción que desee: ")
        if opcion=="1":
            archivo=input("Ingrese el nombre del archivo a usar: ")
            separador=input("Ingrese el método de separación usado dentro del archivo (por ejemplo: -> , =)")
            listaTokens=cargarTokens(archivo, separador, listaTokens)
        elif opcion=="2":
            print("Pendiente")
        elif opcion=="3":
            print("Pendiente")
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