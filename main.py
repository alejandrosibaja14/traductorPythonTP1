#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 26/04/2026
#Ultima actualización: 06/05/2026
#Versión de python: 3.14
#Definición de funciones
import re
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
    tokensCargados=0
    if pseparador.strip()=="":
        retroalimentacionUsuario.append("Debe ingresar un separador válido.")
        return plista, retroalimentacionUsuario
    try:
        with open(pnombreArchivo, "r", encoding="utf-8") as archivo:
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
                if palabraOriginal=="" or reemplazoPalabra=="":
                    retroalimentacionUsuario.append("Token inválido: "+linea)
                    continue
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
                    tokensCargados+=1
        retroalimentacionUsuario.append("Archivo procesado correctamente.")       
        if tokensCargados>0:
            retroalimentacionUsuario.append("Tokens cargados exitosamente.")
    except FileNotFoundError:
        retroalimentacionUsuario.append("Error: el archivo solicitado no existe. Vuelva a intentarlo.")
    return plista, retroalimentacionUsuario

def mostrar_tokens_cargados(plistaTokens):
    print("\n--- TOKENS CARGADOS ---")
    if len(lista_tokens) == 0:
        print("No hay tokens cargados en este momento.")
    else:
        contador = 0
        while contador < len(lista_tokens):
            original = lista_tokens[contador][0]
            reemplazo = lista_tokens[contador][1]
            print(original, "->", reemplazo)
            contador += 1

def agregarModificarTokens(pentrada, pseparador, plista):
    """
    Funcionamiento: Procesa un string que contiene tokens separados por comas, los valida y los agrega o actualiza en la lista de tokens.
    Entradas: pentrada: tokens ingresados por el usuario.
            pseparador: string que separa la palabra original y su reemplazo.
            plista: lista actual de tokens.
    Salidas: Lista de tokens actualizada y una lista de mensajes de retroalimentación.
    """
    retroalimentacionUsuario=[]
    if pseparador.strip()=="":
        retroalimentacionUsuario.append("Debe ingresar un separador válido.")
        return plista, retroalimentacionUsuario
    tokens=pentrada.split(",")
    for t in tokens:
        t=t.strip()
        partesToken=t.split(pseparador)
        if len(partesToken)!=2:
            retroalimentacionUsuario.append("Token inválido: "+t)
            continue
        palabraOriginal=partesToken[0].strip()
        reemplazoPalabra=partesToken[1].strip()
        if palabraOriginal=="" or reemplazoPalabra=="":
            retroalimentacionUsuario.append("Token inválido: "+t)
            continue
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
            retroalimentacionUsuario.append("Token agregado exitosamente: "+palabraOriginal)
    return plista, retroalimentacionUsuario

