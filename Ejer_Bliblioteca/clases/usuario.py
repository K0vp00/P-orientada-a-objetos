from contacto import Contacto
from historial_prestamo import HistorialPrestamo
from libro import Libro
class Usuario(Contacto,HistorialPrestamo,Libro):
    def __init__(self, id_usuario, nombre,id_hist_libro,fecha_d, fecha_p,titulo, us_estado, cod_credencial,correo, telefono):
        Contacto.__init__(self, telefono, correo)
        HistorialPrestamo.__init__(self,id_hist_libro, fecha_d, fecha_p)
        Libro.__init__(self,titulo)
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.us_estado = us_estado
        self.cod_credencial = cod_credencial