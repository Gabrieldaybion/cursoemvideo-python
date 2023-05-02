from time import sleep
import webbrowser
import random
#Degabiontwess 2021. Propriedade Gabriel Xavier..]
#Lucy beta 0,2,0.____.22/07/2020.
#Lucy beta 0,2,1.____.30/07/2020.
#Lucy beta 0,2,2.____.03/08/2020.
#Lucy beta 0.3.0.____.07/08/2020.
#Lucy beta 0.3.1.____.14/08/2020.
#Lucy beta 0.3.2.____.19/08/2020.
#Lucy beta 0.3.3.____.20/08/2020.
#Lucy beta 0.4.0.____.23/09/2020.
#Lucy beta 0.4.5.____.21/10/2020.
#Lucy beta 0.5.0.____.06/01/2021.
#Lucy beta 0.5.5.____.20/01/2021.
#Lucy beta 0.6.0.____.10/02/2021.
#Lucy beta 0.6.5.____.12/02/2021.
#Lucy 3.0  or #Lucy automatica 0.1.0
#Lucy 3.1  or #Lucy automatica 0.1.2
#Lucy 3.2  or #Lucy automatica 0.1.3
#Lucy 3.3  or #Lucy automatica 0.1.4
#Lucy 4.0  or #Lucy automatica 0.1.5
#Lucy 4.5  or #Lucy automatica 0.1.6
#Lucy 5.0  or #Lucy automatica 0.1.7
#Lucy 5.5  or #Lucy automatica 0.1.8
#Lucy 6.0  or #Lucy automatica 0.1.9
#Lucy 6.5  or #Lucy automatica 0.2.0
import pyttsx3
import speech_recognition as sr
def audio_fala(msg):
    spekear=pyttsx3.init()
    voices=spekear.getProperty('voices')

    spekear.setProperty('voice',voices)
    rate=spekear.getProperty('rate')
    spekear.setProperty('rate',rate-25)
    spekear.say(msg)
    spekear.runAndWait()
def recebimento_de_fala():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Diga algo:')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='pt-BR')
            print(f'Você disse {text}')
        except:
            print('Desculpe, não pude enterder oque voçê disse !!\nDiga novamente pvf')
print('\033[34m_'*30)
sleep(0.9)
print('_'*15)
sleep(0.9)
print('\033[34m\nLucy 0.6.5')
sleep(0.5)
for n in range(0, 1):
         print('D', end='')
         sleep(0.5)
         print('E',end='')
         sleep(0.5)
         print('G',end='')
         sleep(0.5)
         print("A",end='')
         sleep(0.5)
         print('B',end='')
         sleep(0.5)
         print('I',end='')
         sleep(0.5)
         print('O',end='')
         sleep(0.5)
         print('N',end='')
         sleep(0.5)
         print('T',end='')
         sleep(0.5)
         print('W',end='')
         sleep(0.5)
         print('E',end='')
         sleep(0.5)
         print('S',end='')
         sleep(0.5)
         print("S",end='')
         sleep(0.5)
         sleep(0.2)
         print('')
print('Para sair do programa digite \033[35m[exit]\033[34m:')
audio_fala('Para sair do programa digite egit.')
audio_fala('Qual é o seu nome ?')
nome=input('Qual é o seu nome ?')
audio_fala(f'Prazer {nome}, espero que voçê esteja bem !!!')
print(f'Prazer {nome}, espero que voçê esteja bem !')

