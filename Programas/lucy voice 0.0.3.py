import speech_recognition as sr
import pyttsx3
from config import *
from random import choice




reproducao=pyttsx3.init()

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()
print('ouvindo...\n---------------------\n')
while True:

    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        while True:
            try:
                audio = rec.listen(s)
                entrada = rec.recognize_google(audio, language='pt')
                if entrada == 'vezes' or entrada == 'Vezes':
                    print('Multiplicação')
                print( 'Você disse: {} .'.format(entrada))

                resposta=conversas[entrada]
                print(f'LUCY:{resposta}')
                sai_som(f'{resposta}')
            except sr.UnknownValueError:
                print( lista_erros)
                sai_som(lista_erros)


