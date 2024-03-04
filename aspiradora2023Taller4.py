
#%% Dependences
import random
import turtle
from time import sleep

#%% Variables
global t1,t2,t3,t4
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()

#%%main
t1.penup()
t1.begin_fill()
t1.setpos(-140,60)
t1.write("Lado A", align="center",font=("Arial",15,"normal"))
t1.end_fill()
t1.penup()

t2.penup()
t2.begin_fill()
t2.setpos(140,60)
t2.write("Lado B", align="center",font=("Arial",15,"normal"))
t2.end_fill()
t2.penup()

t3.penup()
t3.begin_fill()
t3.setpos(-140, -120)
t3.write("Lado C", align="center",font=("Arial",15,"normal"))
t3.end_fill()
t3.penup()

t4.penup()
t4.begin_fill()
t4.setpos(140, -120)
t4.write("Lado D", align="center",font=("Arial",15,"normal"))
t4.end_fill()
t4.penup()

class Ambiente(object):
    def __init__(self):
        self.cont = 0
    # Estado limpio: 0   Estado Sucio: 1
    # Condic iniciales (Sucio, Sucio) ---- Aleatorio 
        self.localizacion={"A":"1","B":"1","C":"1","D":"1"}
    # Las condiciones de la localizacion inicial son aleatorias
        self.localizacion["A"]=random.choice([0,1])
        self.localizacion["B"]=random.choice([0,1])
        self.localizacion["C"]=random.choice([0,1])
        self.localizacion["D"]=random.choice([0,1])
        print(40*"=")
        print('esta es la inicial ',self.localizacion)

        self.A=turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120,0)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        self.A.color("blue")
        self.A.end_fill()
        self.A.penup()

        self.B=turtle.Turtle()
        self.B.penup()
        self.B.setpos(120,0)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        self.B.color("brown")
        self.B.end_fill()
        self.B.penup()

        self.C=turtle.Turtle()
        self.C.penup()
        self.C.setpos(120, -200)
        self.C.begin_fill()
        self.C.shape("square")
        self.C.turtlesize(5)
        self.C.color("purple")
        self.C.end_fill()
        self.C.penup()

        self.D=turtle.Turtle()
        self.D.penup()
        self.D.setpos(-120, -200)
        self.D.begin_fill()
        self.D.shape("square")
        self.D.turtlesize(5)
        self.D.color("yellow")
        self.D.end_fill()
        self.D.penup()


