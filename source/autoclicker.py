import pyautogui as gui
import keyboard as kb
import time

gui.PAUSE = 0 # removes pause between clicks.
INTERVAL_LIMIT = 0.001


amount = int(input("Enter amount of clicks (0 = infty): "))
interval = float(input(f"Enter the interval in seconds between clicks (not lower than {INTERVAL_LIMIT}): "))

if(interval < INTERVAL_LIMIT):
    interval = INTERVAL_LIMIT


print("Press K to start.\nPress L to stop.\nPress J to pause/resume.\n")


kb.wait("k")
count = 0
while True:
    gui.click()
    count += 1
    time.sleep(interval)

    # exit handler
    if kb.is_pressed("l") or (count >= amount and amount != 0):
        break

    # pause handler
    if kb.is_pressed("j"):
        print("Paused. Press J to resume.\n\a")
        time.sleep(0.1)
        kb.wait("j")
        time.sleep(0.1)
        print("Resumed.\n\a")