def traducirCodigo(pnombreArchivo, plistaTokens):
    """
    Funcionamiento: Identifica los tokens presentes en un archivo y genera una versión traducida utilizando ER.
    Entradas: pnombreArchivo: archivo de código a traducir.
            plistaTokens: lista de tokens con la palabra original y su reemplazo.
    Salidas: Lista con las líneas originales del código, lista de tokens encontrados en el archivo, lista con el código traducido y 
    lista de mensajes de retroalimentación.
    """
    retroalimentacionUsuario=[]
    lineasCodigo=[]
    tokensEnArchivo=[]
    codigoTraducido=[]
    try:
        with open(pnombreArchivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea=linea.rstrip()
                if linea=="":
                    continue
                lineasCodigo.append(linea)
                palabras=linea.split()
                for palabra in palabras:
                    for token in plistaTokens:
                        if palabra==token[0]:
                            if palabra not in tokensEnArchivo:
                                tokensEnArchivo.append(palabra)
                lineaTraducida=linea
                for token in plistaTokens:
                    patron=r"\b"+re.escape(token[0])+r"\b"
                    lineaTraducida=re.sub(patron, token[1], lineaTraducida)
                codigoTraducido.append(lineaTraducida)
        if len(lineasCodigo)>0:
            retroalimentacionUsuario.append("El archivo fue leído correctamente.")
        else:
            retroalimentacionUsuario.append("El archivo está vacío.")
    except FileNotFoundError:
        retroalimentacionUsuario.append("El archivo solicitado no existe.")
    return lineasCodigo, tokensEnArchivo, codigoTraducido, retroalimentacionUsuario

def guardarTraduccion(pnombreArchivo, pcodigoTraducido):
    """
    Funcionamiento: Genera un archivo con el código traducido.
    Entradas: pnombreArchivo: nombre del archivo a generar.
            pcodigoTraducido: lista con las líneas del código traducido.
    Salidas: Mensajes de retroalimentación indicando si el archivo fue generado correctamente o si ocurrió un error.
    """
    retroalimentacionUsuario=[]
    try:
        with open(pnombreArchivo, "w", encoding="utf-8") as archivo:
            for linea in pcodigoTraducido:
                archivo.write(linea+"\n")
            retroalimentacionUsuario.append("El archivo con el código traducido ha sido generado correctamente.")
    except Exception:
        retroalimentacionUsuario.append("No se ha podido generar el archivo con el código traducido. Vuelva a intentarlo.")
    return retroalimentacionUsuario

def generarHTML(pnombreArchivo, plineasCodigo, pcodigoTraducido, ptokensEnArchivo):
    """
    Funcionamiento: Genera un archivo HTML con el reporte de traducción del código.
    Entradas: pnombreArchivo: nombre del archivo HTML a generar.
            plineasCodigo: lista con las líneas originales del código.
            pcodigoTraducido: lista con las líneas traducidas.
            ptokensEnArchivo: lista de tokens encontrados en el archivo.
    Salidas: Lista de mensajes de retroalimentación.
    """
    retroalimentacionUsuario=[]
    try:
        with open(pnombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write("<html>\n")
            archivo.write("<head>\n")
            archivo.write('<meta charset="UTF-8">\n')
            archivo.write("<title>Reporte</title>\n")
            archivo.write("</head>\n")
            archivo.write("<body>\n")
            archivo.write("<h1>Reporte de Traducción</h1>\n")
            archivo.write("<h2>Tokens encontrados</h2>\n")
            archivo.write("<ul>\n")
            for token in ptokensEnArchivo:
                archivo.write("<li>"+token+"</li>\n")
            archivo.write("</ul>\n")
            archivo.write("<h2>Código Original</h2>\n")
            archivo.write("<pre>\n")
            for linea in plineasCodigo:
                archivo.write(linea+"\n")
            archivo.write("</pre>\n")
            archivo.write("<h2>Código Traducido</h2>\n")
            archivo.write("<pre>\n")
            for linea in pcodigoTraducido:
                archivo.write(linea+"\n")
            archivo.write("</pre>\n")
            archivo.write("</body>\n")
            archivo.write("</html>\n")
            retroalimentacionUsuario.append("Reporte HTML generado correctamente.")
    except Exception:
        retroalimentacionUsuario.append("No se pudo generar el reporte HTML. Vuelva a intentarlo.")
    return retroalimentacionUsuario

def validarNombreArchivoAux(pmensaje, pextension):
    """
    Funcionamiento: Solicita al usuario un nombre de archivo válido y verifica su extensión.
    Entradas: pmensaje: mensaje que se mostrará al usuario.
            pextension: extensión esperada del archivo.
    Salidas: Nombre de archivo válido.
    """
    nombreArchivo=input(pmensaje)
    while nombreArchivo.strip()=="" or not nombreArchivo.endswith(pextension):
        if nombreArchivo.strip()=="":
            print("Debe ingresar un nombre de archivo válido.")
        else:
            print("El archivo debe tener extensión "+pextension)
        nombreArchivo=input(pmensaje)
    return nombreArchivo

def validarSeparadorAux():
    """
    Funcionamiento: Solicita al usuario un separador válido.
    Entradas: NA
    Salidas: Separador válido.
    """
    separador=input("Ingrese el método de separación usado dentro del archivo (por ejemplo: -> , =): ")
    while separador.strip()=="":
        print("Debe ingresar un separador válido.")
        separador=input("Ingrese el método de separación usado dentro del archivo (por ejemplo: -> , =): ")
    return separador

def main():
    """
    Funcionamiento: Controla la ejecución principal del programa, mostrando el menú de opciones de manera repetitiva.
    Entradas: NA
    Salidas: Resultado según la opción seleccionada por el usuario.
    """
    listaTokens=[]
    lineasCodigo=[]
    tokensEnArchivo=[]
    codigoTraducido=[]
    while True:
        mostrarMenu()
        opcion=input("Seleccione la opción que desee: ")
        if opcion=="1":
            print("\n===== CARGAR TOKENS =====\n")
            print("El archivo debe incluir su extensión correspondiente (.txt).")
            archivo=validarNombreArchivoAux("Ingrese el nombre del archivo a usar: ", ".txt")
            separador=validarSeparadorAux()
            listaTokens, retroalimentacionUsuario=cargarTokens(archivo, separador, listaTokens)
            for m in retroalimentacionUsuario:
                print(m)
        elif opcion=="2":
            print("Pendiente")
        elif opcion=="3":
            print("\n===== AGREGAR/MODIFICAR TOKENS =====\n")
            entrada=input("Ingrese los tokens que desea agregar: ")
            separador=validarSeparadorAux()
            listaTokens, retroalimentacionUsuario=agregarModificarTokens(entrada, separador, listaTokens)
            for mensaje in retroalimentacionUsuario:
                print(mensaje)
        elif opcion=="4":
            print("Pendiente")
        elif opcion=="5":
            print("\n===== TRADUCIR CÓDIGO =====\n")
            if len(listaTokens)==0:
                print("No hay tokens cargados.")
                continue
            print("Debe ingresar un archivo de código válido (por ejemplo: codigo.py).")
            archivoCodigo=validarNombreArchivoAux("Ingrese el archivo de código a traducir: ", ".py")
            lineasCodigo, tokensEnArchivo, codigoTraducido, retroalimentacionUsuario=traducirCodigo(archivoCodigo, listaTokens)
            if len(codigoTraducido)==0:
                for mensaje in retroalimentacionUsuario:
                    print(mensaje)
                continue
            print("El archivo de salida debe incluir extensión (.txt).")
            nombreArchivo=validarNombreArchivoAux("Ingrese el nombre del archivo traducido: ", ".txt")
            mensajes=guardarTraduccion(nombreArchivo, codigoTraducido)
            for mensaje in retroalimentacionUsuario:
                print(mensaje)
            for mensaje in mensajes:
                print(mensaje)
        elif opcion=="6":
            print("Pendiente")
        elif opcion=="7":
            print("\n===== GENERAR REPORTE HTML =====\n")
            if len(codigoTraducido)==0:
                print("Primero debe traducir un archivo.")
                continue
            print("El archivo debe incluir extensión .html.")
            nombreHTML=validarNombreArchivoAux("Ingrese el nombre del archivo HTML a generar: ", ".html")
            mensajes=generarHTML(nombreHTML, lineasCodigo, codigoTraducido, tokensEnArchivo)
            for mensaje in mensajes:
                print(mensaje)
        elif opcion=="8":
            print("Pendiente")
        elif opcion=="9":
            print("Ha salido del sistema.")
            break
        else: print("\nLa opción ingresada no es válida.")
#Inicio del programa principal
main()
