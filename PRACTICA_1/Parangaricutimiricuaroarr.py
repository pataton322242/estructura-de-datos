CADENA="Parangaricutimiricuaro"
cadena2=[]

for i in CADENA:
    cadena2.append(i.upper())
conteo =[0]*26

for cadena2 in cadena2:
           posicion=ord(cadena2)-ord('A')
           conteo[posicion]+=1
           
for i in range(26):
    if conteo[i]>0: 
     print(f"{chr(i+ord('A'))}:{conteo[i]}")
