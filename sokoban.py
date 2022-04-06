from os import system, name
    

class sokoban1:
#0 - Muñeco
    #1 - Espacio
    #2 - Caja
    #3 - Paredes
    #4 - Metas

    # Controles
    # a - Izquirda
    # d - Derecha
    # w - Arriba
    # s - Abajo

    def __init__(self): # Se coloca un constructor 
        pass    

    muneco_fila =  6   #encuentra la posicion del muñeco
    muneco_columna = 4

    archivo = open('mapa1.txt', mode='r')
    texto = archivo.read()
    archivo.close()



    def clear(self):
        if name == 'nt': #win.
            system ('cls')
        else: 
            system ('clear')

    def imprimirmapa (self):       #imprime mapa 
        for fila in self.texto:     #recorre las filas del mapa 
                                    #recorre cada elemnto de cada fila
            if fila=='3':
                print(chr(129521), end=" ")  #Cambia de valor al 3 (pared)
            elif fila=='1':
                print("  ", end=" ") #imprime un espacio vacio
            elif fila=='0':
                print(chr(128522), end=" ") #cambia de valor al persoaje y lo imprime 
            elif fila=='2':
                print(chr(128230), end= " ")#Cabia de valor a la caja 2  y la imprime
            elif fila=='4':
                print(chr(128681), end=" ")#Cambia de valor a la meta y la imprime 
            elif fila=='5':
                print(chr(128515), end=" ")#Cambia d evalor a personaje_meta 
            elif fila=='6':
                print(chr(127873), end=" ")#Cambia de valor a caja_meta
            else:
                print(fila, end = "")
            

    def moverDerecha(self):
        if self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=5
            self.muneco_fila+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna][self.muneco_fila+1]==2 and self.mapa[self.muneco_columna][self.muneco_fila+2]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna][self.muneco_fila+1]=0
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

    def moverIzquierda(self):
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

    def moverArriba(self):
        if self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==4:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==2 and self.mapa[self.muneco_columna-2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.mapa[self.muneco_columna-2][self.muneco_fila]=2
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==2 and self.mapa[self.muneco_columna-2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.mapa[self.muneco_columna-2][self.muneco_fila]=6
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==6 and self.mapa[self.muneco_columna-2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.mapa[self.muneco_columna-2][self.muneco_fila]=2
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna-1][self.muneco_fila]==4 and self.mapa[self.muneco_columna-2][self.muneco_fila]==6: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.mapa[self.muneco_columna-2][self.muneco_fila]=6
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==4:
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.muneco_columna-=1 
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==2 and self.mapa[self.muneco_columna-2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.mapa[self.muneco_columna-2][self.muneco_fila]=2
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==2 and self.mapa[self.muneco_columna-2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=0
            self.mapa[self.muneco_columna-2][self.muneco_fila]=6
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==6 and self.mapa[self.muneco_columna-2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.mapa[self.muneco_columna-2][self.muneco_fila]=2
            self.muneco_columna-=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna-1][self.muneco_fila]==6 and self.mapa[self.muneco_columna-2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna-1][self.muneco_fila]=5
            self.mapa[self.muneco_columna-2][self.muneco_fila]=6
            self.muneco_columna-=1

    def moverAbajo(self):
        if self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==4:
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==2 and self.mapa[self.muneco_columna+2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.mapa[self.muneco_columna+2][self.muneco_fila]=2
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==2 and self.mapa[self.muneco_columna+2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.mapa[self.muneco_columna+2][self.muneco_fila]=6
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==6 and self.mapa[self.muneco_columna+2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.mapa[self.muneco_columna+2][self.muneco_fila]=2
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==0 and self.mapa[self.muneco_columna+1][self.muneco_fila]==4 and self.mapa[self.muneco_columna+2][self.muneco_fila]==6: 
            self.mapa[self.muneco_columna][self.muneco_fila]=1
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.mapa[self.muneco_columna+2][self.muneco_fila]=6
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==1:
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==4:
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.muneco_columna+=1 
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==2 and self.mapa[self.muneco_columna+2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.mapa[self.muneco_columna+2][self.muneco_fila]=2
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==2 and self.mapa[self.muneco_columna+2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=0
            self.mapa[self.muneco_columna+2][self.muneco_fila]=6
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==6 and self.mapa[self.muneco_columna+2][self.muneco_fila]==1: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.mapa[self.muneco_columna+2][self.muneco_fila]=2
            self.muneco_columna+=1
        elif self.mapa[self.muneco_columna][self.muneco_fila]==5 and self.mapa[self.muneco_columna+1][self.muneco_fila]==6 and self.mapa[self.muneco_columna+2][self.muneco_fila]==4: 
            self.mapa[self.muneco_columna][self.muneco_fila]=4
            self.mapa[self.muneco_columna+1][self.muneco_fila]=5
            self.mapa[self.muneco_columna+2][self.muneco_fila]=6
            self.muneco_columna+=1




juego=sokoban1() #crea el objeto de la clase

while True:              #crea el blucle hasta que se acabe el nivel o se slaga
    juego.clear()
    juego.imprimirmapa()
    
    a=input() #ingresa el movimento
    if a=='d': #lee el moviemnto
        juego.moverDerecha()  #hace el mieviento
    elif a=='a':
        juego.moverIzquierda()   
    elif a=='w':
        juego.moverArriba() 
    elif a=='s':
        juego.moverAbajo()
    if a=='q':
        break

