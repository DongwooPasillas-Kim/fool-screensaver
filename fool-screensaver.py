import pyautogui as pa
from time import sleep


t_input=input("Type in the interval [in minutes] between each mouse movement: ")
t_calc=60*float(t_input)
input("Locate your mouse to a position where you want the automated movement to take place, and press Enter.")
p_chosen=pa.position()
p_offset=pa.Point(p_chosen.x+1,p_chosen.y)
while 1:
    sleep(t_calc)
    pa.moveTo(p_chosen)
    pa.click()
    sleep(t_calc)
    pa.moveTo(p_offset)
    pa.click()