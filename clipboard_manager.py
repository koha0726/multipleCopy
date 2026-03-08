import pyperclip


class ClipboardManager:

    def __init__(self, slots=3):
        self.max_slots = slots
        self.slots = {}
        self.last_text = ""

        for i in range(1, slots + 1):
            self.slots[i] = ""

    def save_auto(self):

        try:
            text = pyperclip.paste()

        except Exception as e:
            print("Clipboard error:", e)
            return

        if not text:
            return

        if text == self.last_text:
            return

        self.last_text = text

        # スロットを後ろにずらす
        for i in range(self.max_slots, 1, -1):
            self.slots[i] = self.slots[i - 1]

        self.slots[1] = text

        print("Saved:", text)
        print(self.slots)

    def paste_from_slot(self, slot):

        text = self.slots.get(slot, "")

        if text:
            pyperclip.copy(text)

    def get_slots(self):
        return self.slots