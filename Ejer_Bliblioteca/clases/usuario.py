from contacto import Contacto #importa la clase para heredar los atributos
from Constantes import estado #importa el diccionario que esta en el archivo constantes
class Usuario(Contacto):
    def __init__(self, id_usuario, nombre, us_estado, cod_credencial,correo, telefono):
        #Clases padres (Contacto) y atributos heredados, se aplica herencia simple
        super().__init__(self, telefono, correo) 
        self._id_usuario = id_usuario #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._nombre = nombre 
        self._us_estado = us_estado 
        self._cod_credencial = cod_credencial 
        
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