import pyautogui
import msvcrt
import time

print('获取鼠标的位置，按p退出,3秒后开始')
time.sleep(3)

while True:
    print(pyautogui.position())
    if msvcrt.kbhit():
        if msvcrt.getch().decode('utf-8').lower() == 'p':
            print('停止运行')
            break
