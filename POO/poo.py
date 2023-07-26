class Mascota:
    def __init__(self, nombre):
        #atributos
        self.nombre = nombre
    
    #metodos
    def hablar(self):
        #
        #
        #
        #
        #
        #
        #
        #
        print("no se que decir")

class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        print("miau miau")

# perro chihuahua
# PerroChihuahua
# class Perro:
#     #atributos
#     #nombre
#     #raza
#     def __init__(self, nombre, raza):
#         self.nombre = nombre
#         self.raza = raza

#     def __del__(self):
#         print("adios")

#     #metodos
#     #ladrar
#     def ladrar(self):
#         print("guau guau " + self.nombre)

#     def caminar(self):
#         #
#         #
#         #
#         #
#         #
#         return "caminando"




# firulais = Perro("firulais", "chihuahua") #objeto

# firulais.ladrar()

# print(firulais.caminar())


michi = Gato("michi")

michi.hablar()