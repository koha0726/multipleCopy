from clipboard_manager import ClipboardManager
from hotkey_manager import HotkeyManager
import keyboard


def main():

    # クリップボード管理作成
    clipboard_manager = ClipboardManager()

    # ホットキー管理作成
    hotkey_manager = HotkeyManager(clipboard_manager)

    # ショートカット登録
    hotkey_manager.register_all()

    print("Clipboard Manager 起動中")
    print("終了するには ESC を押してください")

    # 常駐
    keyboard.wait("esc")


if __name__ == "__main__":
    main()