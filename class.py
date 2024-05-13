class Alumno():
    #Alumno de clase virtual
    def __init__(self, nom, ape,dni, edad):
        self.nombre=nom
        self.apelido=ape
        self.nrodni=dni
        self.edad=edad
    
x=Alumno("Josesito", "Pérez", 42521715, 23)
print(x.nombre, x.apelido, x.nrodni, x.edad)
