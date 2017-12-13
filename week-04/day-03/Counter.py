def counter(string):
    lista = []
    for i in range(len(string)):
        lista.append(string[i:i+1])

    return {x: lista.count(x) for x in lista}


