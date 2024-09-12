from autor import Autor
class Libro(Autor):
    def __init__(self,isbn, titulo, id_autor, año, n_copias):
        Autor.__init__(self,id_autor)
        self.isbn = isbn
        self.titulo = titulo
        self.año = año
        self.n_copias = n_copias