from autor import Autor
class Libro(Autor):
    def __init__(self,isbn, titulo, id_autor, año, formato, n_pag, idioma_libro, genero_libro, categoria_libro):
        Autor.__init__(self,id_autor)
        self.isbn = isbn
        self.titulo = titulo
        self.año = año
        self.formato = formato
        self.n_copias = n_pag
        self.idioma_libro = idioma_libro
        self.genero_libro = genero_libro
        self.categoria_libro = categoria_libro