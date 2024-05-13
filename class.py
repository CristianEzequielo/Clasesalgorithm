class Alumno():
    #Alumno de clase virtual
    def __init__(self, nom, ape,dni, edad):
        self.nombre=nom
        self.apelido=ape
        self.nrodni=dni
        self.edad=edad
    
x=Alumno("Cristian", "Linares", 33714571, 36)
print(x.nombre, x.apelido, x.nrodni, x.edad)