def enque_tail(lista, elemento):
    lista.append(elemento)

def enque_head(lista, elemento):
    lista.insert(0, elemento)

def deque_head(lista):
    lista.pop(0)

def deque_tail(lista):
    lista.pop()

def head(lista):
    return lista[0]

def is_empty(lista):
    if lista ==[]:
        return True
    else:   
        return False

def fallo(lista):
    tarea = head(lista)
    nombre= tarea[0]
    fallos= tarea[1]-1
    intentos= tarea[2]+1

    print ("TAREA:", nombre,"- FALLO:")   
    deque_head(lista)
    enque_tail(lista, [nombre, fallos, intentos])

def exito(lista):
    tarea= head(lista)
    nombre= tarea[0]
    print ("TAREA:", nombre,"COMPLETADA:")
    deque_head(lista)

tareas=[]

enque_tail(tareas,["T1",1,0])
enque_tail(tareas,["T2",0,0])
enque_tail(tareas,["T3",2,0])
enque_tail(tareas,["T4",1,0])
enque_tail(tareas,["T5",2,2])
enque_tail(tareas,["T6",2,1])

fallo(tareas)
print(tareas)
exito(tareas)
print(tareas)
fallo(tareas)
print(tareas)
fallo(tareas)
print(tareas)
fallo(tareas)
print(tareas)
fallo(tareas)
print(tareas)