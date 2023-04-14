from PyQt5 import uic,QtWidgets
from pygame import mixer
def funcao_principal():
    print('butao precionado')
    if formulario.att.isChecked():
        print('Attention')
        from pygame import mixer
        mixer.init()
        mixer.music.load('Attention.mp3')
        mixer.music.play()

    elif formulario.wann.isChecked():
        print('Wanna')
        from pygame import mixer
        mixer.init()
        mixer.music.load('mp3 .mp3')
        mixer.music.play()

    elif formulario.runa.isChecked():
        print('Runaray')
        from pygame import mixer
        mixer.init()
        mixer.music.load('09 Runaway (U & I) [Svidden & Jarly.mp3')
        mixer.music.play()

    elif formulario.the.isChecked():
        print('The weekd')
        from pygame import mixer
        mixer.init()
        mixer.music.load('The Weeknd - I Feel It Coming ft. Daft Punk (Offic(MP3_160K).mp3')
        mixer.music.play()

    elif formulario.old.isChecked():
        print('Old me')
        from pygame import mixer
        mixer.init()
        mixer.music.load('5 Seconds of Summer - Old Me (Official Video)(MP3_160K).mp3')
        mixer.music.play()

    elif formulario.im.isChecked():
        print('Im So Sorry')
        from pygame import mixer
        mixer.init()
        mixer.music.load('I_m So Sorry(MP3_160K).mp3')
        mixer.music.play()
def pausar_musica():
    print('musica pausada')
    from pygame import mixer
    mixer.music.pause()

def continuar_musica():
    print('musica continuada')
    mixer.music.unpause()


app=QtWidgets.QApplication([])
formulario=uic.loadUi('app_music.ui')
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(pausar_musica)
formulario.pushButton_3.clicked.connect(continuar_musica)
formulario.show()
app.exec()
