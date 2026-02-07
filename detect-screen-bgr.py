# click_pixel_bgr.py


# 1390, 199
# 1478, 262
import mss
import numpy as np
from pynput import mouse, keyboard

print("Click anywhere to read that pixel's BGR value.")
print("Press any key to stop.\n")

def on_click(x, y, button, pressed):
    if not pressed:
        return

    # IMPORTANT: create mss inside the callback thread
    with mss.mss() as sct:
        monitor = {
            "left": x,
            "top": y,
            "width": 1,
            "height": 1
        }

        img = np.array(sct.grab(monitor))
        b, g, r, a = img[0, 0]

        print(f"Click at ({x}, {y}) -> BGR = ({b}, {g}, {r})")

def on_press(key):
    print("\nStopping...")
    return False

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

keyboard_listener.join()
mouse_listener.stop()
