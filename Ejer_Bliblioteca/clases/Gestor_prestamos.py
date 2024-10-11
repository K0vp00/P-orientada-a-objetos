from datetime import datetime, timedelta #Bibliteca utilizada
from prestamos import Prestamo #importa la clase prestamo para heredar
class gestorPrestamos(Prestamo):
    def __init__(self, id_prestamo, fecha_prestamo,fecha_estimada, fecha_devolucion,dias_retraso, nombre,us_estado, isbn, titulo,cantidad_libro):
        #Clase padre (prestamo) y atributos eredados, se aplica herencia simple
        super().__init__(id_prestamo, fecha_prestamo,fecha_estimada, fecha_devolucion,dias_retraso, nombre,us_estado, isbn, titulo,cantidad_libro)
    
    def buscarLibro(self):#metodo para buscar el isbn del libro o si existe el libro
        nomLibro = input('Ingrese el titulo del libro') 
        if nomLibro.lower() == self.titulo.lower(): 
            return f'Titulo: {self.titulo}\nisbn: {self.isbn}' 
        else:
            return 'No se encontro el libro'
    
    def calcularFechaEstimada(self): #metodo para calcular la fecha de dvolucion usando la biblioteca datatime
        self.fecha_estimada  = self.fecha_prestamo + timedelta(days=15) #se utiliza la clase (timdelta) de biblioteca datetime
        return self.fecha_estimada
    
    #se aplica polimorfismo con el metodo calcularFechaEstimada
    class PrestamoLargoPlazo(Prestamo):
        def calcularFechaEstimada(self):
            # Sobrescribe devolver una fecha estimada de 30 días
            return self.fecha_prestamo + timedelta(days=30)
    
    
    def prestarLibro(self): #metodo para prestar el libro  
        codLibro = input('ingrese el isbn del titulo a prestar')
        if codLibro == self.isbn and self.cantidad_libro > 0:
            Usuario = input('ingrese el nombre del usuario')
        elif Usuario.lower == self.nombre and self.us_estado == 'habilitado':
            descontarPrestamo = self.cantidad_libro - 1
            self.cantidad_libro = descontarPrestamo                
            return f'Libro prestado a {self.nombre}\nCantidad disponible: {self.cantidad_libro}'
        else:
            return f'No se puede prestar el libro, usuario no existe o no esta habilitado'

    def calcularDiasRetraso(self):
        self.dias_Retraso = (self.fecha_devolucion - self.fecha_estimada).days
        return max(0,{self.dias_retraso})

    def devolverLibro(self): #metodo para ingresar el libro prestado
        nombreLibroDevuelto = input('Ingrese el titulo del libro')
        if nombreLibroDevuelto.lower == self.titulo:
            agregarLibro = self.cantidad_libro + 1
            self.cantidad_libro = agregarLibro
