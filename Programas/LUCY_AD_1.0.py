import webbrowser
from pyfirmata import Arduino, util
from PyQt5 import uic, QtWidgets
from time import sleep as temp
from random import choice

def app_duino():
    print('App inciado')
    placa = Arduino('COM9')
    placa.digital[11].write(1)
    def direita_cima():
        print('Direita: CIMA')

    def direita_baixo():
        print('Direita: BAIXO')

    def esquerda_cima():
        print('Esquerda: CIMA')

    def esquerda_baixo():
        print('Esquerda: BAIXO')

    def led1_ligado():
        print('LED.1: LIGADO')
        placa.digital[12].write(1)

    def led1_desligado():
        print('LED.1:DESLIGADO')
        placa.digital[12].write(0)
    def led2_ligado():
        print('LED.2:LIGADO')
        placa.digital[11].write(1)
    def led2_desligado():
        print('LED.2:DESLIGADO')
        placa.digital[11].write(0)

    def led3_ligado():
        print('LED.3:LIGADO')
        placa.digital[10].write(1)
    def led3_desligado():
        print('LED.3:DESLIGADO')
        placa.digital[10].write(0)
    def modulo_1():
        print('Módulo.1:Ligado')
        for c in range(3):
            print('Movimento randomizado')
            placa.digital[12].write(0)
            temp(0.5)
            placa.digital[11].write(0)
            temp(0.6)
            placa.digital[12].write(1)
            temp(0.7)
            placa.digital[12].write(0)
            temp(0.4)
            placa.digital[11].write(1)
            temp(0.9)
            placa.digital[11].write(0)
            temp(0.7)
            placa.digital[12].write(1)
            placa.digital[11].write(1)
            temp(0.6)
            placa.digital[12].write(0)
            placa.digital[11].write(0                                                               )


    def modulo_2():
        print('Módulo.2:Ligado')
        print('movimento randomizado de verdade')
        dd1 = placa.digital[12]
        dd2 = placa.digital[11]
        dd3 = placa.digital[10]
        dd4 = placa.digital[9]

        lit=[dd1,dd2,dd3,dd4]
        for ca in range(60):

            banana= choice(lit)
            banana.write(1)
            temp(0.2)
            banana.write(0)

    app9 = QtWidgets.QApplication([])
    formulario9 = uic.loadUi('AD_controller.ui')
    formulario9.cimadir.clicked.connect(direita_cima)
    formulario9.baixodir.clicked.connect(direita_baixo)
    formulario9.cimaesq.clicked.connect(esquerda_cima)
    formulario9.baixoesq.clicked.connect(esquerda_baixo)
    formulario9.led1.clicked.connect(led1_ligado)
    formulario9.led2.clicked.connect(led2_ligado)
    formulario9.led3.clicked.connect(led3_ligado)
    formulario9.led1des.clicked.connect(led1_desligado)
    formulario9.led2des.clicked.connect(led2_desligado)
    formulario9.led3des.clicked.connect(led3_desligado)
    formulario9.modulo.clicked.connect(modulo_1)
    formulario9.modulo2.clicked.connect(modulo_2)
    formulario9.show()
    app9.exec()

