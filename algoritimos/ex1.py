def entradaMes(mes):
    lista_mes=['Janeiro','Fevereivo','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    if (mes==1):
        print(lista_mes[0])
    if (mes==2):
        print(lista_mes[1])
    if (mes==3):
        print(lista_mes[2])
    if (mes==4):
        print(lista_mes[3])
    if (mes==5):
        print(lista_mes[4])
    if (mes==6):
        print(lista_mes[5])
    if (mes==7):
        print(lista_mes[6])
    if (mes==8):
        print(lista_mes[7])
    if (mes==9):
        print(lista_mes[8])
    if (mes==10):
        print(lista_mes[9])
    if (mes==11):
        print(lista_mes[10])
    if (mes==12):
        print(lista_mes[11])
    elif (mes<1 or mes>12):
        print('Mes inexistente')
entradaMes(13)