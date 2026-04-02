"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    pares = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares += 1
    return print("hay",pares,"pares entre el numero")
print(contar_pares_ciclo(20))

def contar_pares_recursivo(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + contar_pares_recursivo(n - 1)
    else:
        return 0 + contar_pares_recursivo(n - 1)
print("hay",contar_pares_recursivo(30),"pares hasta el numero")