import numpy as np

def generar_matriz(columnas,filas):

    return np.add(np.zeros((filas,columnas)),np.random.randint(0,2,(filas,columnas)))

def mostrar_info_matriz(matriz):
    num_elementos = np.size(matriz)
    print(matriz)
    print(matriz.sum() / float(num_elementos) * 100)

while True:
    aspiradora = {'cordenadas': [0,0], 'valor_actual': 0} #[[0,0], 0]
    lista_movimientos = {'w': ('columna',-1),'a': ('fila',-1),'s': ('columna',1),'d': ('fila',1)}

    matriz = generar_matriz(int(input("columnas: ")),int(input("filas: ")))

    dimenciones = np.shape(matriz)

    mostrar_info_matriz(matriz)

    if input("modificar (y/n): ") == 'y':
        if input("Todo en ceros (y/n): ") == 'y':
                matriz = np.zeros(dimenciones)

        while True:
            print('Moverse con "wasd".\nSalir con "l')
            movimiento = input()

            if movimiento in lista_movimientos:
                if lista_movimientos[movimiento][0] == 'columna':
                    if aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1] >= 0 and aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1] < dimenciones[1]:
                        matriz[aspiradora['cordenadas']] = aspiradora['valor_actual']
                        aspiradora['cordenadas'][1] = aspiradora['cordenadas'][1] + lista_movimientos[movimiento][1]
                        aspiradora['valor_actual'] = matriz[aspiradora['cordenadas']]
                        print(aspiradora['cordenadas'])

            elif movimiento == 'l':
                break
            else:
                print('Movimiento no identificado')

            mostrar_info_matriz(matriz)
            


    if input("salir (y/n): ") == 'y':
        break 