import pyautogui as pag
from time import sleep

def main():
    buttonLocation = pag.locateCenterOnScreen("C:/Users/uidj9600/eclipse-workspace/Goals2018/img/back.PNG")
    pag.click(buttonLocation,duration=0.01)
    sleep(5)
    buttonLocation = pag.locateCenterOnScreen("C:/Users/uidj9600/eclipse-workspace/Goals2018/img/help.PNG")
    pag.click(buttonLocation,duration=0.01)
    sleep(5)

if __name__ == '__main__':
    main()