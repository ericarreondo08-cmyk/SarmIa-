from ... import configuracion
from ..utilidades import horas, textos

def turnoDe(horario):
    """OPCIONAL. Recibe un horario.
    Se fija en qué turno empieza, según TURNOS en configuracion.py.
    Devuelve "mañana", "tarde" o "noche", o "" si el horario es virtual.
    Ejemplo: un horario que empieza a las 18:00 devuelve "noche"."""
    if horario[configuracion.POSICION_DIA] == configuracion.DIA_VIRTUAL or horario[configuracion.POSICION_HORA_INICIO] == "":
        return ""
    minutosInicio = horas.horaAMinutos(horario[configuracion.POSICION_HORA_INICIO])
    for rango in configuracion.TURNOS:
        inicioTurno = horas.horaAMinutos(rango[1])
        finTurno = horas.horaAMinutos(rango[2])

        if inicioTurno <= minutosInicio <= finTurno:
            return rango[0]
    return ""


def filtrarPorTurno(horarios, turno):
    """OPCIONAL. Recibe una lista de horarios y un turno ("mañana", "tarde" o "noche").
    Se queda con los horarios que empiezan en ese turno.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Álgebra I y "noche", devuelve el de la COM-02 (miércoles 18:00)."""
    resultado=[]
    turnoBuscado= textos.normalizar(turno)

    for horario in horarios:
        turnoActual=textos.normalizar(turnoDe(horario))
        if turnoActual==turnoBuscado: 
           resultado.append(horario)
    
    return resultado

