# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

from maestro import Maestro_Pokemon, Boss
from pokemon import Agua, Rayo, Fuego
from pueblo import Ruta, Pueblo, Liga
import random
from batalla import combate

def inicio():
    starters = [Rayo("Elecwing", 500),
                Agua("Hydroclaw", 700),
                Fuego("Vulcano", 400)]

    maestro_usuario = None
    maestro_amigo = None

    starter_comp_1 = Agua("Sharknado", 200)
    starter_comp_2 = Rayo("Anguilectrico", 200)
    starter_comp_3 = Fuego("Teeth_Kong", 200)

    amigos = [Maestro_Pokemon("Cali", 25, "La Guaira", starter_comp_1),
                  Maestro_Pokemon("Daniela", 20, "Maracaibo", starter_comp_2),
                  Maestro_Pokemon("Samuel", 40, "Falcón", starter_comp_3)]

    while maestro_usuario == None:
        print("Dime tu nombre de maestro pokemon")
        origen = None
        name = input("--> ")
        starter_user = None
        edad = input("Edad: ")
        while origen == None:
            print("""Seleccione su lugar de origen:
--> [1]: La Guaira
--> [2]: Maracaibo
--> [3]: Falcón""")
            opcion = input("--> ")
            if opcion == "1":
                origen = "La Guaira"
                for amigo in amigos:
                    if amigo.lugar_de_origen == "La Guaira":
                        maestro_amigo = amigo
                        break
            elif opcion == "2":
                origen = "Maracaibo"
                for amigo in amigos:
                    if amigo.lugar_de_origen == "Maracaibo":
                        maestro_amigo = amigo
                        break
            elif opcion == "3":
                origen = "Falcón"
                for amigo in amigos:
                    if amigo.lugar_de_origen == "Falcón":
                        maestro_amigo = amigo
                        break
            else:
                print("Escoge una opción válida")

        while starter_user == None:
            print('''Seleccione a tu starter:
[1]-Elecwing(Rayo)----> vida=500
[2]-Hydroclaw(Agua)----> vida=700
[3]-Vulcano(Fuego)----> vida=400
            ''')
            opcion = input("--> ")

            if opcion == "1":
                for i in starters:
                    if isinstance(i, Rayo) == True:
                        starter_user = i
                        break
            elif opcion == "2":
                for i in starters:
                    if isinstance(i, Agua) == True:
                        starter_user = i
                        break
            elif opcion == "3":
                for i in starters:
                    if isinstance(i, Fuego) == True:
                        starter_user = i
                        break
            else:
                print("Escoja una opción válida")

        maestro_usuario = Maestro_Pokemon(name, edad, origen, starter_user)
        print("Hiciste un nuevo compañero")
        print("Será tu amigo durante todo tu viaje")
        print(maestro_amigo.show())

    return maestro_usuario, maestro_amigo
