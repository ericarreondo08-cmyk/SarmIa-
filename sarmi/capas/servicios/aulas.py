from ... import configuracion
from ..utilidades import horas, listas, textos

    # Recibe la oferta, un aula (por ejemplo "7118") y un día (por ejemplo "viernes").
    # Busca los horarios que se dictan en esa aula ese día, sin importar mayúsculas ni tildes.
    # Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    # Ejemplo: horariosEnAula(oferta, "7118", "viernes") devuelve los horarios de Análisis
    # Numérico y de Introducción a la Programación.

def horariosEnAula(oferta, aula, dia):
    horarios_aula = [] #Aqui se guardaran los horarios cuando encontremos uno que coincida con lo pedido

    for horario in oferta: #Revisamos cada horario 
        au = horario[configuracion.POSICION_AULA] #Guardamos su aula
        d = horario[configuracion.POSICION_DIA] #Guardamos su dia
        if textos.normalizar(au) == textos.normalizar(aula) and textos.normalizar(d) == textos.normalizar(dia): #Comparamos con lo ingresado
            horarios_aula.append(horario) #Si coinciden, se agrega al resultado

    return horarios_aula


    # Recibe una lista de horarios.
    # Arma una copia ordenada por hora de inicio, de la más temprana a la más tarde, con el método
    # de inserción (sin usar sorted). La lista que recibe no cambia.
    # Devuelve la lista ordenada.
    # Ejemplo: con un horario que empieza a las 18:00 y otro a las 13:00, devuelve primero el de las 13:00.


def ordenarPorHora(horarios):
    copia = listas.copiarLista(horarios)

    for i in range(1, len(copia)):
        actual = copia[i]
        minutos_actual = horas.horaAMinutos(actual[configuracion.POSICION_HORA_INICIO])
        j = i - 1

        while j >= 0 and horas.horaAMinutos(copia[j][configuracion.POSICION_HORA_INICIO]) > minutos_actual:
            copia[j + 1] = copia[j]
            j = j - 1

        copia[j + 1] = actual

    return copia