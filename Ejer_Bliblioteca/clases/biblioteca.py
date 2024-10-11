from contacto import Contacto
class Biblioteca(Contacto):
    def __init__(self, id_biblio, b_nombre, b_direccion, id_contacto,telefono, correo):
        #Clase padre (Contacto) y atributos heredados, se aplica herencia simple
        super().__init__(self,id_contacto,telefono, correo)
        self._b_nombre = b_nombre #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._id_biblio = id_biblio
        self._direccion = b_direccion
        self._id_contacto = id_contacto
