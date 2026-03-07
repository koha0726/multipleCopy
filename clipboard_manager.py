import pyperclip


class ClipboardManager:

    def __init__(self, slots=3):
        self.slots = {}

        for i in range(1, slots + 1):
            self.slots[i] = ""

    def save_to_slot(self, slot):
        text = pyperclip.paste()
        self.slots[slot] = text

    def paste_from_slot(self, slot):
        text = self.slots.get(slot, "")

        if text:
            pyperclip.copy(text)

    def get_slots(self):
        return self.slots