import keyboard #pip install keyboard
import time
import ctypes

# create volume gesture with controller keyboard and mouse

def gesture_volume(volume:int):
    keyboard.press_and_release("windows+g")

    cross_product = 4.6 * volume / 2
    # 4.6 = 2
    # ? = volume
    print(cross_product)
    ctypes.windll.user32.SetCursorPos((635 + round(cross_product)), 540 )
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) #left up

    

def main():
    gesture_volume(15)

main()