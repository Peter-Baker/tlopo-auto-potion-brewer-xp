import mss
import numpy as np
from pynput import mouse, keyboard

# Left Hexagon 1390, 199
# Left Hexagon BGR RED: (51, 50, 108)
# Left Hexagon BGR BLUE: (248, 191, 22)
# Left Hexagon BGR GREEN: (78, 129, 155)

# Right Hexagon 1478, 262
# Right Hexagon BGR RED: (83, 88, 168)
# Right Hexagon BGR BLUE: (182, 88, 14)
# Right Hexagon BGR GREEN: (29, 80, 72)

def on_click(x, y, button, pressed):
    if not pressed:
        return

    with mss.mss() as sct:

        # Detect left hexagon, find color

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
        else:
            color_left = "GREEN"

        monitor_right = {
            "left": 1478,
            "top": 262,
            "width": 1,
            "height": 1
        }

        # Detect right hexagon, find color

        img = np.array(sct.grab(monitor_right))
        b, g, r, a = img[0, 0]

        if b == 83 and g == 88 and r == 168:
            color_right = "RED"
        elif b == 182 and g == 88 and r == 14:
            color_right = "BLUE"
        else:
            color_right = "GREEN"

        # Color combo, print

        if color_left == "RED" and color_right == "RED":
            print ("RED/RED")
        elif color_left == "RED" and color_right == "GREEN":
            print ("RED/GREEN")
        elif color_left == "RED" and color_right == "BLUE":
            print ("RED/BLUE")
        elif color_left == "GREEN" and color_right == "RED":
            print ("GREEN/BLUE")
        elif color_left == "GREEN" and color_right == "GREEN":
            print ("GREEN/GREEN")
        elif color_left == "GREEN" and color_right == "BLUE":
            print ("GREEN/BLUE")
        elif color_left == "BLUE" and color_right == "RED":
            print ("BLUE/RED")
        elif color_left == "BLUE" and color_right == "GREEN":
            print ("BLUE/GREEN")
        elif color_left == "BLUE" and color_right == "BLUE":
            print ("BLUE/BLUE")
        else:
            print("ERROR")

def on_press(key):
    print("\nStopping...")
    return False

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

keyboard_listener.join()
mouse_listener.stop()