def asignar_lugares():
    pokemones=[Agua("WaterCap",350,nivel=2),
               Fuego("Infernoflame",400,nivel=3),
               Rayo("Voltstrike",350,nivel=2),
               Agua("Wavegazer",550,nivel=3),
               Fuego("Blazeflare",500,nivel=4),
               Rayo("Thunderlash",650,nivel=3),
               Agua("Coralith",800,nivel=4),
               Fuego("Flametide",650,nivel=5),
               Rayo("Elektron",700,nivel=4),
               Agua("Aquashade",950,nivel=5),
               Fuego("Pyroclaww",700,nivel=5),
               Rayo("Thunderflare",750,nivel=5),
               Agua("Seashimmer",1000,nivel=6),
               Fuego("Flarestrake",750,nivel=6),
               Rayo("Sparktail",850,nivel=6)]
    pokemones_bosses=[Agua("Wavestorm",900,nivel=2),
                      Fuego("Incinder",500,nivel=4),
                      Rayo("Lightningbolt",950,nivel=4),
                      Agua("Bubbleray",1200,nivel=5),
                      Fuego("Firestorm",900,nivel=5),
                      Rayo("Thunderstorm",1000,nivel=6),
                      Agua("Torrentide",1300,nivel=7),
                      Fuego("Infernoblaze",1000,nivel=8),
                      Rayo("Shockwing",1150,nivel=9)]
    rivales=[Maestro_Pokemon("Juan",40,"China", pokemones[0]),
             Maestro_Pokemon("Fabiuki", 59, "Japón", pokemones[1]),
             Maestro_Pokemon("Pedrito", 34, "Francia", pokemones[2]),
             Maestro_Pokemon("John", 33, "Italia", pokemones[3]),
             Maestro_Pokemon("Trut", 19, "Inglaterra", pokemones[4]),
             Maestro_Pokemon("Fansh", 22, "Rusia", pokemones[5]),
             Maestro_Pokemon("Bob", 44, "Nigeria", pokemones[6]),
             Maestro_Pokemon("Guagu", 21, "Brasil", pokemones[7]),
             Maestro_Pokemon("SusFim", 67, "Uruguay", pokemones[8]),
             Maestro_Pokemon("Juanmi", 40, "España", pokemones[9]),
             Maestro_Pokemon("Ruth", 21, "Suecia", pokemones[10]),
             Maestro_Pokemon("Carlos", 23, "Argentina", pokemones[11]),
             Maestro_Pokemon("Vito", 22, "Perú", pokemones[12]),
             Maestro_Pokemon("Yut", 87, "Nepal", pokemones[13]),
             Maestro_Pokemon("Trey", 21, "Estados Unidos", pokemones[14])]
    bosses = [Boss("Fito", 20, "Venezuela", [pokemones_bosses[0], pokemones_bosses[1]]),
              Boss("Julio", 46, "Carúpano", [pokemones_bosses[1], pokemones_bosses[2]]),
              Boss("Franco", 100, "Bolivia", [pokemones_bosses[0], pokemones_bosses[3]]),
              Boss("Frank", 35, "Chile", [pokemones_bosses[3], pokemones_bosses[4]]),
              Boss("Jillo",  20, "Espala", [pokemones_bosses[4], pokemones_bosses[5]]),
              Boss("Mariano", 33, "Eslovenia", [pokemones_bosses[5], pokemones_bosses[6]]),
              Boss("Arnaldo", 15, "Caracas", [pokemones_bosses[1], pokemones_bosses[6]])]
    boss_liga = Boss("Mitroglu", 20, "Grecia", [pokemones_bosses[6], pokemones_bosses[7], pokemones_bosses[8]])
    rutas = []
    maestro_control = Maestro_Pokemon("control", 18, "control", pokemones[0])
    pueblos = [Pueblo("Pueblo Rojo", bosses[0]),
               Pueblo("Pueblo Azul", bosses[1]),
               Pueblo("Pueblo Verde", bosses[2]),
               Pueblo("Pueblo Rosa", bosses[3]),
               Pueblo("Pueblo Violeta", bosses[4]),
               Pueblo("Pueblo Marrón", bosses[5]),
               Pueblo("Pueblo Morado", bosses[6])]
    liga = Liga("Liga final", boss_liga)
    for i in range(13):
        aleatorio = random.randrange(1,3)
        if aleatorio == 1:
            rutas.append(Ruta(f"Ruta {i + 1}", rivales[i]))
        if aleatorio == 2:
            rutas.append(Ruta(f"Ruta {i+1}", maestro_control))
    aleatorio = random.randrange(1,3)
    if aleatorio == 1:
        rutas.append(Ruta("Ruta 14", rivales[13]))
    if aleatorio == 2:
        rutas.append(Ruta("Ruta 14", rivales[14]))

    return rutas, pueblos, liga

