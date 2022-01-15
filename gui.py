from __future__ import print_function
import pyautogui as pag
import appJar
import utils
import os

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
        ##Row1 - 4
        guiRow = 0
        self.app.startLabelFrame("Keyboard Input", guiRow, 0,1,3,'ew')
        self.app.setPadding(20, 10)
        self.app.addOptionBox("Type Kind", ["Plain Text", "Key Combo","Single Press"])
        self.app.addEntry("TypeArea")
        self.app.addButton("Save Typing",self.parseTextCommands)
        self.app.stopLabelFrame()

        self.app.startLabelFrame("Image Search",guiRow,1,1,3,'ew')
        self.app.setPadding(20, 10)
        self.app.addLabelFileEntry("Select image")
        self.app.addButton("Save Button",self.getImageButton)
        self.app.stopLabelFrame()

        self.app.startLabelFrame("Mouse Clicks", guiRow, 2,1,3,'ew')
        self.app.setPadding(20, 10)

        self.app.addButton("Capture Click Position",self.getClickPositionButton,0,0)
        self.app.addButton("?",self.genericButton,0,1)
        self.app.addLabel("Click Position","")
        self.app.addButton("Save Click Position",self.getClickPositionButton,2,0,2)
        self.app.stopLabelFrame()

        ##Row5
        guiRow = 4
        self.app.startLabelFrame("Saved Command List", guiRow, 0, 3, 3,'ew')
        self.app.setPadding(20, 10)
        self.app.addLabelEntry("Delay(s)",guiRow , 0)
        self.app.addButton("Clear Last Command",self.clearLastCommandButton,guiRow,2)
        ##Row6
        guiRow = 5
        self.app.addScrolledTextArea("CommandList",guiRow,0,5)
        ##Row7
        guiRow = 6
        self.app.addLabelEntry("AutoScript File Name",guiRow,0,1)
        self.app.addLabel(".py",".py",guiRow,1,1)
        self.app.setLabelAlign(".py","left")
        self.app.addButton("Save AutoScript File",self.genericButton,guiRow,2)
        self.app.stopLabelFrame()


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
            fileName = self.app.getEntry("AutoScript File Name")


            if fileName == "":

                self.app.infoBox("Error: File Name Missing", "Type a name for the script before saving", parent=None)

            elif self.commandList == []:

                self.app.infoBox("Error: No command created", "Create a command to generate automated script", parent=None)

            else:

                fileName = fileName+".py"
                with open(fileName,'w') as outfile:
                    outfile.write(utils.buildFile(self.pythonCommands))
                self.app.infoBox("PyAutoScript Generated", "The script "+fileName+" was successfully generated", parent=None)


        elif btn == '?':

            self.app.infoBox("Capture a new cursor location","Select \"Capture Click Position\", place your cursor in the desired\n screen location and press SPACE BAR to capture the new location.", parent=None)

        else:

            self.commandList.append("Button pressed {}, not yet implemented".format(btn))

            self.app.setEntry("Delay(s)", "0.01")
            self.writeCommands()

    def parseTextCommands(self,btn):
        opt = self.app.getOptionBox("Type Kind")
        txt = self.app.getEntry("TypeArea").lower()
        pause = self.app.getEntry("Delay(s)")
        #Plain text handler
        if(opt == "Plain Text"):
            txt = self.app.getEntry("TypeArea")
            self.commandList.append("Plain write '{}'".format(txt))
            self.pythonCommands.append(utils.write(txt,pause))

        #Key Combo handler
        elif (opt == "Key Combo"):
            txt = self.app.getEntry("TypeArea").lower()
            lst = [item for item in txt.split() if item in utils.keys]
            self.commandList.append("Key Combo '{}'".format("+".join(lst)))
            self.pythonCommands.append(utils.hotkey(lst,pause))

        #Single Press handler
        elif (opt == "Single Press" and txt in utils.keys):
            txt = self.app.getEntry("TypeArea").lower()
            self.commandList.append("Single Press '{}'".format(txt))
            self.pythonCommands.append(utils.press(txt,pause))


        #Invalid Handler
        else:
            print("Invalid Option")
        #Post-parse actions
        self.app.clearEntry("TypeArea")
        self.writeCommands()

    def getClickPositionButton(self,btn):

        pause = self.app.getEntry("Delay(s)")
        if (btn == "Capture Click Position"):
            self.storedXpos = self.xpos
            self.storedYpos = self.ypos
            self.app.setLabel("Click Position","X:"+str(self.storedXpos)+",Y:"+str(self.storedYpos))
        elif (btn == "Save Click Position"):
            x,y = self.app.getLabel("Click Position").split(',')
            self.commandList.append("Click on position X:{} Y:{}".format(x[2:],y[2:]))
            self.pythonCommands.append(utils.click(x[2:],y[2:],pause))
            self.writeCommands()

    def getImageButton(self,btn):

        pause = self.app.getEntry("Delay(s)")

        if (btn == "Save Button"):
            imagePath = self.app.getEntry("Select image")
            self.commandList.append("Click on image {}".format(imagePath))

            if imagePath != "":
                self.pythonCommands.append(utils.imageClick(imagePath,pause))

                self.writeCommands()

    def clearLastCommandButton(self,btn):
        if len(self.commandList) == 0:
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
        else:
            self.commandList.pop()
            self.pythonCommands.pop()
            self.writeCommands()

    def clearAllCommandsButton(self,btn):
        if len(self.commandList) == 0:
            self.app.clearTextArea("CommandList")
            self.app.setTextArea("CommandList","Command List Empty!")
        else:
            self.commandList = []
            self.pythonCommands = []
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


def main():
    new = App()
    new.start()

if __name__ == '__main__':
    main()
