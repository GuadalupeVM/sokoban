from os import system, name
class sokoban1:

    def __init__(self): # Se coloca un constructor 
        pass    
        

    muneco_fila =  6   #encuentra la posicion del muñeco
    muneco_columna = 4

    mapa = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],   #Diseño del mapa del juego 
        [3, 3, 3, 3, 3, 2, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 1, 1, 2, 0, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3 ,3 ,3, 3, 3 ,3, 3, 3, 3],
        [3, 1, 1, 1, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 1, 4 ,4, 3],
        [3, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3],
        [3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 3, 1, 3, 3, 1 ,1 ,4 ,4, 3],
        [3, 3, 3 ,3 ,3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    ]
    
    def clear(self):
        if name == 'nt': #win.
            system ('cls')
        else: 
            system ('clear')
 
    def imprimirmapa (self):       #imprime mapa 
        for fila in self.mapa:
            for columna in fila:   #recorre cada elemnto de cada fila
                if columna==3:
                    print(chr(129521), end=" ")  #Cambia de valor al 3 (pared)
                elif columna==1:
                    print(" ", end="  ") #imprime un espacio vacio
                elif columna==0:
                    print(chr(128522), end=" ") #cambia de valor al persoaje y lo imprime 
                elif columna==2:
                    print(chr(128230), end= " ")#Cabia de valor a la caja 2  y la imprime
                elif columna==4:
                    print(chr(128681), end=" ")#Cambia de valor a la meta y la imprime 
                elif columna==5:
                    print(chr(128515), end=" ")#Cambia d evalor a personaje_meta 
                elif columna==6:
                    print(chr(127873), end=" ")#Cambia de valor a caja_meta
                else:
                    print(columna, end = " ")
            print() 
            
    def moverDerecha(self):     #Funcion para los movimientos de Derecha
        if self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==1: #Personaje, epacio
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==4:  #Personaje, meta
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==2 and self.mapa[self.muneco_columna][self.muneco_fila+2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0  #personaje, caja, meta
            self.mapa[self.muneco_columna][self.muneco_fila+2]=2
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==2 and self.mapa[self.muneco_columna][self.muneco_fila+2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.mapa[self.muneco_columna][self.muneco_fila+2]=6
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==6 and self.mapa[self.muneco_columna][self.muneco_fila+2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.mapa[self.muneco_columna][self.muneco_fila+2]=2
            self.muneco_fila+=1 
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==6 and self.mapa[self.muneco_columna][self.muneco_fila+2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.mapa[self.muneco_columna][self.muneco_fila+2]=6
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==2 and self.mapa[self.muneco_columna][self.muneco_fila+2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.mapa[self.muneco_columna][self.muneco_fila+2]=2
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==2 and self.mapa[self.muneco_columna][self.muneco_fila+2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.mapa[self.muneco_columna][self.muneco_fila+2]=6
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==6 and self.mapa[self.muneco_columna][self.muneco_fila+2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.mapa[self.muneco_columna][self.muneco_fila+2]=2
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila+1]==6 and self.mapa[self.muneco_columna][self.muneco_fila+2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.mapa[self.muneco_columna][self.muneco_fila+2]=6
            self.muneco_fila+=1
            
    def moverIzquierda(self):      #Funcion para mover a izquierda 
        if self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==2 and self.mapa[self.muneco_columna][self.muneco_fila-2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.mapa[self.muneco_columna][self.muneco_fila-2]=2
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==2 and self.mapa[self.muneco_columna][self.muneco_fila-2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.mapa[self.muneco_columna][self.muneco_fila-2]=6
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==6 and self.mapa[self.muneco_columna][self.muneco_fila-2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.mapa[self.muneco_columna][self.muneco_fila-2]=2
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila-1]==6 and self.mapa[self.muneco_columna][self.muneco_fila-2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.mapa[self.muneco_columna][self.muneco_fila-2]=6
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==2 and self.mapa[self.muneco_columna][self.muneco_fila-2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.mapa[self.muneco_columna][self.muneco_fila-2]=2
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==2 and self.mapa[self.muneco_columna][self.muneco_fila-2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=0
            self.mapa[self.muneco_columna][self.muneco_fila-2]=6
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==6 and self.mapa[self.muneco_columna][self.muneco_fila-2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.mapa[self.muneco_columna][self.muneco_fila-2]=2
            self.muneco_fila-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna][self.muneco_fila-1]==6 and self.mapa[self.muneco_columna][self.muneco_fila-2]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna][self.muneco_fila-1]=5
            self.mapa[self.muneco_columna][self.muneco_fila-2]=6
        

juego=sokoban1()
juego.imprimirmapa() 


while True:              #crea el blucle hasta que se acabe el nivel o se slaga
    juego.clear()
    juego.imprimirmapa()
    
    a=input() #ingresa el movimento #lee el mviento 
    if a=='d': #lee el moviemnto
        juego.moverDerecha()  #hace el mieviento
    if a=='q':
        break
