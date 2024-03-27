# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

class Pokemon:
    def __init__(self,nombre,vida,defensa=0,ataque=0,nivel=1):
        self.nombre = nombre
        self.vida=int(vida)
        self.defensa=int(defensa)
        self.ataque=int(ataque)
        self.nivel=int(nivel)
    def reinicio(self):
        self.ataque=0
        self.defensa=0
    def placaje(self):
        self.ataque=100
    def subir_nivel(self):
        self.nivel=self.nivel+1
class Rayo(Pokemon):
    def __init__(self,nombre,vida,defensa=0,ataque=0,nivel=1):
        Pokemon.__init__(self,nombre,vida,defensa,ataque,nivel)
    def mordedura(self):
        self.ataque=50
        self.defensa=25
    def tormenta(self):
        self.ataque=25
        self.defensa=45
    def relampago(self):
        self.ataque=100
        self.defensa=50
    def chispa(self):
        self.ataque=225
        self.defensa=75
    def centella(self):
        self.ataque=250
        self.defensa=100
    def radiacion(self):
        self.ataque=275
        self.defensa=125
    def voltio(self):
        self.ataque=300
        self.defensa=150
    def carga_electrica(self):
        self.ataque = 125
        self.defensa = 175
    def pulso_electrico(self):
        self.ataque = 450
        self.defensa = 200
class Agua(Pokemon):
    def __init__(self,nombre, vida, defensa=0, ataque=0, nivel=1):
        Pokemon.__init__(self, nombre, vida, defensa, ataque, nivel)
    def regeneracion(self):
        self.defensa=50
    def burbujas(self):
        self.ataque=50
        self.defensa = 25
    def ola(self):
        self.ataque = 75
        self.defensa = 45
    def granizo(self):
        self.ataque = 90
        self.defensa = 45
    def lluvia_acida(self):
        self.ataque = 100
        self.defensa = 70
    def congelacion(self):
        self.ataque = 200
        self.defensa = 90
    def torbellino(self):
        self.ataque = 300
        self.defensa = 50
    def maremoto(self):
        self.ataque = 250
        self.defensa = 250
    def ciclon(self):
        self.ataque = 500
        self.defensa = 175
class Fuego(Pokemon):
    def __init__(self, nombre, vida, defensa=0, ataque=0, nivel=1):
        Pokemon.__init__(self, nombre, vida, defensa, ataque, nivel)
    def onda_de_fuego(self):
        self.ataque = 50
        self.defensa = 50
    def furia_vulcana(self):
        self.ataque=80
        self.defensa=50
    def llamas(self):
        self.ataque = 100
        self.defensa = 75
    def fogonazo(self):
        self.ataque = 100
        self.defensa = 100
    def explosion(self):
        self.ataque = 150
        self.defensa = 90
    def lava(self):
        self.ataque = 190
        self.defensa = 130
    def cenizas(self):
        self.ataque = 200
        self.defensa = 160
    def escudo_igneo(self):
        self.ataque = 350
        self.defensa = 450
    def llamarada_solar(self):
        self.ataque = 600
        self.defensa = 300