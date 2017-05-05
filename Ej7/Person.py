class Person (object):
    Name = ''
    Surname = ''
    DNI = ''

    def setName (self, name):
        self.Name = str(name)

    def setSurname (self, surname):
        self.Surname = str(surname)

    def setDNI (self, dni):
        self.DNI = int(dni)
