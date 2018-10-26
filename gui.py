from __future__ import print_function
import appJar
import pyautogui as pag
import os




class App(object):    
    def __init__(self):
        #General configuration
        self.app = appJar.gui("Python Automation Tool","1280x720")
        #Menu Bar
        self.app.addMenuList("File", ["Save","-","Exit"], self.genericButton)
        self.app.addMenuList("Help",["Help Contents","-","About PyAuTo"],self.genericButton)
        #Buttons
        ##Row1
        self.app.addLabel("Click","Click",0,0)
        self.app.addLabel("Button","Button",0,1)
        self.app.addLabel("Text","Text",0,2)
        ##Row2
        self.app.addTextArea("clickdef",1,0)
        self.app.addTextArea("buttondef",1,1)
        self.app.addTextArea("typedef",1,2)
        ##Row3
        self.app.addButton("Save Position",self.genericButton,2,0)
        self.app.addButton("Save Typing",self.genericButton,2,2)
        ##Row5
        self.app.addLabel("commlist","Command List",3,0)
        ##Row4
        self.app.addTextArea("CommandList",4,0,3)
        #Status bar configuration
        self.app.addStatusbar(fields=3)
        self.app.setStatusbar("Mouse",0)
        self.app.setStatusbar("x: ",1)
        self.app.setStatusbar("y: ",2)
        #Status bar event polling
        self.app.registerEvent(self.position_cbk)
        self.app.setPollTime(100)

    def genericButton(self,btn):
        if btn == 'Exit':
            self.stop()
        elif btn == 'About PyAuTo':
            self.app.infoBox("About PyAuTo", "This tool was created by\nJavier Alvarez & Enrique Espinosa\nFor Continental Engineering Services")
        else:
            print ("Button pressed",btn, "Not yet implemented")

    def start(self):
        self.app.go()
    
    def stop(self):
        self.app.stop()

    def position_cbk(self):
        x,y = pag.position()
        self.app.setStatusbar("x: "+str(x),1)
        self.app.setStatusbar("y: "+str(y),2)

def main():
    new = App()
    new.start()

if __name__ == '__main__':
    main()
