# Declaracion de las variables del programa.
inicio = int(input("Valor inicial: "))
final = int(input("Valor final: "))
suma = 0
control = inicio

while control <= final:
    suma = suma + control
    control = control + 1
    
print("La suma de los enteros entre", inicio,"y", final,"es:", suma)
