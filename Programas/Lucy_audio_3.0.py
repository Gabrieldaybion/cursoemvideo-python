print('Comando de voz sendo iniciado')
print('''\033[34m Escolha, falando o numero:
[2]ligar leds
[3]desligar leds
[4]sair''')

import speech_recognition as sr
from pyfirmata import Arduino, util
placa = Arduino('COM9')
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Diga algo:')
        audio = r.listen(source)

        try:
            text = 'banana'
            text = r.recognize_google(audio, language='pt-BR')
            print(f'Você disse: {text}')


        except:
            print('Desculpe, não pude enterder oque voçê disse !!\nDiga novamente pvf ;)')

        if text == '2' or text == '22' or text == '2 2':
            print('''(4)Ligar led vermelho
(5)Liga led amarelo
(6)Ligar led verde''')
        elif text == '5' or text == '55' or text=='cinco' or text=='Cinco':
            placa.digital[12].write(1)

        elif text == '4' or text == '44' or text=='quatro' or text=='Quatro':
            placa.digital[11].write(1)

        elif text == '6' or text == '66'or text=='seis' or text=='Seis':
            placa.digital[10].write(1)


        elif text == '3' or text == '33' or text == '3 3' or text=='Três':
            print('''(8)Desligar led vermelho
(9)Desligar led amarelo
(10)Desligar led verde''')
        elif text == '8' or text == '8' or text=='oito'or text=='Oito':
            placa.digital[11].write(0)

        elif text == '9' or text == '99' or text =='nove' or text=='Nove':
            placa.digital[12].write(0)

        elif text == '10' or text == '1010' or text=='dez' or text=='Dez':
            placa.digital[10].write(0)


