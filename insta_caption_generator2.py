import tkinter as tk
import random

class CaptionGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Caption Generator 📸")


        self.themes = {
            "Travel ✈️": [
                "Lost in Tokyo 🏮",
                "Adventure begins here 🌍",
                "Catching flights, not feelings ✈️",
                "Wander often, wonder always 🌌",
            ],
            "Food 🍣": [
                "Good food, good mood 😋",
                "Sushi is my love language 🍣",
                "Fries before guys 🍟",
                "Powered by pizza 🍕",
            ],
            "Funny 😂": [
                "Do it for the plot 🎬",
                "404: Homework not found 📚",
                "I told you I was debugging 🐞",
                "Running on vibes only ✨",
            ],
            "Lifestyle 🌸": [
                "Just vibes ✨",
                "Living my best life 💕",
                "Good vibes only 🌈",
                "Weekend mood 🌸",
            ]
        }

        # Dropdown for themes
        self.selected_theme = tk.StringVar(value="Travel ✈️")
        self.theme_menu = tk.OptionMenu(root, self.selected_theme, *self.themes.keys())
        self.theme_menu.pack(pady=10)

        # Entry for custom captions
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Type your own caption...")

        # Buttons
        self.custom_btn = tk.Button(root, text="Show My Caption", command=self.show_caption)
        self.custom_btn.pack(pady=5)

        self.random_btn = tk.Button(root, text="Random Caption 🎲", command=self.random_caption)
        self.random_btn.pack(pady=5)

        # Label for output
        self.caption_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="center")
        self.caption_label.pack(pady=20)

  

    def show_caption(self):
        text = self.entry.get()
        self.caption_label.config(text=text)

    def random_caption(self):
        theme = self.selected_theme.get()
        caption = random.choice(self.themes[theme])
        self.caption_label.config(text=caption)


if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionGenerator(root)
    root.mainloop()
