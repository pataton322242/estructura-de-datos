import random
def bubble_sort(lista):
    swap_counter = 0
    n = len(lista)

    swapped = True

    while swapped:
        swapped = False

        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]:
           
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
                swap_counter += 1

        n -= 1  

    return lista, swap_counter



datos = [10,50,23,3,43,23,29,49,12,40]
ordenada, intercambios = bubble_sort(datos)

print("Bubble Sort:", ordenada)

def selection_sort(datos):

 n = len(datos)
 for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if datos[j] < datos[min_index]:
      min_index = j
  min_value = datos.pop(min_index)
  datos.insert(i, min_value)
print("SELECTION SORT")
print(datos)

def insertion_sort(datos):
     
  n = len(datos)
  for i in range(1,n):
    insert_index = i
  current_value = datos.pop(i)
  for j in range(i-1, -1, -1):
    if datos[j] > current_value:
      insert_index = j
  datos.insert(insert_index, current_value)

print("INSERTION SORT")
print(datos)


def merge_sort(datos):
    if len(datos) > 1:
        mid = len(datos) // 2
        L = datos[:mid]
        R = datos[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                datos[k] = L[i]
                i += 1
            else:
                datos[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            datos[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            datos[k] = R[j]
            j += 1
            k += 1
            print("MERGE SORT")
            print(datos)     



def partition(datos, low, high):
    pivot = datos[high]
    i = low - 1
    for j in range(low, high):
        if datos[j] <= pivot:
            i += 1
            datos[i], datos[j] = datos[j], datos[i]
    datos[i + 1], datos[high] = datos[high], datos[i + 1]
    return i + 1

def quick_sort(datos, low, high):
    if low < high:
        p = partition(datos, low, high)
        quick_sort(datos, low, p - 1)
        quick_sort(datos, p + 1, high)


quick_sort(datos, 0, len(datos) - 1)
print("QUICK SORT")
print(datos)            


def quick_sort_random(datos):
    if len(datos) <= 1:
        return datos
    pivot= random.choice(datos)
    less = [x for x in datos if x < pivot]
    middle = [x for x in datos if x == pivot]
    right = [x for x in datos if x > pivot]
    return quick_sort_random(less) + middle + quick_sort_random(right)
print("QUICK SORT RANDOM")
print(quick_sort_random(datos))

def counting_sort(datos):
    if not datos:
        return []

   
    max_val = max(datos)
    count = [0] * (max_val + 1)
    output = [0] * len(datos)

    for num in datos:
        count[num] += 1

    
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(datos):
        output[count[num] - 1] = num
        count[num] -= 1

    return output


sorted_data = counting_sort(datos)
print(sorted_data) 