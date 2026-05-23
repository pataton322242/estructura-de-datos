Cal_alumnos = [8,8,7,5,10,9,9,5,6,10]
sum=0
for i in Cal_alumnos:
    sum+=i
    prom=sum/len(Cal_alumnos)
    
print("El promedio de las calificaciones es:",prom)
vi =0
vs =0
aa=0
for i in Cal_alumnos:
    if i <= 6:
        vi += 1 
    aa = 10-vi
print( "Alumnos reprobados,",vi, "Alumnos aprobados,",aa)

va =0
ve =0
bb=0
for i in Cal_alumnos:
    if i >= 8:
       ve += 1    
    bb = 10 - ve 
    

           
print("Alumnos regulares.",bb, "Alumnos sobresalientes,",ve)