class IAspirador(Ambiente):
    def __init__(self,Ambiente):
        # Localización del aspirador, si el salon es A o B
        global localizacionAspirador

        if Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["C"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.A.color("green")
            Ambiente.B.color("green")
            Ambiente.C.color("green")
            Ambiente.D.color("green")

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["C"] == 0:
            Ambiente.A.color("green")
            Ambiente.B.color("green")
            Ambiente.C.color("green")

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.A.color("green")
            Ambiente.B.color("green")
            Ambiente.D.color("green")

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["C"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.A.color("green")
            Ambiente.C.color("green")
            Ambiente.D.color("green")

        elif Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["C"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.B.color("green")
            Ambiente.C.color("green")
            Ambiente.D.color("green")

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["B"] == 0:
            Ambiente.A.color("green")
            Ambiente.B.color("green")
            # Puedes agregar el código correspondiente aquí

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["C"] == 0:
            Ambiente.A.color("green")
            Ambiente.C.color("green")
            # Puedes agregar el código correspondiente aquí

        elif Ambiente.localizacion["A"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.A.color("green")
            Ambiente.D.color("green")
            # Puedes agregar el código correspondiente aquí

        elif Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["C"] == 0:
            Ambiente.B.color("green")
            Ambiente.C.color("green")
            # Puedes agregar el código correspondiente aquí

        elif Ambiente.localizacion["B"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.B.color("green")
            Ambiente.D.color("green")
            # Puedes agregar el código correspondiente aquí

        elif Ambiente.localizacion["C"] == 0 and Ambiente.localizacion["D"] == 0:
            Ambiente.C.color("green")
            Ambiente.D.color("green")

        
        
        localizacionAspirador=random.choice(["A","B","C","D"])
        
        print(40*"*")
        print("El ambiente esta: ",Ambiente.localizacion)
        
        

        global Asp
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,0)
        Asp.begin_fill()
        Asp.shape("circle")
        #Asp.turtlesize(5)
        Asp.color("red")
        Asp.end_fill()
        Asp.penup()

    def verifica_estado_aspirador(self, Ambiente):
        if localizacionAspirador=="A" and Ambiente.localizacion["A"]==1:
            result1="El aspirador es colocado en el local A \n"
            Ambiente.cont +=1
            Asp.speed(10)
            Asp.setpos(-120,0)
            return print(result1)
        elif localizacionAspirador=="B" and Ambiente.localizacion["B"]==1:
            result2="El aspirador es colocado en el local B \n"
            Ambiente.cont +=1
            Asp.speed(10)
            Asp.setpos(120,0)
            return print(result2)
        elif localizacionAspirador=="A" and Ambiente.localizacion["A"]==0:
            result1="El lado A ya se encuentra limpio, por ende la aspiradora no se mueve \n"
            Ambiente.cont +=1
            Asp.speed(10)
            Asp.setpos(0,0)
            return print(result1)
        
        elif (localizacionAspirador=="A" or localizacionAspirador=="B") or (Ambiente.localizacion["A"]==0 and Ambiente.localizacion["B"]==0):
            result1="Los dos lados ya se encuentran limpios, la aspiradora no se mueve \n"
            Ambiente.cont +=1
            Asp.speed(10)
            Asp.setpos(0,0)
            return print(result1)
        else:
            result2="El lado B ya se encuentra limpio, por ende la aspiradora no se mueve \n"
            Ambiente.cont +=1
            Asp.speed(10)
            Asp.setpos(0,0)
            return print(result2)
    
    def verifica_estado_ambiente(self,Ambiente):
        # Si el lado A estuviese sucio
        if Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==0:
                Ambiente.cont +=1
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)

        elif Ambiente.localizacion["A"]==0 and Ambiente.localizacion["B"]==1:
                Ambiente.cont +=1
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                # IAspirador.moverse(self, Ambiente)
                # print("El lado A ya esta limpio")
        elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==1:
            if localizacionAspirador=="A":
                Ambiente.cont +=1
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                IAspirador.moverse(self,Ambiente)
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
            else:
                Ambiente.cont +=1
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                IAspirador.moverse(self, Ambiente)
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
        else:
            Ambiente.cont = 0
            print("\n --- Los dos lados ya se encontraban limpios ---")
    
    def aspiraA(self, Ambiente):
        Ambiente.cont +=1
        Ambiente.A.color("green")
        Ambiente.localizacion["A"]=0
        Asp.setpos(-120,0)
        print("El lado A fue limpiado")
    
    def aspiraB(self,Ambiente):
        Ambiente.cont +=1
        Ambiente.B.color("green")
        Ambiente.localizacion["B"]=0
        Asp.setpos(120,0)
        print("El lado B fue limpiado")

    def moverse(self,Ambiente):
        if localizacionAspirador=="A":
            Ambiente.cont +=1
            print("\nSe mueve para el lado B..\n.")
            IAspirador.localizacionAspirador="B"
            sleep(2.25)
            Asp.setpos(120,0)
        else:
            Ambiente.cont +=1
            print("\n Se mueve para el lado A...")
            IAspirador.localizacionAspirador="A"
            sleep(2.25)
            Asp.setpos(-120,0)

    def posInic(self, Ambiente):
        Ambiente.cont +=1
        Asp.setpos(0,0)
        print(f"La cantidad de pasos realizados fue de: {Ambiente.cont}")


#####   LIMPIAR
ElAmbiente=Ambiente()
ElAspirador=IAspirador(ElAmbiente)
sleep(3)
ElAspirador.verifica_estado_aspirador(ElAmbiente)
sleep(3)
ElAspirador.verifica_estado_ambiente(ElAmbiente)
sleep(3)
ElAspirador.posInic(ElAmbiente)
sleep(3)


#### Al terminar muestra los dos lados limpios
print("\nDespues de la accion del  aspirador, el ambiente esta:  ", ElAmbiente.localizacion,"\nY la aspiradora vuelve al centro.")
turtle.done()
#quit()