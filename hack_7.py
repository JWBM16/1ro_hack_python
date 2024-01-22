"""
loop: while [] output => [5,4,3,2,1,0]
"""


def fn_hack_7():
    resultados = 5

    result = []

    while resultados >= 0:
        result.append(resultados)
        resultados -= 1
    # ...
    return result


r = fn_hack_7()
print(r)
