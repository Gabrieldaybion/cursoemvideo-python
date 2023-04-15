import Binary_uteis

from random import choice
from time import sleep
la=12 #Led amarelo.Serve para avisar quando vai ser a proxima letra.
lr=11 #Led vermelho.Igual a 0.
lg=10 #Led verde.Igual a 1.

l=1#Variavel para ascender o led.Não tem a ver com o codigo binario.
d=0#Variavel para apagar o led.Não tem a ver com o codigo binario.
while True:
    s_n=input('Digite s/n para saber se o arduino está conectado: ')
    if s_n=='s':

            print('''[1].Para fazer o binary falar oi. 
[2].Transformar binário em letra.
[3]..Transformar letra em binario.
[4].Sair            ''')
            while True:
                gt=input('==: ')
                if gt=='1':
                     try:
                        def liga_leds(num_digital,l_d=l):
                            placa = Arduino('COM9')
                            placa.digital[num_digital].write(l_d)
                            sleep(0.5)
                            placa.digital[num_digital].write(d)
                            sleep(0.4)
                        print('Binary 0.1')
                        print('A maquina irá falar oi em binario.')
                        sleep(0.9)
                        liga_leds(lr,l)
                        liga_leds(lg,l)
                        liga_leds(lg,l)
                        liga_leds(lr,l)
                        liga_leds(lg,l)
                        liga_leds(lg,l)
                        liga_leds(lg,l)
                        liga_leds(lg,l)
                        #A letra 'o' foi dita
                        print('O',end='')
                        liga_leds(la,l)#Led que acende para mostrar que a letra já foi escrita
                        liga_leds(lr,l)#0
                        liga_leds(lg,l)#1
                        liga_leds(lg,l)#1
                        liga_leds(lr,l)#0
                        liga_leds(lg)#1
                        liga_leds(lr)#0
                        liga_leds(lr)#0
                        liga_leds(lg)#1
                        print('I')
                     except (ValueError,PermissionError,FileNotFoundError ):
                         print('Ops o arduino não está conectado')

                     finally:
                         print('O app concluiu seu obejetvo.')

                elif gt=='2':
                    Binary_uteis.binary_programa_2()
                elif gt=='3':
                   Binary_uteis.binary_programa()
                elif gt =='4':
                    break
                else:
                    print('Desculpe mas comando invalido.')
    elif s_n=='n':
        print('''[1]Transformar binário em letra.
[2].Transformar letra em binario.
[3]Sair.''')
        while True:
            fr=input('==: ')
            if fr=='1':
                Binary_uteis.binary_programa_2()
            elif fr=='2':
                Binary_uteis.binary_programa()
            elif fr=='3':
                break
            else:
                print('Desculpe, valor incorreto')
    else:
        print('Desculpe, digite s ou n para continuar.')
