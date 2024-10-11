from libro import Libro #importa la clase para heredar los atributos
from usuario import Usuario
from disponibilidad_libro import disponibilidadLibro
from Gestor_prestamos import gestorPrestamos
from datetime import datetime #se importa la biblioteca datatime
class Prestamo(Libro,Usuario,disponibilidadLibro):
    def __init__(self, id_prestamo,fecha_prestamo,fecha_estimada, fecha_devolucion,dias_retraso, nombre,us_estado , isbn, titulo,cantidad_libro):
        #Clases padres (Usuario,Libro,disponibilidadLibro) y atributos heredados, se aplica herencia múltiple
        Usuario.__init__(self,nombre,us_estado)
        Libro.__init__(self,isbn, titulo)
        disponibilidadLibro.__init__(self,cantidad_libro)
        self.id_prestamo = id_prestamo #atributo adicional de la clase
        self.fecha_prestamo = datetime.now().date #se usa la funcion .date de la biblioteca datatime para extraer solo la fecha
        self.fecha_estimada = fecha_estimada
        self.fecha_devolucion = fecha_devolucion
        self.dias_retraso = dias_retraso