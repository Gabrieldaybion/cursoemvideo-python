from pymata4 import pymata4
from time import sleep
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

from datetime import date
atual = date.today().day
atual2 = date.today().year
atual3 = date.today().month


triggerpin=5
echo_pin=4

placa=pymata4.Pymata4()
placa.set_pin_mode_digital_output(pin_number=8)
placa.set_pin_mode_digital_output(pin_number=10)
placa.set_pin_mode_digital_output(pin_number=9)
placa.set_pin_mode_digital_output(pin_number=11)
r=0
def the_callback(data):
    global r
    print('Distancia:',data[2])

    if data[2]<30:

        placa.digital_pin_write(11,0)

        print('2S')


        #audio_fala(f'Olá meu criador,sejá bem vindo a seu quarto.')
        #audio_fala(f'Hoje é dia {atual}, do mês{atual3} do ano de {atual2}')
        meu_aniversario=10-atual
        #audio_fala(f'Faltam {meu_aniversario}, dias para o seu aniversário.')
        #if atual==10:
            #audio_fala('Parabéns meu criador,Eu fico feliz que esteja fazendo mais um ano de vida, fico grata por ter me criado e saiba que sempre irei o ajudar')

        #audio_fala('Que o senhor tenha uma ótima noite.')
        r=1
    else:
        placa.digital_pin_write(11,1)
    return r

placa.set_pin_mode_sonar(triggerpin,echo_pin,the_callback)

while True:

        sleep(0.03)
        placa.sonar_read(triggerpin)
        if r==1:
            break
