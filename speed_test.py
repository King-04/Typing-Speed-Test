import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test App")

        self.text_to_type = self.load_text_to_type()

        self.label = tk.Label(master, text="Type the following text:")
        self.label.pack()

        self.text_display = tk.Text(master, height=5, width=40, wrap="word")
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state="disabled")
        self.text_display.pack()

        self.entry_label = tk.Label(master, text="Your typing:")
        self.entry_label.pack()

        self.user_input = tk.Entry(master, width=40)
        self.user_input.pack()

        self.start_button = tk.Button(master, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.time_label = tk.Label(master, text="")
        self.time_label.pack()

    def load_text_to_type(self):
        # You can replace this with your own text file or provide a list of strings
        sample_text = """This is a sample text for typing speed test. You can replace this with your own text."""
        return sample_text

    def start_typing_test(self):
        self.start_time = time.time()
        self.text_display.config(state="normal")
        self.start_button.config(state="disabled")
        self.user_input.bind('<KeyRelease>', self.check_typing)

    def check_typing(self, event):
        user_input = self.user_input.get()
        if user_input == self.text_to_type:
            self.end_time = time.time()
            elapsed_time = round(self.end_time - self.start_time, 2)
            wpm = self.calculate_wpm(user_input, elapsed_time)
            messagebox.showinfo("Typing Speed Test", f"Your typing speed: {wpm} WPM")
            self.reset_typing_test()
        elif self.text_to_type.startswith(user_input):
            self.text_display.tag_configure("correct", foreground="green")
            self.text_display.delete("1.0", "end")
            self.text_display.insert(tk.END, self.text_to_type[:len(user_input)], "correct")
            self.text_display.insert(tk.END, self.text_to_type[len(user_input):])
        else:
            self.text_display.tag_configure("incorrect", foreground="red")
            self.text_display.delete("1.0", "end")
            self.text_display.insert(tk.END, self.text_to_type[:len(user_input)], "incorrect")
            self.text_display.insert(tk.END, self.text_to_type[len(user_input):])

    def calculate_wpm(self, text, time_elapsed):
        words_typed = len(text.split())
        minutes = time_elapsed / 60
        wpm = round(words_typed / minutes)
        return wpm

    def reset_typing_test(self):
        self.text_display.config(state="disabled")
        self.user_input.delete(0, tk.END)
        self.user_input.unbind('<KeyRelease>')
        self.start_button.config(state="normal")
        self.time_label.config(text=f"Time elapsed: {round(self.end_time - self.start_time, 2)} seconds")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
