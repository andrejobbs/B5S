def getEntrada(sacar):
    print(f'O valor é de {sacar}R$')
    cedulas=[200,100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]
    for cedula in cedulas:
        n_cedulas= int(sacar/cedula)
        retorno=([cedula, n_cedulas])
        print(retorno)
        sacar -=n_cedulas*cedula

getEntrada(152)