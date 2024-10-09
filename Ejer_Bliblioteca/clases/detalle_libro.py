from libro import Libro
from editorial import Editorial
class detalle_libro(Libro,Editorial):
    def __init__(self, isbn, genero, formato, n_pag, id_editorial):
        #se aplica herencia múltiple
        Libro.__init__(self,isbn)
        Editorial.__init__(self,id_editorial)
        self.genero = genero
        self.formato = formato
        self.n_pag = n_pag