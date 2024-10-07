from libro import Libro
class DisponibilidadLibro(Libro):
    def __init__(self, id_dispo, cantidad_libro, ejemplares_libro, estado, isbn):
        Libro.__init__(self,isbn)
        self.id_dispo = id_dispo
        self.cantidad_libro = cantidad_libro
        self.ejemplares_libro = ejemplares_libro
        self.estado = estado 