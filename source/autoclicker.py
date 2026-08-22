import mouse
import keyboard as kb
import time
import threading

# Keybinds
key_start = "alt + shift + k"
key_stop = "alt + shift + l"
key_pause = "alt + shift + j"

INTERVAL_LIMIT = 0.01 # should be changed to OS' actual limit? 0.0158, perhaps?

while True:
    try:
        amount = int(input("Enter amount of clicks (0 = infty, default = 0): "))
        if amount < 0:
            raise(ValueError)
        break
    except Exception:
        print("Using default.")
        amount = 0
        break

while True:
    try:
        interval = float(input(f"Enter the interval in seconds (float) between clicks (below {INTERVAL_LIMIT} and 0 are not recommended, default = {INTERVAL_LIMIT}): "))
        if interval < 0:
            raise(ValueError)
        break
    except Exception:
        print("Using default.")
        interval = INTERVAL_LIMIT
        break

counter = 0

# An event to put a threaded process on pause
pause_event = threading.Event()
pause_event.set()

def pause_handler():
    global pause_event
    while True:
        kb.wait(key_pause)
        pause_event.clear() if pause_event.is_set() else pause_event.set()
        print("Resumed.\n\a" if pause_event.is_set() else "Paused.\n\a")
        time.sleep(0.1)

def clicker_counted():
    global pause_event, counter, interval
    if interval != 0:
        while True:
            pause_event.wait()
            mouse.click("left")
            counter += 1
            time.sleep(interval)
    else:  
        while True:
            pause_event.wait()
            mouse.click("left")
            counter += 1

def clicker_not_counted():
    global pause_event, interval
    if interval != 0:
        while True:
            pause_event.wait()
            mouse.click("left")
            time.sleep(interval)
    else:  
        while True:
            pause_event.wait()
            mouse.click("left")

print(f"\nPress {key_start.upper()} to start.\nPress {key_stop.upper()} to stop.\nPress {key_pause.upper()} to pause/resume.\n")

kb.wait(key_start)
print("The program has started.\n")

threading.Thread(target=pause_handler, daemon=True).start() # Pause handler.
threading.Thread(target=(clicker_counted if amount != 0 else clicker_not_counted), daemon=True).start() # Clicker handler.

# Main Thread. Exit handler.
while True:
    if kb.is_pressed(key_stop) or (counter >= amount and amount != 0):
        break
    time.sleep(0.01)