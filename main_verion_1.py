import keyboard #pip install keyboard
import time
import ctypes
from VoiceGesture import voice_gesture

vg = voice_gesture()

# create volume gesture with controller keyboard and mouse

def gesture_volume(volume:int):
    keyboard.press_and_release("windows+g")

    cross_product = 4.6 * volume / 2
    # 4.6 = 2
    # ? = volume
    ctypes.windll.user32.SetCursorPos((635 + round(cross_product)), 540 )
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) #left up

    

def main():
    while True : 
        message = vg.reconize_voice()
        gesture_volume(20)
        vg.speak(f"le volume est de {20} desormais, vous avez dit {message}")

main()