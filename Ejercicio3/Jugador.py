class Jugador(object):
    Nombre = ''
    Apellido = ''
    Fecha_Nacimiento = None
    Numero = ''

    def setNombre (self, nombre):
        self.Nombre = str(nombre)

    def setApellido (self, apellido):
        self.Apellido = str(apellido)

    def setFecha_Nacimiento (self, fecha_nac):
        self.Decha_Nacimiento = fecha_nac

    def setNumero (self, n):
        self.Numero = n
