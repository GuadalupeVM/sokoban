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

    def imprimirmapa (self):       #imprime mapa 
        for fila in self.mapa:
            print(fila)#recorre las filas del mapa  
              

juego=sokoban1()
juego.imprimirmapa() 