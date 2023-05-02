""" import pyttsx3
import speech_recognition as sr
import webbrowser """
from time import sleep as temp
import random
def audio_fala(msg):
    spekear=pyttsx3.init()
    voices=spekear.getProperty('voices')
    spekear.setProperty('voice',voices)
    rate=spekear.getProperty('rate')
    spekear.setProperty('rate',rate-25)
    spekear.say(msg)
    spekear.runAndWait()

triste = ['eu estou mal', 'eu estou triste', 'estou chateado', 'me sinto sozinho', 'eu estou me sentindo sozinho',
          'olha estou me sentido mal', 'estou cansado de passar por isso', 'eu queria morrer',
          'eu estou me sentido triste', 'eu so queria ser feliz', 'como eu faço para ser feliz ?', 'estou muito mal',
          'eu estou muito mal', 'eu estou muito triste', 'estou cansado de me sentir sozinho', 'eu queria ser feliz',
          'como faço para me sentir melhor', 'ninguem me ama', 'ninguem gosta de mim', 'eu so queria nao estar mal',
          'me ajuda a nao ficar mal pfv', 'que conversar ?', 'vamos conversar estou mal', 'eu estou triste ',
          'eu estou mal ', 'eu estou chateda']

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
    print('__Lucy 1.3.0__')
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
        audio_fala('Você sabia que o meu criador se chama Gabriel')
    elif nome == 'lucy' or nome == 'Lucy' or nome == ' lucy' or nome == ' Lucy':
        print('Nossa,o meu nome tambem e lucy ksksksk ')
        audio_fala('Nossa, o meu nome tambem é luci ksksksk')
    elif nome == 'ana' or nome == 'gabriela' or nome == 'lucia' or nome == 'bruna' or nome == 'lucas' or nome == 'matheus' or nome == 'andreia' or nome == 'fabio' or nome == 'Fabio' or nome == ' fabio':
        print('Você possuí um nome bonito :)')
        audio_fala('Você possuí um nome bonito')
    else:
        print('Eu gostei do seu nome !')
        audio_fala('Eu gostei do seu nome')
    print(f'Seja bem vindo(a){nome}.')
    audio_fala(f'Seja bem vindo {nome}')
    print('Digite algo para começar. Tudo em minusculo .')
    audio_fala('Digite algo para começar. Tudo em minusculo.')
    print('Digite help para saber oque eu posso fazer')
    audio_fala('Digite relp para saber oque eu posso fazer')
    '''from pygame import mixer

    mixer.init()
    mixer.music.load('lcms.mp3')
    mixer.music.play()
    from time import sleep
    for contagem in range(0, 2):
        sleep(7.3)'''
    ajuda = '''[pause-cont]-[fale]-[sair]-[pesquisar]-[music]-[oii]-[divida]-[help]-[multiplique] 
[somar]-[obrigado]-[menos]-[versao]-[qual e a data]-[estou mal]-[meu nome]
[tabuada]-[raiz]-[media]-[lucy1]-[eq2grau]-[conversar]-[piada]-[mudar meu nome]
[novidade]'''
    # Varialvel de versão
    vs1 = '1.3.0 OFICIAL'
    from pygame import mixer

    mixer.init()
    mixer.music.load('lc_music/History of iPhone 2007 to 2020 Evolution(MP3_70K) - Copia.mp3')

    mixer.music.play()
    mixer.music.set_volume(4)
    print('DEGABIONTWESS')
    print('')
    print('Para sair digite sair')
    while True:  #

        sx = str(input('==: '))

        if sx == nome34:
            print('Oi :/')
            audio_fala('Oi emogi meio chateado')

        elif sx == 'pause' or sx =='p' :
            mixer.music.pause()

        elif sx == 'cont' or sx =='c':
            mixer.music.unpause()

        elif sx == 'fale':
            kl = input('Digite oque você deseja que eu fale: ')
            spekear = pyttsx3.init()
            voices = spekear.getProperty('voices')
            spekear.setProperty('voice', voices)
            rate = spekear.getProperty('rate')
            spekear.setProperty('rate', rate - 25)
            spekear.say(kl)
            spekear.runAndWait()
            print(kl)


        elif sx == '':
            print('Desculpe mas vc não digitou nada :(')
            audio_fala('Desculpe, mas você não digitou nada.')

        elif sx == 'help':
            print(ajuda)

        elif sx == 'novidade':
            print('Novidades 1.3.0')
            print('''Botão novidade.
Tela inicial.
Lucy arduino-incompleto.
Lucy voice-incompleto.''')

        elif sx == 'mudar meu nome':
            print('Mude seu nome, digite como devo chamar-lo(a)')
            audio_fala('Mude seu nome, digite como devo chamar lo ')
            nome = input('==: ')


        elif sx == 'sair':
            break

        elif sx == 'piada' or sx == 'conte uma piada' or sx == 'conte me uma piada' or sx == 'piadas':
            n56 = 'Em primeiro lugar, o que o pato falou para a pata ? "vem qua" '
            n57 = 'Então, você sabe qual a fórmula da água benta? H Deus o.'
            n58 = '''Assim, por que Napoleão era sempre chamado para as festas na França?
                        Então, é porque ele era Bom Na Party (Bonaparte)'''
            n59 = '''Então, o que o pagodeiro foi fazer na igreja? Foi cantar Pá God'''
            n60 = '''Então quando foi que os americanos comeram carne pela primeira vez?
                         Quando chegou Cristóvão Com Lombo.'''
            lista = [n56, n57, n58, n59, n60]
            escolhido = random.choice(lista)
            print('{}'.format(escolhido))
            if escolhido == n56:
                audio_fala('Em primeiro lugar, o que o pato falou para a pata ? vem qua ')
            elif escolhido == n57:
                audio_fala('Então, você sabe qual a fórmula da água benta? H Deus o')
            elif escolhido == n58:
                audio_fala(
                    'Assim, por que Napoleão era sempre chamado para as festas na França? Então, é porque ele era Bom Na Party')
            elif escolhido == n59:
                audio_fala('Então, o que o pagodeiro foi fazer na igreja? Foi cantar Pá God')
            elif escolhido == n60:
                audio_fala(
                    'Então quando foi que os americanos comeram carne pela primeira vez? Quando chegou Cristóvão Com Lombo.')

        elif sx == triste[0] or sx == triste[1] or sx == triste[2] or sx == triste[3] or sx == triste[4] or sx == \
                triste[5] or sx == triste[6] or sx == triste[7] or sx == triste[8] or sx == triste[9] or sx == triste[
            10] or sx == triste[11] or sx == triste[12] or sx == triste[13] or sx == triste[14] or sx == triste[
            15] or sx == triste[16] or sx == triste[17] or sx == triste[18] or sx == triste[19] or sx == triste[
            20] or sx == triste[21] or sx == 'conversar' or sx == 'conversa' or sx == 'quero conversar':

            ssdfr5 = input('Você deseja converar comigo {} ?'.format(nome))
            audio_fala(f'Você deseja conversar comigo {nome}')
            if ssdfr5 == 'sim' or ssdfr5 == 's':
                print('Otimo!!!')
                audio_fala('Otimo')
                print('Meu nome é Lucy, muito prazer', nome, ':)')
                audio_fala(f'Meu nome é luci, muito prazer {nome} ')
                nome3 = 'mal'
                chute = input('Como você esta ?:')
                audio_fala('Como você está ')
                s1 = 'sim'
                if chute == nome3:
                    pq = input('Você deseja conversar sobre isso ? ==: ')
                    audio_fala('Você deseja conversar sobre isso ?')
                    if pq == s1 or pq == 's':
                        n = input('Oque ouve pra você esta assim ? ==: ')
                        print('Então você esta assim por causa de ', n, )
                        audio_fala(f'Então você está assim por conta de {n}')
                        from time import sleep

                        for contagem in range(0, 5):
                            sleep(1)

                        print(
                            'Não fique assim :(.Olha eu sei que as coisas podem estar dificies, mas tudo ira melhorar')
                        audio_fala(
                            'Não fique assim,Olha eu sei que as coisas podem estar dificies, mas tudo ira melhorar ')
                    else:
                        print('Qual quer coisa pode contar comigo')
                        audio_fala('Qual quer coisa pode contar comigo')

                else:
                    print('Otimo :)')
                    audio_fala('Ótimo')
                for contagem in range(0, 8):
                    sleep(1)

                print('---')
                # variaveis do jogo.
                x = 'sim' or 's'
                chute = input('Você que jogar um jogo comigo ? ')
                audio_fala('Você que jogar um jogo comigo ')
                if chute == 's' or chute == 'sim':
                    print(
                        'O jogo funciona assim,\nvocê vai ter que adivinhar um numero que eu estou pensando de 1 a 9:')

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
                    print('Fim de jogo Probiedade GX')

                else:
                    print('Tudo bem então :(')
                audio_fala('Qual tipo de música você gosta')
                n1 = str(input('Qual tipo de musica voçê gosta ?==: '))
                audio_fala('Qual é a sua comida favorita ? ')
                n2 = str(input('Qual é a sua comida favorita ?==: '))
                audio_fala('Qual é a sua cor favorita')
                n3 = str(input('Qual é a sua cor favorita ?==: '))
                audio_fala('Qual é o seu jogo favorito')
                n4 = str(input('Qual é o seu jogo favorito?==: '))

                lista = [n1, n2, n4]
                escolhido = random.choice(lista)
                print(
                    'Eu tambem gosto de {}, mas eu não posso usufruir como eu dejesaria, pois o meu criador não me deu essa opção ksksskskssk'.format(
                        escolhido))
                audio_fala(
                    f'Eu também gosto de {escolhido}, mas eu não posso usufruir como eu dejesaria, pois o meu criador não me deu essa opção')
                if n1 == 'rock' or n1 == ' rock':
                    audio_fala('Você gosta de rock  que legal')
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

                                print('Poxa kskskskkks...')
                        else:
                            print('Poxa mas que pena, pois eu gosto muito deles...')



            else:
                print('poxa:(')

        elif sx == 'pesquisar' or sx == 'Pesquisar' or sx == 'pesquise' or sx == 'Pesquise':
            audio_fala('Para sair das pesquisar digite egiti')
            print('Para sair das pesquisas digite: exit')
            audio_fala('Oque eu devo pesquisar')
            print('Oque eu devo pesquisar ?')

            import webbrowser

            while True:

                pg = input('==: ')
                if pg == 'exit':
                    print(f'{nome} vc acabou de sair da pesquisa')
                    break
                else:
                    pesquisar = ('https://www.google.com.br/search?q=')
                    pesquisng = (pesquisar + pg)
                    webbrowser.open(pesquisng)


        elif sx == 'musicas' or sx == 'play' or sx == 'music' or sx == 'tocar':
            while True:
                print('Musicas')
                msc = input('Digite play para iniciar uma musica/para sair digite sair: ')
                if msc == 'play':
                    print('''[1]Artic Monkens
[2]Imortal
[3]The week
[4]Dragon ball
[5]I Follow Rivers
[6]kostromin
[7]Måneskin
[8]Harry Styles
[9]I_m So Sorry
[10]sair
''')

                    while True:
                        esc78 = input('==: ')
                        if esc78 == '1':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load('lc_music/mp3 .mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break


                        elif esc78 == '2':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load('lc_music/Immortals(MP3_160K).mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')
                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break

                        elif esc78 == '3':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load(
                                'lc_music/The Weeknd - I Feel It Coming ft. Daft Punk (Offic(MP3_160K).mp3')
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
                            mixer.music.load('lc_music/dg.mp3')
                            mixer.music.play()
                            print('Digite stop para parar a musica.')
                            ggh = input('==: ')
                            if ggh == 'pause' or ggh == 'stop':
                                mixer.music.stop()
                                break

                            while mixer.music.get_busy() == True: continue

                        elif esc78 == '5':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load(
                                'lc_music/I Follow Rivers - Lykke Li (La Vie d_Adèle_La Vida de Adele)(MP3_320K).mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break


                        elif esc78 == '6':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load(
                                'lc_music/kostromin _ Моя голова винтом (My head is spinning like a screw) (Official Video)(MP3_160K).mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break

                        elif esc78 == '7':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load('lc_music/Måneskin - I WANNA BE YOUR SLAVE (Official Video)(MP3_320K).mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break

                        elif esc78 == '8':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load('lc_music/Harry Styles - Golden (Official Video)(MP3_160K).mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break


                        elif esc78 == '9':
                            from pygame import mixer

                            mixer.init()
                            mixer.music.load('lc_music/I_m So Sorry(MP3_160K) - Copia.mp3')
                            mixer.music.play()
                            print('Para parar a musica digite stop')

                            ggh = input('==: ')
                            if ggh == 'stop' or ggh == 'pausar':
                                mixer.music.stop()
                                break


                        elif esc78 == '10':
                            break



                elif msc == 'sair':
                    break
                else:
                    print('Comando invalido digite oque foi pedido.')

        elif sx == 'oii' or sx == 'OII' or sx == 'eai' or sx == 'oie' or sx == 'Oie' or sx == 'oiii' or sx == 'oiiii':
            n1 = 'Eai ;)'
            n2 = 'oii'
            n3 = 'Oie:)'
            n4 = f'Oi {nome} ;)'
            n5 = 'Oi meu bem .'
            lista = [n1, n2, n3, n4, n5]
            escolhido = random.choice(lista)
            print('{}'.format(escolhido))
            if escolhido == n1:
                audio_fala('Eai')
            elif escolhido == n2:
                audio_fala('Oii')
            elif escolhido == n3:
                audio_fala('Oiee')
            elif escolhido == n4:
                audio_fala(f'Oi, {nome}')
            elif escolhido == n5:
                audio_fala('Oi meu bem')

        elif sx == 'multiplique' or sx == 'multiplicaçao ' or sx == 'vezes' or sx == 'x' or sx == 'multipicar':
            ct1 = int(input('Primeiro numero: '))
            ct2 = int(input('Segundo numero: '))
            ct3 = ct1 * ct2
            print('_{}_X_{}_=_{}_'.format(ct1, ct2, ct3))
            audio_fala(f'{ct1} vezes {ct2} é igual a {ct3}')

        elif sx == 'divida' or sx == 'divisao' or sx == 'dividir':

            dv1 = int(input('Primeiro numero: '))
            dv2 = int(input('Segundo numero: '))
            if dv1 == 0 and dv2 == 0:
                print('0 dividido por 0 é igual a 0')
                audio_fala('Zero dividido por zero é igual a zero')
            elif dv1 >= 1 and dv2 >= 1:
                dv3 = dv1 / dv2
                print('_{}_/_{}_=_{}_'.format(dv1, dv2, dv3))
                audio_fala(f'{dv1} dividido por {dv2} é igual a {dv3}')

        elif sx == 'adiçao' or sx == '+' or sx == 'somar' or sx == 'some':
            mais = int(input('Primeiro valor: '))
            mais1 = int(input('Segundo valor: '))
            mais2 = mais + mais1
            print('_{}_+{}_=_{}'.format(mais, mais1, mais2))
            audio_fala(f'{mais} mais {mais2} é igual a {mais2}')

        elif sx == 'obrigado' or sx == 'Obrigado' or sx == 'obj' or sx == 'obrigada':
            o = 'De nada :), eu estou aqui para ajudar'
            o2 = 'De nada meu bem :)'
            o3 = f'Que isso {nome}, eu que agradeço :)'
            mi = [o, o2, o3]
            ra = random.choice(mi)

            if ra == o:
                audio_fala('De nada, eu estou aqui para ajudar')
            elif ra == o2:
                audio_fala('De nada meu bem ')
            elif ra == o3:
                audio_fala(f'Que isso {nome}, eu que agradeço ')
            print(ra)

        elif sx == 'menos' or sx == 'subitraçao ' or sx == '-' or sx == 'subitraia':
            menos = int(input('Primeiro numero: '))
            menos1 = int(input('Segundo numero: '))
            menos2 = menos - menos1
            audio_fala(f'{menos} menos {menos1} é igual a {menos2}')
            print('_{}_-_{}_=_{}_.'.format(menos, menos1, menos2))

        elif sx == 'versao' or sx == 'mostre me a versao' or sx == 'qual ea sua versao':
            print('{}'.format(vs1))

        elif sx == 'ano' or sx == 'qual ea data' or sx == 'qual e a data' or sx == 'data' or sx == 'Que ano estamos' or sx == 'Que ano estamos ?' or sx == 'que ano estamos' or sx == 'que ano estamos?':
            from datetime import date

            atual = date.today().day
            atual2 = date.today().year
            atual3 = date.today().month
            audio_fala(f'Hoje é dia {atual}, do mês {atual3}, no ano de {atual2} ')
            print('{}/{}/{}'.format(atual, atual3, atual2))
        elif sx == 'mal' or sx == 'estou mal' or sx == 'estou trite':
            while True:
                audio_fala('Como você está ')
                cmvc = input('Como você esta ?: ')
                if cmvc == 'bem' or cmvc == 'otimo' or cmvc == 'otima':
                    audio_fala('Mas que maravilha')
                    print('Mas que maravilha :)')
                    break
                elif cmvc == 'mal' or cmvc == 'triste':
                    audio_fala('Você que conversar sobre isso')
                    pq = input('Você que conversar sobre isso ?: ')
                    if pq == 'n' or pq == 'nao':
                        audio_fala('Tudo bem eu entendo, Qualquer coisa que você precisar pode contar comigo')
                        print('Tudo bem eu entendo:(. Qual quer coisa que você precisar pode contar comigo.')
                        break
                    elif pq == 's' or pq == 'sim':
                        audio_fala('Oque houve para você está assim')
                        sç = input('Oque houve para você esta assim ?: ')
                        from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    audio_fala('Eu entendo isso')
                    print('Eu entendo isso...')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    audio_fala('Tente não pensar muito sobre isso')
                    print('Tente não pensar muito sobre isso.')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    audio_fala('Já que é algo que lhe faz mal')
                    print('Já que é algo que lhe faz mal.')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    audio_fala('Se isso ficar muito na sua cabeça, tente fazer algo para relaxar')
                    print('Se isso ficar muito na sua cabeça, tente fazer algo para relaxar.')
                    sleep(1)
                    audio_fala('Se eu pudesse eu lhe abraçaria')
                    print('Se eu pudesse eu lhe abraçaria :(')
                    from time import sleep

                    for contagem in range(0, 2):
                        sleep(1)
                        for n in range(1, 2):
                            print('.', end='')
                            sleep(1.5)
                    print('.')
                    audio_fala('Não se preucupe tudo irá melhorar')
                    print('Não se preucupe tudo irá melhorar.:)')
                    break

        elif sx == 'nome' or sx == 'qual eo meu nome?' or sx == 'meu nome' or sx == 'qual eo meu nome ?':
            audio_fala(f'O seu nome é {nome}')
            print('O seu nome é {}'.format(nome))


        elif sx == 'tabuada' or sx == ' tabuada' or sx == 'tabu':
            # MULTIPLICAÇÃO 2.0
            num = int(input('Digite um valor: '))
            for c in range(1, 11):
                print('{} x {:2} = {}'.format(num, c, num * c))

        elif sx == 'raiz' or sx == 'raiz quadrada' or sx == ' raiz' or sx == 'Raiz':
            n66 = int(input("Digite um valor: "))
            if n66 == 0:
                audio_fala('A raiz de zero é zero')
                print('A raiz de zero é zero')
            else:
                r = n66 ** (1 / 2)
                audio_fala(f'A raiz de {n66} é igual a {r} ')
                print('A raiz de {} é igual a {}'.format(n66, r))

        elif sx == 'media' or sx == 'media ' or sx == 'Media':
            ny = float(input('Primeiro numero: '))
            ny1 = float(input('Segundo numero: '))
            if ny == 0 and ny1 == 0:
                audio_fala('A média é igual a zero')
                print('A média é igual a zero')

            else:
                md = (ny + ny1) / 2
                audio_fala(f'A média entre {ny} e {ny1} é igual a {md}')
                print('A média entre {} e {} é igual a {}'.format(ny, ny1, md))

        elif sx == 'lucy1.0' or sx == 'lucy1' or sx == 'lucy 0.1.0' or sx == 'lucy 1.0' or sx == 'lucy 1':
            print('_' * 15)
            print('LUCY 1.0 apha sendo iniciada...')
            for contagem in range(1, 7):
                sleep(0.5)
                print('.', end='')
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
            audio_fala('Seja bem vindo ou bem vinda ao sistema automatico de equação de segundo grau')
            print('Seja bem vindo ao sistema automatico de equação de 2 grau. ')

            print('.')
            while True:
                print('Informe o A,B e C:')
                a = int(input('A.==: '))
                b = int(input('B.==: '))
                c = int(input('C.==: '))

                delt = (b ** 2) - 4 * a * c
                audio_fala(f'O valor de delta é {delt}')
                print(f'O valor de delta é {delt} ')

                def x():
                    print('Calculando o valor de x.')
                    x1 = (((-b) + (delt ** (1 / 2))) / (2 * a))
                    x2 = (((-b) - (delt ** (1 / 2))) / (2 * a))
                    audio_fala(f'X1 é igual a{x1}, e X2 é igual a {x2}')
                    print(f'x1= {x1}, x2= {x2}')

                x()
                res = str(input('Deseja continuar ?(s/n)'))
                if res == 's':
                    print('Okay')
                elif res == 'n':
                    break
            print('FIM :)')

        else:
            ds = 'Descupe-me,mas ainda não e possivel efetuar essa ação.talvez em próximas atualizações seja possivel:).'
            ds2 = 'Você digitou algum comando errado'
            ds3 = 'Desculpe-me comando invalido'
            ds4 = 'Eu ainda não posso fazer oque você deseja'
            ds5 = 'Digite help para ver oque eu posso fazer'
            ll = [ds, ds2, ds3, ds4, ds5]
            bs = random.choice(ll)

            print(bs)
    from time import sleep

    for contagem in range(0, 3):
        sleep(1)
    print('-' * 20)
    from time import sleep

    for contagem in range(0, 3):
        sleep(1)
    print('...')
    from time import sleep

    for contagem in range(0, 3):
        sleep(1)
    print('DEGABIONTWESS')

    from time import sleep

    for contagem in range(0, 2):
        sleep(1)
    print('LUCY 1.3.0')
    from time import sleep

    for contagem in range(0, 3):
        sleep(1)
    print('Lançamento lucy 1.3.0  16/01/22')
    for n in range(1, 10):
        print('.', end=' ')
        sleep(0.5)
    print('[Criador Gabriel]')
    from time import sleep

    for contagem in range(0, 2):
        sleep(1)
    print('-' * 40)

