import tkinter as tk
import random

# uses - chatbots to use for repetative tasks such as FAQ on websites 
# or used for learning new langauges, vocabulary, grammer etc 

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hi there!", "Hello! How are you?", "Hey hey hey!"])
    elif "how are you" in user_input:
        return "I’m just a chatbot, but I’m happy to chat! 🤖"
    elif "bye" in user_input:
        return "Goodbye! Talk soon"
    elif "joke" in user_input:
        return random.choice([
            "Why was the computer cold? It left its Windows open! 😂",
            "What do you call a robot that loves sweets? A candy-bot 🍬"
        ])
    else:
        return "Hmm, I don’t know what to say… 🤔 Try asking me something else!"


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot 🤖")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # Chat window (Text box)
        self.chat_window = tk.Text(root, bg="white", fg="black", wrap="word", state="disabled", 
                                   font=("Arial", 12), bd=2, relief="flat")
        self.chat_window.place(x=10, y=10, width=380, height=400)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(root, command=self.chat_window.yview)
        self.chat_window['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.place(x=390, y=10, height=400)

        # Entry box
        self.entry = tk.Entry(root, font=("Arial", 12), bg="#e6f7ff", fg="black")
        self.entry.place(x=10, y=420, width=300, height=40)
        self.entry.bind("<Return>", self.send_message)  # Press Enter to send

        # Send button
        self.send_btn = tk.Button(root, text="Send ➤", font=("Arial", 12, "bold"), bg="#00bfff", fg="white", 
                                  command=self.send_message)
        self.send_btn.place(x=320, y=420, width=70, height=40)

        # Greeting
        self.insert_message("Chatbot", "Hello! Type 'hi' to start chatting 😄")

    def insert_message(self, sender, message):
        self.chat_window.config(state="normal")
        self.chat_window.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_window.config(state="disabled")
        self.chat_window.see(tk.END)  # Auto scroll

    def send_message(self, event=None):
        user_text = self.entry.get()
        if user_text.strip():
            # Show user message
            self.insert_message("You", user_text)
            self.entry.delete(0, tk.END)

            # Get chatbot response
            bot_reply = chatbot_response(user_text)
            self.insert_message("Chatbot", bot_reply)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

