def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2, lista[0])
    lista.pop(0)

def retiros(lista, lista2):
    r = lista[0] - lista2[0]   
    deque(lista, lista2)
    enque(lista, r)
    
def depositos(lista, lista2):
    d = lista[0] + lista2[0]
    deque(lista, lista2)
    enque(lista, d)

def peek(lista):
    return lista[0]

def isEmpty(lista):
      if lista == []:
        return True
      else:
        return False

def size(lista):
    return len(lista)

saldos = []
retiro = []
deposito=[]

print(isEmpty(saldos))
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(retiro, 500)
print(retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print(saldos)
enque(deposito, 300)
print(deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print(saldos)
print(peek(saldos))
size(saldos)
print(size(saldos))
