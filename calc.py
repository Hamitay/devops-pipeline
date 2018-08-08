'''
    Modulo basico de operacoes matematicas
'''

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise Exception("Divisao por zero")
    else:
        return a / b