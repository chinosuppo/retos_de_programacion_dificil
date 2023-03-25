### Reto #15: ¿CUÁNTOS DÍAS? ###

"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * La función recibirá dos String y retornará un Int.
 * La diferencia en días será absoluta (no importa el orden de las fechas).
 * Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

from datetime import datetime

def diferencia_fechas(fecha_1, fecha_2):
    try:
        formateo = "%d/%m/%Y"
        fecha_1 = datetime.strptime(fecha_1, formateo)
        fecha_2 = datetime.strptime(fecha_2, formateo)
        diferencia = abs(fecha_1-fecha_2)
        return diferencia
    except:
        raise ValueError("Una de las fechas ingresadas no cumple el formato que se pidio")
    

fecha1 = "22/02/1998"
fecha2 = "14/03/2001"

print(diferencia_fechas(fecha1,fecha2))
