@echo off
python --version
if ERRORLEVEL 1 goto nopython

echo Installing PyMsgBox v1.0.6
pip install PyMsgBox-1.0.6.zip
if ERRORLEVEL 1 goto msgbox

echo Installing PyTweening v1.0.3
pip install PyTweening-1.0.3.zip
if ERRORLEVEL 1 goto pytweening

echo Installing AppJar v0.93.0
pip install appJar-0.93.0.tar.gz
if ERRORLEVEL 1 goto appjar

echo Installing Pillow v5.3.0 for Python 2.7 64-bit
pip install Pillow-5.3.0-cp27-cp27m-win_amd64.whl
if ERRORLEVEL 1 (echo Failed, trying another version; goto pillow2) else (goto next)

:pillow2
echo Installing Pillow v5.3.0 for Python 2.7 32-bit
pip install Pillow-5.3.0-cp27-cp27m-win32.whl
if ERRORLEVEL 1 (echo Failed, trying another version; goto pillow3) else (goto next)

:pillow3
echo Installing Pillow v5.3.0 for Python 3.6 64-bit
pip install Pillow-5.3.0-cp36-cp36m-win_amd64.whl
if ERRORLEVEL 1 (echo Failed, trying another version; goto pillow4) else (goto next)

:pillow4
echo Installing Pillow v5.3.0 for Python 3.6 32-bit
pip install Pillow-5.3.0-cp36-cp36m-win32.whl
if ERRORLEVEL 1 goto pillowError

:next
echo Installing PyScreeze v0.1.18
pip install PyScreeze-0.1.18.tar.gz
if ERRORLEVEL 1 goto pyscreeze

echo Installing PyAutoGUI v0.9.38
pip install PyAutoGUI-0.9.38.tar.gz
if ERRORLEVEL 1 goto pyautogui

echo Installing Python Automation Tool
mkdir %APPDATA%\..\..\Desktop\PyAutoTool
move *.py %APPDATA%\..\..\Desktop\PyAutoTool

echo Installation succesful
pause
exit 0

:nopython
echo Python not present, please install and retry
exit 1

:pillowError
echo Python or System architecture not compatible with Pillow, please contact support
exit 1

:msgbox
echo Error installing PyMsgBox, please retry
exit 1

:pyscreeze
echo Error installing PyScreeze, please retry
exit 1

:pytweening
echo Error installing PyTweening, please retry
exit 1

:pyautogui
echo Error installing PyAutoGUI, please retry
exit 1

:appjar
echo Error installing AppJar, please retry
exit 1