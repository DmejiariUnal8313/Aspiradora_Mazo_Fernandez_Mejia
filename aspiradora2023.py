## documentación
## Daniel Felipe Mejia Rios
## Codigo: 1007233138
## Sistemas Inteligentes Computacionales
## Universidad Nacional de Colombia


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

class Ambiente(object):
    def __init__(self):
        self.localizacion={"A":"1","B":"1"}
        self.localizacion["A"]=random.choice([0,1])
        self.localizacion["B"]=random.choice([0,1])
        print(40*"=")
        print('esta es la inicial ',self.localizacion)

        self.A=turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120,0)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        self.A.end_fill()
        self.A.penup()

        self.B=turtle.Turtle()
        self.B.penup()
        self.B.setpos(120,0)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        self.B.end_fill()
        self.B.penup()

        # Cambio 1: El color de la habitación A es verde si está limpia desde el inicio
        self.A.color("green" if self.localizacion["A"] == 0 else "blue")
        # Cambio 1: El color de la habitación B es verde si está limpia desde el inicio
        self.B.color("green" if self.localizacion["B"] == 0 else "yellow")

class IAspirador(Ambiente):
    def __init__(self,Ambiente):
        # Localización del aspirador, si el salon es A o B
        global localizacionAspirador
        localizacionAspirador=random.choice(["A","B"])
        print(40*"*")
        print("El ambiente esta: ",Ambiente.localizacion)
        
        global Asp
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,0)
        Asp.begin_fill()
        # Cambio 2: La forma de la aspiradora es la tortuga
        Asp.shape("turtle")
        #Asp.turtlesize(5) 
        Asp.color("red") 
        Asp.end_fill()
        Asp.penup()

        # Cambio 5: Se agrega un contador para llevar un registro de las acciones realizadas
        self.contador = 0
        
    def verifica_estado_aspirador(self, Ambiente):
        if localizacionAspirador=="A":
            result1="El aspirador es colocado aleatoriamente en el local A \n"
            Asp.speed(10)
            Asp.setpos(-120,0)
            return print(result1)
        elif localizacionAspirador=="B":
            result2="El aspirador es colocado aleatoriamente en el local B \n"
            Asp.speed(10)
            Asp.setpos(120,0)
            return print(result2)
    
    def verifica_estado_ambiente(self,Ambiente):
        # Si el lado A estuviese sucio
        if Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==0:
            if localizacionAspirador=="B":
                print("El lado B ya esta limpio")
                IAspirador.moverse(self,Ambiente)
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
            else:
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                IAspirador.moverse(self, Ambiente)
                print("El lado B ya esta limpio")
        elif Ambiente.localizacion["A"]==0 and Ambiente.localizacion["B"]==1:
            if localizacionAspirador=="A":
                print("El lado A ya esta limpio")
                IAspirador.moverse(self,Ambiente)
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
            else:
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                IAspirador.moverse(self, Ambiente)
                print("El lado A ya esta limpio")
        elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==1:
            if localizacionAspirador=="A":
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                IAspirador.moverse(self,Ambiente)
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
            else:
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                IAspirador.moverse(self, Ambiente)
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
        else:
            if localizacionAspirador=="A":
                print("El lado A ya esta limpio")
                IAspirador.moverse(self,Ambiente)
                print("El lado B ya esta limpio...")
            else:
                print("El lado B ya esta limpio.")
                IAspirador.moverse(self, Ambiente)
                print("El lado A ya esta limpio")
            print("\n --- Los dos lados estan limpios ---")
    
    def aspiraA(self, Ambiente):
        # Cambio 4: Se agrega un tiempo de espera antes de cambiar el color de la habitación
        sleep(2)
        Ambiente.A.color("green") 
        Ambiente.localizacion["A"]=0
        print("El lado A fue limpiado")
        # Cambio 5: Se incrementa el contador cuando se realiza una acción
        self.contador += 1

    def aspiraB(self,Ambiente):
        # Cambio 4: Se agrega un tiempo de espera antes de cambiar el color de la habitación
        sleep(2)
        Ambiente.B.color("green") 
        Ambiente.localizacion["B"]=0
        print("El lado B fue limpiado")
        # Cambio 5: Se incrementa el contador cuando se realiza una acción
        self.contador += 1

    def moverse(self,Ambiente):
        # Cambio 6: Se verifica si una habitación ya está limpia antes de mover la aspiradora a esa habitación
        if localizacionAspirador=="A":
            print("\nSe mueve para el lado B..\n.")
            IAspirador.localizacionAspirador="B"
            sleep(2.25)
            Asp.forward(120) # Se mueve 120 unidades hacia el lado B (regresa a la posicion inicial)
        elif localizacionAspirador=="B":
            print("\n Se mueve para el lado A...")
            IAspirador.localizacionAspirador="A"
            sleep(2.25)
            Asp.back(120) # Se mueve 120 unidades hacia el lado A (regresa a la posicion inicial)

    # Cambio 3: Se agrega un método para mover la aspiradora al centro después de realizar todas las acciones
    def moverse_al_centro(self):
        Asp.setpos(0,0)

#####   LIMPIAR
ElAmbiente=Ambiente()
ElAspirador=IAspirador(ElAmbiente)
sleep(4)
ElAspirador.verifica_estado_aspirador(ElAmbiente)
sleep(4)
ElAspirador.verifica_estado_ambiente(ElAmbiente)
sleep(4)
ElAspirador.moverse_al_centro()

#### Al terminar muestra los dos lados limpios
print("\nDespues de la accion del  aspirador, el ambiente esta:  ", ElAmbiente.localizacion)
# Cambio 5: Se muestra el puntaje al final
print("Puntaje final: ", ElAspirador.contador)
turtle.done()