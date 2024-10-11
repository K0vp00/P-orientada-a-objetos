from libro import Libro
from editorial import Editorial
class detalle_libro(Libro,Editorial):
    def __init__(self, isbn, genero, formato, n_pag, id_editorial):
        #Clases padres (Libro,editorial) y atributos heredados, se aplica herencia múltiple
        Libro.__init__(self,isbn)
        Editorial.__init__(self,id_editorial)
        self.genero = genero #atributo adicional de la clase
        self.formato = formato
        self.n_pag = n_pag