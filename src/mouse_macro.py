import pyautogui
import sys


##pyautogui.click(clicks=2, interval = 1)
##
##pyautogui.doubleClick()

##pyautogui.moveTo(750,70,2)
##
##pyautogui.click(clicks=1,interval=1)
##
##pyautogui.typewrite('hello world',interval =0.05)

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X : ' + str(x).rjust(4) +'\n'+ 'Y : ' + str(y).rjust(4)+'\n\n'
        print(positionStr, end='')
        

except KeyboardInterrupt:
    print('\n')

