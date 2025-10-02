def mesclar_dicionarios(dic1, dic2):
    return {**dic1, **dic2}

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

resultado = mesclar_dicionarios(d1, d2)
print(resultado)
