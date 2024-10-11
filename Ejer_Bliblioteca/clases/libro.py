from autor import Autor
class Libro(Autor):
    def __init__(self,isbn, titulo, nombre,id_autor, biografia, año, formato, n_pag, idioma_libro, genero_libro, categoria_libro):
        #Clase padre (autor) y atributos heredados, se aplica herencia simple
        super().__init__(self,id_autor,nombre,biografia)
        self.isbn = isbn #atributo adicional de la clase
        self.titulo = titulo
        self.año = año
        self.formato = formato
        self.n_copias = n_pag
        self.idioma_libro = idioma_libro
        self.genero_libro = genero_libro
        self.categoria_libro = categoria_libro
        