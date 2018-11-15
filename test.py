import pyautogui as pag
from time import sleep

def main():
    pag.hotkey("win",pause=0.5)
    pag.typewrite('ibm notes',pause=0.5)
    pag.hotkey("enter",pause=0.5)
    pag.hotkey("alt","f",pause=0.5)
    pag.typewrite('n',pause=0.5)
    pag.typewrite('m',pause=0.5)
    pag.typewrite('Enrique Espinosa/usr/cag,',pause=0.5)
    pag.hotkey("tab",pause=0.5)
    pag.hotkey("tab",pause=0.5)
    pag.hotkey("tab",pause=0.5)
    pag.typewrite('saludos',pause=0.5)
    pag.hotkey("alt","1",pause=0.5)

if __name__ == '__main__':
    main()