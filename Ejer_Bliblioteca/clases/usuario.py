from contacto import Contacto #importa la clase para heredar los atributos
from libro import Libro 
from Constantes import estado #importa el diccionario que esta en el archivo constantes
class Usuario(Contacto,Libro):
    def __init__(self, id_usuario, nombre,titulo, us_estado, cod_credencial,correo, telefono):
        #Clases padres (Contacto,Libro) y atributos heredados, se aplica herencia múltiple
        Contacto.__init__(self, telefono, correo) 
        Libro.__init__(self,titulo)
        self.id_usuario = id_usuario #atributo adicional de la clase
        self.nombre = nombre 
        self.us_estado = us_estado 
        self.cod_credencial = cod_credencial 
        
    # metodo para cambiar el estado a un usuario    
    def cambiarEstado(self):
        nombreUsuario = input('ingrese el nombre del usuario')
        if nombreUsuario == self.nombre: 
            nuevoEstado = input('Ingrese el estado')
            if nuevoEstado in estado: 
                self.us_estado = estado[nuevoEstado] 
                print(f'el estado del {self.nombre} ha sido cambiado a {self.us_estado}') 
            else:
                print(f'el usuario {self.nombre} no existe')