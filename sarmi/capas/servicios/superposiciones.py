from ... import configuracion
from ..utilidades import horas

    #esta funcion recibe dos horarios, verifica si los dos son presenciales, son el mismo día y sus horas se cruzan. si uno termina justo cuando empieza el otro (de 14 a 18 y de 18 a 22), no se superponen
    #devuelve True si se superponen y False si no
    #ejemplo: un viernes de 18:00 a 22:00 y un viernes de 20:00 a 22:00 se superponen: devuelve True

def seSuperponen(horarioA,horarioB):
    diaA = horarioA[configuracion.POSICION_DIA] #Guardamos en variables los dias de cada materia para compararlas
    diaB = horarioB[configuracion.POSICION_DIA]
    if diaA == configuracion.DIA_VIRTUAL or diaB == configuracion.DIA_VIRTUAL:  ##con que una sea virtual basta para que no se superpongan
        return False
    if diaA != diaB: ## como son dias distintos no se van a superponer y devolvemos false
        return False

#Pasamos a minutos las horas de inicio y fin de cada materia para compararlas y ver si se superponen
    inicioA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_INICIO]) 
    inicioB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_INICIO])
    finA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_FIN]) 
    finB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_FIN])

    if inicioA < finB and inicioB < finA:  #si las dos materias se superponen, devolvemos true
        return True
    else: #si no se superponen devolvemos false 
        return False
    


#recibe dos listas de horarios (por ejemplo, los de dos comisiones), compara cada horario de la primera lista con cada horario de la segunda.
#devuelve una lista de pares [horarioA, horarioB] que se superponen, o una lista vacía si no hay ninguno.
#ejemplo: con [viernesDe18a22] y [viernesDe20a22, lunesDe18a22] devuelve [[viernesDe18a22, viernesDe20a22]].    

def buscarSuperposiciones(horariosA, horariosB):
    lista_superpuestos = [] #aca se guardan los horarios superpuestos
    for horarioA in horariosA: #Recorremos cada horario de A
        for horarioB in horariosB: #Recorremos cada horario de B
            if seSuperponen(horarioA, horarioB): #Si se superponen, los agregamos a la lista
                lista_superpuestos.append([horarioA, horarioB])

    return lista_superpuestos

