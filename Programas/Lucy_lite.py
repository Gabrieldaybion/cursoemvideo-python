from datetime import date
from time import sleep
from random import  choice
def conversa_lite():
    from time import sleep
    print('-'*40)
    sleep(1)
    print('__GX__')
    sleep(1)
    print('-'*20)

    sleep(1)
    print('__Lucy-1.0.0-lite__')
    sleep(1)
    print('-'*20)
    vs1='Lucy-1.0.0-lite'
    sleep(2)
    nome=input('Qual é o seu nome ?: ')
    if nome =='gabriel' or nome == 'Gabriel' or nome == 'biel' or nome == ' gabriel' or nome == 'Gabriel':
        print('Você sabia que o meu criador se chama', nome, '!')



    elif nome == 'lucy' or nome == 'Lucy' or nome == ' lucy' or nome == ' Lucy':
        print('Nossa,o meu nome tambem é lucy ksksksk ')

    elif nome == 'ana' or nome == 'gabriela' or nome == 'lucia' or nome == 'bruna' or nome == 'lucas' or nome == 'matheus' or nome == 'andreia' or nome == 'fabio' or nome == 'Fabio' or nome == ' fabio':
        print('Você possuí um nome bonito :)')
    else:
        print(f'Sr {nome}, eu gostei do seu nome :)')
    print(f'Seja bem vindo(a) {nome}')
    sleep(1)
    print('Para sair do programa digite exit.')
    sleep(1)
    print('Para descobrir oque eu posso fazer digite help')
    print('Por favor digite tudo em minusculo e sem acentos ')
    ajuda='''   Comandos possives que eu sei fazer.
vezes,divida,some,versao,eq2grau,menos,obj,
ano,estou mal,tabuada,raiz,media,lucy1,python serve para oque ?
python'''
    while True:
        sx=input('==: ')
        if sx=='oi'or sx=='oie' or sx=='oii' or sx=='ola' or sx=='hello':
            print('Oiee (✿◠‿◠)')

        elif sx == 'lucy1.0' or sx == 'lucy1' or sx == 'lucy 0.1.0' or sx == 'lucy 1.0' or sx == 'lucy 1':
            print('_' * 15)
            print('LUCY 1.0 apha sendo iniciada...')
            for contagem in range(1, 7):
                sleep(0.5)
                print('\033[37m.\033[m', end='')
            nggh = input('Qual eo seu nome ?')
            print('Oi,', nggh, '.''Seja bem vindo', nggh, 'espero que goste do programa lucy')
            idade = int(input('Qual ea sua idade ? '))
            print('Então você possui', idade, 'anos,eo seu nome é', nggh, 'Seja bem vindo(a)')
            nhdg = str(input('Qual eo seu nome completo ?...'))
            print('Era necessario saber o seu nome', nhdg, '\nmas ainda vamos precisar de mais informações...')
            print('Como você esta se sentindo', nggh, '?')
            input('Como você esta se sentindo agora ?')
            print('Otimo,qualquer coisa pode me chamar', nggh, ':)')
            for contagem in range(0, 2):
                sleep(0.3)
            print('LUCY 0.1.0 terminando')
            for contagem in range(1, 8):
                sleep(0.3)
                print('.', end='')
            print('lucy 1.0 terminada...')
            print('-' * 15)

        elif sx=='python':
            print('''Python é uma linguagem de programação de alto nível,
interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte.
Foi lançada por Guido van Rossum em 1991. ''')

        elif sx=='python serve para oque ?':
            print('''Ele é usado em vários campos, incluindo:
Desenvolvimento de website de back-end.
Desenvolvimento de jogos.
Ciência e análise de dados.
Desenvolvimento de aplicativos para dispositivos móveis.
Robótica e AI''')

        elif sx == 'tabuada' or sx == ' tabuada' or sx == 'tabu':
            # MULTIPLICAÇÃO 2.0
            num = int(input('Digite um valor: '))
            for c in range(1, 11):
                print('{} x {:2} = {}'.format(num, c, num * c))

        elif sx == 'raiz' or sx == 'raiz quadrada' or sx == ' raiz' or sx == 'Raiz':
            n66 = int(input("Digite um valor: "))
            r = n66 ** (1 / 2)
            print('A raiz de {} e igual a {}'.format(n66, r))

        elif sx == 'media' or sx == 'media ' or sx == 'Media':
            ny = float(input('Primeiro numero: '))
            ny1 = float(input('Segundo numero: '))
            md = (ny + ny1) / 2
            print('A media entre {} e {} é igual a {}'.format(ny, ny1, md))



        elif sx ==ord('e'):
            print('Botão e precionado..')

        elif sx == 'ano' or sx == 'qual ea data' or sx == 'data' or sx == 'Que ano estamos' or sx == 'Que ano estamos ?' or sx == 'que ano estamos' or sx == 'que ano estamos?':

            atual = date.today().day
            atual2 = date.today().year
            atual3 = date.today().month
            print('{}/{}/{}'.format(atual, atual3, atual2))

        elif sx=='exit':
            print('Programa finalizado')
            break
        elif sx == 'obrigado' or sx == 'Obrigado' or sx == 'obj':
            print('De nada :), eu estou aqui para ajudar')

        elif sx== 'estou mal':
            while True:
                cmvc = input('Como você esta ?: ')
                if cmvc == 'bem' or cmvc == 'otimo' or cmvc == 'otima':
                    print('Mas que maravilha :)')
                    break
                elif cmvc == 'mal' or cmvc == 'triste':
                    pq = input('Você que conversar sobre isso ?: ')
                    if pq == 'n' or pq == 'nao':
                        print('Tudo bem eu entendo:(.\nQual quer coisa que você precisar pode contar comigo.')
                        break
                    elif pq == 's' or pq == 'sim':
                        sç = input('Oque houve para você esta assim ?: ')
                        from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    print('Eu entendo isso...')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    print('Tente não pensar muito sobre isso.')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    print('Já que e algo que lhe faz mal.')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    print('Se isso ficar muito na sua cabeça,\ntente fazer algo para relaxar.')
                    print('Se eu pudesse eu lhe abraçaria :(')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    print('Não se preucupe tudo irá melhorar.:)')
                    break

        elif sx == 'menos' or sx == 'subitraçao ' or sx == '-' or sx == 'subitraia':
            menos = int(input('Primeiro numero: '))
            menos1 = int(input('Segundo numero: '))
            menos2 = menos - menos1
            print('_{}_-_{}_=_{}_.'.format(menos, menos1, menos2))

        elif sx=='versao':
            print(vs1)

        elif sx=='help':
            print(ajuda)

        elif sx=='divida' or sx=='dividir':
            dv1 = int(input('Primeiro numero: '))
            dv2 = int(input('Segundo numero: '))
            dv3 = dv1 / dv2
            print('_{}_/_{}_=_{}_'.format(dv1, dv2, dv3))

        elif sx == 'multiplique' or sx == 'multiplicaçao ' or sx == 'vezes' or sx == 'x' or sx == 'multipicar':
            ct1 = int(input('Primeiro numero: '))
            ct2 = int(input('Segundo numero: '))
            ct3 = ct1 * ct2
            print('_{}_X_{}_=_{}_'.format(ct1, ct2, ct3))

        elif sx == 'adiçao' or sx == '+' or sx == 'somar' or sx == 'some':
            mais = int(input('Primeiro valor: '))
            mais1 = int(input('Segundo valor: '))
            mais2 = mais + mais1
            print('_{}_+{}_=_{}'.format(mais, mais1, mais2))

        elif sx=='eq2grau':
            print('Seja bem vindo ao sistema automatico \nde equação de 2 grau. ')
            for n in range(1, 10):
                print('.', end='')
                tempo(0.7)

            print('.')
            while True:
                print('Informe o A,B e C:')
                a = int(input('A.==: '))
                b = int(input('B.==: '))
                c = int(input('C.==: '))

                delt = (b ** 2) - 4 * a * c
                print(f'O valor de delta é {delt} ')
                def x():
                    print('Calculando o valor de x.')
                    x1 = (((-b) + (delt ** (1 / 2))) / (2 * a))
                    x2 = (((-b) - (delt ** (1 / 2))) / (2 * a))
                    print(f'x1= {x1}, x2= {x2}')
                x()
                res = str(input('Deseja continuar ?(s/n)'))
                if res == 's':
                    print('Okay')
                elif res == 'n':
                    break
            print('FIM :)')

        else:
            print('Desculpe-me comando ivalido, digite help para vc ver oque é possivel fazer. ')


conversa_lite()