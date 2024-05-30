#from flask import Flask
#import pywhatkit as kit #Impotar biblioteca para mandar mensasem no zap
#from time import sleep as t
#import pyautogui
'''def programa_mensagem_whatzap():
    print('Digite um número de telefone')
    print('Ex:22996071277')
    try:
        numero=input('.==: ')
        mensagem=input('Digite a mesagem que deseja digitar==: ')
        horario_hora=int(input('Digite a hora que deseja mandar a mensagem==: ',end=''))
        horario_min=int(input('Digite o min que deseja mandar mensagem==: '))
        kit.sendwhatmsg(numero,mensagem,horario_hora,horario_min)
        print('Mensagem enviada')
        t(35)
        pyautogui.press("enter")
    except:
        print('Ops deu erro')

    finally:
        print('Mensagem concluida app irá acabar')

    #kit.sendwhatmsg('+5522996071277','oiee',22,17)'''
n=int(input('N=: '))
p=int(input('P=: '))
rl=n-p
c=n


def fa(g):
    global f

    if g >= 1:
        f = g
    else:
        f = 0
    c = g
    f = 1
    while c > 0:
        f *= c
        c -= 1
def fay(g):
    global mn

    if g >= 1:
        mn = g
    else:
        mn = 0
    c = g
    mn = 1
    while c > 0:
        mn *= c
        c -= 1
def far(g):
    global dx

    if g >= 1:
        dx = g
    else:
        dx = 0
    c = g
    dx = 1
    while c > 0:
        dx *= c
        c -= 1
fa(n)
fay(p)
far(rl)
print(f)
print(mn)
print(dx)
yb=f/mn
ttth=yb/dx
print(ttth)