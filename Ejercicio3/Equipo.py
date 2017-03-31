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

    def setDisponibilidad (self, Disponibilidad):
        self.Disponibilidad = Disponibilidad

    def modDisponibilidad (self, dia, turno, activo):
        self.Disponibilidad[dia][turno] = activo