// Diccionario de base de datos de tus proyectos
const proyectos = {
    bubble: {
        titulo: "Bubble Sort (Ordenamiento Burbuja)",
        descripcion: "Compara elementos adyacentes y los intercambia si están en el orden incorrecto. El elemento más grande 'burbujea' hasta el final de la lista en cada pasada. Complejidad Promedio: O(n²).",
        consola: "--- Ejecutando Bubble Sort ---\nLista original: [64, 34, 25, 12, 22]\nPasada 1: [34, 25, 12, 22, 64]\nPasada 2: [25, 12, 22, 34, 64]\nPasada 3: [12, 22, 25, 34, 64]\nLista Ordenada: [12, 22, 25, 34, 64]\n¡Proceso terminado con éxito!",
        codigo: `def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Prueba del algoritmo
lista = [64, 34, 25, 12, 22]
print("Lista ordenada:", bubble_sort(lista))`
    },
    insertion: {
        titulo: "Insertion Sort (Ordenamiento por Inserción)",
        descripcion: "Toma un elemento a la vez y lo inserta en su posición correcta dentro de la parte de la lista que ya ha sido procesada, de manera similar a como acomodas las cartas en tu mano. Complejidad Promedio: O(n²).",
        consola: "--- Ejecutando Insertion Sort ---\nArreglo inicial: [12, 11, 13, 5, 6]\nInsertando 11: [11, 12, 13, 5, 6]\nInsertando 5:  [5, 11, 12, 13, 6]\nInsertando 6:  [5, 6, 11, 12, 13]\nResultado final: [5, 6, 11, 12, 13]",
        codigo: `def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

lista = [12, 11, 13, 5, 6]
print("Lista ordenada:", insertion_sort(lista))`
    },
    merge: {
        titulo: "Merge Sort (Ordenamiento por Mezcla)",
        descripcion: "Utiliza la técnica de 'divide y vencerás'. Divide la lista en mitades recursivamente hasta tener elementos individuales y luego los vuelve a fusionar de manera ordenada. Complejidad garantizada: O(n log n).",
        consola: "--- Ejecutando Merge Sort ---\nDividiendo: [38, 27, 43, 3]\nDividiendo: [38, 27] y [43, 3]\nMezclando de forma ordenada: [27, 38] y [3, 43]\nResultado de la Fusión: [3, 27, 38, 43]",
        codigo: `def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1
    return arr`
    },
    hash: {
        titulo: "Estructura de Datos: Tabla Hash",
        descripcion: "Asocia claves con valores mediante una función Hash que calcula un índice en un arreglo. El principal reto de diseño es gestionar las colisiones cuando dos claves generan el mismo índice.",
        consola: "--- Simulación de Tabla Hash ---\nInsertando 'llave_1' -> Índice calculado: 4\nInsertando 'llave_2' -> Índice calculado: 7\n¡Alerta de Colisión detectada en índice 4! Aplicando direccionamiento cerrado (lista ligada).",
        codigo: `class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        self.table[idx].append((key, value)) # Manejo de colisión`
    }
};

let algoritmoActual = null;

function mostrarAlgoritmo(id) {
    algoritmoActual = proyectos[id];
    
    document.getElementById('titulo-algoritmo').innerText = algoritmoActual.titulo;
    document.getElementById('descripcion-algoritmo').innerText = algoritmoActual.descripcion;
    
    // Inyectar el código texto al contenedor HTML
    const contenedorCodigo = document.getElementById('codigo-python');
    contenedorCodigo.textContent = algoritmoActual.codigo;
    
    // Limpiar pantalla de consola anterior
    document.getElementById('pantalla-ejecucion').innerText = "Consola lista. Presiona 'Simular Ejecución'...";
    document.getElementById('pantalla-ejecucion').style.color = "#888888";

    // Forzar a la librería Prism a pintar de colores el nuevo código
    Prism.highlightElement(contenedorCodigo);
}

function simularEjecucion() {
    if (!algoritmoActual) {
        alert("Por favor selecciona un algoritmo primero.");
        return;
    }
    const terminal = document.getElementById('pantalla-ejecucion');
    terminal.innerText = algoritmoActual.consola;
    terminal.style.color = "#00ff00"; // Cambia a verde activo estilo consola
}