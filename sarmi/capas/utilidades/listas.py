
# Funcion que recibe un elemento y una lista.
# Se fija si el elemento aparece en la lista.
# Devuelve True si aparece y False si no.
# Ejemplo: esta("COM-07", ["COM-01", "COM-07"]) devuelve True.

def esta(elemento, lista):

    for elem in lista:
        if elemento == elem:
            return True

    return False



# Funcion que recibe una lista.
# Arma una lista nueva con los mismos elementos, en el mismo orden.
# Devuelve la lista nueva: si después se modifica la copia, la original no cambia.
# Ejemplo: copiarLista([1, 2, 3]) devuelve otra lista [1, 2, 3].

def copiarLista(lista):

    copia_lista = []  #Creamos la lista que luego sera la copia

    for i in range(len(lista)): #Recorre item por item de la lista original 
        copia_lista.append(lista[i]) #Agrega cada item a la nueva lista


    return copia_lista