audio_fala('Digite oque deseja fazer,  conversar por voz ou por textos.')
while True:
    esc=input('Digite oque deseja fazer:conversar por voz[v]/conversar por texto[t]:')
    if esc == 'v':
        print('Voçê escolheu conversar por voz:')
        audio_fala('Voçê escolheu conversar por voz.')
    elif esc=='t':
        audio_fala('Voçê escolheu conversar por textos')
        print("Voçê escolheu conversar por textos")
        audio_fala('Digite algum comando para iniciar')
        audio_fala('Dica digite algo como data ou a raiz de um número.')
        while True:
            cmd=input('==: ')
            if cmd == 'sair':
                break
            elif cmd=='bom dia':
                audio_fala(f'Bom dia {nome}')
            elif cmd =='boa noite':
                audio_fala(f'Boa noite {nome}')
            elif cmd =='boa tarde':
                audio_fala(f'boa tarde{nome}')
            elif cmd =='obrigado' or cmd=='obrigada':
                audio_fala('De nada, é um prazer ajudar.')
            elif cmd =='oi':
                audio_fala('oi')
            elif cmd=='oie' or cmd=='oii' or cmd=='oiii' or cmd=='oiee' or cmd=='oiiii' or cmd=='ola' or cmd =='olaa':
                n1 = 'Eai '
                n2 = 'oii'
                n3 = 'Oie'
                n4 = 'Oiiii '
                n5 = 'OOiii '
                lista = [n1, n2, n3, n4, n5]
                escolhido = random.choice(lista)
                audio_fala(escolhido)
            elif cmd == 'data' or cmd=='qual é a data ?'or cmd=='qual ea data' or cmd=='qual éa data' or cmd=='qual e a data' or cmd =='qual e a data?':
                from datetime import date

                atual = date.today().day
                atual2 = date.today().year
                atual3 = date.today().month
                print('hoje é dia {} do mês {} no ano de {}'.format(atual, atual3, atual2))
                audio_fala(f'Hoje é dia {atual} do mês {atual3} no ano de {atual2}')
            elif cmd == 'dividir' or cmd=='dividisão' or cmd=='divisao' or cmd== 'divizao' or cmd=='divida' or cmd=='dividaa':
                div1 = int(input('Primeiro número: '))
                div2 = int(input('Segundo número: '))
                div3 = div1 / div2
                audio_fala(f'{div1} dividido por {div2} é igual a {div3}')
                print(f'{div1} dividido por {div2} é igual a {div3}')
            elif cmd == 'multiplicar' or cmd=='vezes' or cmd =='multiplique' or cmd == 'x':
                mtp=int(input('Primeiro numero: '))
                mtp2=int(input('Segundo numero'))
                mtp3= mtp * mtp2
                audio_fala(f'{mtp} vezes {mtp2} é igual a {mtp3}')
            elif cmd == 'adição'or cmd=='mais' or cmd == '+' or cmd =='adicao' or cmd =='adiçao':
                mais=int(input('Primeiro número: '))
                mais2=int(input('Segundo número: '))
                mais3= mais + mais2
                audio_fala(f'{mais}mais{mais2}é igual a{mais3}')
            elif cmd=='-' or cmd=='menos' or cmd=='subtração':
                sub=int(input('Primeiro número: '))
                sub2=int(input('Segundo múmero: '))
                sub3= sub - sub2
                audio_fala(f'{sub}menos{sub2}é igual a {sub3}')
            elif cmd =='pesquisa' or cmd=='pesquise' or cmd == 'pesquisar':
                while True:
                    print('Para sair digite sair')
                    pg = input('Oque deseja pesquisar ?')
                    if pg=='sair':
                        break
                    pesquisar = ('https://www.google.com.br/search?q=')
                    pesquisng = (pesquisar + pg)
                    webbrowser.open(pesquisng)
                    audio_fala(f'Voçê pesquisou sobre {pg}')
            elif cmd =='tudo bem? 'or cmd=='tudo bem ?':
                audio_fala(f'Tudo bem sim {nome}, ecom voçê ?')
            elif cmd == 'sim':
                audio_fala('Otimooooo')
            elif cmd =='piadas' or cmd =='piada' or cmd=='conte piada' or cmd=='piada ' or cmd==' piada':
                n6 = '''A professora chega para o Joãozinho e diz:
 Joãozinho qual é o tempo da frase: Eu procuro um homem fiel?
 E então Joãozinho responde
 É tempo perdido!'''
                n7 = '''O que o pato disse para a pata?

 Vem Quá!'''
                n8 = """Porque o menino estava falando no telefone deitado?
Para não cair a ligação"""
                n9 = '''A enfermeira diz ao médico:
Tem um homem invisível na sala de espera
O médico responde
Diga a ele que não posso vê-lo agora'''
                n0 = ''
                np = ''
                lista1 = [n6, n7, n8, n9, n0,np]
                escolhido1 = random.choice(lista1)
                print('{}'.format(escolhido1))

            else:
                audio_fala('Desculpe-me, comando inválido.Talvez em proximas atualizações seja possivel ')

    else:
        audio_fala('Errro 01. desculpe digite t ou v para continuar')
        print('ERRR 01: Descupe digite t ou v para continuar')
