Tonelada_cereal = [12, 24, 16, 15, 20, 18, 6, 10, 12, 11, 15, 12]
print ("LAS TONELADAS DE CEREAL POR MES SON:", Tonelada_cereal)
suma = 0
for i in Tonelada_cereal:
    suma += i

promedio = suma / len(Tonelada_cereal)
print("EL PROMEDIO ANUAL DE TONELADAS DE CEREAL ES: ",promedio)
superior =[]
inferior =[]
for i in Tonelada_cereal:
   if promedio > i:
       superior.append(i)
       
   else:
      inferior.append(i)


print("LOS QUE FUERON INFERIORES A EL PROMEDIO ANUAL SON:",inferior)
print("LOS QUE FUERON SUPERIORES A EL PROMEDIO ANUAL SON:",superior)
