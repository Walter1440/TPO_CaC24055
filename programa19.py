inicio = int(input("Valor inicial:"))
final = int(input("Valor final:"))
final = final + 1  # Esto se hace para que al ejecutarse el programa el valor final este incluido.

for i in range(inicio, final):
    print(i)
    
# Tambien puede escribir el codigo de este manera.

# inicio = int(input("Valor inicial:"))
# final = int(input("Valor final:"))

# for i in range(inicio, final + 1):
#     print(i)