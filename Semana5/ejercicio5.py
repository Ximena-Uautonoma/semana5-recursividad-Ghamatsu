"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
print(potencia_ciclo(2,3))

def potencia_recursiva(base, exponente):
    pass
