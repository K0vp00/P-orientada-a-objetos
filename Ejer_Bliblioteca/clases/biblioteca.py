from contacto import Contacto
class Biblioteca(Contacto):
    def __init__(self, id_biblio, b_nombre, b_direccion, id_contacto,telefono, correo):
        #La clase esta heredando de contacto
        Contacto.__init__(self,id_contacto,telefono, correo)
        self.b_nombre = b_nombre
        self.id_biblio = id_biblio
        self.direccion = b_direccion
        self.id_contacto = id_contacto
        
        