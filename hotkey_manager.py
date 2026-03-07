import keyboard

class HotkeyManager:

    def __init__(self, clipboard_manager):
        self.clipboard_manager = clipboard_manager

# コピーショートカット
    def register_copy_hotkeys(self):
        keyboard.add_hotkey(
            "ctrl+shift+1",
            lambda: self.clipboard_manager.save_to_slot(1)
        )

        keyboard.add_hotkey(
            "ctrl+shift+2",
            lambda: self.clipboard_manager.save_to_slot(2)
        )

        keyboard.add_hotkey(
            "ctrl+shift+3",
            lambda: self.clipboard_manager.save_to_slot(3)
        )

    # 貼り付けショートカット
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

    # 登録まとめ
    def register_all(self):
        self.register_copy_hotkeys()
        self.register_paste_hotkeys()