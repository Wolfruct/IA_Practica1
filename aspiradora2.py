import numpy as np
import time

class aspiradora:
    def __init__(self):
        self.coordenadas = [0,0]
        self.valor_actual_celda = 0
        self.movimientos = {0: [1/4,-1],1: [1/4,-1],2: [1/4,1],3: [1/4,1]}
        self.borde = False

    def eleccion(self):
        opcion = np.random.choice([0,1,2,3],p = [self.movimientos[0][0],self.movimientos[1][0],self.movimientos[2][0],self.movimientos[3][0]],size=(1))
        return opcion
 
    def cambiar_probabilidad(self,tipo_mov,tipo_mov2 = -1):
        prob = 1/3
        self.movimientos[tipo_mov][0] = 0

        if tipo_mov2 != -1:
            prob = 1/2
            self.movimientos[tipo_mov2][0] = 0
            
        for i in range(0,4):
            if tipo_mov != i and tipo_mov2 != i:
                self.movimientos[i][0] = prob

    def cambiar_probabilidad2(self,tipo_mov):
        if not self.borde:
            prob = 1/3
            self.borde = True
        else :
            prob = 1/2
            self.borde = False
        
        self.movimientos[tipo_mov][0] = 0
            
        for i in range(0,4):
            if self.movimientos[i][0] != 0:
                self.movimientos[i][0] = prob

    def regresar_probabilidad(self):
        #print('reinicio prob')
        self.movimientos = {0: [1/4,-1],1: [1/4,-1],2: [1/4,1],3: [1/4,1]}
        self.borde = False
            

#-----------------------------------------------------------------------------------------------------

def generar_matriz(columnas,filas):

    return np.random.randint(0,2,(filas,columnas))

def mostrar_info_matriz(matriz):
    num_elementos = np.size(matriz)
    print('-------------\n', matriz,'\n-------------')
    print('porcentaje de suciedad: ',(matriz.sum()-4) / float(num_elementos) * 100, '%')

while True:
    aspiradora1 = aspiradora()
    cont_movimientos = [0,0]

    matriz = generar_matriz(int(input("columnas: ")),int(input("filas: ")))

    dimenciones = np.shape(matriz)
    print(type(dimenciones))
    aspiradora1.valor_actual_celda = matriz[0][0]
    matriz[0][0] = 4

    mostrar_info_matriz(matriz)

    if input("Todo en ceros (y/n): ") == 'y':
        matriz = np.zeros(dimenciones)
    
    while matriz.sum()-4 != 0:
        
        ban = True
        #print(type(movimiento[0]))

        if aspiradora1.coordenadas[1] == 0:
            ban = False
            aspiradora1.cambiar_probabilidad(0)
            #print('bloquear izquierda')
        elif aspiradora1.coordenadas[1] == dimenciones[1] - 1:
            ban = False
            aspiradora1.cambiar_probabilidad(2)
            #print('bloquear derecha')
        if aspiradora1.coordenadas[0] == 0 :
            ban = False
            aspiradora1.cambiar_probabilidad(1)
            #print('bloquear arriba')
        elif aspiradora1.coordenadas[0] == dimenciones[0] - 1:
            ban = False
            aspiradora1.cambiar_probabilidad(3)
            #print('bloquear abajo')

        if aspiradora1.coordenadas[1] == 0 and aspiradora1.coordenadas[0] == 0:
            ban = False
            aspiradora1.cambiar_probabilidad(0, 1)
            #print('bloquear izquierda, arriba')
        elif aspiradora1.coordenadas[1] == dimenciones[1] - 1 and aspiradora1.coordenadas[0] == dimenciones[0]-1:
            ban = False
            aspiradora1.cambiar_probabilidad(2, 3)
            #print('bloquear derecha, abajo')
        if aspiradora1.coordenadas[0] == 0 and aspiradora1.coordenadas[1] == dimenciones[1]-1:
            ban = False
            aspiradora1.cambiar_probabilidad(1, 2)
            #print('bloquear arriba, derecha')
        elif aspiradora1.coordenadas[0] == dimenciones[0] - 1 and aspiradora1.coordenadas[1] == 0:
            ban = False
            aspiradora1.cambiar_probabilidad(3, 0)
            #print('bloquear abajo, izquierda')

        movimiento = aspiradora1.eleccion()

        #print(aspiradora1.movimientos)

        #columnas
        if movimiento[0] == 0 or movimiento[0] == 2:
            if aspiradora1.coordenadas[1] + aspiradora1.movimientos[movimiento[0]][1] >= 0 and aspiradora1.coordenadas[1] + aspiradora1.movimientos[movimiento[0]][1] < dimenciones[1]:
                matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] = aspiradora1.valor_actual_celda
                if matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] == 1:
                    matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] = 0
                    cont_movimientos[1] += 1
                aspiradora1.coordenadas[1] = aspiradora1.coordenadas[1] + aspiradora1.movimientos[movimiento[0]][1]
                aspiradora1.valor_actual_celda = matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]]
                matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] = 4
                print('\n\n\nPosición aspiradora: ',aspiradora1.coordenadas)
                #ban = True

            else:
                print("Fuera del rango!")
                ban = False
                '''
                if aspiradora1.coordenadas == [0,0]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],0)
                elif aspiradora1.coordenadas == [dimenciones[0],0]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],2)
                elif aspiradora1.coordenadas == [0,dimenciones[1]]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],0)
                elif aspiradora1.coordenadas == [dimenciones[0],dimenciones[1]]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],2)
                else:'''
                aspiradora1.cambiar_probabilidad(movimiento[0])
        
        if movimiento[0] == 1 or movimiento[0] == 3:
            if aspiradora1.coordenadas[0] + aspiradora1.movimientos[movimiento[0]][1] >= 0 and aspiradora1.coordenadas[0] + aspiradora1.movimientos[movimiento[0]][1] < dimenciones[0]:
                matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] = aspiradora1.valor_actual_celda 
                if matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]]==1:
                    matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]]=0
                    cont_movimientos[1] += 1
                aspiradora1.coordenadas[0] = aspiradora1.coordenadas[0]  + aspiradora1.movimientos[movimiento[0]][1]
                aspiradora1.valor_actual_celda= matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]]
                matriz[aspiradora1.coordenadas[0]][aspiradora1.coordenadas[1]] = 4
                
                print('\n\n\nPosición aspiradora: ', aspiradora1.coordenadas)
                #ban = True
                
            else:
                print("Fuera del rango!")
                ban = False
                '''
                if aspiradora1.coordenadas == [0,0]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],0)
                elif aspiradora1.coordenadas == [dimenciones[0],0]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],2)
                elif aspiradora1.coordenadas == [0,dimenciones[1]]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],0)
                elif aspiradora1.coordenadas == [dimenciones[0],dimenciones[1]]:
                    aspiradora1.cambiar_probabilidad(movimiento[0],2)
                else:'''
                aspiradora1.cambiar_probabilidad(movimiento[0])

        if not ban:
            aspiradora1.regresar_probabilidad()

        
        
        mostrar_info_matriz(matriz)
        cont_movimientos[0] += 1
        print('Movimientos totales:',cont_movimientos[0],'Movimientos utiles:', cont_movimientos[1])
        time.sleep(1)

    if input("salir (y/n): ") == 'y':
        break 