from pyfirmata import Arduino, util
from PyQt5 import uic, QtWidgets,QtGui
#placa = Arduino('COM9')
v=1
k=1
d=1
pq=input('O arduino esta conectado ? (s/n): ')
if pq =='s':
    placa = Arduino('COM9')
    def liga_desliga_led_vermelho(porta_digital,ligado1_desligado0):
        placa.digital[porta_digital].write(ligado1_desligado0)

    def liga_desliga_led_verde(porta_digital,ligado1_desligado0):
        placa.digital[porta_digital].write(ligado1_desligado0)

    def liga_desliga_led_amarelo(porta_digital,ligado1_desligado0):
        placa.digital[porta_digital].write(ligado1_desligado0)

elif pq=='n':
    print('Okay arduino não conectado.')


def liga_led1():
    global v
    v= v+1
    if v==3:
        print('Led desligado')
        if pq=='s':
            io=liga_desliga_led_amarelo(12,0)
            io
        elif pq=='n':
            io=1
        v= v-2
    elif v==2:
        print('Led ligado')
        if pq=='s':
            io=liga_desliga_led_amarelo(12,1)
            io
        elif pq=='s':
            io=1

def desligaled1():
    print('função1')

def ligaled2():
    global k
    k=k+1
    if k==3:
        print('Desligado')
        if pq=='s':
            ui=liga_desliga_led_verde(10,0)
            ui
        elif pq=='n':
            ui=1
        k=k-2
    elif k==2:
        print('Ligado')
        if pq=='s':
            ui=liga_desliga_led_verde(10,1)
            ui
        elif pq=='n':
            ui=1
def desligaled2():
    print('led2 desligado')

def ledligado3():
    global d
    d=d+1
    if d==3:
        print('Desligado')
        if pq=='s':
            yi=liga_desliga_led_vermelho(11,0)
            yi
        elif pq=='n':
            yi=1
        d=d-2
    elif d==2:
        print('Ligado')
        if pq=='s':
            yi=liga_desliga_led_vermelho(11,1)
            yi
        elif pq=='n':
            yi=1

def leddesligado3():
    print('led3 desligado')

app9 = QtWidgets.QApplication([])
formulario9 = uic.loadUi('ad_controller2.ui')
#Importa a imagem/redimenciona ela.
formulario9.label.setPixmap(QtGui.QPixmap('28.JPEG'))
formulario9.label.resize(399,350)
formulario9.btnL_1.clicked.connect(liga_led1)
formulario9.btnl2.clicked.connect(ligaled2)
formulario9.btnl3.clicked.connect(ledligado3)
formulario9.btnd1.clicked.connect(desligaled1)
formulario9.btnd2.clicked.connect(desligaled2)
formulario9.btn3d.clicked.connect(leddesligado3)
formulario9.show()
app9.exec()