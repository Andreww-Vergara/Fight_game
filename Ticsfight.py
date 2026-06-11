import random
import os
class Tico():#clase es molde
    def __init__(self,name,edad,poder,fuerza,agilidad,defensa,olor):#atributos
        self.name=name
        self.edad=edad
        self.poder=poder
        self.fuerza=fuerza
        self.agilidad=agilidad
        self.defensa=defensa
        self.olor=olor#se guardan en valores locales de la funcion
        self.vida=100
        self.carga=0#valores ya predefinidos
    def ataque(self):
        if self.carga>40:
           self.carga=0
           suma=random.randint(int(self.olor/2),self.olor)#valor aleatorio entre los 2 valores
           print(self.name," uso bomba fetida, poder: ",suma)#poder especial
        else:
            pod=random.randint(0,int(self.poder/2))
            fuer=random.randint(0,int(self.fuerza/2))#valores aleatorios que suman el ataque
            suma=pod+fuer#ataque
            print(self.name," esta atacando con un poder de",suma)
        input("")
        return suma#se manda el chingadazo
    def defending(self,valor):
        defen=random.randint(0,int(self.defensa/2))
        agil=random.randint(0,int(self.agilidad/2))
        suma=defen+agil#este valor contraresta el ataque
        print(" poder de defensa de: ",self.name,suma)
        suma=suma-valor
        if suma<0:
            print("dano infligido: ",suma)#si la defensa no fue suficiente
            self.vida=self.vida+suma
            self.carga=self.carga-suma
        else:
            print(" ataque esquivado ")
        if self.vida<0:self.vida=0#la defensa si fue suficiente       
    def presentacion(self,modo):
        print("Jugador: ",self.name,"  . vida: ",self.vida,)
        print("")
        if modo=="ataca":#modo es valor local
            print("poder: ",self.poder,"  . fuerza: ",self.fuerza)
        elif modo=="defiende":
            print("defensa: ",self.defensa,"  . agilidad: ",self.agilidad)
        print("")#mostramos las características con las que combaten los players
        print("")

def pvp(j1,j2):#funcion de los madrazos
    while(True):
        os.system('cls')
        print(f" Solo hoy : {j1.name} vs. {j2.name}")
        print("")
        print("")
        j1.presentacion("ataca")
        j2.presentacion("defiende")#no es lo mismo atacar que defender
        j2.defending(j1.ataque())
        input("")
        if j2.vida==0:
            print(f" {j2.name} Defeated, Rip")#se acabo el nivel de vida del player
            input("")
            break
        input("")
        os.system('cls')
        print(f" Solo hoy : {j2.name} vs. {j1.name}")
        print("")
        print("")
        j2.presentacion("ataca")
        j1.presentacion("defiende")
        j1.defending(j2.ataque())#es el turno del otro jugador
        input("")
        if j1.vida==0:
            print(f" {j1.name} Defeated, Rip")
            input("")
            break
        input("")

Cony=Tico("Cony",20,42,50,67,30,2)
Albert=Tico("Alberto",26,70,65,30,59,30)
Leonard=Tico("Daniel",21,100,100,100,1,100)
Apu=Tico("Apu",24,58,34,80,27,100)
Erwin=Tico("Erwin",40,65,82,17,83,80)
Lalo=Tico("Lalo",30,90,68,40,100,25)
Max=Tico("Max",28,72,83,54,74,15)
Zuazzzo=Tico("Zuazzzo",32,75,98,40,90,85)
Cris=Tico("Cris",35,85,75,40,91,82)#ticos de muestra, objetos a escoger

while True:
    print("SELECT YOUR PLAYERS")
    print(f"1. Hola soy {Cony.name}, y tengo {Cony.edad}")
    print(f"2. Hola soy {Albert.name}, y tengo {Albert.edad}")
    print(f"3. Hola soy {Leonard.name}, y tengo {Leonard.edad}")
    print(f"4. Hola soy {Apu.name}, y tengo {Apu.edad}")
    print(f"5. Hola soy {Erwin.name}, y tengo {Erwin.edad}")
    print(f"6. Hola soy {Lalo.name}, y tengo {Lalo.edad}")
    print(f"7. Hola soy {Max.name}, y tengo {Max.edad}")
    print(f"8. Hola soy {Zuazzzo.name}, y tengo {Zuazzzo.edad}")
    print(f"9. Hola soy {Cris.name}, y tengo {Cris.edad}")
    player1=int(input("FIRST..."))#selecciona primer jugador
    if player1==1:
        pl1=Cony
    elif player1==2:
        pl1=Albert
    elif player1==3:
        pl1=Leonard
    elif player1==4:
        pl1=Apu
    elif player1==5:
        pl1=Erwin
    elif player1==6:
        pl1=Lalo
    elif player1==7:
        pl1=Max
    elif player1==8:
        pl1=Zuazzzo
    elif player1==9:
        pl1=Cris
    else: 
        print("Invalid player")
        input("Continue...")
        continue
    player2=int(input("VS..."))#selecciona segundo jugador
    if player2==1:
        pl2=Cony
    elif player2==2:
        pl2=Albert
    elif player2==3:
        pl2=Leonard
    elif player2==4:
        pl2=Apu
    elif player2==5:
        pl2=Erwin
    elif player2==6:
        pl2=Lalo
    elif player2==7:
        pl2=Max
    elif player2==8:
        pl2=Zuazzzo
    elif player2==9:
        pl2=Cris
    else: 
        print("Invalid player")
        input("Continue...")
        continue
    pvp(pl1,pl2)
    print("CONTINUE?...")
    print("1. YES")
    print("2. NO")
    yes=int(input("..."))
    if yes==1:
        continue
    elif yes==2:
        break
    else:
        print("Invalid input.")
print("SEE YOU NEXT TIME!")