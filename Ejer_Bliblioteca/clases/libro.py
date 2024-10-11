from autor import Autor
class Libro(Autor):
    def __init__(self,isbn, titulo, nombre,id_autor, biografia, año, formato, n_pag, idioma_libro, genero_libro, categoria_libro):
        #Clase padre (autor) y atributos heredados, se aplica herencia simple
        super().__init__(self,id_autor,nombre,biografia)
        self._isbn = isbn #atributo adicional encapsulacion (privada) solo contiene un _ en cambio __ seria muy privada y no nos dejaria manipular o heredar el atributo
        self._titulo = titulo
        self._año = año
        self._formato = formato
        self._n_copias = n_pag
        self._idioma_libro = idioma_libro
        self._genero_libro = genero_libro
        self._categoria_libro = categoria_libro
        