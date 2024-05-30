from time import sleep as tempo
print('\033[32m-=\033[m'*30)
print('\033[34m-'*17)
print('[Eq2grau beta 0.2.3]')
print('-'*17)
tempo(1.9)
print('\033[34mSeja bem vindo ao sistema automatico \nde equação de 2 grau. ')
for n in range(1,10):
    print('.', end='')
    tempo(0.7)

print('.')
while True:
    print('Informe o A,B e C:')
    a=int(input('A.==: '))
    b=int(input('B.==: '))
    c=int(input('C.==: '))

    delt=(b**2) -4*a*c
    print(f'O valor de delta é {delt} ')
    def x():
        print('Calculando o valor de x.')
        x1= (((-b) + (delt ** (1/2) ))/(2*a))
        x2= (((-b) - (delt ** (1/2) ))/(2*a))
        print(f'x1= {x1}, x2= {x2}')
    x()

    res=str(input('Deseja continuar ?(s/n)'))
    if res == 's':
        print('Okay')
    elif res =='n':
        break

print('FIM :)')
print('\033[32m-=\033[m'*30)
