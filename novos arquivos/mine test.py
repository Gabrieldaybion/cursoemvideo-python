#14/06/2024
from pynput.keyboard import Key, Controller #Automação completa.
from time import sleep
import pyautogui    #automaçao simples

keybord = Controller()

def andar(tecla,tempo):
    keybord.press(tecla)
    s(tempo)
    keybord.release(tecla)
def fricandini(tecla,tempo,mete):
    keybord.press(tecla)
    s(0.4)
    keybord.press(tecla)
    for _ in range(mete):
        keybord.press(Key.shift)
        s(tempo)
        keybord.release(Key.shift)
        s(tempo)


def mover(a):
    pyautogui.press(a)

def atalho(e,t):
    pyautogui.hotkey(e,t)

def s(tempo):
    sleep(tempo)


sleep(1)
print('1')
sleep(1)
print('2')
sleep(1)
print('3')
atalho('alt','tab')
s(1.8)
keybord.press(Key.esc)
s(0.8)
keybord.release(Key.esc)
s(2.5)
andar('w',3)
s(1)
andar('d',3)
fricandini(Key.f5,0.057,80)

