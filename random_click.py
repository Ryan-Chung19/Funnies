import pyautogui
import random

x = random.randint(0,2000)
y = random.randint(0,2000)


while True:
    pyautogui.hotkey('alt','tab')
    pyautogui.leftClick(x,y)
    pyautogui.rightClick(x,y)
    x = random.randint(0,2000)
    y = random.randint(0,2000)
