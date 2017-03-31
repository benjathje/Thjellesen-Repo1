class Partido(object):
    Dia = None
    Turno = ''
    Equipo_1 = None
    Equipo_2 = None
    Ganador = None

    def setDia(self, n):
        self.Dia = n

    def setTurno(self, n):
        self.Turno = str(n)

    def setEquipo_1(self, n):
        self.Equipo_1 = n

    def setEquipo_2(self, n):
        self.Equipo_2 = n

