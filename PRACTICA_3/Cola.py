def enque(lista, elemento):
    lista.append(elemento)

def deque(lista):
    lista.pop(0)

def peek(lista):
    return lista[0]

def isEmpty(lista):
    if lista == []:
        return True
    else:
        return False

def size(lista):
     return len(lista)   

list=[]
print(isEmpty(list))
enque(list,1)
print(isEmpty(list))
deque(list)
print(isEmpty(list))
enque(list,8)
enque(list,7)
print(peek(list))
size(list)
print(size(list))


