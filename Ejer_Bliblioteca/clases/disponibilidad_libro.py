from libro import Libro
class disponibilidadLibro(Libro):
    def __init__(self, id_dispo, cantidad_libro, isbn):
        #se aplica herencia simple
        super.__init__(self,isbn)
        self.id_dispo = id_dispo
        self.cantidad_libro = cantidad_libro