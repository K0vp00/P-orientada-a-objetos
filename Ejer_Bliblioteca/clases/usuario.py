from contacto import Contacto
from libro import Libro
class Usuario(Contacto,Libro):
    def __init__(self, id_usuario, nombre,titulo, us_estado, cod_credencial,correo, telefono):
        Contacto.__init__(self, telefono, correo)
        Libro.__init__(self,titulo)
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.us_estado = us_estado
        self.cod_credencial = cod_credencial