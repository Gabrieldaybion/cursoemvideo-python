import pyttsx3
import speech_recognition as sr
import webbrowser
from time import sleep as temp
import random
from pyfirmata import Arduino, util
import time
import Lucy_13_ad_utei
import Lucy_13_saudio_utei
import Lucy_13_com_utei
#Degabiontwess 2022. Propriedade Gabriel Xavier..]
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
#Lucy oficial 1.0.0._.27/08/2021.
#Lucy oficial 1.1.0._.15/09/2021.
#Lucy oficial 1.2.0._.17/10/2021.
#Lucy oficial 1.3.0._.15/01/2022.
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
#Lucy 1.0  or #Lucy automatica 0.3.0
#Lucy 1.1  or #Lucy automatica 0.3.1
#Lucy 1.2  or #Lucy automatica 0.3.2
#Lucy 1.3  or #Lucy automatica 0.3.3
print('''[1]Lucy 1.3 sem voz.
[2]Lucy 1.3 completa.
[3]Lucy conversa por voz.
[4]Lucy arduino.
[5]sair.''')
while True:
    gl=input('==: ')
    if gl =='5':
        break
    elif gl =='4':
        Lucy_13_ad_utei.Lucy_ad_13()
        print('''[1]Lucy 1.3 sem voz.
[2]Lucy 1.3 completa.
[3]Lucy conversa por voz.
[4]Lucy arduino.
[5]sair.''')
    elif gl=='':
        print('Deculpe mas você não digitou nada.')
    elif gl =='2':
        Lucy_13_com_utei.lucy_cvs()
        print('''[1]Lucy 1.3 sem voz.
[2]Lucy 1.3 completa.
[3]Lucy conversa por voz.
[4]Lucy arduino.
[5]sair.''')
    elif gl=='1':
        Lucy_13_saudio_utei.Lucy_sem_audio()
        Lucy_13_saudio_utei.lucy_cvs()
        print('''[1]Lucy 1.3 sem voz.
[2]Lucy 1.3 completa.
[3]Lucy conversa por voz.
[4]Lucy arduino.
[5]sair.''')
    elif gl=='hora':
        import datetime

        datetime.datetime.now().time()
        datetime.time(15, 8, 24)
        data=datetime.datetime.now().time()
        print(data)
        


    else :
        print('Deculpe mas comando invalido.')
