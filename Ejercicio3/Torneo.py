class Torneo(object):
    Lista_Equipos = []
    Lista_Partidos = []

    def __init__(self):
        self.Lista_Equipos = []
        self.Lista_Partidos = []

    def setAgregar_Equipo(self, n):
        self.Lista_Equipos.append(n)

    def setAgregar_Partido(self, n):
        self.Lista_Partidos.append (n)
