from pymata4 import pymata4
from time import sleep
from random import choices
triggerpin=5
echo_pin=4

placa=pymata4.Pymata4()

placa.set_pin_mode_digital_output(pin_number=8)
placa.set_pin_mode_digital_output(pin_number=10)
placa.set_pin_mode_digital_output(pin_number=9)
placa.set_pin_mode_digital_output(pin_number=11)
placa.digital_pin_write(10,1)
def the_callback(data):
    global r
    r=1
    print('Distancia:',data[2])

    if data[2]<30:

        placa.digital_pin_write(9,1)

        print('2S')

        r=1
    else:
        placa.digital_pin_write(9,0)
    return r

placa.set_pin_mode_sonar(triggerpin,echo_pin,the_callback)
while True:

        sleep(0.6)
        placa.sonar_read(triggerpin)



