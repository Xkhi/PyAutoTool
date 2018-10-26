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

        
        ##Row1
        guiRow = 0
        self.app.addLabel("Click","Click",guiRow,0)
        self.app.addLabel("Button","Button",guiRow,1)
        self.app.addLabel("Text","Text",guiRow,2)
        
        ##Row2
        guiRow = 1
        self.app.addButton("Get Click Position",self.getClickPositionButton,guiRow,0)
        self.app.addOptionBox("Type Kind", ["Plain Text", "Key Combo"], guiRow, 2)
        
        ##Row3
        guiRow = 2
        self.app.addLabel("Click Position","",guiRow,0)
        self.app.addLabelFileEntry("Select image", guiRow, 1)
        self.app.addTextArea("TypeArea",guiRow,2)
        
        ##Row4
        guiRow = 3
        self.app.addButton("Save Click Position",self.genericButton,guiRow,0)
        self.app.addButton("Save Button",self.genericButton,guiRow,1)
        self.app.addButton("Save Typing",self.genericButton,guiRow,2)
        
        ##Row5
        guiRow = 4
        #self.app.addLabel("CommandListLabel","Command List",guiRow,0)
        self.app.addLabelEntry("Delay(s)",guiRow , 0)
        self.app.addButton("Clear Last Command",self.clearLastCommandButton,guiRow,2)
        #self.app.addButton("Clear All Commands",self.clearAllCommandsButton,guiRow,2)
        #self.app.addLabel("commlist","Command List",Label2Level,0)
        
        ##Row6
        guiRow = 5
        self.app.addScrolledTextArea("CommandList",guiRow,0,3)
        
        ##Row7
        guiRow = 6
        self.app.addLabelEntry("AutoScrip File Name",guiRow , 0)
        self.app.addButton("Save AutoScript File",self.genericButton,guiRow,2)
        
        
        #Status bar configuration
        self.app.addStatusbar(fields=3)
        self.app.setStatusbar("Mouse",0)
        self.app.setStatusbar("x: ",1)
        self.app.setStatusbar("y: ",2)
        #Status bar event polling
        self.app.registerEvent(self.position_cbk)
        self.app.setPollTime(100)
        self.app.setEntry("Delay(s)", "0.01")
        
        self.xpos = 0
        self.ypos = 0
        
        self.storedXpos = 0
        self.storedYpos = 0
        
        self.commandList = []

    def genericButton(self,btn):
        if btn == 'Exit':
            self.stop()
        elif btn == 'About PyAuTo':
            self.app.infoBox("About PyAuTo", "This tool was created by\nJavier Alvarez & Enrique Espinosa\nFor Continental Engineering Services")
        else:
            self.commandList.append("Button pressed"+btn+"Not yet implemented")
            print ("Button pressed",btn, "Not yet implemented")
            
            self.app.setEntry("Delay(s)", "0.01")
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList",self.writeCommands())
            
    def getClickPositionButton(self,btn):
        
            self.storedXpos = self.xpos
            self.storedYpos = self.ypos
            
            self.app.setLabel("Click Position","x:"+str(self.storedXpos)+",y:"+str(self.storedYpos))
            print ("Position Stored",self.storedXpos,self.storedYpos)
            print(self.app.getEntry("Delay(s)"))
            
    def clearLastCommandButton(self,btn):
        
        if len(self.commandList) == 0:
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
        else:
            self.commandList.pop()
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList",self.writeCommands())
            
    def clearAllCommandsButton(self,btn):
        
        if len(self.commandList) == 0:
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
        else:
            self.commandList = []
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
            
    def start(self):
        self.app.go()
    
    def stop(self):
        self.app.stop()

    def position_cbk(self):
        x,y = pag.position()
        self.app.setStatusbar("x: "+str(x),1)
        self.app.setStatusbar("y: "+str(y),2)
        
        self.xpos = x
        self.ypos = y
        
    def writeCommands(self):
        
        commandText = ""
        
        for command in self.commandList:
            commandText = commandText + command + "\n"
        
        return commandText
        
        

def main():
    new = App()
    new.start()

if __name__ == '__main__':
    main()
