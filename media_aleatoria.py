import random

def aleatorio():
    soma = 0
    i = 1
    while i <= 10000:
        numero = random.randint(0, 100)
        soma = soma + numero
        i += 1
    return soma/10000
