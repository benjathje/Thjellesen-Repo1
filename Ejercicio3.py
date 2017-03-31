from .Ejercicio3.Equipo import Equipo
from .Ejercicio3.Jugador import Jugador
from .Ejercicio3.Partido import Partido
from .Ejercicio3.Torneo import Torneo
from datetime import date

J1 = Jugador()
J2 = Jugador()
J3 = Jugador()
J4 = Jugador()
E1 = Equipo()
E2 = Equipo()
E3 = Equipo()
E4 = Equipo()
P1 = Partido()
T1 = Torneo()

J1.setNombre('Eduardo')
J1.setApellido('Perez')
J1.setFecha_Nacimiento(1990,4,5)
J1.setNumero(5)

J2.setNombre('Pedro')
J2.setApellido('Gonzandrelli')
J2.setFecha_Nacimiento(1989,6,12)
J2.setNumero(11)

J3.setNombre('Sergio')
J3.setApellido('Marianollo')
J3.setFecha_Nacimiento(1990,7,11)
J3.setNumero(2)

J4.setNombre('Yeison')
J4.setApellido('Grasa')
J4.setFecha_Nacimiento(1991,8,10)
J4.setNumero(16)

E1.Nombre('Empanada de Carne CC')
E1.setBarrio('Cohgland')
E1.setJugador(J1)
E1.setCapitan(J1)

E2.Nombre('Nautilus')
E2.setBarrio('Cohgland')
E2.setJugador(J2)
E2.setCapitan(J2)

E3.Nombre('Filetito CC')
E3.setBarrio('Villa Santa Rita')
E3.setJugador(J3)
E3.setCapitan(J3)

E4.Nombre('Python Console')
E4.setBarrio('Etapa de Zafra')
E4.setJugador(J4)
E4.setCapitan(J4)