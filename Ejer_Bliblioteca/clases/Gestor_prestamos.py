from datetime import datetime, timedelta
from prestamos import Prestamo
class gestorPrestamos(Prestamo):
    def __init__(self, id_prestamo, fecha_p, fecha_e, fecha_d, nombre, isbn, titulo,cantidad_libro):
        super().__init__(id_prestamo, fecha_p, fecha_e, fecha_d, nombre, isbn, titulo,cantidad_libro)
    
    def BuscarLibro(self):
        nomLibro = input('Ingrese el titulo del libro')
        if nomLibro == {self.titulo}:
            return f'Titulo: {self.titulo}\nisbn: {self.isbn}'
    

    def calcularFechaDev(self):
        fechaDevolucion  = datetime.now() + timedelta(days=15)
        {self.fecha_p} = fechaDevolucion
     
        
    def prestarLibro(self):
        codLibro = input('ingrese el isbn del titulo a prestar')
        if codLibro == {self.isbn} and {self.cantidad_libro} > 0:
            Usuario = input('ingrese el nombre del usuario')
            
            if Usuario.lower == {self.nombre} and {self.us_estado} == 'hbilitado':
                
                return f'El libro {self.titulo} ha sido prestado a {Usuario}'
            else:
                return f'el usuario no existe'
        else:
            return f'El libro {self.titulo} no cuenta con existancias disponibles'
        