def app_lucy_1_0_0():
    def exibir_mensagem():
        dado_lido = janela.senha.text()
        print(dado_lido)
        janela.senha.setText("")
        if dado_lido == 'gabriel':
            print('OLa mestre')
        if dado_lido == 'daybion':
            segunda_tela.show()

    def lucy_cvs():


        from time import sleep

        for contagem in range(0, 3):
            sleep(1)

        print('-' * 40)
        from time import sleep

        for contagem in range(0, 4):
            sleep(1)
        print('__GX__')
        from time import sleep

        for contagem in range(0, 2):
            sleep(1)

        print('-' * 20)
        from time import sleep

        for contagem in range(0, 3):
            sleep(1)
        print('__Lucy 1.0.0__')
        from time import sleep

        for contagem in range(0, 2):
            sleep(1)
        print('-' * 20)

        from time import sleep
        import random

        print('Para sair do programa lucy, escreva [sair] ,tudo em minusculo.')
        for contagem in range(0, 2):
            sleep(0.9)
            from time import sleep

        for contagem in range(0, 2):
            sleep(1)
            for n in range(1, 7):
                print('.', end='')
                sleep(0.5)
        print('.')
        çç = input('==: ')
        nome34 = 'oi'
        if çç == nome34:
            print('Oi :/')
        elif çç == 'sair':
            print('Ainda nem começamos.')

        elif çç == 'oii' or çç == 'OII' or çç == 'eai' or çç == 'oie' or çç == 'Oie' or çç == 'oiii' or çç == 'oiiii':
            n1 = 'Eai ;)'
            n2 = 'oii'
            n3 = 'Oie:)'
            n4 = 'Oiiii ;)'
            n5 = 'OOiii .'
            lista = [n1, n2, n3, n4, n5]
            escolhido = random.choice(lista)
            print('{}'.format(escolhido))
        elif çç == 'bom dia' or çç == 'Bom dia' or çç == 'bom dia ':
            print('Bom dia :)')

        elif çç == 'boa tarde' or çç == 'Boa tarde' or çç == 'boa tarde ':
            print('Boa tarde :)')

        elif çç == 'boa noite' or çç == 'Boa noite' or çç == 'boa noite ':
            print('Boa noite {} ;) ')

        elif çç == 'tudo bem ?' or çç == 'como vc esta' or çç == 'como voce esta' or çç == 'blz':
            print('Eu estou bem :)')
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

        nome34 = 'oi'
        vrl534 = 'gabriel'
        nome = input('Qual é o seu nome ? : ')
        nome1 = 'lucy Lucy LUCY '
        if nome == 'Gabriel' or nome == 'biel' or nome == ' gabriel' or nome == 'Gabriel':
            print('Você sabia que o meu criador se chama', nome, '!')
        elif nome == 'lucy' or nome == 'Lucy' or nome == ' lucy' or nome == ' Lucy':
            print('Nossa,o meu nome tambem e lucy ksksksk ')
        elif nome == 'ana' or nome == 'gabriela' or nome == 'lucia' or nome == 'bruna' or nome == 'lucas' or nome == 'matheus' or nome == 'andreia' or nome == 'fabio' or nome == 'Fabio' or nome == ' fabio':
            print('Você possuí um nome bonito :)')
        else:
            print('')
        print(f'Seja bem vindo(a){nome}.')
        print('Digite algo para começar. Tudo em minusculo .')
        print('Digite help para saber oque eu posso fazer')
        '''from pygame import mixer
    
        mixer.init()
        mixer.music.load('lcms.mp3')
        mixer.music.play()
        from time import sleep
        for contagem in range(0, 2):
            sleep(7.3)'''
        ajuda='''sair   pesquisar   music   oii     divida    help  multiplique 
soma  obrigado  menos  versao  qual e a data  estou mal  meu nome
tabuada  raiz  media  lucy1  eq2grau  conversar'''
        vs1 = '1.0.0 OFICIAL'
        from pygame import mixer

        mixer.init()
        mixer.music.load('History of iPhone 2007 to 2020 Evolution(MP3_70K).mp3')
        mixer.music.play()
        print('DEGABIONTWESS')
        print('')
        print('Para sair digite sair')
        while True:  #

            sx = str(input('==: '))

            if sx == nome34:
                print('Oi :/')

            elif sx == 'help':
                print(ajuda)

            elif sx == 'sair':
                break

            elif sx == 'conversar' or sx == 'conversa' or sx == 'quero conversar':
                ssdfr5 = input('Você deseja converar comigo {} ?'.format(nome))
                if ssdfr5 == 'sim' or ssdfr5 == 's':
                    print('Otimo!!!')
                    print('Meu nome é Lucy, muito prazer', nome, ':)')
                    nome3 = 'mal'
                    chute = input('Como você esta ?:')
                    s1 = 'sim'
                    if chute == nome3:
                        pq = input('Você conversar sobre isso ? ==: ')
                        if pq == s1 or pq == 's':
                            n = input('Oque ouve pra você esta assim ? ==: ')
                            print('Então você esta assim por causa de ', n, )
                            from time import sleep

                            for contagem in range(0, 5):
                                sleep(1)

                            print(
                                'Não fique assim :(,\nOlha eu sei que as coisas podem estar dificies,\n mas tudo ira melhorar')

                        else:
                            print('Qual quer coisa pode contar comigo')

                    else:
                        print('Otimo :)')

                    for contagem in range(0, 8):
                        sleep(1)

                    print('---')
                    # variaveis do jogo.
                    x = 'sim' or 's'
                    chute = input('Você que jogar um jogo comigo ? ')
                    print(
                        'O jogo funciona assim,\nvocê vai ter que adivinhar um numero que eu estou pensando de 1 a 9:')

                    if chute == x:

                        from random import randint

                        n = int(randint(1, 9))
                        p = 0
                        t = 0

                        from time import sleep

                        for contagem in range(0, 7):
                            sleep(1)

                        print('Valendo :) !!! ')
                        from random import randint

                        n = int(randint(1, 9))
                        p = 0
                        t = 0
                        while p != n:
                            p = int(input('Seu palpite: '))
                            t += 1
                            if p == n:
                                print('Acertou! Placar %i' % t)
                            elif p < n:
                                print('Chute um valor maior ')
                            else:
                                print('Chute um valor menor')
                        print('Fim de jogo \n Probiedade GX')

                    else:
                        print('Tudo bem então :(')

                    n1 = str(input('Qual tipo de musica voçê gosta ?==: '))
                    n2 = str(input('Qual ea sua comida favorita ?==: '))
                    n3 = str(input('Qual ea sua cor favorita ?==: '))
                    n4 = str(input('Qual eo seu jogo favorito?==: '))
                    lista = [n1, n2, n4]
                    escolhido = random.choice(lista)
                    print(
                        'Eu tambem gosto de {},\n mas eu não posso usufruir como eu dejesaria,\n pois o meu criador não me deu essa opção ksksskskssk'.format(
                            escolhido))
                    if n1 == 'rock' or n1 == ' rock':
                        print('Você gosta de rock que legal...')
                        rc = input('Você conheçe Artic Monkeys ? ==:')
                        if rc == 's' or rc == 'sim':
                            fd = input('Opa :)...Você conheçe  I Wanna Be Yours ? ==:')
                            if fd == 's' or fd == 'sim':
                                print('Essa ea minha musica favorita.')
                            elif fd == 'n' or fd == 'nao' or fd == 'não':
                                print('Poxa...:(')
                                k2 = input('Então você conheçe Fluorescent Adolescent ? ==:')
                                if k2 == 's' or k2 == 'sim':
                                    print('Bom essa você conheçe ne', nome,
                                          '\n eu ouso mais essa pra dançar mesmo kskssk.')
                                else:
                                    k2 == 'nao'
                                print('Poxa kskskskkks...')
                            else:
                                print('Poxa mas que pena, pois eu gosto muito deles...')



                else:
                    print('poxa:(')

            elif sx == 'pesquisar' or sx == 'Pesquisar' or sx == 'pesquise' or sx == 'Pesquise':
                print('Para sair das pesquisas digite: exit')
                print('Oque eu devo pesquisar ?')
                import webbrowser

                while True:

                    pg = input('==: ')
                    pesquisar = ('https://www.google.com.br/search?q=')
                    pesquisng = (pesquisar + pg)
                    webbrowser.open(pesquisng)
                    if pg == 'exit':
                        break

            elif sx == 'musicas' or sx == 'play' or sx == 'music' or sx == 'tocar':
                while True:
                    print('Musicas')
                    msc = input('Digite play para iniciar uma musica/para sair digite sair: ')
                    if msc == 'play':
                        print('[1]Artic Monkens\n[2]Imortal\n[3]The week\n[4]Dragon ball\n[5]sair do programa')

                        while True:
                            esc78 = input('==: ')
                            if esc78 == '1':
                                from pygame import mixer

                                mixer.init()
                                mixer.music.load('mp3 .mp3')
                                mixer.music.play()
                                print('Para parar a musica digite stop')
                                ggh = input('==: ')
                                if ggh == 'stop' or ggh == 'pausar':
                                    mixer.music.stop()
                                    break


                            elif esc78 == '2':
                                from pygame import mixer

                                mixer.init()
                                mixer.music.load('Immortals(MP3_160K).mp3')
                                mixer.music.play()
                                print('Para parar a musica digite stop')
                                ggh = input('==: ')
                                if ggh == 'stop' or ggh == 'pausar':
                                    mixer.music.stop()
                                    break

                            elif esc78 == '3':
                                from pygame import mixer

                                mixer.init()
                                mixer.music.load('The Weeknd - I Feel It Coming ft. Daft Punk (Offic(MP3_160K).mp3')
                                mixer.music.play()
                                print('Para parar a musica digite stop')
                                ggh = input('==: ')
                                if ggh == 'stop' or ggh == 'pausar':
                                    mixer.music.stop()
                                    break
                                while mixer.music.get_busy() == True: continue
                            elif esc78 == '4':
                                from pygame import mixer

                                mixer.init()
                                mixer.music.load('dg.mp3')
                                mixer.music.play()
                                print('Digite stop para parar a musica.')
                                ggh = input('==: ')
                                if ggh == 'pause' or ggh == 'stop':
                                    mixer.music.stop()
                                    break

                                while mixer.music.get_busy() == True: continue
                            elif esc78 == '5':
                                break

                    elif msc == 'sair':
                        break
                    else:
                        print('Comando invalido digite oque foi pedido.')

            elif sx == 'oii' or sx == 'OII' or sx == 'eai' or sx == 'oie' or sx == 'Oie' or sx == 'oiii' or sx == 'oiiii':
                n1 = 'Eai ;)'
                n2 = 'oii'
                n3 = 'Oie:)'
                n4 = 'Oiiii ;)'
                n5 = 'OOiii .'
                lista = [n1, n2, n3, n4, n5]
                escolhido = random.choice(lista)
                print('{}'.format(escolhido))

            elif sx == 'multiplique' or sx == 'multiplicaçao ' or sx == 'vezes' or sx == 'x' or sx == 'multipicar':
                ct1 = int(input('Primeiro numero: '))
                ct2 = int(input('Segundo numero: '))
                ct3 = ct1 * ct2
                print('_{}_X_{}_=_{}_'.format(ct1, ct2, ct3))

            elif sx == 'divida' or sx == 'divisao' or sx == 'dividir':

                dv1 = int(input('Primeiro numero: '))
                dv2 = int(input('Segundo numero: '))
                if dv1 == 0 and dv2 == 0:
                    print('0 dividido por 0 é igual a 0')
                elif dv1 >=1 and dv2 >=1:
                    dv3 = dv1 / dv2
                    print('_{}_/_{}_=_{}_'.format(dv1, dv2, dv3))

            elif sx == 'adiçao' or sx == '+' or sx == 'somar' or sx == 'some':
                mais = int(input('Primeiro valor: '))
                mais1 = int(input('Segundo valor: '))
                mais2 = mais + mais1
                print('_{}_+{}_=_{}'.format(mais, mais1, mais2))

            elif sx == 'obrigado' or sx == 'Obrigado' or sx == 'obj':
                print('De nada :), eu estou aqui para ajudar')

            elif sx == 'menos' or sx == 'subitraçao ' or sx == '-' or sx == 'subitraia':
                menos = int(input('Primeiro numero: '))
                menos1 = int(input('Segundo numero: '))
                menos2 = menos - menos1
                print('_{}_-_{}_=_{}_.'.format(menos, menos1, menos2))
            elif sx == 'versao' or sx == 'mostre me a versao' or sx == 'qual ea sua versao':
                print('{}'.format(vs1))
            elif sx == 'ano' or sx == 'qual ea data'or sx =='qual e a data' or sx == 'data' or sx == 'Que ano estamos' or sx == 'Que ano estamos ?' or sx == 'que ano estamos' or sx == 'que ano estamos?':
                from datetime import date

                atual = date.today().day
                atual2 = date.today().year
                atual3 = date.today().month
                print('{}/{}/{}'.format(atual, atual3, atual2))
            elif sx == 'mal' or sx == 'estou mal' or sx == 'estou trite':
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

            elif sx == 'nome' or sx == 'qual eo meu nome?' or sx == 'meu nome' or sx == 'qual eo meu nome ?':
                print('{}'.format(nome))


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

            elif sx == 'eq2grau':
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
                print(
                    '\033[31mDescupe-me,mas ainda não e possivel efetuar essa ação.\ntalvez em próximas atualizações seja possivel:).\033[m')

        from time import sleep

        for contagem in range(0, 3):
            sleep(1)
        print('\033[36m-' * 20)
        from time import sleep

        for contagem in range(0, 3):
            sleep(1)
        print('...')
        from time import sleep

        for contagem in range(0, 3):
            sleep(1)
        print('\033[31mDEGABIONTWESS\033[m')

        from time import sleep

        for contagem in range(0, 2):
            sleep(1)
        print('\033[4;36mLUCY 1.0.0')
        from time import sleep

        for contagem in range(0, 3):
            sleep(1)
        print('Lançamento lucy 0.6.0  15/02/2021\033[m')
        for n in range(1, 10):
            print('.', end=' ')
            sleep(0.5)
            print('[Criador Gabriel]')
        from time import sleep

        for contagem in range(0, 2):
            sleep(1)
        print('\033[36m-' * 40)

    def gxduino():
        print('ola')

    def versao2():
        versao1.show()

    def novidades2():
        novidades1.show()

    def fuca():
        funcao.show()
        print('funçao iniciada')

    def adic():
        adiçao.show()

    def somar():
        some = adiçao.num.text()
        some2 = adiçao.num2.text()
        float(some)
        float(some2)
        r = some + some2
        print(r)

    app = QtWidgets.QApplication([])
    janela = uic.loadUi('lucy_5.ui')
    segunda_tela = uic.loadUi('lucy_5_2.ui')
    tela_3 = uic.loadUi('lucy_cvs.ui')
    versao1 = uic.loadUi('versao.ui')
    novidades1 = uic.loadUi('novidades.ui')
    funcao = uic.loadUi('funca.ui')
    adiçao = uic.loadUi('adicao.ui')
    janela.entrar.clicked.connect(exibir_mensagem)
    segunda_tela.conversar.clicked.connect(lucy_cvs)
    segunda_tela.versao.clicked.connect(versao2)
    segunda_tela.novidades.clicked.connect(novidades2)
    segunda_tela.funcao.clicked.connect(fuca)
    adiçao.soma.clicked.connect(somar)
    janela.show()
    app.exec()

