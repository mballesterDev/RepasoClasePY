#Herencia de clases y Super

"""La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, 
compartiendo sus métodos y atributos. Además de ello, una clase hija hereda los atriburos de clase y los puede cambiar,
los métodos LOS HEREDA PERO SI SE ESCRIBE ALGO DE CÓDIGO SE SOBRE ESCRIBE, POR LO TANTO HAY QUE USAR EL SUPER, QUE NOS PERMITE
REHEREDAR EL METODO ORIGINAL Y AÑADIRLE NUEVO CÓDIGO, 
o incluso definir unos nuevos."""

#ejemplo de herencia ne atributos de clase 

class planBasico:
    usuario = "Básico"
    permisos = "5/10"

    def mostrarAtributos(self):
        print()
        print(f"Usuario: {self.usuario}")
        print(f"Permisos: {self.permisos}")


class planPremium(planBasico):
    horasIlimitadas = "ACTIVADAS"

    def mostrarAtributos(self):
        print("")
        print("EL PLAN BÁSICO CONTIENE")
        super().mostrarAtributos() #EL SUPER IMPORTA EL CÓDIGO ANTERIOR SINO LO PUSEIRAMOS SE SOBREESCRIBIRÍA     
        print(f"PERO COMO TIENES EL PREMIUM ADEMAS TIENES LAS HORAS ILIMITADAS {self.horasIlimitadas}")




plan_basico = planBasico()
plan_premium = planPremium()

plan_basico.mostrarAtributos() #el plan Básico contiene dos atributos 
plan_premium.mostrarAtributos() # el plan premium contiene los dos atributos heredados automáticamente(por ser atributos de clase) y 
                                # además uno nuevo