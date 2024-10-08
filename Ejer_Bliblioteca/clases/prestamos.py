from libro import Libro
from usuario import Usuario
from disponibilidad_libro import disponibilidadLibro
class Prestamo(Libro,Usuario,disponibilidadLibro):
    def __init__(self, id_prestamo, fecha_p, fecha_e, fecha_d, nombre, isbn, titulo,cantidad_libro):
        Usuario.__init__(self,nombre)
        Libro.__init__(self,isbn, titulo)
        disponibilidadLibro.__init__(self,cantidad_libro)
        self.id_prestamo = id_prestamo
        self.fecha_p = fecha_p
        self.fecha_e = fecha_e
        self.fecha_d = fecha_d