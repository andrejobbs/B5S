def trocaVogais(entrada):
    vogais=['A','E','I','O','U','a','e','i','o','u']
    for vogal in vogais:
        entrada=entrada.replace(vogal,'?')


    print(entrada)
    return entrada

trocaVogais('Ola mundo')
