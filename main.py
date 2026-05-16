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

def mostrarTokens(plistaTokens):
    """
    Funcionamiento: Recorre la lista de tokens y prepara su visualización.
    Entradas: plistaTokens: lista actual de tokens.
    Salidas: Lista de mensajes de retroalimentación para mostrar en pantalla.
    """
    retroalimentacionUsuario = []
    if len(plistaTokens) == 0:
        retroalimentacionUsuario.append("No hay tokens cargados en este momento.")
    else:
        retroalimentacionUsuario.append("\n--- TOKENS CARGADOS ---")
        contador = 0
        while contador < len(plistaTokens):
            original = plistaTokens[contador][0]
            reemplazo = plistaTokens[contador][1]
            retroalimentacionUsuario.append(original + " -> " + reemplazo)
            contador += 1
    return retroalimentacionUsuario

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

def guardarTokens(pnombreArchivo, pseparador, plistaTokens):
    """
    Funcionamiento: Guarda la lista de tokens actual en un archivo de texto.
    Entradas: pnombreArchivo: nombre del archivo destino.
              pseparador: caracter que separará los tokens.
              plistaTokens: lista actual de tokens.
    Salidas: Lista de mensajes indicando el éxito o error de la operación.
    """
    retroalimentacionUsuario = []
    try:
        with open(pnombreArchivo, "w", encoding="utf-8") as archivo:
            contador = 0
            while contador < len(plistaTokens):
                original = plistaTokens[contador][0]
                reemplazo = plistaTokens[contador][1]
                linea = original + pseparador + reemplazo + "\n"
                archivo.write(linea)
                contador += 1
        retroalimentacionUsuario.append("El archivo ha sido guardado exitosamente.")
    except IOError:
        retroalimentacionUsuario.append("Error: Ocurrió un problema al intentar guardar el archivo.")
    return retroalimentacionUsuario

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

