import keyboard
import time


class HotkeyManager:

    def __init__(self, clipboard_manager):
        self.clipboard_manager = clipboard_manager

    def register_copy_hotkey(self):

        def on_copy():
            time.sleep(0.05)
            self.clipboard_manager.save_auto()

        keyboard.add_hotkey("ctrl+c", on_copy)

    def register_paste_hotkeys(self):

        keyboard.add_hotkey(
            "alt+1",
            lambda: self.clipboard_manager.paste_from_slot(1)
        )

        keyboard.add_hotkey(
            "alt+2",
            lambda: self.clipboard_manager.paste_from_slot(2)
        )

        keyboard.add_hotkey(
            "alt+3",
            lambda: self.clipboard_manager.paste_from_slot(3)
        )

    def register_all(self):

        self.register_copy_hotkey()
        self.register_paste_hotkeys()