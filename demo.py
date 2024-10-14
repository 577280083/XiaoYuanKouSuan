import pyautogui
import time
from cnocr import CnOcr
import numpy as np

ocr = CnOcr(det_model_name='naive_det', cand_alphabet='0123456789') 

def left():
    pyautogui.moveTo(441, 634, duration=0.1)
    pyautogui.dragTo(300, 700, button='left')
    pyautogui.dragTo(436, 800, button='left')
def right():
    pyautogui.moveTo(250, 620, duration=0.1)
    pyautogui.dragTo(350, 680, button='left')
    pyautogui.dragTo(240, 760, button='left')

while True:
    pyautogui.screenshot('left.png',region=(270,290,75,75))
    pyautogui.screenshot('right.png',region=(400,290,75,75))
    time.sleep(0.05)
    outLeft = ocr.ocr('left.png')
    outRight = ocr.ocr('right.png')
    leftNum = int(outLeft[0]['text'])
    rightNum = int(outRight[0]['text'])
    print('左侧：',outLeft[0]['text'],'右侧：',outRight[0]['text'])
    print('预测准确度',outLeft[0]['score'],outRight[0]['score'])
    if leftNum < rightNum:
        left()
    elif leftNum > rightNum:
        right()
    elif leftNum ==  rightNum:
        print('识别出错')
    time.sleep(0.29)