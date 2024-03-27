# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

class Ruta:
    def __init__(self,name,maestro="None",activo=False):
        self.name = name
        self.maestro = maestro
        self.activo = activo
class Pueblo:
    def __init__(self,name,boss,activo=False):
        self.name = name
        self.boss = boss
        self.activo = activo
class Liga:
    def __init__(self,name,boss,activo=False):
        self.name = name
        self.boss = boss
        self.activo = activo
