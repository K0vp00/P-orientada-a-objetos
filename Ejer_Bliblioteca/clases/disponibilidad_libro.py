from libro import Libro
class disponibilidadLibro(Libro):
    def __init__(self, id_dispo, cantidad_libro, isbn):
        #Clase padre (libro) y atributos heredados, se aplica herencia simple
        super().__init__(self,isbn)
        self._id_dispo = id_dispo #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._cantidad_libro = cantidad_libro