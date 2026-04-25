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

pause_event = threading.Event()
pause_event.set()

def pause_handler():
    global pause_event
    while True:
        kb.wait("j")
        pause_event.clear() if pause_event.is_set() else pause_event.set()
        print("Resumed.\n\a" if pause_event.is_set() else "Paused.\n\a")
        time.sleep(0.1)

def clicker():
    global pause_event, count, interval
    while True:
        pause_event.wait()
        gui.click()
        count += 1
        time.sleep(interval)



print("\nPress K to start.\nPress L to stop.\nPress J to pause/resume.\n")

kb.wait("k")
print("The program has started.\n")

threading.Thread(target=pause_handler, daemon=True).start() # Pause handler.
threading.Thread(target=clicker, daemon=True).start() # Clicker handler.

# Main Thread. Exit handler.
while True:
    if kb.is_pressed("l") or (count >= amount and amount != 0):
        break