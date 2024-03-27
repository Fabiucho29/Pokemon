# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

from funciones import inicio, asignar_lugares, juego
import random
from batalla import*

def main():
    maestro_usuario, maestro_amigo = inicio()
    rutas, pueblos, liga = asignar_lugares()
    ubicaciones = [rutas[0], rutas[1], pueblos[0], rutas[2], rutas[3], pueblos[1],
                   rutas[4], rutas[5], pueblos[2], rutas[6], rutas[7], pueblos[3],
                   rutas[8], rutas[9], pueblos[4], rutas[10], rutas[11], pueblos[5],
                   rutas[12], rutas[13], pueblos[6], liga]
    print("Ahora vas a empezar tu aventura")
    print(f"Te toca pelear contra tu compañero, {maestro_amigo.nombre}")
    primer_combate, _ = combate(maestro_usuario, maestro_amigo.starter)
    if primer_combate == True:
        print("Ganaste tu primer combate, ahora a empezar el viaje")
    elif primer_combate == False:
        if isinstance(maestro_usuario.starter, Rayo) == True:
            (maestro_usuario.starter).vida = 500
        if isinstance(maestro_usuario.starter, Agua) == True:
            (maestro_usuario.starter).vida = 700
        if isinstance(maestro_usuario.starter, Fuego) == True:
            (maestro_usuario.starter).vida = 400

        print("Perdiste maestro, pero aprenderas en el camino")

    ubicaciones[0].activo = True

    while True:
        juego(ubicaciones, maestro_usuario, maestro_amigo)


main()