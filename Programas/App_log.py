from PyQt5 import uic, QtWidgets
from time import sleep as s
def exibir_mensagem():
    dado_lido= janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText("")
    if dado_lido=='gabriel':
        print('OLa mestre')
    if dado_lido=='daybion':
        segunda_tela.show()
        print('Sea bem vindo sr daybion')



app=QtWidgets.QApplication([])
janela=uic.loadUi('App_log.ui')
segunda_tela=uic.loadUi('AD_controller.ui')
tela_3=uic.loadUi('primeira_tela.ui')
janela.pushButton.clicked.connect(exibir_mensagem)

janela.show()
print('SENHA:daybion')
app.exec()
