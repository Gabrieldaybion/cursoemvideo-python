from PyQt5 import uic, QtWidgets
from time import sleep as tempo
def direita_cima():
    print('Direita: CIMA')

def direita_baixo():
    print('Direita: BAIXO')

def esquerda_cima():
    print('Esquerda: CIMA')

def esquerda_baixo():
    print('Esquerda: BAIXO')

def led1_ligado():
    print('LED.1: LIGADO')

def led1_desligado():
    print('LED.1:DESLIGADO')

def led2_ligado():
    print('LED.2:LIGADO')

def led2_desligado():
    print('LED.2:DESLIGADO')

def led3_ligado():
    print('LED.3:LIGADO')

def led3_desligado():
    print('LED.3:DESLIGADO')

def modulo_1():
    print('Módulo.1:Ligado')

def modulo_2():
    print('Módulo.2:Ligado')

app=QtWidgets.QApplication([])
formulario=uic.loadUi('AD_controller.ui')
formulario.cimadir.clicked.connect(direita_cima)
formulario.baixodir.clicked.connect(direita_baixo)
formulario.cimaesq.clicked.connect(esquerda_cima)
formulario.baixoesq.clicked.connect(esquerda_baixo)
formulario.led1.clicked.connect(led1_ligado)
formulario.led2.clicked.connect(led2_ligado)
formulario.led3.clicked.connect(led3_ligado)
formulario.led1des.clicked.connect(led1_desligado)
formulario.led2des.clicked.connect(led2_desligado)
formulario.led3des.clicked.connect(led3_desligado)
formulario.modulo.clicked.connect(modulo_1)
formulario.modulo2.clicked.connect(modulo_2)
formulario.show()
app.exec()
