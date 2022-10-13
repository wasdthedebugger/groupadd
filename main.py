#SET THE COORDINATES ACCORDING TO YOUR SCREEN

import pandas as pd 
import pyautogui as pg
import time

j = 0
pg.moveTo(100, 200)

data = pd.read_excel('PATH TO YOUR EXCEL FILE')
list = data['NAME OF YOUR COLUMN'].tolist()

time.sleep(10)

def name():
    pg.moveTo(719, 317)
    pg.click()

def wait():
    time.sleep(1)

def add():
    pg.moveTo(1215, 506)
    pg.click()

def write(i):
    pg.typewrite(i)
    wait()
    pg.press('enter')

def clear():
    name()
    pg.hotkey('ctrl', 'a')
    pg.press('delete')

for i in list:
    j=j+1
    clear()
    wait()
    name()
    wait()
    write(i)
    wait()
    add()
    if j%3==0:
        pg.moveTo(964, 853)
        pg.click()
        time.sleep(10)




    