# Fabio Carrozza y Arnaldo Vallerugo
# Cedula: 30714977; 30906842

from funciones import *
import random
def combate(maestro,rival):
    oponente=rival
    pokemon=maestro.starter
    vida=pokemon.vida
    vida_oponente=oponente.vida
    while vida>0 and vida_oponente>0:
        pokemon.reinicio()
        oponente.reinicio()
        print(f'''
    {pokemon.nombre} - Salud={vida}
    {rival.nombre} - Salud_Oponente={vida_oponente}
    ''')
        if isinstance(pokemon,Rayo) == True:
            print('''Seleciona el ataque a ejecutar:
[1]-Placaje daño=100/defensa=0
[2]-Mordedura daño=50/defensa=25
[3]-Tormenta daño=25/defensa=45
[4]-Relampago daño=100/defensa=50 (Nivel-2)
[5]-Chispa daño=225/defensa=75 (Nivel-3)
[6]-Centella daño=250/defensa=100 (Nivel-4)
[7]-Radiación daño=275/defensa=125 (Nivel-5)
[8]-Voltio daño=300/defensa=150 (Nivel-6)
[9]-Carga_eléctrica daño=125/defensa=175 (Nivel-7)
[10]-Pulso_eléctrico daño=450/defensa=200 (Nivel-8)
            ''')
            i= input("----> ")
            if i =="1":
                pokemon.placaje()
            elif i=="2":
                pokemon.mordedura()
            elif i=="3":
                pokemon.tormenta()
            elif i == "4":
                if pokemon.nivel > 1:
                    pokemon.relampago()
                else:
                    print(f"Necesitas ser mínimo nivel 2, eres {pokemon.nivel}")
                    continue
            elif i=="5":
                if pokemon.nivel > 2:
                    pokemon.chispa()
                else:
                    print(f"Necesitas ser mínimo nivel 3, eres {pokemon.nivel}")
                    continue
            elif i=="6":
                if pokemon.nivel > 3:
                    pokemon.centella()
                else:
                    print(f"Necesitas ser mínimo nivel 4, eres {pokemon.nivel}")
                    continue
            elif i=="7":
                if pokemon.nivel > 4:
                    pokemon.radiacion()
                else:
                    print(f"Necesitas ser mínimo nivel 5, eres {pokemon.nivel}")
                    continue
            elif i=="8":
                if pokemon.nivel > 5:
                    pokemon.voltio()
                else:
                    print(f"Necesitas ser mínimo nivel 6, eres {pokemon.nivel}")
                    continue
            elif i=="9":
                if pokemon.nivel > 6:
                    pokemon.carga_electrica()
                else:
                    print(f"Necesitas ser mínimo nivel 7, eres {pokemon.nivel}")
                    continue
            elif i=="10":
                if pokemon.nivel > 7:
                    pokemon.pulso_electrico()
                else:
                    print(f"Necesitas ser mínimo nivel 8, eres {pokemon.nivel}")
                    continue
        elif isinstance(pokemon,Agua):
            print('''Seleciona el ataque a ejecutar:
[1]-Placaje daño=100/defensa=0
[2]-Regeneracion daño=0/defensa=50
[3]-Burbujas daño=50/defensa=25
[4]-Ola daño=75/defensa=45 (Nivel-2)
[5]-Granizo daño=90/defensa=45 (Nivel-3)
[6]-Lluvia_ácida daño=100/defensa=70 (Nivel-4)
[7]-Congelación daño=200/defensa=90 (Nivel-5)
[8]-Torbellino daño=300/defensa=50 (Nivel-6)
[9]-Maremoto daño=250/defensa=250 (Nivel-7)
[10]-Ciclon daño=500/defensa=175 (Nivel-8)
            ''')
            i= input("----> ")
            if i =="1":
                pokemon.placaje()
            elif i=="2":
                pokemon.regeneracion()
            elif i=="3":
                pokemon.burbujas()
            elif i == "4":
                if pokemon.nivel > 1:
                    pokemon.ola()
                else:
                    print(f"Necesitas ser mínimo nivel 2, eres {pokemon.nivel}")
                    continue
            elif i=="5":
                if pokemon.nivel > 2:
                    pokemon.granizo()
                else:
                    print(f"Necesitas ser mínimo nivel 3, eres {pokemon.nivel}")
                    continue
            elif i=="6":
                if pokemon.nivel > 3:
                    pokemon.lluvia_acida()
                else:
                    print(f"Necesitas ser mínimo nivel 4, eres {pokemon.nivel}")
                    continue
            elif i=="7":
                if pokemon.nivel > 4:
                    pokemon.congelacion()
                else:
                    print(f"Necesitas ser mínimo nivel 5, eres {pokemon.nivel}")
                    continue
            elif i=="8":
                if pokemon.nivel > 5:
                    pokemon.torbellino()
                else:
                    print(f"Necesitas ser mínimo nivel 6, eres {pokemon.nivel}")
                    continue
            elif i=="9":
                if pokemon.nivel > 6:
                    pokemon.maremoto()
                else:
                    print(f"Necesitas ser mínimo nivel 7, eres {pokemon.nivel}")
                    continue
            elif i=="10":
                if pokemon.nivel > 7:
                    pokemon.ciclon()
                else:
                    print(f"Necesitas ser mínimo nivel 8, eres {pokemon.nivel}")
                    continue
        elif isinstance(pokemon,Fuego):
            print('''Seleciona el ataque a ejecutar:
[1]-Placaje daño=100/defensa=0
[2]-Furia Vulcana daño=50/defensa=50
[3]-Onda de fuego daño=80/defensa=50
[4]-Llamas daño=100/defensa=75 (Nivel - 2)
[5]-Fogonazo daño=100/defensa=100 (Nivel - 3)
[6]-Explosion daño=150/defensa=90 (Nivel - 4)
[7]-Lava daño=190/defensa=130 (Nivel - 5)
[8]-Ceniza daño=200/defensa=160 (Nivel - 6)
[9]-Escudo ígneo daño=350/defensa=450 (Nivel - 7)
[10]-Llamarada solar daño=600/defensa=300 (Nivel - 8)
            ''')
            i = input("----> ")
            if i == "1":
                pokemon.placaje()
            elif i == "2":
                pokemon.furia_vulcana()
            elif i == "3":
                pokemon.onda_de_fuego()
            elif i == "4":
                if pokemon.nivel > 1:
                    pokemon.llamas()
                else:
                    print(f"Necesitas ser mínimo nivel 2, eres {pokemon.nivel}")
                    continue
            elif i == "5":
                if pokemon.nivel > 2:
                    pokemon.fogonazo()
                else:
                    print(f"Necesitas ser mínimo nivel 3, eres {pokemon.nivel}")
                    continue
            elif i == "6":
                if pokemon.nivel > 3:
                    pokemon.explosion()
                else:
                    print(f"Necesitas ser mínimo nivel 4, eres {pokemon.nivel}")
                    continue
            elif i == "7":
                if pokemon.nivel > 4:
                    pokemon.lava()
                else:
                    print(f"Necesitas ser mínimo nivel 5, eres {pokemon.nivel}")
                    continue
            elif i == "8":
                if pokemon.nivel > 5:
                    pokemon.cenizas()
                else:
                    print(f"Necesitas ser mínimo nivel 6, eres {pokemon.nivel}")
                    continue
            elif i == "9":
                if pokemon.nivel > 6:
                    pokemon.escudo_igneo()
                else:
                    print(f"Necesitas ser mínimo nivel 7, eres {pokemon.nivel}")
                    continue
            elif i == "10":
                if pokemon.nivel > 7:
                    pokemon.llamarada_solar()
                else:
                    print(f"Necesitas ser mínimo nivel 8, eres {pokemon.nivel}")
                    continue
        
        if oponente.nivel == 1:
            aleatorio = random.randrange(1,4)
        if oponente.nivel == 2:
            aleatorio = random.randrange(1,5)
        if oponente.nivel == 3:
            aleatorio = random.randrange(1,6)
        if oponente.nivel == 4:
            aleatorio = random.randrange(1,7)
        if oponente.nivel == 5:
            aleatorio = random.randrange(3,8)
        if oponente.nivel == 6:
            aleatorio = random.randrange(4,9)
        if oponente.nivel == 7:
            aleatorio = random.randrange(5,10)
        if oponente.nivel > 7:
            aleatorio = random.randrange(7,11)

        if isinstance(oponente, Rayo) == True:
            if aleatorio == 1:
                oponente.placaje()
                print("Te ataco con placaje")
            elif aleatorio == 2:
                oponente.mordedura()
                print("Te ataco con mordedura")
            elif aleatorio == 3:
                oponente.tormenta()
                print("Te ataco con tormenta")
            elif aleatorio == 4:
                oponente.relampago()
                print("Te ataco con relámpago")
            elif aleatorio == 5:
                oponente.chispa()
                print("Te ataco con chispa")
            elif aleatorio == 6:
                oponente.centella()
                print("Te ataco con centella")
            elif aleatorio == 7:
                oponente.radiacion()
                print("Te ataco con radiación")
            elif aleatorio == 8:
                oponente.voltio()
                print("Te ataco con voltio")
            elif aleatorio == 9:
                oponente.carga_electrica()
                print("Te ataco con carga eléctrica")
            elif aleatorio == 10:
                oponente.pulso_electrico()
                print("Te ataco con pulso eléctrico")
               
        elif isinstance(oponente, Agua):
            if  aleatorio == 1:
                oponente.placaje()
                print("Te ataco con placaje")
            elif aleatorio == 2:
                oponente.regeneracion()
                print("Me regenero")
            elif aleatorio == 3:
                oponente.burbujas()
                print("Te ataco con burbujas")
            elif aleatorio == 4:              
                oponente.ola()
                print("Te ataco con ola")
            elif aleatorio == 5:                
                oponente.granizo()
                print("Te ataco con granizo")
            elif aleatorio == 6:
                oponente.lluvia_acida()
                print("Te ataco con lluvia ácida")
            elif aleatorio == 7:
                oponente.congelacion()
                print("Te ataco con congelación")
            elif aleatorio == 8:
                oponente.torbellino()
                print("Te ataco con torbellino")
            elif aleatorio == 9:                
                oponente.maremoto()
                print("Te ataco con maremoto")
            elif aleatorio == 10:           
                oponente.ciclon()
                print("Te ataco con ciclón")

        elif isinstance(oponente, Fuego):
            if aleatorio == 1:
                oponente.placaje()
                print("Te ataco con placaje")
            elif aleatorio == 2:
                oponente.furia_vulcana()
                print("Te ataco con furia vulcana")
            elif aleatorio == 3:
                oponente.onda_de_fuego()
                print("Te ataco con onda de fuego")
            elif aleatorio == 4:
                oponente.llamas()
                print("Te ataco con llamas")
            elif aleatorio == 5:
                oponente.fogonazo()
                print("Te ataco con fogonazo")
            elif aleatorio == 6:
                oponente.explosion()
                print("Te ataco con explosión")
            elif aleatorio == 7:
                oponente.lava()
                print("Te ataco con lava")
            elif aleatorio == 8:
                oponente.cenizas()
                print("Te ataco con cenizas")
            elif aleatorio == 9:
                oponente.escudo_igneo()
                print("Te ataco con escudo ígneo")
            elif aleatorio == 10:
                oponente.llamarada_solar()
                print("Te ataco con llamarada solar")

        vida_restar=oponente.ataque-pokemon.defensa
        if vida_restar>0:
            vida=vida-vida_restar
        vida_oponente_restar=pokemon.ataque-oponente.defensa
        if vida_oponente_restar>0:
            vida_oponente=vida_oponente-vida_oponente_restar


    if vida_oponente <= 0:
        print("Felicidades maestro, ganaste la batalla")
        return True, vida
    
    elif vida <= 0 and vida_oponente > 0:
        print("Perdiste, vuelve a intentarlo")
        return False, vida