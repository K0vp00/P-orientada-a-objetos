from libro import Libro #importa la clase para heredar los atributos
from usuario import Usuario
from disponibilidad_libro import disponibilidadLibro
from datetime import datetime #se importa la biblioteca datatime
class Prestamo(Libro,Usuario,disponibilidadLibro):
    def __init__(self, id_prestamo,fecha_prestamo,fecha_estimada, fecha_devolucion,dias_retraso,id_usuario , nombre,us_estado , isbn, titulo,id_dispo ,cantidad_libro):
        #Clases padres (Usuario,Libro,disponibilidadLibro) y atributos heredados, se aplica herencia múltiple
        Usuario.__init__(self,id_usuario,nombre,us_estado)
        Libro.__init__(self,isbn, titulo)
        disponibilidadLibro.__init__(self,id_dispo,cantidad_libro)
        self._id_prestamo = id_prestamo #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._fecha_prestamo = datetime.now().date #se usa la funcion .date de la biblioteca datatime para extraer solo la fecha
        self._fecha_estimada = fecha_estimada
        self._fecha_devolucion = fecha_devolucion
        self._dias_retraso = dias_retraso