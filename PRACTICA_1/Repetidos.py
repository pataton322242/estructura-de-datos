X=[1,2,4,4,5,7,9,11,11,13,14,15,16,16]

print("LISTA ORIGINAL:",X)

for i in range(len(X)-1,0,-1):
    if X[i]==X[i-1]:
        X.pop(i)

print("LISTA ACTUALIZADA:",X)