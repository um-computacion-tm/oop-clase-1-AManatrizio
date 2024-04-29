import unittest
from oop import Alumno, Materia, Profesor  # Importa las clases que necesitas probar desde el módulo oop


class TestOOP(unittest.TestCase):
    def test_alumno(self):
        """
        Pruebas para la clase Alumno.
        """
        # Crea una instancia de Alumno con valores específicos
        nombre = "Juan"
        edad = 20
        alumno = Alumno(nombre, edad)

        # Verifica si los atributos se inicializan correctamente
        self.assertEqual(alumno.obtener_nombre(), nombre)  # Verifica que el nombre sea el esperado
        self.assertEqual(alumno.obtener_edad(), edad)      # Verifica que la edad sea la esperada


    def test_materia(self):
        """
        Pruebas para la clase Materia.
        """
       # Crea una instancia de Materia con valores específicos
        nombre_materia = "Matemáticas"
        profesores = ["Juan", "María"]
        materia = Materia(nombre_materia, profesores)

        # Verifica si los atributos se inicializan correctamente
        self.assertEqual(materia.__nombre__, nombre_materia)  # Verifica que el nombre sea el esperado
        self.assertEqual(materia.__profesores__, profesores)  # Verifica que los profesores sean los esperados
        self.assertEqual(materia.__alumnos__, [])            # Verifica que la lista de alumnos esté vacía al inicio

        # Agrega un alumno a la materia y verifica si se agrega correctamente
        alumno = Alumno("Pedro", 22)
        materia.agregar_alumno(alumno)
        self.assertIn(alumno, materia.obtener_alumnos())      # Verifica que el alumno esté en la lista de alumnos



    def test_profesor(self):
        """
        Pruebas para la clase Profesor.
        """
        # Crea una instancia de Profesor con valores específicos
        nombre = "Juan"
        cargo = "Profesor de Matemáticas"
        legajo = "1234"
        profesor = Profesor(nombre, cargo, legajo)

        # Verifica si los atributos se inicializan correctamente
        self.assertEqual(profesor.__nombre__, nombre)    # Verifica que el nombre sea el esperado
        self.assertEqual(profesor.__cargo__, cargo)      # Verifica que el cargo sea el esperado
        self.assertEqual(profesor.__legajo__, legajo)    # Verifica que el legajo sea el esperado






if __name__ == '__main__':
    unittest.main()
