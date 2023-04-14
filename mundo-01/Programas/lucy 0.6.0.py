from pyfirmata import Arduino, util
from random import choice
import audio
from PyQt5 import uic, QtWidgets
from time import sleep as s
#Degabiontwess 2021. Propriedade Gabriel Xavier..]
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
#Lucy 3.0  or #Lucy automatica 0.1.0
#Lucy 3.1  or #Lucy automatica 0.1.2
#Lucy 3.2  or #Lucy automatica 0.1.3
#Lucy 3.3  or #Lucy automatica 0.1.4
#Lucy 4.0  or #Lucy automatica 0.1.5
#Lucy 4.5  or #Lucy automatica 0.1.6
#Lucy 5.0  or #Lucy automatica 0.1.7
#Lucy 5.5  or #Lucy automatica 0.1.8
#Lucy 6.0  or #Lucy automatica 0.1.9


def exibir_mensagem():
    dado_lido= janela.senha.text()
    print(dado_lido)
    janela.senha.setText("")
    if dado_lido=='gabriel':
        print('OLa mestre')
    if dado_lido=='daybion':
        segunda_tela.show()
def lucy_cvs():
    print()

def gxduino():
    print('ola')
    app_duino()

def versao2():
    versao1.show()
def novidades2():
    novidades1.show()
def fuca():
    funcao.show()
    print('funçao iniciada')
def adic():
    adiçao.show()
def somar():
    some=adiçao.num.text()
    some2=adiçao.num2.text()
    float(some)
    float(some2)
    r= some + some2
    print(r)
app=QtWidgets.QApplication([])
janela=uic.loadUi('lucy_5.ui')
segunda_tela=uic.loadUi('lucy_5_2.ui')
tela_3=uic.loadUi('lucy_cvs.ui')
versao1=uic.loadUi('versao.ui')
novidades1=uic.loadUi('novidades.ui')
funcao=uic.loadUi('funca.ui')
adiçao=uic.loadUi('adicao.ui')
janela.entrar.clicked.connect(exibir_mensagem)
segunda_tela.conversar.clicked.connect(lucy_cvs)
segunda_tela.versao.clicked.connect(versao2)
segunda_tela.novidades.clicked.connect(novidades2)
segunda_tela.funcao.clicked.connect(fuca)
funcao.adi.clicked.connect(adic)
funcao.duino.clicked.connect(gxduino)
adiçao.soma.clicked.connect(somar)
janela.show()
app.exec()
