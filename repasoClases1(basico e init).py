
# esta es la sintaxis en phyton NO HAY CORCHETES SOLO INDEXACIÓN Y : DESOUES DE DECLARAR LA CLASE Y LOS MÉTODOS
# PARA CRERA MÉTODOS SE USA DEF Y EL SELF ES OBLIGATORIO SIEMPRE Y SI QUEREMOS CREAR UN METODO SIN PAARMETROS PODEMOS USAR @staticmethod
# EL SELF SIRVE PARA INSTANCIAR 
class Futbolista:
    
    #ARRIBA VAN LOS ATRIBUTOS FIJOS(DE CLASE) (SI SE CREA UN OBJETO A PARTIR DE ESTA CLASE EL OBJETOS LA HEREDARÁ)
    # NO HACE FALTA(NO SE PUEDE) PONER SELF EN LOS ATRIBUTOS DE CLASE PARA PODER INSTANCIARLO YA SON DIRECTAMENTE ISNTANCIABLES
    equipo = "Barcelona"

    def crearJugador (self):
        self.nombre= input("elija el nombre") # aqui es inpresciendible poner self ya que sin self no puede ser instanciado y no lo podemos usar debajo
        self.posicion= input("elija la posición")
        self.goles = input("Cuantos goles ha marcado?")
    def mostrarJugador(self):
        print("")
        print(f"Su nombre es22 {self.nombre}")
        print(f"Su posicion es {self.posicion}")
        print(f"Ha marcado {self.goles} y es del equipo {self.equipo}")

futbolista = Futbolista()
futbolista.crearJugador()
futbolista.mostrarJugador()    

#CREAR UN CONSTRUCTOR RÁPIDO

class Alumno:
    def __init__(self,nombre,curso,notaMedia): #El init nos permite pasar argumentos directamente al crera el objeto 
        self.nombre = nombre
        self.curso = curso
        self.notaMedia = notaMedia
   
    def mostrarAlumno(self):
        print("")
        print(f"El nombre del alumno es {self.nombre}  el curso es {self.curso} y su nota media es {self.notaMedia}")

alumno1 = Alumno("Cristian","Segundo",9.9)
alumno1.mostrarAlumno()
