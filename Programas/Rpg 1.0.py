from random import choice
from time import sleep
#funções
def dega(g):
    print(g,end='')
    sleep(0.3)

print('=-=-'*10+'=')
sleep(0.2)
for n in range(7):
    print('.',end='')
    sleep(0.7)
print('.')
print('Bem vindo(a) ao Rpg 1.0 , espero que goste:)')
print('''Escolha seu modo de jogo:
[1]Very hard-(Vida personagem 80/Inimigo 120/Dano baixo/Mernor defesa
[2]Hard-(Vida personagem 80/Inimigo 100/Dano dormal/Menor defesa)
[3]Normal-(Tudo igual)
[4]Easy-(Vida personagem 120/Inimigo 80/Dano alto, maior defesa)
    ''')
while True:
    dificuldade=input('==: ')
    if dificuldade=='3':
        nome_do_personagem=input('Digite o nome do seu personagem ==: ')
        while True:
            s_n=input('È esse nome que você deseja ter :)? s/n: ')
            if s_n=='s' or s_n=='S' or s_n=='sim':
                break

            elif s_n =='n'or s_n=='N' or s_n=='nao' or s_n=='não':
                nome_do_personagem=input('Digite o seu novo nome: ')

            else:
                print('Desculpe, escreva s para sim, e n para não.')
        print('-'*37)
        print(f'Olá seja bem vindo(a) {nome_do_personagem}')
        print('-'*37)
        print('-'*13)
        dega('D'),dega('E'),dega('G'),dega('A'),dega('B'),dega('I'),dega('O'),dega('N'),dega('T'),dega('W'),dega('E'),dega('S'),dega('S')
        print('')
        print('-'*13)
        print('''Escolha a arma do seu personagem:
[1]Espada /dano máximo[10] nível difícil.
[2]Cajado magico /dano máximo[7] nível normal.
[3]Arco e flecha /dano máximo[5] nível fácil.
        ''')
        while True:
            arma=input('Escolha a arma do seu persoganagem: 1 , 2 ou 3: ')
            if arma=='1' or arma=='2' or arma=='3':
                break
            else:
                print('Desculpe mas escolha entre 1 2 ou 3:')
        while True:
            sim=input(f'È essa arma que você deseja {nome_do_personagem} ? s/n: ')
            if sim=='n':
                while True:
                    arma=input('Escolha novamente a sua arma: 1/2/3: ')
                    if arma=='1'or arma=='2' or arma=='3':
                        break
                    else:
                        print('Você digitou errado')
            elif sim=='s':
                break
            else:
                print('Desculpe comando invalido escreva s ou n:')
        if arma =='1':
            arma='Espada'
            espada=1
        elif arma=='2':
            arma='Cajado magico'
            cajado=2
        elif arma=='3':
            arma='Arco e flexa'
            arco=3
        print(f'Sua arma é : {arma}')

        ni1='Lucas'
        ni2='Sarah'
        ni3='Lucy'
        ni4='Gustavo'
        ni5='Noxy'
        l=[ni1,ni2,ni3,ni4,ni5]
        inimigo= choice(l)

        espada_inimigo='Espada'
        cajado_inimigo='Cajado mágico'
        arco_inimigo='Arco e flexa'
        k=[cajado_inimigo,arco_inimigo,espada_inimigo]
        Arma_inimigo=choice(k)
        print(f'O inimigo escolhido foi {inimigo}')
        print(f'A arma esolhida foi {Arma_inimigo}')
        print('Carregando jogo.')
        for b in range(7):
            print('.',end='')
            sleep(0.7)
        print('.')
        # Comando de dano das armas
        #Espada
        vida_inimigo=100.0
        vida_persoganem=100.0
        while True:
            print(f'''Vida:{vida_persoganem}-------------------------------Vida:{vida_inimigo}
Nome:{nome_do_personagem}------------------------------Nome:{inimigo}
Arma={arma}-------------------------------Arma:{Arma_inimigo}
        ''')
            if vida_persoganem==0:
                print(f'Você morreu {nome_do_personagem}')
                sleep(2)
                print('GAME OVER')
                break
            elif vida_inimigo==0:
                print('Parabens você venceu ')
                print('Game over')
                break
            que=input('Digite "d" para jogar o dado.==: ')

            if que=='at':


                    print(f'o dano é ={dano_espada_escolhido}')
            elif que=='danoi':
                vida_inimigo=vida_inimigo-50
                print('perdeu 50 de vida')
            elif que=='danoeu':
                vida_persoganem=vida_persoganem-50
                print('Eu perdi 50 de vida')
            elif que=='d':
                dado=1
                dado2=2
                dado3=3
                dado4=4
                dado5=5
                w=[dado,dado2,dado3,dado4,dado5]
                dado_sorteado=choice(w)
                print(f'Você tirou:{dado_sorteado}')
                sleep(0.7)
                dade=1
                dade2=2
                dade3=3
                dade4=4
                dade5=5
                i=[dade,dade2,dade3,dade4,dade5]
                dado_sorteado_inimigo=choice(i)
                print(f'{inimigo} tirou :{dado_sorteado_inimigo}')
                banana='oi'
                if banana=='':
                    print('oi')
                elif   dado_sorteado>dado_sorteado_inimigo:
                    if arma=='Espada':
                        dano_espada = 1
                        dano_espada2 = 2
                        dano_espada3 = 3
                        dano_espada4 = 4
                        dano_espada5 = 5
                        dano_espada6 = 6
                        dano_espada7 = 7
                        dano_espada8 = 8
                        dano_espada9 = 9
                        dano_espada10 = 10
                        r = [dano_espada, dano_espada2, dano_espada3, dano_espada4, dano_espada5, dano_espada6, dano_espada7,
                             dano_espada8, dano_espada9, dano_espada10]
                        dano_espada_escolhido = choice(r)
                        print(f'o numero do dado deu {dano_espada_escolhido}')
                        if dano_espada_escolhido == 9:
                            dano_espada_escolhido = dano_espada9

                        elif dano_espada_escolhido == 10:
                            dano_espada_escolhido = dano_espada10

                        elif dano_espada_escolhido == 8:
                            dano_espada_escolhido = 6.9

                        elif dano_espada_escolhido == 7:
                            dano_espada_escolhido = 5.6

                        elif dano_espada_escolhido == 6:
                            dano_espada_escolhido = 4.4

                        elif dano_espada_escolhido == 5:
                            dano_espada_escolhido = 3.1

                        elif dano_espada_escolhido == 4:
                            dano_espada_escolhido = 2.1

                        elif dano_espada_escolhido == 3:
                            dano_espada_escolhido = 1.5

                        elif dano_espada_escolhido == 2:
                            dano_espada_escolhido = 1

                        elif dano_espada_escolhido == 1:
                            dano_espada_escolhido = 0.6
                        vida_inimigo = vida_inimigo - dano_espada_escolhido
                        print(f'{inimigo} perdeu {dano_espada_escolhido}')

                    elif arma=='Cajado magico':
                        dano_caado = 1
                        dano_cajado2 = 2
                        dano_cajado3 = 3
                        dano_cajado4 = 4
                        dano_cajado5 = 5
                        dano_cajado6 = 6
                        dano_cajado = 7
                        fr = [dano_caado, dano_cajado, dano_cajado2, dano_cajado3, dano_cajado4, dano_cajado5, dano_cajado6]
                        dano_cajado_escolhido = choice(fr)
                        print(f'O dado caiu {dano_cajado_escolhido}')
                        if dano_cajado_escolhido == 7:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 6:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 5:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 4:
                            dano_cajado_escolhido = 3.0

                        elif dano_cajado_escolhido == 3:
                            dano_cajado_escolhido = 2.3

                        elif dano_cajado_escolhido == 2:
                            dano_cajado_escolhido = 1.3

                        elif dano_cajado_escolhido == 1:
                            dano_cajado_escolhido = 0.8

                        vida_inimigo= vida_inimigo - dano_cajado_escolhido
                        print(f'{inimigo} perdeu:{dano_cajado_escolhido}')

                    elif arma=='Arco e flexa':
                        dano_arco = 1
                        dano_arco2 = 2
                        dano_arco3 = 3
                        dano_arco4 = 4
                        dano_arco5 = 5
                        ty = [dano_arco, dano_arco2, dano_arco3, dano_arco4, dano_arco5]
                        dano_arco_escolhido = choice(ty)
                        print(f'Vc tirou no dado {dano_arco_escolhido}')
                        if dano_arco_escolhido == 5:
                            dano_arco_escolhido = 5

                        elif dano_arco_escolhido == 4:
                            dano_arco_escolhido = 4

                        elif dano_arco_escolhido == 3:
                            dano_arco_escolhido = 3

                        elif dano_arco_escolhido == 2:
                            dano_arco_escolhido = 1.7

                        elif dano_arco_escolhido == 1:
                            dano_arco_escolhido = 0.9
                        vida_inimigo=vida_inimigo-dano_arco_escolhido
                        print(f'{inimigo} perdeu:{dano_cajado_escolhido}')

                elif dado_sorteado<dado_sorteado_inimigo:
                    if Arma_inimigo=='Espada':
                        dano_espada = 1
                        dano_espada2 = 2
                        dano_espada3 = 3
                        dano_espada4 = 4
                        dano_espada5 = 5
                        dano_espada6 = 6
                        dano_espada7 = 7
                        dano_espada8 = 8
                        dano_espada9 = 9
                        dano_espada10 = 10
                        r = [dano_espada, dano_espada2, dano_espada3, dano_espada4, dano_espada5, dano_espada6, dano_espada7,
                             dano_espada8, dano_espada9, dano_espada10]
                        dano_espada_escolhido = choice(r)
                        print(f'o numero do dado do {inimigo} deu {dano_espada_escolhido}')
                        if dano_espada_escolhido == 9:
                            dano_espada_escolhido = dano_espada9

                        elif dano_espada_escolhido == 10:
                            dano_espada_escolhido = dano_espada10

                        elif dano_espada_escolhido == 8:
                            dano_espada_escolhido = 6.9

                        elif dano_espada_escolhido == 7:
                            dano_espada_escolhido = 5.6

                        elif dano_espada_escolhido == 6:
                            dano_espada_escolhido = 4.4

                        elif dano_espada_escolhido == 5:
                            dano_espada_escolhido = 3.1

                        elif dano_espada_escolhido == 4:
                            dano_espada_escolhido = 2.1

                        elif dano_espada_escolhido == 3:
                            dano_espada_escolhido = 1.5

                        elif dano_espada_escolhido == 2:
                            dano_espada_escolhido = 1

                        elif dano_espada_escolhido == 1:
                            dano_espada_escolhido = 0.6
                        vida_persoganem=vida_persoganem-dano_espada_escolhido
                        print(f'Você perdeu:{dano_espada_escolhido}')

                    elif Arma_inimigo=='Cajado mágico':
                        dano_caado = 1
                        dano_cajado2 = 2
                        dano_cajado3 = 3
                        dano_cajado4 = 4
                        dano_cajado5 = 5
                        dano_cajado6 = 6
                        dano_cajado = 7
                        fr = [dano_caado, dano_cajado, dano_cajado2, dano_cajado3, dano_cajado4, dano_cajado5, dano_cajado6]
                        dano_cajado_escolhido = choice(fr)
                        print(f'O {inimigo} jogou o dado e caiu {dano_cajado_escolhido}')
                        if dano_cajado_escolhido == 7:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 6:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 5:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 4:
                            dano_cajado_escolhido = 3.0

                        elif dano_cajado_escolhido == 3:
                            dano_cajado_escolhido = 2.3

                        elif dano_cajado_escolhido == 2:
                            dano_cajado_escolhido = 1.3

                        elif dano_cajado_escolhido == 1:
                            dano_cajado_escolhido = 0.8
                        vida_persoganem=vida_persoganem-dano_cajado_escolhido
                        print(f'Você perdeu:{dano_cajado_escolhido}')

                    elif Arma_inimigo=='Arco e flexa':
                        dano_arco = 1
                        dano_arco2 = 2
                        dano_arco3 = 3
                        dano_arco4 = 4
                        dano_arco5 = 5
                        ty = [dano_arco, dano_arco2, dano_arco3, dano_arco4, dano_arco5]
                        dano_arco_escolhido = choice(ty)
                        print(f'O {inimigo} {dano_arco_escolhido}')
                        if dano_arco_escolhido == 5:
                            dano_arco_escolhido = 5

                        elif dano_arco_escolhido == 4:
                            dano_arco_escolhido = 4

                        elif dano_arco_escolhido == 3:
                            dano_arco_escolhido = 3

                        elif dano_arco_escolhido == 2:
                            dano_arco_escolhido = 1.7

                        elif dano_arco_escolhido == 1:
                            dano_arco_escolhido = 0.9
                        vida_persoganem=vida_persoganem-dano_arco_escolhido
                        print(f'Você perdeu:{dano_arco_escolhido}')
            elif que =='aj':
                print('Opa esse comando erra para ter saido na beta ')
            elif que=='aq':
                print('ops desculpa isso é opção de desenvolvedor')

    elif dificuldade=='1':
        print('Very Hard.')

    elif dificuldade=='2':
        print('Hard')
        nome_do_personagem = input('Digite o nome do seu personagem ==: ')
        while True:
            s_n = input('È esse nome que você deseja ter :)? s/n: ')
            if s_n == 's' or s_n == 'S' or s_n == 'sim':
                break

            elif s_n == 'n' or s_n == 'N' or s_n == 'nao' or s_n == 'não':
                nome_do_personagem = input('Digite o seu novo nome: ')

            else:
                print('Desculpe, escreva s para sim, e n para não.')
        print('-' * 37)
        print(f'Olá seja bem vindo(a) {nome_do_personagem}')
        print('-' * 37)
        print('-' * 13)
        dega('D'), dega('E'), dega('G'), dega('A'), dega('B'), dega('I'), dega('O'), dega('N'), dega('T'), dega(
            'W'), dega('E'), dega('S'), dega('S')
        print('')
        print('-' * 13)
        print('''Escolha a arma do seu personagem:
[1]Espada /dano máximo[10] nível difícil.
[2]Cajado magico /dano máximo[7] nível normal.
[3]Arco e flecha /dano máximo[5] nível fácil.
                ''')
        while True:
            arma = input('Escolha a arma do seu persoganagem: 1 , 2 ou 3: ')
            if arma == '1' or arma == '2' or arma == '3':
                break
            else:
                print('Desculpe mas escolha entre 1 2 ou 3:')
        while True:
            sim = input(f'È essa arma que você deseja {nome_do_personagem} ? s/n: ')
            if sim == 'n':
                while True:
                    arma = input('Escolha novamente a sua arma: 1/2/3: ')
                    if arma == '1' or arma == '2' or arma == '3':
                        break
                    else:
                        print('Você digitou errado')
            elif sim == 's':
                break
            else:
                print('Desculpe comando invalido escreva s ou n:')
        if arma == '1':
            arma = 'Espada'
            espada = 1
        elif arma == '2':
            arma = 'Cajado magico'
            cajado = 2
        elif arma == '3':
            arma = 'Arco e flexa'
            arco = 3
        print(f'Sua arma é : {arma}')

        ni1 = 'Lucas'
        ni2 = 'Vitória'
        ni3 = 'Lucy'
        ni4 = 'Gustavo'
        ni5 = 'Noxy'
        l = [ni1, ni2, ni3, ni4, ni5]
        inimigo = choice(l)

        espada_inimigo = 'Espada'
        cajado_inimigo = 'Cajado mágico'
        arco_inimigo = 'Arco e flexa'
        k = [cajado_inimigo, arco_inimigo, espada_inimigo]
        Arma_inimigo = choice(k)
        print(f'O inimigo escolhido foi {inimigo}')
        print(f'A arma esolhida foi {Arma_inimigo}')
        print('Carregando jogo.')
        for b in range(7):
            print('.', end='')
            sleep(0.7)
        print('.')
        # Comando de dano das armas
        # Espada
        vida_inimigo = 100.0
        vida_persoganem = 80.0
        while True:
            print(f'''Vida:{vida_persoganem}-------------------------------Vida:{vida_inimigo}
Nome:{nome_do_personagem}------------------------------Nome:{inimigo}
Arma={arma}-------------------------------Arma:{Arma_inimigo}
                ''')
            if vida_persoganem < 0:
                print(f'Você morreu {nome_do_personagem}')
                sleep(2)
                print('GAME OVER')
                break
            if vida_inimigo == 0:
                print('Parabens você venceu ')
                print('Game over')
                break
            que = input('Digite "d" para jogar o dado.==: ')

            if que == 'at':

                print(f'o dano é ={dano_espada_escolhido}')
            elif que == 'danoi':
                vida_inimigo = vida_inimigo - 50
                print('perdeu 50 de vida')
            elif que == 'danoeu':
                vida_persoganem = vida_persoganem - 50
                print('Eu perdi 50 de vida')
            elif que == 'd':
                dado = 1
                dado2 = 2
                dado3 = 3
                dado4 = 4
                dado5 = 5
                w = [dado, dado2, dado3, dado4, dado5]
                dado_sorteado = choice(w)
                print(f'Você tirou:{dado_sorteado}')
                sleep(0.7)
                dade = 1
                dade2 = 2
                dade3 = 3
                dade4 = 4
                dade5 = 5
                i = [dade, dade2, dade3, dade4, dade5]
                dado_sorteado_inimigo = choice(i)
                print(f'{inimigo} tirou :{dado_sorteado_inimigo}')
                banana = 'oi'
                if banana == '':
                    print('oi')
                elif dado_sorteado > dado_sorteado_inimigo:
                    if arma == 'Espada':
                        dano_espada = 1
                        dano_espada2 = 2
                        dano_espada3 = 3
                        dano_espada4 = 4
                        dano_espada5 = 5
                        dano_espada6 = 6
                        dano_espada7 = 7
                        dano_espada8 = 8
                        dano_espada9 = 9
                        dano_espada10 = 10
                        r = [dano_espada, dano_espada2, dano_espada3, dano_espada4, dano_espada5, dano_espada6,
                             dano_espada7,
                             dano_espada8, dano_espada9, dano_espada10]
                        dano_espada_escolhido = choice(r)
                        print(f'o numero do dado deu {dano_espada_escolhido}')
                        if dano_espada_escolhido == 9:
                            dano_espada_escolhido = dano_espada9

                        elif dano_espada_escolhido == 10:
                            dano_espada_escolhido = dano_espada10

                        elif dano_espada_escolhido == 8:
                            dano_espada_escolhido = 6.9

                        elif dano_espada_escolhido == 7:
                            dano_espada_escolhido = 5.6

                        elif dano_espada_escolhido == 6:
                            dano_espada_escolhido = 4.4

                        elif dano_espada_escolhido == 5:
                            dano_espada_escolhido = 3.1

                        elif dano_espada_escolhido == 4:
                            dano_espada_escolhido = 2.1

                        elif dano_espada_escolhido == 3:
                            dano_espada_escolhido = 1.5

                        elif dano_espada_escolhido == 2:
                            dano_espada_escolhido = 1

                        elif dano_espada_escolhido == 1:
                            dano_espada_escolhido = 0.6
                        vida_inimigo = vida_inimigo - dano_espada_escolhido
                        print(f'{inimigo} perdeu {dano_espada_escolhido}')

                    elif arma == 'Cajado magico':
                        dano_caado = 1
                        dano_cajado2 = 2
                        dano_cajado3 = 3
                        dano_cajado4 = 4
                        dano_cajado5 = 5
                        dano_cajado6 = 6
                        dano_cajado = 7
                        fr = [dano_caado, dano_cajado, dano_cajado2, dano_cajado3, dano_cajado4, dano_cajado5,
                              dano_cajado6]
                        dano_cajado_escolhido = choice(fr)
                        print(f'O dado caiu {dano_cajado_escolhido}')
                        if dano_cajado_escolhido == 7:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 6:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 5:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 4:
                            dano_cajado_escolhido = 3.0

                        elif dano_cajado_escolhido == 3:
                            dano_cajado_escolhido = 2.3

                        elif dano_cajado_escolhido == 2:
                            dano_cajado_escolhido = 1.3

                        elif dano_cajado_escolhido == 1:
                            dano_cajado_escolhido = 0.8

                        vida_inimigo = vida_inimigo - dano_cajado_escolhido
                        print(f'{inimigo} perdeu:{dano_cajado_escolhido}')

                    elif arma == 'Arco e flexa':
                        dano_arco = 1
                        dano_arco2 = 2
                        dano_arco3 = 3
                        dano_arco4 = 4
                        dano_arco5 = 5
                        ty = [dano_arco, dano_arco2, dano_arco3, dano_arco4, dano_arco5]
                        dano_arco_escolhido = choice(ty)
                        print(f'Vc tirou no dado {dano_arco_escolhido}')
                        if dano_arco_escolhido == 5:
                            dano_arco_escolhido = 5

                        elif dano_arco_escolhido == 4:
                            dano_arco_escolhido = 4

                        elif dano_arco_escolhido == 3:
                            dano_arco_escolhido = 3

                        elif dano_arco_escolhido == 2:
                            dano_arco_escolhido = 1.7

                        elif dano_arco_escolhido == 1:
                            dano_arco_escolhido = 0.9
                        vida_inimigo = vida_inimigo - dano_arco_escolhido
                        print(f'{inimigo} perdeu:{dano_cajado_escolhido}')

                elif dado_sorteado < dado_sorteado_inimigo:
                    if Arma_inimigo == 'Espada':
                        dano_espada = 1
                        dano_espada2 = 2
                        dano_espada3 = 3
                        dano_espada4 = 4
                        dano_espada5 = 5
                        dano_espada6 = 6
                        dano_espada7 = 7
                        dano_espada8 = 8
                        dano_espada9 = 12
                        dano_espada10 = 15
                        r = [dano_espada, dano_espada2, dano_espada3, dano_espada4, dano_espada5, dano_espada6,
                             dano_espada7,
                             dano_espada8, dano_espada9, dano_espada10]
                        dano_espada_escolhido = choice(r)
                        print(f'o numero do dado do {inimigo} deu {dano_espada_escolhido}')
                        if dano_espada_escolhido == 12:
                            dano_espada_escolhido = dano_espada9

                        elif dano_espada_escolhido == 15:
                            dano_espada_escolhido = dano_espada10

                        elif dano_espada_escolhido == 8:
                            dano_espada_escolhido = 9.9

                        elif dano_espada_escolhido == 7:
                            dano_espada_escolhido = 8.6

                        elif dano_espada_escolhido == 6:
                            dano_espada_escolhido = 7.4

                        elif dano_espada_escolhido == 5:
                            dano_espada_escolhido = 6.1

                        elif dano_espada_escolhido == 4:
                            dano_espada_escolhido = 5.1

                        elif dano_espada_escolhido == 3:
                            dano_espada_escolhido = 4.5

                        elif dano_espada_escolhido == 2:
                            dano_espada_escolhido = 3

                        elif dano_espada_escolhido == 1:
                            dano_espada_escolhido = 2
                        vida_persoganem = vida_persoganem - dano_espada_escolhido
                        print(f'Você perdeu:{dano_espada_escolhido}')

                    elif Arma_inimigo == 'Cajado mágico':
                        dano_caado = 1
                        dano_cajado2 = 2
                        dano_cajado3 = 3
                        dano_cajado4 = 4
                        dano_cajado5 = 7
                        dano_cajado6 = 9
                        dano_cajado = 10
                        fr = [dano_caado, dano_cajado, dano_cajado2, dano_cajado3, dano_cajado4, dano_cajado5,
                              dano_cajado6]
                        dano_cajado_escolhido = choice(fr)
                        print(f'O {inimigo} jogou o dado e caiu {dano_cajado_escolhido}')
                        if dano_cajado_escolhido == 10:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 9:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 7:
                            dano_cajado_escolhido = dano_cajado_escolhido

                        elif dano_cajado_escolhido == 4:
                            dano_cajado_escolhido = 6.0

                        elif dano_cajado_escolhido == 3:
                            dano_cajado_escolhido = 5.3

                        elif dano_cajado_escolhido == 2:
                            dano_cajado_escolhido = 3.3

                        elif dano_cajado_escolhido == 1:
                            dano_cajado_escolhido = 1.8
                        vida_persoganem = vida_persoganem - dano_cajado_escolhido
                        print(f'Você perdeu:{dano_cajado_escolhido}')

                    elif Arma_inimigo == 'Arco e flexa':
                        dano_arco = 1
                        dano_arco2 = 2
                        dano_arco3 = 3
                        dano_arco4 = 4
                        dano_arco5 = 5
                        ty = [dano_arco, dano_arco2, dano_arco3, dano_arco4, dano_arco5]
                        dano_arco_escolhido = choice(ty)
                        print(f'O {inimigo} {dano_arco_escolhido}')
                        if dano_arco_escolhido == 5:
                            dano_arco_escolhido = 5

                        elif dano_arco_escolhido == 4:
                            dano_arco_escolhido = 4

                        elif dano_arco_escolhido == 3:
                            dano_arco_escolhido = 3

                        elif dano_arco_escolhido == 2:
                            dano_arco_escolhido = 1.7

                        elif dano_arco_escolhido == 1:
                            dano_arco_escolhido = 1.5
                        vida_persoganem = vida_persoganem - dano_arco_escolhido
                        print(f'Você perdeu:{dano_arco_escolhido}')
            elif que == 'aj':
                print('Opa esse comando erra para ter saido na beta ')
            elif que == 'aq':

                print('ops desculpa isso é opção de desenvolvedor')

    elif dificuldade=='4':
        print('Easy')
    else:
        print('Err, digite o valor correto.')
    '''vida=100
    print(f'Vida: {vida}')
    while True:
        print(f'Sua vida agora: {vida}')
        dano=int(input('Quanto de dano vc deseja se lidar ?'))
        vida=vida-dano
        if vida <0:
            print('Você morreu')
            break
    sleep(0.5)
    print(f'Vida:{vida}')
    print('Fim de jogo')'''
