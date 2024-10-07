from autor import Autor
class Libro():
    def __init__(self,isbn, titulo, Autor, año, formato, n_pag, idioma_libro, genero_libro, categoria_libro):
        self.isbn = isbn
        self.titulo = titulo
        self.Autor = Autor
        self.año = año
        self.formato = formato
        self.n_copias = n_pag
        self.idioma_libro = idioma_libro
        self.genero_libro = genero_libro
        self.categoria_libro = categoria_libro
        