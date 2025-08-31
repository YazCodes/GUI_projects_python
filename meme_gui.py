import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
# pillow a python libiary for using image file formats
import random

# Medium/hard level (can make it harder by adding more features)

# Learnings : 
# Classes (blueprint, cookie cutter)
# Variables, self.image, self.captions, caption
# Functions, load_image(), add_text(), random_caption()
# Events, using buttons to trigger a response 
# User input (typing your captions)

# class for my GUI behaviour 
class MemeGenerator:
    def __init__(self, root):
        self.root = root # root is the tkinter window
        self.root.title("Meme Generator 🎉")

        # Choose an image button
        self.choose_btn = tk.Button(root, text="Choose Image", command=self.load_image)
        self.choose_btn.pack(pady=5) # design - the space between the buttons content and the boarder 

        # Text entry for captions
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.entry.insert(0, "Type your meme caption here...")

        # Generate meme button
        self.generate_btn = tk.Button(root, text="Generate Meme", command=self.add_text) # calling the add_text function
        self.generate_btn.pack(pady=5)

        # Random caption button
        self.random_btn = tk.Button(root, text="Random Caption 🤪", command=self.random_caption)
        self.random_btn.pack(pady=5)

        # Canvas to show the image
        self.canvas = tk.Label(root)
        self.canvas.pack(pady=10)

        # Store current image
        self.image = None # no image yet! 

        # Captions
        # Learnings - Lists 
        self.captions = [
            "Emotional damage",
            "Skibidi toilet",
            "Aura farming in progress",
            "Rizz level 100",
            "404: Homework not found",
            "Brain rot king"
        ]

    # A function to load the image the user chooses 
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    # A function to display the image in the GUI 
    def display_image(self, img):
        img = img.resize((400, 300))   # resing the image for good UI 
        tk_img = ImageTk.PhotoImage(img) # converting the PIL image for Tkinter to use
        self.canvas.config(image=tk_img)
        self.canvas.image = tk_img  # Keep reference!

    # A function to add text to the meme ONLY if an image is loaded 
    def add_text(self):
        if self.image:    # if true then do the next line of code
            text = self.entry.get()  # getting the user input 
            meme = self.image.copy()  # does not use the orginal image, uses a copy instead 
            draw = ImageDraw.Draw(meme)

        # Try and except block used to load a font but default to another font if needed
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        # Place text at the bottom
        W, H = meme.size
        bbox = draw.textbbox((0, 0), text, font=font) # creates a space, a rectangle to place the text
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        draw.text(((W - w) / 2, H - h - 10), text, font=font, fill="white") # can change text colour 

        self.display_image(meme)

    # A function to add a random caption 
    def random_caption(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, random.choice(self.captions))


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MemeGenerator(root)
    root.mainloop()

# python filename.py 

# can also customise the design of the GUI

# self.choose_btn = tk.Button(
#     root, 
#     text="Choose Image", 
#     command=self.load_image,
#     bg="black", 
#     fg="white",
#     activebackground="gray",
#     activeforeground="yellow"
# )

# self.root.config(bg="lightblue")

