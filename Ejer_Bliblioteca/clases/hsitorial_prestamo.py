from libro import Libro
from usuario import Usuario
from prestamos import Prestamo
class HistorialPrestamo:
    def __init__(self, id_hist_libro, Libro, Usuario, Prestamo):
        #se aplica la composición
        self.id_hist_libro = id_hist_libro
        self.Libro = Libro
        self.usuario = Usuario
        self.Prestamo= Prestamo