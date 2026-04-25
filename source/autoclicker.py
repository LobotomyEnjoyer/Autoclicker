import pyautogui as gui
import keyboard as kb
import time
import threading

gui.PAUSE = 0 # removes pause between clicks.
INTERVAL_LIMIT = 0.001

amount = int(input("Enter amount of clicks (0 = infty): "))
interval = float(input(f"Enter the interval in seconds between clicks (not lower than {INTERVAL_LIMIT}): "))
count = 0

if(interval < INTERVAL_LIMIT):
    interval = INTERVAL_LIMIT

is_paused = False
def pause_handler():
    global is_paused
    while True:
        kb.wait("j")
        is_paused = not is_paused
        print("Paused.\n\a" if is_paused else "Resumed.\n\a")
        time.sleep(0.1)

def clicker():
    global is_paused, count, interval
    while True:
        if not is_paused:
            gui.click()
            count += 1
            time.sleep(interval)
        else:
            time.sleep(0.1)


print("\nPress K to start.\nPress L to stop.\nPress J to pause/resume.\n")

kb.wait("k")

threading.Thread(target=pause_handler, daemon=True).start() # Pause handler.
threading.Thread(target=clicker, daemon=True).start() # Clicker handler.

# Main Thread. Exit handler.
while True:
    if kb.is_pressed("l") or (count >= amount and amount != 0):
        break