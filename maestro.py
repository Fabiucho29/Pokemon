# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

class Persona:
    def __init__(self,nombre, edad,lugar_de_origen):
        self.nombre=nombre
        self.edad=edad
        self.lugar_de_origen=lugar_de_origen
class Maestro_Pokemon(Persona):
    def __init__(self,nombre,edad,lugar_de_origen,starter):
        Persona.__init__(self,nombre,edad,lugar_de_origen)
        self.starter=starter
    def show(self):
        return f"""Hola, me llamo {self.nombre}, tengo {self.edad} años
y vengo de {self.lugar_de_origen}
Te voy a aplastar"""
class Boss(Persona):
    def __init__(self,nombre,edad,lugar_de_origen,pokemones):
        Persona.__init__(self,nombre,edad,lugar_de_origen)
        self.pokemones=pokemones
    def show(self):
        return f"""Hola, me llamo {self.nombre}, tengo {self.edad} años
y vengo de {self.lugar_de_origen}
No eres rival para mi"""

