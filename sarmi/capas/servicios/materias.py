from ... import configuracion
from ..utilidades import listas, textos

    # Recibe una lista de horarios y una posición (ver POSICION_... en configuracion.py).
    # Junta el dato que está en esa posición en cada horario, sin repetir.
    # Devuelve la lista de esos valores, en el orden en que aparecen.
    # Ejemplo: con los horarios de Introducción a la Programación y POSICION_COMISION,
    # devuelve ["COM-01", "COM-02", "COM-03", ...].

def valoresDistintos(horarios, posicion):
    resultado = [] #Aca se va a almacenar cada dato

    for i in horarios: #Recorremos la tabla horarios
        dato = horarios[posicion] 
        if not listas.esta(dato, resultado): #Si el dato que revisamos no esta en nuestra nueva lista lo agregamos
            resultado.append(dato)

    return resultado


    # Recibe la oferta y el nombre de una materia, o una parte (por ejemplo "programacion").
    # Busca los horarios cuya materia contiene ese nombre, sin importar mayúsculas ni tildes.
    # Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    # Ejemplo: buscarMateria(oferta, "programacion") devuelve los horarios de Introducción a la
    # Programación, Programación I, Programación II y otras.

def buscarMateria(oferta, nombre):
    lista_horarios = [] #Preparamos donde guardaremos los horarios
    
    for horario in oferta: #Oferta es una lista de listas, recorremos cada fila de esa lista
        materia = horario[configuracion.POSICION_MATERIA] #Buscamos dentro de esa fila en especifico, cual es la materia
        if textos.contiene(materia, nombre): #Si coincide con el nombre que se pregunto, se agrega al resultado
            lista_horarios.append(horario)

    return lista_horarios 


    # Recibe una lista de horarios y el nombre de una materia.
    # Se queda con los horarios cuya materia se llama exactamente así, sin importar mayúsculas ni tildes.
    # Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    # Ejemplo: si están los horarios de Programación I y de Programación II, con "programación i"
    # devuelve solo los de Programación I.

def filtrarMateriaExacta(horarios, nombre):

    lista_horarios_mExacta = [] #Donde se guardan los horarios
    for horario in horarios: #Horarios es una lista de listas, recorremos cada fila de esa lista
        materiaE = horario[configuracion.POSICION_MATERIA] #Buscamos en la posicion donde se guardan las materias
        if textos.normalizar(materiaE) == textos.normalizar(nombre): #Si coinciden los textos (sin mayus ni tildes) se los agrega al resulado
            lista_horarios_mExacta.append(horario)

    return lista_horarios_mExacta


# Recibe una lista de horarios y una comisión, escrita como sea ("7", "07", "COM-07" o "comisión 7").
# Se queda con los horarios de esa comisión, comparando solo el número.
# Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
# Ejemplo: con los horarios de Introducción a la Programación y "7", devuelve los dos horarios
# de la COM-07: el del viernes y el virtual.

def filtrarPorComision(horarios, comision):
    resultado_horarios = [] #Aqui se guardarán los horarios

    for horario in horarios: #Horarios es una lista de listas, recorremos cada fila de esa lista 
        com = horario[configuracion.POSICION_COMISION] #Buscamos en la posicion donde se guardan los horarios
        if textos.extraerNumero(comision) == textos.extraerNumero(com): #Si coincide el numero de la comision la agrega al resultado
            resultado_horarios.append(horario)

    return resultado_horarios
