#comando para ejecutar las pruebas python3 -m unittest test_oop

# Definición de la clase Alumno
class Alumno:
    def __init__(self, nombre, edad):
        # Constructor: inicializa los atributos de la clase
        self.__nombre__ = nombre  # Atributo privado '__nombre__'
        self.__edad__ = edad      # Atributo privado '__edad__'

    def obtener_nombre(self):
        # Método para obtener el nombre del alumno
        return self.__nombre__

    def obtener_edad(self):
        # Método para obtener la edad del alumno
        return self.__edad__


# Definición de la clase Materia
class Materia:
    def __init__(self, nombre, profesores):
        # Constructor: inicializa los atributos de la clase
        self.__nombre__ = nombre            # Atributo privado '__nombre__'
        self.__profesores__ = profesores    # Atributo privado '__profesores__'
        self.__alumnos__ = []               # Lista de alumnos inicialmente vacía

    def obtener_profesores(self):
        # Método para obtener la lista de profesores de la materia
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        # Método para cambiar el nombre de la materia
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        # Método para obtener la lista de alumnos de la materia
        return self.__alumnos__
    
    def agregar_alumno(self, alumno):
        self.__alumnos__.append(alumno)


# Definición de la clase Profesor
class Profesor:
    def __init__(self, nombre, cargo, legajo):
        # Constructor: inicializa los atributos de la clase
        self.__nombre__ = nombre    # Atributo privado '__nombre__'
        self.__cargo__ = cargo      # Atributo privado '__cargo__'
        self.__legajo__ = legajo    # Atributo privado '__legajo__'

    def obtener_nombre(self):
        # Método para obtener el nombre del profesor
        return self.__nombre__

    def obtener_cargo(self):
        # Método para obtener el cargo del profesor
        return self.__cargo__

    def obtener_legajo(self):
        # Método para obtener el legajo del profesor
        return self.__legajo__
