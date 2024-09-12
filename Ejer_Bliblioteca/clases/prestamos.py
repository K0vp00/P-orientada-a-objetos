from libro import Libro
from usuario import Usuario
class Prestamo(Libro,Usuario):
    def __init__(self, isbn, fecha_p, fecha_e, fecha_d, n_usuario, estado):
        Libro.__init__(self,isbn)
        Usuario.__init__(self, n_usuario)
        self.fecha_p = fecha_p
        self.fecha_e = fecha_e
        self.fecha_d = fecha_d