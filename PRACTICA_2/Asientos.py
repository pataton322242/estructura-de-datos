A=[ [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
 ]

def reservar(i,j):
    global A
    i-=1
    j-=1
    if A[i][j] == 0:
        A[i][j] = 1
        print("OK: reservado")
    else:
        print("RECHAZO: ocupado")


def liberar(i,j):
    global A
    i-=1
    j-=1
    if A[i][j] == 1:
        A[i][j] = 0
        print("OK: liberado")
    else:
        print("RECHAZO: ya libre")


def consultar(i,j):
    global A
    i-=1
    j-=1
    if A[i][j] == 1:
        print("Estado: reservado")
    else:
        print("Estado: libre")

reservar(1,1)
reservar(1,2)
reservar(1,1)
consultar(1,1)
liberar(1,1)
liberar(1,1)
reservar(3,4)
reservar(6,6)
consultar(6,6)
reservar(2,5)
print(A)

TOTAL=sum(sum(fila) for fila in A)
print("Total de asientos reservados al final:",TOTAL)

Filas_con_mas_reservas = [i+1 for i, row in enumerate(A) if sum(row) == max(sum(r) for r in A)]
print("Filas con más reservas:", Filas_con_mas_reservas)    