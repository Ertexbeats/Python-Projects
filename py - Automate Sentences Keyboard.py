import random
import pyautogui as pg
import time

Palabras = ("test1", "test2", "test3")

time.sleep(1)

for i in range(100):
    a = random.choice(Palabras)
    pg.write(a)
    pg.press("enter")
