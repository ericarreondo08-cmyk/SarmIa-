from ... import configuracion

#Funcion que recibe un texto
#Lo pasa a minúsculas y le saca las tildes (ver LETRAS_CON_TILDE en configuracion.py).
#Devuelve el texto nuevo.
#Ejemplo: normalizar("Introducción a la PROGRAMACIÓN") devuelve "introduccion a la programacion".

def normalizar(texto):

    texto_normalizado = ""  #Es donde se iran sumando los caracteres normalizados
                            #para formar el nuevo texto

  
    for letra in texto: 
        letra_min = letra.lower() #Convertimos a minuscula, ya que en letras_con_tilde estan solo las minusculas
        if letra_min in (configuracion.LETRAS_CON_TILDE): 
            #Si tiene tilde, Recorremos por indice letras_con_tilde, ya que letras_sin_tilde tiene las mismas letras, correspondidas al indice
            for i in range(len((configuracion.LETRAS_CON_TILDE))):  
                if letra_min == (configuracion.LETRAS_CON_TILDE[i]):
                    texto_normalizado += (configuracion.LETRAS_SIN_TILDE[i])

        else: #Si no es una letra con tilde, simplemente la agregamos al nuevo texto
            texto_normalizado += letra_min

    return texto_normalizado

    # Recibe dos textos: texto y buscado.
    # Se fija si buscado aparece en alguna parte de texto.
    # Devuelve True si aparece y False si no.
    # Ejemplo: contiene("introduccion a la programacion", "program") devuelve True.

def contiene(texto, buscado):
    if normalizar(buscado) in normalizar(texto): #Quita mayus y tildes y chequea si esta buscado en texto
        return True #Si se cumple devuelve True
    else: #Devuelve False
        return False 
    
    # Recibe un texto.
    # Junta los dígitos que aparecen en el texto y los convierte en número.
    # Devuelve ese número, o -1 si el texto no tiene dígitos.
    # Ejemplo: extraerNumero("COM-07") devuelve 7.

def extraerNumero(texto):
    nums=["0","1", "2", "3", "4", "5", "6", "7", "8", "9"] #Es donde se fijara la funcion si el digito es un numero
    digito="" #Es donde guardaremos los numeros

    for elem in texto: #Recorremos caracter por caracter buscando si ese caracter esta en la lista nums
        if elem in nums:
            digito+=elem #Lo agregamos

    if digito=="": #Si es == "" quiere decir que no se agrego ningun numero, por lo tanto devuelve -1
        return -1
    else: 
        return int(digito) #Convierte a int y lo devuelve
    
