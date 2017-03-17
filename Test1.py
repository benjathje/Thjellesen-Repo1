import datetime

class Alumno (object):
    nombre = ''
    apellido = ''
    fechaNacimiento = None
    listaDeNotas = []

def setNombre (self, nombre):
    self.nombre = str(nombre)

def setApellido (self, apellido):
    self.apellido = str(apellido)

def setFechaDeNacimiento (self, fechaNacimiento):
    self.fechaDeNacimiento = fechaNacimiento

def agregarNota (self, nota):
    self.listaDeNotas.append(nota)

def menorNota (self):
    return min(self.listaDeNotas)

def mayorNota (self):
    return max(self.listaDeNotas)

def promedioNotas (self):
    return sum(self.listaDeNotas)/len(listaDeNotas)
