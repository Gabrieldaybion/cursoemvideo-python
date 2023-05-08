import pyautogui as pa
from time import sleep
print('Rodando...')
def esc():
    pa.hotkey("alt","tab")
    sleep(0.3)
    pa.write('console.log("Poxa vem programar a sra vai adorar criar alguem como eu :)!");')
    sleep(0.2)
    pa.hotkey("enter")
esc()
print('Finalizado')
