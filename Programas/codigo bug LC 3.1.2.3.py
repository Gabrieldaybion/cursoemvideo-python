fg=0
print('Digite 999 para sair.')
while fg !='999':
    fg=input('==: ')
    if fg=='vezes':
        vz=int(input('primeiro numero:'))
        vz2=int(input('segundo numero: '))
        vz3=vz+vz2
        print(f'{vz3}')
    elif fg =='bom dia':
        print('bom dia')
    else:
        print('\033[34mERR@#321')

#programa 2.1\que concerta elif e comando inicial duplo:
ddr=0

print('DIGITE \033[32msair.\033[m para sair.')
while True:
    nh=input('==: ')
    if nh=='banana':
        print('oiii')
    elif nh=='sair':
        break
    elif nh=='bom dia':
        print('bom dia')
    elif nh=='mais':
        ms=int(input('N: '))
        ms1=int(input('n2: '))
        ms2=ms+ms1
        print(f'{ms2}')
    else:
        print('\033[35mERR@#$22\033\[m')
print('ACABOU!!!!!!!!!')