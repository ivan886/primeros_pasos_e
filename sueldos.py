import random

trabajadores = []

for x in  range(100):
    sueldo = random.randrange(100,1000)
    trabajadores.append(sueldo)

contMayor = 0
contMenor = 0
totalNomina = 0
for sueldo in range(len(trabajadores)):
    totalNomina += sueldo
    if sueldo >= 500:
        contMayor+=1
    else:
        contMenor+=1

print(f"Trabajadores con sueldo mayor a 500 {contMayor}")
print(f"Trabajadores con sueldo menor a 500 {contMenor}")
print(f"Total nomina : {totalNomina}")