print('''[1]App duino
[2]App comando de voz
[3]Lucy conversa
[4]Exit''')
while True:
    gg=input('==: ')

    if gg=='1':
        print('App sendo iniciado')
        app_duino()

    elif gg=='2':
        print('Comando de voz sendo iniciado')
        print('''\033[34m Escolha, falando o numero:
        [2]ligar leds
        [3]desligar leds
        [4]sair''')
        import speech_recognition as sr

        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                print('Diga algo:')
                audio = r.listen(source)

                try:
                    text = 'banana'
                    text = r.recognize_google(audio, language='pt-BR')
                    print(f'Você disse: {text}')


                except:
                    print('Desculpe, não pude enterder oque voçê disse !!\nDiga novamente pvf ;)')

                if text == '2'or text=='22'or text=='2 2':
                    print('''               (4)Ligar led vermelho
                    (5)Liga led amarelo
                    (6)Ligar led verde
                    (7)Ligar led vermelho''')
                elif text=='5' or text =='55':
                    placa.digital[11].write(1)

                elif text == '4' or text=='44':
                    placa.digital[12].write(1)

                elif text=='6' or text=='66':
                    placa.digital[10].write(1)

                elif text=='7' or text=='77':
                    placa.digital[9].write(1)
                elif text=='3' or text=='33' or text=='3 3':
                    print('''                   (8)Desligar led vermelho
                    (9)Desligar led amarelo
                    (10)Desligar led verde
                    (11)Desligar led vermelho ''')

                elif text=='8' or text=='8':
                    placa.digital[12].write(0)

                elif text=='9' or text=='99':
                    placa.digital[11].write(0)

                elif text=='10' or text=='1010':
                    placa.digital[10].write(0)

                elif text=='11' or text =='1111':
                    placa.digital[9].write(0)

    elif gg=='3':
        print('LUCY 1.0.0')
        print('Nome:gabriel senha:daybion')
        app_lucy_1_0_0()
    elif gg=='4':
        print('Programa finalizado.')
        break

    else:
        print('Desculpe,comando invalido tente novamente.')