def generarCSV(pnombreArchivo, plistaTokens):
    """
    Funcionamiento: Exporta los tokens a un formato separado por comas.
    Entradas: pnombreArchivo: nombre del archivo CSV destino.
              plistaTokens: lista actual de tokens.
    Salidas: Lista de mensajes indicando el éxito o error de la operación.
    """
    retroalimentacionUsuario = []
    try:
        with open(pnombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write("Palabra Original,Reemplazo\n")
            contador = 0
            while contador < len(plistaTokens):
                original = str(plistaTokens[contador][0])
                reemplazo = str(plistaTokens[contador][1])
                linea = original + "," + reemplazo + "\n"
                archivo.write(linea)
                contador += 1
        retroalimentacionUsuario.append("Reporte CSV creado con éxito.")
    except IOError:
        retroalimentacionUsuario.append("Error: No se pudo generar el documento CSV.")
    return retroalimentacionUsuario

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

def insertarBitacora(pbitacora, pfecha, paccion, pdetalle):
    """
    Funcionamiento: Agrega un nuevo evento a la estructura de la bitácora.
    Entradas: pbitacora: lista principal de la bitácora.
              pfecha: fecha del evento.
              paccion: nombre de la acción realizada.
              pdetalle: descripción profunda del evento.
    Salidas: Lista de bitácora actualizada.
    """
    nuevoEvento = [pfecha, paccion, pdetalle]
    pbitacora.append(nuevoEvento)
    return pbitacora

def filtrarBitacoraPorDia(pbitacora, pdiaBuscado):
    """
    Funcionamiento: Busca y extrae los registros que coincidan con un día específico.
    Entradas: pbitacora: lista principal de la bitácora.
              pdiabuscado: Dia a buscar en la bitácora.
    Salidas: Bitácora por dia.    
    """
    retroalimentacionUsuario = []
    encontrado = False
    contador = 0
    while contador < len(pbitacora):
        registroActual = pbitacora[contador]
        fechaRegistro = registroActual[0]
        if fechaRegistro == pdiaBuscado:
            accion = registroActual[1]
            detalle = registroActual[2]
            retroalimentacionUsuario.append("Acción: " + accion + " | Detalle: " + detalle)
            encontrado = True
        contador += 1
    if not encontrado:
        retroalimentacionUsuario.append("No se encontraron eventos registrados para esa fecha.")
    return retroalimentacionUsuario

def filtrarBitacoraPorPalabra(pbitacora, ppalabraBuscada):
    """
    Funcionamiento: Busca una palabra clave dentro de los detalles de todos los eventos.
    """
    retroalimentacionUsuario = []
    encontrado = False
    contador = 0
    while contador < len(pbitacora):
        registroActual = pbitacora[contador]
        detalleStr = str(registroActual[2])
        if ppalabraBuscada in detalleStr:
            fecha = registroActual[0]
            accion = registroActual[1]
            retroalimentacionUsuario.append("Fecha: " + fecha + " | Acción: " + accion + " | Detalle: " + detalleStr)
            encontrado = True
        contador += 1
    if not encontrado:
        retroalimentacionUsuario.append("No se encontraron coincidencias para esa palabra.")
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
    listaBitacora = []
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
            fechaActual = input("Ingrese la fecha de hoy para la bitácora (ej. 15/05/2026): ")
            listaBitacora = insertarBitacora(listaBitacora, fechaActual, "Cargar Tokens", "Se intentó cargar el archivo " + archivo)
        elif opcion=="2":
            print("\n===== MOSTRAR TOKENS =====\n")
            mensajes = mostrarTokens(listaTokens)
            for mensaje in mensajes:
                print(mensaje)          
        elif opcion=="3":
            print("\n===== AGREGAR/MODIFICAR TOKENS =====\n")
            entrada=input("Ingrese los tokens que desea agregar: ")
            separador=validarSeparadorAux()
            listaTokens, retroalimentacionUsuario=agregarModificarTokens(entrada, separador, listaTokens)
            for mensaje in retroalimentacionUsuario:
                print(mensaje)
        elif opcion=="4":
            print("\n===== GUARDAR TOKENS =====\n")
            if len(listaTokens) == 0:
                print("No hay tokens cargados para guardar.")
                continue
            nombreArchivo = validarNombreArchivoAux("Ingrese el nombre del archivo a guardar: ", ".txt")
            separador = validarSeparadorAux()
            mensajes = guardarTokens(nombreArchivo, separador, listaTokens)
            for mensaje in mensajes:
                print(mensaje)
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
        elif opcion == "6":
            print("\n===== GENERAR CSV =====\n")
            if len(listaTokens) == 0:
                print("No hay tokens cargados para generar el archivo CSV.")
                continue
            nombreArchivo = validarNombreArchivoAux("Ingrese el nombre del archivo CSV a generar (ejemplo: reporte.csv): ", ".csv")
            mensajes = generarCSV(nombreArchivo, listaTokens)
            for mensaje in mensajes:
                print(mensaje)
            fechaActual = input("Ingrese la fecha de hoy para la bitácora: ")
            listaBitacora = insertarBitacora(listaBitacora, fechaActual, "Generar CSV", "Se generó el archivo " + nombreArchivo)
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
        elif opcion == "8":
            print("\n===== CONSULTAR BITÁCORA =====\n")
            print("1. Filtrar bitácora por día")
            print("2. Filtrar bitácora por palabra clave")
            subOpcion = input("Seleccione el método de búsqueda: ")
            if subOpcion == "1":
                diaBuscado = input("Ingrese el día a buscar (ejemplo: 06/05/2026): ")
                mensajes = filtrarBitacoraPorDia(listaBitacora, diaBuscado)
                for mensaje in mensajes:
                    print(mensaje)
            elif subOpcion == "2":
                palabraBuscada = input("Ingrese la palabra clave a buscar: ")
                mensajes = filtrarBitacoraPorPalabra(listaBitacora, palabraBuscada)
                for mensaje in mensajes:
                    print(mensaje)   
            else:
                print("La opción ingresada no es válida.")
        elif opcion=="9":
            print("Ha salido del sistema.")
            break
        else: print("\nLa opción ingresada no es válida.")
#Inicio del programa principal
main()
