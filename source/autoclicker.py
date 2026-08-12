import mouse
import keyboard as kb
import time
import threading

# Keybinds
key_start = "alt + shift + k"
key_stop = "alt + shift + l"
key_pause = "alt + shift + j"

INTERVAL_LIMIT = 0.0001 # should be changed to OS' actual limit? 0.0158, perhaps?

while True:
    try:
        amount = int(input("Enter amount of clicks (0 = infty, default = 0): "))
        break
    except Exception:
        print("Using default.")
        amount = 0
        break

while True:
    try:
        interval = float(input(f"Enter the interval in seconds between clicks (0 is allowed but not recommended, interval cap starts at = {INTERVAL_LIMIT}): "))
        break
    except Exception:
        print("Using default.")
        interval = INTERVAL_LIMIT
        break
count = 0

interval = 0 if interval < 0 else interval

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

def clicker():
    global pause_event, count, interval
    if interval <= INTERVAL_LIMIT:
        while True:
            pause_event.wait()
            mouse.click("left")
            count += 1
    else:  
        while True:
            pause_event.wait()
            mouse.click("left")
            count += 1
            time.sleep(interval) 

print(f"\nPress {key_start.upper()} to start.\nPress {key_stop.upper()} to stop.\nPress {key_pause.upper()} to pause/resume.\n")

kb.wait(key_start)
print("The program has started.\n")

threading.Thread(target=pause_handler, daemon=True).start() # Pause handler.
threading.Thread(target=clicker, daemon=True).start() # Clicker handler.

# Main Thread. Exit handler.
while True:
    if kb.is_pressed(key_stop) or (count >= amount and amount != 0):
        break
    time.sleep(0.01)