from datetime import datetime, timedelta
from prestamos import Prestamo
class gestorPrestamos(Prestamo):
    def __init__(self, id_prestamo, fecha_prestamo,fecha_estimada, fecha_devolucion, nombre, isbn, titulo,cantidad_libro):
        #se aplica herencia simple
        super().__init__(id_prestamo, fecha_prestamo,fecha_estimada, fecha_devolucion, nombre, isbn, titulo,cantidad_libro)
    
    def buscarLibro(self):#metodo para buscar el isbn del libro
        nomLibro = input('Ingrese el titulo del libro')
        if nomLibro.lower == {self.titulo}:
            return f'Titulo: {self.titulo}\nisbn: {self.isbn}'
    
    def calcularFechaEstimada(self): #metodo para calcular la fecha de dvolucion usando la biblioteca datatime
        fechaEstimada  = datetime.now() + timedelta(days=15)
        {self.fecha_estimada} = fechaEstimada
    
    #se aplica polimorfismo con el metodo calcularFechaEstimada
    def calcularDiasRetraso(self, fecha_devolucion):
        fechaEstimada = self.cacularFechaEstimada()
        diasRetraso = (fecha_devolucion - fechaEstimada).days
        return max(0,diasRetraso)# para que entregue el numero mayor
    
    def prestarLibro(self): #metodo para prestar el libro, comprobacion de cantidad disponible, si el usuario existe y si esque puede pedir libros 
        codLibro = input('ingrese el isbn del titulo a prestar')
        if codLibro == {self.isbn} and {self.cantidad_libro} > 0:
            Usuario = input('ingrese el nombre del usuario')
        elif Usuario.lower == {self.nombre} and {self.us_estado} == 'habilitado':
            descontarPrestamo = {self.cantidad_libro} - 1
            {self.cantidad_libro} = descontarPrestamo                
            return f'Libro prestado a {self.nombre}\nCantidad disponible: {self.cantidad_libro}'
        else:
            return f'No se puede prestar el libro, usuario no existe o no esta habilitado'
    
    