import mss
import numpy as np
import time
import threading
import pyautogui
from pynput import keyboard

# I didnt account for things combining
# I think its clicking before switching cords?

# Left Hexagon 1390, 199
# Left Hexagon BGR RED: (51, 50, 108)
# Left Hexagon BGR BLUE: (248, 191, 22)
# Left Hexagon BGR GREEN: (78, 129, 155)

# Right Hexagon 1478, 262
# Right Hexagon BGR RED: (83, 88, 168)
# Right Hexagon BGR BLUE: (182, 88, 14)
# Right Hexagon BGR GREEN: (29, 80, 72)

running = False
stop_program = False

def find_combo(color_left, color_right):
    if color_left == "RED" and color_right == "RED":
        print ("RED/RED")
        pyautogui.moveTo(1473, 340)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "RED" and color_right == "GREEN":
        print ("RED/GREEN")
        pyautogui.moveTo(2056, 374)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "RED" and color_right == "BLUE":
        print ("RED/BLUE")
        pyautogui.moveTo(1498, 355)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "GREEN" and color_right == "RED":
        print ("GREEN/RED")
        pyautogui.moveTo(2059, 394)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "GREEN" and color_right == "GREEN":
        print ("GREEN/GREEN")
        pyautogui.moveTo(1804, 387)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "GREEN" and color_right == "BLUE":
        print ("GREEN/BLUE")
        pyautogui.moveTo(1821, 754)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "BLUE" and color_right == "RED":
        print ("BLUE/RED")
        pyautogui.moveTo(1931, 744)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "BLUE" and color_right == "GREEN":
        print ("BLUE/GREEN")
        pyautogui.moveTo(1808, 431)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "BLUE" and color_right == "BLUE":
        print ("BLUE/BLUE")
        pyautogui.moveTo(1918, 838)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "VOLCANIC" and color_right == "VOLCANIC":
        print ("VOLCANIC/VOLCANIC")
        pyautogui.moveTo(1602, 943)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "VOLCANIC" and color_right == "RED":
        print ("VOLCANIC/RED")
        pyautogui.moveTo(1398, 827)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "VOLCANIC" and color_right == "GREEN":
        print ("VOLCANIC/GREEN")
        pyautogui.moveTo(1695, 1308)
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "VOLCANIC" and color_right == "BLUE":
        print ("VOLCANIC/BLUE")
        pyautogui.moveTo(1588, 691)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "RED" and color_right == "VOLCANIC":
        print ("RED/VOLCANIC")
        pyautogui.moveTo(1398, 827)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "GREEN" and color_right == "VOLCANIC":
        print ("GREEN/VOLCANIC")
        pyautogui.moveTo(1695, 1308)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click()
    elif color_left == "BLUE" and color_right == "VOLCANIC":
        print ("BLUE/VOLCANIC")
        pyautogui.moveTo(1588, 691)
        time.sleep(0.5)
        pyautogui.click()
    else:
        print("ERROR")


def check_hexagons():

    with mss.mss() as sct:

        # -------- Left hexagon --------

        monitor_left = {
            "left": 1390,
            "top": 199,
            "width": 1,
            "height": 1
        }

        img = np.array(sct.grab(monitor_left))
        b, g, r, a = img[0, 0]

        if b == 51 and g == 50 and r == 108:
            color_left = "RED"
        elif b == 248 and g == 191 and r == 22:
            color_left = "BLUE"
        elif b == 16 and g == 48 and r == 81:
            color_left = "VOLCANIC"
        else:
            color_left = "GREEN"

        monitor_right = {
            "left": 1478,
            "top": 262,
            "width": 1,
            "height": 1
        }

        # -------- Right hexagon --------

        img = np.array(sct.grab(monitor_right))
        b, g, r, a = img[0, 0]

        if b == 83 and g == 88 and r == 168:
            color_right = "RED"
        elif b == 182 and g == 88 and r == 14:
            color_right = "BLUE"
        elif b == 24 and g == 63 and r == 164:
            color_right = "VOLCANIC"
        else:
            color_right = "GREEN"

        # -------- Find out what combo, press buttons --------

        find_combo()

        # (1275, 1086) -> BGR = (9, 13, 17)

        monitor_replay = {
            "left": 1229,
            "top": 621,
            "width": 1,
            "height": 1
        }

        img = np.array(sct.grab(monitor_replay))
        b, g, r, a = img[0, 0]

        if b == 254 and g == 254 and r == 254:
            print ("Restarting Game...")
            pyautogui.click(1293, 1095) # Click Brew Again
            time.sleep(0.5)
            pyautogui.click(1685, 910) # Click OK to maxed out potions
            time.sleep(0.5)


def worker():
    global running, stop_program

    while not stop_program:
        if running:
            check_hexagons()
            time.sleep(2)
            pyautogui.moveTo(1430, 338)
        else:
            time.sleep(0.1)

def on_press(key):
    global running, stop_program

    # toggle with any key
    if key == keyboard.Key.esc:
        print("Exiting...")
        stop_program = True
        return False

    running = not running

    if running:
        print("Started checking every 2 seconds...")
    else:
        print("Stopped checking.")

print("Press any key to start / stop checking.")
print("Press ESC to exit.")

t = threading.Thread(target=worker, daemon=True)
t.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# PRESS ESC TO END PROGRAM