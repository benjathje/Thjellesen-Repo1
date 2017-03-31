class Equipo(object):
    Lista_Jugadores = []
    Nombre = ''
    Barrio = ''
    Capitan = None
    Disponibilidad = []

    def __init__ (self):
        self.Lista_Jugadores = []
        self.Disponibilidad = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]

    def setJugador(self, n):
        self.Lista_Jugadores.append(n)

    def setBarrio (self, n):
        self.Barrio = str(n)

    def setCapitan(self, n):
        self.Capitan = (n)

    def setDisponibilidad (self, dia, turno):
        i = 0;
        if turno == "M":
            i = 1
        if turno == "T":
            i = 2
        if turno == "N":
            i = 3
        self.Disponibilidad [dia-1] [i-1] = True