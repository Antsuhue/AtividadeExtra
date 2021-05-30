categorias = {
    "procedencia": {
        "Sul": [1],
        "Norte": [2],
        "Leste": [3],
        "Oeste": [4],
        "Nordeste": [5, 6, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        "Sudeste": [7, 8, 9],
        "Centro-Oeste": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    }
}
entrada = 25

for x in categorias["procedencia"]:
    for y in categorias["procedencia"][x]:
        if entrada == y:
            print(x)
            break
