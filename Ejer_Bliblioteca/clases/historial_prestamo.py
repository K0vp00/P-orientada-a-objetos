from prestamos import Prestamo
class HistorialPrestamo( Prestamo):
    def __init__(self, id_hist_libro,fecha_p,fecha_d):
        Prestamo.__init__(self,fecha_p,fecha_d)
        self.id_hist_libro = id_hist_libro