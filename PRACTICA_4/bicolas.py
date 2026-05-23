from collections import deque
def enque_tail(lista, elemento):
    lista.append(elemento)

def enque_head(lista, elemento):
    lista.appendleft(elemento)

def dequeue(q:deque):
    return q.popleft()

def deque_tail(lista):
    lista.pop()

def head(lista):
    return lista[0]

def tail(lista):
    return lista[-1]

def is_empty(lista):
    return lista == []

def size(lista):
    return len(lista)

def colas():
    cola = deque()
    tiempo = [0,2,4,6,12]

    for t in tiempo:
        while len(cola) > 0 and t - cola[0] >= 10:
            cola.popleft()
        if len(cola) < 3:
            cola.appendleft(t)
           
            print("tiempo", t, "aceptada", list(cola))
        else:
            print("tiempo", t, "rechazada",list(cola))

    print("COLA", list(cola))
colas()

