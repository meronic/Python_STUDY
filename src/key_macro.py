import pyautogui
import time


time.sleep(3)

width, height = pyautogui.size()

print('width={0}, height={1}'.format(width,height))

x,y = pyautogui.position()

print('mouse position = x {0}, y {1}'.format(x,y))

pyautogui.moveTo(20,20,0)

x,y = pyautogui.position()
print('mouse position = x {0}, y {1}'.format(x,y))
