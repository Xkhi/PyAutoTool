import pyautogui as pag
from time import sleep

def main():
    pag.click(240,290,duration=0.01)
    sleep(2)
    pag.click(1721,272,duration=0.01)
    sleep(2)

if __name__ == '__main__':
    main()