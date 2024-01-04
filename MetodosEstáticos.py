# self sirve para poder instanciar parametrosy es obligatorio por defecto(aunque no requeramos parametros)
# si no queremos usar parametros podemos poner la etiqueta @staticmethod
# los métodos staticos son aquellos que no reciben parámetros


class Alumno:
    nombre = "Manel"
    edad = "16"
    notaNedia = 7.7

    @staticmethod
    def saludo():
        print("Hola que tal soy un alumno")

alumno001 = Alumno()

alumno001.saludo()