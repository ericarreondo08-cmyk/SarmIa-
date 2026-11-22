MINUTOS_POR_HORA = 60

    # Recibe una hora escrita como "HH:MM".
    # Calcula cuántos minutos pasaron desde las 00:00.
    # Devuelve esa cantidad de minutos.
    # Ejemplo: horaAMinutos("18:30") devuelve 1110.

def horaAMinutos(hora):
    partes = hora.split(":") #Divide la cadena en el caracter ":"

    horas = int(partes[0])
    mins = int(partes[1])

    return horas * MINUTOS_POR_HORA + mins #Ejemplo: Si son 8 horas, 8 * 60 + minutos
