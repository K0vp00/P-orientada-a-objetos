from libro import Libro
from usuario import Usuario
from disponibilidad_libro import disponibilidadLibro
class Prestamo(Libro,Usuario,disponibilidadLibro):
    def __init__(self, id_prestamo, fecha_prestamo,fecha_estimada, fecha_devolucion, nombre, isbn, titulo,cantidad_libro):
        #se aplica herencia multiple
        Usuario.__init__(self,nombre)
        Libro.__init__(self,isbn, titulo)
        disponibilidadLibro.__init__(self,cantidad_libro)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_estimada = fecha_estimada
        self.fecha_devolucion = fecha_devolucion