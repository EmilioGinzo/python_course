# PerroChihuahua
class Perro:
    #atributos
    #nombre
    #raza
    def __init__(self, n, raza, color):
        # parte de encapsulamiento
        self.__nombre = n #private _Perro__nombre
        self._raza = raza #protected
        self.color = color #public

    #getter
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n):
        if n != "firulais2":
            self.__nombre = n
        else:
            print("nombre incorrecto")
        print("SETTER")

    #metodos
    #ladrar
    def ladrar(self):
        print("guau guau " + self.nombre)

    def caminar(self):
        #
        #
        #
        #
        #
        return "caminando"
    

firulais = Perro("firulais", "chihuahua", "cafe") #objeto

firulais.nombre = "firulais2" #setter
firulais.color = "negro" #atributo publico

print(firulais.nombre)