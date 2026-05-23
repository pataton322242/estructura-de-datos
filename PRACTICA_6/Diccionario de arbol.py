class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


def insertar_nodo(raiz, clave, valor=None):
    if raiz is None:
        return NodoArbol(clave, valor)
    if clave < raiz.clave:
        if raiz.hijoIzquierdo:
            insertar_nodo(raiz.hijoIzquierdo, clave, valor)
        else:
            raiz.hijoIzquierdo = NodoArbol(clave, valor, padre=raiz)
    elif clave > raiz.clave:
        if raiz.hijoDerecho:
            insertar_nodo(raiz.hijoDerecho, clave, valor)
        else:
            raiz.hijoDerecho = NodoArbol(clave, valor, padre=raiz)
    return raiz

def arbol_a_diccionario(nodo):
    if nodo is None:
        return None
    if not nodo.tieneAlgunHijo():
        return None
    
    hijos = {}
    
  
    if nodo.hijoIzquierdo:
        hijos[nodo.hijoIzquierdo.clave] = arbol_a_diccionario(nodo.hijoIzquierdo)
    else:
        hijos[None] = None
                          
        del hijos[None] 
   
    if nodo.hijoDerecho:
        hijos[nodo.hijoDerecho.clave] = arbol_a_diccionario(nodo.hijoDerecho)



lista = [1, 13, 11, 5, 9, 10, 1, 12, 3, 6] 

raiz = None
for numero in lista:
    raiz = insertar_nodo(raiz, numero, numero)


resultado = {raiz.clave: arbol_a_diccionario(raiz)}

print("Diccionario del árbol:")
print(resultado)