from libro import Libro
from usuario import Usuario
class Prestamo(Libro,Usuario):
    def __init__(self, id_prestamo, isbn, fecha_p, fecha_e, fecha_d, n_usuario):
        Libro.__init__(self,isbn)
        Usuario.__init__(self, n_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_p = fecha_p
        self.fecha_e = fecha_e
        self.fecha_d = fecha_d