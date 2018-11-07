from __future__ import print_function
import pyautogui as pag
import appJar
import utils
import os
from nt import lstat

class App(object):
    def __init__(self):
        #Local properties
        self.xpos = 0
        self.ypos = 0

        self.storedXpos = 0
        self.storedYpos = 0

        self.commandList = []
        self.pythonCommands = []
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
        self.app.addButton("Capture Click Position",self.getClickPositionButton,guiRow,0)
        self.app.addOptionBox("Type Kind", ["Plain Text", "Key Combo","Single Press"], guiRow, 2)
        ##Row3
        guiRow = 2
        self.app.addLabel("Click Position","",guiRow,0)
        self.app.addLabelFileEntry("Select image", guiRow, 1)
        self.app.addTextArea("TypeArea",guiRow,2)
        ##Row4
        guiRow = 3
        self.app.addButton("Save Click Position",self.getClickPositionButton,guiRow,0)
        self.app.addButton("Save Button",self.genericButton,guiRow,1)
        self.app.addButton("Save Typing",self.parseTextCommands,guiRow,2)
        ##Row5
        guiRow = 4
        self.app.addLabelEntry("Delay(s)",guiRow , 0)
        self.app.addButton("Clear Last Command",self.clearLastCommandButton,guiRow,2)
        ##Row6
        guiRow = 5
        self.app.addScrolledTextArea("CommandList",guiRow,0,3)
        ##Row7
        guiRow = 6
        self.app.addLabelEntry("AutoScript File Name",guiRow , 0)
        self.app.addButton("Save AutoScript File",self.genericButton,guiRow,2)
        #Status bar configuration
        self.app.addStatusbar(fields=3)
        self.app.setStatusbar("Mouse",0)
        self.app.setStatusbar("X: ",1)
        self.app.setStatusbar("Y: ",2)
        #Status bar event polling
        self.app.registerEvent(self.positionCbk)
        self.app.setPollTime(100)
        self.app.setEntry("Delay(s)", "0.01")

    def genericButton(self,btn):
        if btn == 'Exit':
            self.stop()
        elif btn == 'About PyAuTo':
            self.app.infoBox("About PyAuTo", utils.about)
        elif btn == 'Save AutoScript File':
            with open(self.app.getEntry("AutoScript File Name"),'w') as outfile:
                outfile.write(utils.buildFile(self.pythonCommands))
        else:
            self.commandList.append("Button pressed {}, not yet implemented".format(btn))

            self.app.setEntry("Delay(s)", "0.01")
            self.writeCommands()

    def parseTextCommands(self,btn):
        opt = self.app.getOptionBox("Type Kind")
        txt = self.app.getTextArea("TypeArea").lower()
        pause = self.app.getEntry("Delay(s)")
        #Plain text handler
        if(opt == "Plain Text"):
            self.commandList.append("Plain write '{}'".format(txt))
            self.pythonCommands.append(utils.write(txt,pause))
        #Key Combo handler
        elif (opt == "Key Combo"):
            lst = [item for item in txt.split() if item in utils.keys]
            self.commandList.append("Key Combo '{}'".format("+".join(lst)))
            self.pythonCommands.append(utils.hotkey(lst,pause))
        #Single Press handler
        elif (opt == "Single Press" and txt in utils.keys):
            self.commandList.append("Single Press '{}'".format(txt))
            self.pythonCommands.append(utils.press(txt,pause))
        #Invalid Handler
        else:
            print("Invalid Option")
        #Post-parse actions
        self.app.clearTextArea("TypeArea")
        self.writeCommands()

    def getClickPositionButton(self,btn):
        duration = self.app.getEntry("Delay(s)")
        if (btn == "Capture Click Position"):
            self.storedXpos = self.xpos
            self.storedYpos = self.ypos
            self.app.setLabel("Click Position","X:"+str(self.storedXpos)+",Y:"+str(self.storedYpos))
        elif (btn == "Save Click Position"):
            x,y = self.app.getLabel("Click Position").split(',')
            self.commandList.append("Click on position X:{} Y:{}".format(x[2:],y[2:]))
            self.pythonCommands.append(utils.click(x[2:],y[2:],duration))
            self.writeCommands()

    def clearLastCommandButton(self,btn):
        if len(self.commandList) == 0:
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
        else:
            self.commandList.pop()
            self.writeCommands()

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

    def positionCbk(self):
        self.xpos,self.ypos = pag.position()
        self.app.setStatusbar("x: "+str(self.xpos),1)
        self.app.setStatusbar("y: "+str(self.ypos),2)

    def writeCommands(self):
        self.app.clearTextArea("CommandList")
        commandText = ""

        for command in self.commandList:
            commandText = commandText + command + "\n"

        self.app.setTextArea("CommandList", commandText)
        print(self.pythonCommands)


def main():
    new = App()
    new.start()

if __name__ == '__main__':
    main()
