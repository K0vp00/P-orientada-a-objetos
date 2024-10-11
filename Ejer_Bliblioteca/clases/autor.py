class Autor: #clase
    def __init__(self, id_autor, a_nombre, a_apellido, biografia, nacionalidad, fech_nacimiento):
        self._id_autor = id_autor #atributo de la clase con encapsulacion (privada)
        self._a_nombre = a_nombre
        self._a_apellido = a_apellido
        self._biografia = biografia
        self._nacionalidad = nacionalidad
        self._fech_nacimiento = fech_nacimiento