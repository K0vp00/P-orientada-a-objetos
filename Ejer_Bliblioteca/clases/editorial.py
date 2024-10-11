from contacto import Contacto
class Editorial(Contacto):
    def __init__(self,id_editorial, e_nombre, contacto,telefono):
        #Clase padre (Contacto) y atributos heredados, se aplica herencia simple
        super().__init__(self,contacto,telefono)
        self.id_editorial = id_editorial
        self.e_nombre = e_nombre