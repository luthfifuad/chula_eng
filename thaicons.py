import tkinter as tk
from tkinter import font

# List of Thai consonants and their names
thai_consonants = {
    "ก": "gor kai",
    "ข": "khor khai",
    "ฃ": "khor khuat",
    "ค": "khor khwai",
    "ฅ": "khor khon",
    "ฆ": "khor ra-khang",
    "ง": "ngor ngu",
    "จ": "jor jan",
    "ฉ": "chor ching",
    "ช": "chor chang",
    "ซ": "sor so",
    "ฌ": "chor choe",
    "ญ": "yor ying",
    "ฎ": "dor chada",
    "ฏ": "tor patak",
    "ฐ": "thor than",
    "ฑ": "thor montho",
    "ฒ": "thor phu-thao",
    "ณ": "nor nen",
    "ด": "dor dek",
    "ต": "tor tao",
    "ถ": "thor thung",
    "ท": "thor thahan",
    "ธ": "thor thong",
    "น": "nor nu",
    "บ": "bor baimai",
    "ป": "por pla",
    "ผ": "phor phueng",
    "ฝ": "for fa",
    "พ": "phor phan",
    "ฟ": "for fan",
    "ภ": "phor sam-phao",
    "ม": "mor ma",
    "ย": "yor yak",
    "ร": "ror ruea",
    "ล": "lor ling",
    "ว": "wor waen",
    "ศ": "sor sala",
    "ษ": "sor rue-si",
    "ส": "sor suea",
    "ห": "hor hip",
    "ฬ": "lor chu-la",
    "อ": "or ang",
    "ฮ": "hor nok-huk"
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("300x200")

        self.current_consonant = None
        self.showing_name = False

        self.card_label = tk.Label(root, text="", font=("Arial", 48))
        self.card_label.pack(expand=True)

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()

        self.next_card()

    def next_card(self):
        self.current_consonant = next(iter(thai_consonants.keys()))
        self.showing_name = False
        self.card_label.config(text=self.current_consonant)
        self.flip_button.config(state=tk.NORMAL)

    def flip_card(self):
        if not self.showing_name:
            self.card_label.config(text=thai_consonants[self.current_consonant])
            self.showing_name = True
        else:
            self.card_label.config(text=self.current_consonant)
            self.showing_name = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()