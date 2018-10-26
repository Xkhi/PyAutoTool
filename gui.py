import appJar
import pyautogui as pag
import os



class App(object):    
    def __init__(self):
        #General configuration
        self.app = appJar.gui("Python Automation Tool","480x360")
        self.app.addButton("Save Position",self.getBtn,1,1)
        self.app.addButton("Save Typing",self.getBtn,2,1)
        self.app.addLabel("TypeArea","Type Area",0,2)
        self.app.addTextArea("typedef",1,2)
        #Status bar configuration
        self.app.addStatusbar(fields=3)
        self.app.setStatusbar("Mouse",0)
        self.app.setStatusbar("x: ",1)
        self.app.setStatusbar("y: ",2)
        #Status bar event polling
        self.app.registerEvent(self.position_cbk)
        self.app.setPollTime(100)

    def getBtn(self,btn):
        print ("Button pressed",btn)
        cwd = os.getcwd()
        filename = self.app.openBox(title=None, dirName=cwd, fileTypes=None, asFile=False, parent=None)
        print(filename)
        
    def start(self):
        self.app.go()

    def position_cbk(self):
        x,y = pag.position()
        self.app.setStatusbar("x: "+str(x),1)
        self.app.setStatusbar("y: "+str(y),2)

def main():
    new = App()
    new.start()

if __name__ == '__main__':
    main()
