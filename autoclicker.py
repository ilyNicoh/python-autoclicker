import pyautogui
from pynput.keyboard import *

#  ======== optiones ========
delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// shit clicker)
    print("// - Opciones: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controles:")
    print("\t F1 = Reanudar")
    print("\t F2 = Pausar")
    print("\t F3 = Salir")
    print("-----------------------------------------------------")
    print('Presiona F1 para empezar ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
