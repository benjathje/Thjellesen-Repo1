from Test1 import Alumno
from datetime import date

a = Alumno()
a.setNombre('piripipi')
a.setApellido('chuaman')

a.setFechaDeNacimiento (date (2013,3,4))

a.agregarNota (4)
a.agregarNota (10)

print(a.promedioNotas())