def torre_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print("Mover disco 1 del poste", origen, "al poste", destino)
        return
    torre_de_hanoi(n-1, origen, auxiliar, destino)
    print("Mover disco", n, "del poste", origen, "al poste", destino)
    torre_de_hanoi(n-1, auxiliar, destino, origen)

n = 5
torre_de_hanoi(n, 'A', 'B', 'C')