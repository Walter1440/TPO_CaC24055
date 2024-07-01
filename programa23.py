# Esta funcion recibe tres valores
# como parametros y calcula el promedio
# solo si estan comprendidos entre 1 y 10.

def calcular_promedio( v1, v2, v3):
    if v1>=1 and v1<=10 and v2>=1 and v2<=10 and v3>=1 and v3<=10:
        promedio = (v1 + v2 + v3)/3
        print("El promedio es:", promedio)
    else:
        print("Hay un error en los parametros.")
    
calcular_promedio(4,10,7)        