def juego(ubicaciones, maestro_usuario, maestro_amigo):
    lugar = None
    vida_max = 0
    for i in ubicaciones:
        if i.activo == True:
            lugar = i
            break

    if isinstance(maestro_usuario.starter, Rayo) == True:
        vida_max = 500 + ((maestro_usuario.starter.nivel - 1) * 150) 

    if isinstance(maestro_usuario.starter, Agua) == True:
        vida_max = 700 + ((maestro_usuario.starter.nivel - 1) * 150)

    if isinstance(maestro_usuario.starter, Fuego) == True:
        vida_max = 400 + ((maestro_usuario.starter.nivel - 1) * 150)

    if isinstance(lugar, Ruta) == True:
        print(f"{maestro_usuario.nombre}, bienvenido a la {lugar.name}")
        if lugar.maestro.nombre == "control":
            print(f"""{maestro_amigo.nombre}: {maestro_usuario.nombre}, no hay más enemigos en esta zona
pasemos a la siguiente ubicación""")
            if maestro_usuario.starter.vida < vida_max:
                while True:
                    print(f"""--> [1]: Pasar a la siguiente ubicacion
--> [2]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        lugar.activo = False
                        indice = ubicaciones.index(lugar)
                        ubicaciones[indice + 1].activo = True
                        break
                    if opcion == "2":
                        maestro_usuario.starter.vida = vida_max
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()

            elif maestro_usuario.starter.vida == vida_max:
                print("Ya tienes vida maxima, ahora vamos a pasar a la siguiente ubicacion")
                lugar.activo = False
                indice = ubicaciones.index(lugar)
                ubicaciones[indice + 1].activo = True

        if lugar.maestro.nombre != "control":
            print(lugar.maestro.show())
            pokemon_rival = lugar.maestro.starter
            resultado, vida = combate(maestro_usuario, pokemon_rival)
            if resultado == True:
                lugar.maestro.nombre = "control"
                (maestro_usuario.starter).subir_nivel()
                print("Felicidades, has subido de nivel")
                while True:
                    print(f"""--> [1]: Pasar a la siguiente ubicacion
--> [2]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        lugar.activo = False
                        maestro_usuario.starter.vida = vida
                        indice = ubicaciones.index(lugar)
                        ubicaciones[indice + 1].activo = True
                        break
                    if opcion == "2":
                        maestro_usuario.starter.vida = vida_max + 150
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()

            elif resultado == False:
                print("Perdiste la batalla") 
                while True:
                    print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        maestro_usuario.starter.vida = vida_max
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()


    if isinstance(lugar, Pueblo) == True:
        print(f"{maestro_usuario.nombre}, bienvenido al {lugar.name}")
        if lugar.boss.nombre == "control":
            print(f"""{maestro_amigo.nombre}: {maestro_usuario.nombre}, no hay más enemigos en esta zona
pasemos a la siguiente ubicación""")
            if maestro_usuario.starter.vida < vida_max:
                while True:
                    print(f"""--> [1]: Pasar a la siguiente ubicacion
--> [2]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        lugar.activo = False
                        indice = ubicaciones.index(lugar)
                        ubicaciones[indice + 1].activo = True
                        break
                    if opcion == "2":
                        maestro_usuario.starter.vida = vida_max
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()

            elif maestro_usuario.starter.vida == vida_max:
                print("Ya tienes vida maxima, ahora vamos a pasar a la siguiente ubicacion")
                lugar.activo = False
                indice = ubicaciones.index(lugar)
                ubicaciones[indice + 1].activo = True

        if lugar.boss.nombre != "control":
            print(lugar.boss.show())
            pokemon_rival_1 = lugar.boss.pokemones[0]
            pokemon_rival_2 = lugar.boss.pokemones[1]
            resultado_1, vida_boss_1 = combate(maestro_usuario, pokemon_rival_1)
            if resultado_1 == True:
                print(f"{maestro_amigo.nombre}: Ganamos al primero, ahora seguimos con el segundo")
                maestro_usuario.starter.vida = vida_boss_1
                resultado_2, vida_boss_2 = combate(maestro_usuario, pokemon_rival_2)
                if resultado_2 == True: 
                    lugar.boss.nombre = "control"
                    (maestro_usuario.starter).subir_nivel()
                    print("Felicidades, has subido de nivel")
                    while True:
                        print(f"""--> [1]: Pasar a la siguiente ubicacion
--> [2]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                        opcion = input("--> ")
                        if opcion == "1":
                            lugar.activo = False
                            maestro_usuario.starter.vida = vida_boss_2
                            indice = ubicaciones.index(lugar)
                            ubicaciones[indice + 1].activo = True
                            break
                        if opcion == "2":
                            maestro_usuario.starter.vida = vida_max + 150
                            print("Te sanaste en el pueblo mas cercano")
                            print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                            break
                        if opcion == "0":
                            quit()
                elif resultado_2 == False:
                    print("Perdiste la batalla") 
                    while True:
                        print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                        opcion = input("--> ")
                        if opcion == "1":
                            maestro_usuario.starter.vida = vida_max
                            print("Te sanaste en el pueblo mas cercano")
                            print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                            break
                        if opcion == "0":
                            quit()
            elif resultado_1 == False:
                print("Perdiste la batalla") 
                while True:
                    print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        maestro_usuario.starter.vida = vida_max
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()

    if isinstance(lugar, Liga) == True:
        print(f"{maestro_usuario.nombre}, bienvenido a la Liga Final")
        print("Aqui se vera de que estas hecho")
        print("Soy Mitroglu, el dios de los Pokemones")
        print("Voy a ser tu peor pesadilla")
        pokemon_rival_1 = lugar.boss.pokemones[0]
        pokemon_rival_2 = lugar.boss.pokemones[1]
        pokemon_rival_3 = lugar.boss.pokemones[2]
        resultado_1, vida_boss_1 = combate(maestro_usuario, pokemon_rival_1)
        if resultado_1 == True:
            print(f"{maestro_amigo.nombre}: Ganamos al primero, ahora seguimos con el segundo")
            maestro_usuario.starter.vida = vida_boss_1
            resultado_2, vida_boss_2 = combate(maestro_usuario, pokemon_rival_2)
            if resultado_2 == True: 
                print(f"{maestro_amigo.nombre}: Ganamos al segundo, ahora seguimos con el tercero")
                maestro_usuario.starter.vida = vida_boss_2
                resultado_3, vida_boss_3 = combate(maestro_usuario, pokemon_rival_3)
                if resultado_3 == True:
                    print(f"{maestro_amigo.nombre}: Hemos ganado")
                    print(f"{maestro_usuario.nombre}, ahora eres el lider de la Liga")
                    print("Felicidades por ser el Gran Maestro Pokemon")
                    quit()
                elif resultado_3 == False:
                    print("Perdiste la batalla") 
                    while True:
                        print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                        opcion = input("--> ")
                        if opcion == "1":
                            maestro_usuario.starter.vida = vida_max
                            print("Te sanaste en el pueblo mas cercano")
                            print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                            break
                        if opcion == "0":
                            quit()
            elif resultado_2 == False:
                print("Perdiste la batalla") 
                while True:
                    print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                    opcion = input("--> ")
                    if opcion == "1":
                        maestro_usuario.starter.vida = vida_max
                        print("Te sanaste en el pueblo mas cercano")
                        print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                        break
                    if opcion == "0":
                        quit()
        elif resultado_1 == False:
            print("Perdiste la batalla") 
            while True:
                print(f"""--> [1]: Regresarte al pueblo mas cercano y sanarte
--> [0]: Salir del juego""")
                opcion = input("--> ")
                if opcion == "1":
                    maestro_usuario.starter.vida = vida_max
                    print("Te sanaste en el pueblo mas cercano")
                    print(f"{maestro_amigo.nombre}: Ahora vamos a volver donde nos quedamos")
                    break
                if opcion == "0":
                    quit()