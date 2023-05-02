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

triggerpin=5
echo_pin=4

placa=pymata4.Pymata4()
placa.set_pin_mode_digital_output(pin_number=8)
placa.set_pin_mode_digital_output(pin_number=10)
placa.set_pin_mode_digital_output(pin_number=9)
placa.set_pin_mode_digital_output(pin_number=11)


def the_callback(data):
    global v

    v = 1
    v = v + 1

    print('Distancia:',data[2])
    if data[2] >30:
        placa.digital_pin_write(8, 1)
        placa.digital_pin_write(10, 0)
        placa.digital_pin_write(9, 0)
        placa.digital_pin_write(11, 1)




    elif data[2] <10:
        placa.digital_pin_write(8, 0)
        placa.digital_pin_write(10, 1)
        placa.digital_pin_write(9, 0)
        placa.digital_pin_write(11, 0)
        from datetime import date
        atual = date.today().day
        atual2 = date.today().year
        atual3 = date.today().month

        e = audio_fala

        if v==2:
            print(v)
            global f
            f = 0
            data[2]=50
            e(f'Hoje é dia {atual}, do mês {atual3}, no ano de {atual2}')
            print('{}/{}/{}'.format(atual, atual3, atual2))

            if f==0 or f>0:
                print(f)
                e('')

    else:
        placa.digital_pin_write(9, 1)
        placa.digital_pin_write(8, 0)
        placa.digital_pin_write(10, 0)
        placa.digital_pin_write(11, 0)






placa.set_pin_mode_sonar(triggerpin,echo_pin,the_callback)
while True:
    try:
        sleep(0.03)
        placa.sonar_read(triggerpin)
    except Exception:
        placa.shutdown()