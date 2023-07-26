class Terrestre():
    def caminar(self):
        print("Caminando...")

    def comer(self):
        print("carne")

class Acuatico():
    def nadar(self):
        print("Nadando...")

    def comer(self):
        print("pescado")

class Cocodrilo(Acuatico, Terrestre):
    def nadar_caminar(self):
        print("Ambos")
        Acuatico.nadar(self)
        Terrestre.caminar(self)

c1 = Cocodrilo()
c1.caminar()
c1.nadar()
c1.nadar_caminar()

c1.comer()

