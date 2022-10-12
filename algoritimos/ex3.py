from readline import append_history_file


def paresExistentes():
    entrada=[1,2,3,4,5,6,7]
    lista_par=[[]]
    for x in entrada:
        if x % 2 == 0:
            lista_par[0].append(x)
    print(lista_par)

paresExistentes()


