import pyautogui as gui
import keyboard as kb
import time

gui.PAUSE = 0 # убирает паузу между "нажатиями"

INTERVAL_LIMIT = 0.001

amount = int(input("Enter amount of clicks (0 = infty): "))
interval = float(input(f"Enter the interval in seconds between clicks (not lower than {INTERVAL_LIMIT}): "))

if(interval < INTERVAL_LIMIT):
    interval = INTERVAL_LIMIT

count = 0
print("Press K to start.\nPress L to stop.\n")
kb.wait("k")
while True:
    gui.click()
    count += 1
    # print(f"click! {count}")
    time.sleep(interval)

    if kb.is_pressed("l") or (count >= amount and amount != 0):
        break