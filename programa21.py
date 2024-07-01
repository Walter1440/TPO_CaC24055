# Tips sobre range():

# 1) Acepta de 1 a 3 argumentos enteros.
# 2) Un argumento: va de 0 a final -1.
# 3) Dos argumentos: va de inicio a final -1.
# 4) Tres argumentos: va de inicio a final -1, de paso en paso.
# 5) El paso puede ser negativo.

for i in range(1, 6, 1):
    print("Valor i:",i,"--->", i*0.5)
    