from contacto import Contacto
class Editorial(Contacto):
    def __init__(self,id_editorial, e_nombre, contacto,telefono):
        #Clase padre (Contacto) y atributos heredados, se aplica herencia simple
        super().__init__(self,contacto,telefono)
        self._id_editorial = id_editorial #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._e_nombre = e_nombre