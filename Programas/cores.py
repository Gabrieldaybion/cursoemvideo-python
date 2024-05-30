while True:
    cds=str(input('==:'))
    if cds=='sair':
        break
    elif cds=='dividir'  or cds == 'divida':
        div1 = int(input('Primeiro número: '))
        div2 = int(input('Segundo número: '))
        div3 = div1 / div2
        print(f'{div1} dividido por {div2} é igual a {div3}')

    else:
        print('err desculpe mas comando invalido')