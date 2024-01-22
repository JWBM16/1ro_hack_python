"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""


def fn_hack_9():
    result = [1, 2, 3]
    new_result = []  # Inicializa una lista vacía para almacenar el resultado final

    i = 0
    while i < len(result):
        new_result.append("@")  # Agrega '@' a la nueva lista
        new_result.append(result[i])  # Agrega el número a la nueva lista
        i += 1
        
    new_result.insert(7, "@")
    del new_result[0]  # Elimina el último elemento de la lista
    return new_result

r = fn_hack_9()
print(r)

