import keyboard

while keyboard.wait("esc")!=True:
    recorded = keyboard._listener
    print("_________________________")
    print(recorded)

hm.KeyDown