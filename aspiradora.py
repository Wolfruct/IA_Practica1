import numpy as np

def generar_matriz(columnas,filas):

    return np.random.randint(0,2,(filas,columnas))

def mostrar_info_matriz(matriz,aux):
    num_elementos = np.size(matriz)
    print('------------------\n', matriz,'\n------------------')
    print('porcentaje de suciedad: ',aux.sum() / float(num_elementos) * 100, '%')

while True:
    aspiradora = {'cordenadas': [0,0], 'valor_actual': 0} #[[0,0], 0]
    lista_movimientos = {'a': ('columna',-1),'w': ('fila',-1),'d': ('columna',1),'s': ('fila',1)}

    matriz = generar_matriz(int(input("columnas: ")),int(input("filas: ")))

    dimenciones = np.shape(matriz)
    aspiradora['valor_actual'] = matriz[0][0]

    mostrar_info_matriz(matriz,matriz)

    if input("-------\nmoverse (y/n): ") == 'y':
        if input("Todo en ceros (y/n): ") == 'y':
            matriz = np.zeros(dimenciones)

        aux = np.array(matriz)
        while True:
            print('Moverse con "wasd".\nSalir con "l"')
            movimiento = input()

            if movimiento in lista_movimientos:
                if lista_movimientos[movimiento][0] == 'columna':
                    if aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1] >= 0 and aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1] < dimenciones[1]:
                        matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]] = aspiradora['valor_actual']
                        aspiradora['cordenadas'][1] = aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1]
                        aspiradora['valor_actual'] = matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]]
                        matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]] = 4
                        print('Posición aspiradora: ',aspiradora['cordenadas'])
                    else:
                        print("Fuera del rango!")
            
            if movimiento in lista_movimientos:
                if lista_movimientos[movimiento][0] == 'fila':
                    if aspiradora['cordenadas'][0] + lista_movimientos[movimiento][1] >= 0 and aspiradora['cordenadas'][0] + lista_movimientos[movimiento][1] < dimenciones[0]:
                        matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]] = aspiradora['valor_actual']
                        aspiradora['cordenadas'][0] = aspiradora['cordenadas'][0] + lista_movimientos[movimiento][1]
                        aspiradora['valor_actual'] = matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]]
                        matriz[aspiradora['cordenadas'][0]][aspiradora['cordenadas'][1]] = 4
                        print('Posición aspiradora: ', aspiradora['cordenadas'])
                    else:
                        print("Fuera del rango!")

            elif movimiento == 'l':
                break
            else:
                print('Movimiento no identificado')

            mostrar_info_matriz(matriz,aux)

    if input("salir (y/n): ") == 'y':
        break 