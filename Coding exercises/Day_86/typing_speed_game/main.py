# Import needed modules
from tkinter import *
from tkinter import messagebox
import random
import time

# Define constants
WORD_LIST = [
                "about",
                "search",
                "other",
                "information",
                "which",
                "their",
                "there",
                "contact",
                "business",
                "online",
                "first",
                "would",
                "services",
                "these",
                "click",
                "service",
                "price",
                "people",
                "state",
                "email",
                "health",
                "world",
                "products",
                "music",
                "should",
                "product",
                "system",
                "policy",
                "number",
]


# Define the application
class TypingSpeedApp:
    def __init__(self, app_window):
        # Define main app views
        self.window = app_window
        self.window.title("Typing speed test")
        self.window.minsize(width=800, height=500)
        self.window.config(padx=10, pady=10)
        self.window.resizable(False, False)

        # Define a frame to contain the GUI
        self.frame = Frame(self.window)
        self.frame.pack(expand=True)

        # Define starting state variables
        self.typing_speed = "N/A"
        self.word_list = self.random_word_list()
        self.timer_begun = False
        self.start_time = 0

        # Define app heading and instructions
        self.heading = Label(self.frame, text="TYPING SPEED TEST", font=('Arial', 20, 'bold'))
        self.heading.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.instructions = Label(self.frame, text="Type the words on screen until you reach the end. The program "
                                                   "will calculate the time it took you from start to finish, "
                                                   "and calculate a words per minute speed. If you make a mistake, "
                                                   "correct it to continue. This assesses speed with perfect "
                                                   "accuracy.", font=('Arial', 10),
                                  wraplength=600)
        self.instructions.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.speed_label = Label(self.frame, text=f"Typing speed: {self.typing_speed}", font=('Arial', 12, 'bold'))
        self.speed_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Define words to type
        self.word_list_label = Label(self.frame, text="Words to type:", font=("Arial", 10, 'bold'))
        self.word_list_label.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
        self.words_to_type = Text(self.frame, font=("Arial", 12), borderwidth=2, height=2, width=80, wrap="word")
        self.words_to_type.insert(END, self.word_list)
        self.words_to_type.config(state=DISABLED)
        self.words_to_type.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Define user input typing box
        self.user_type_box = Text(self.frame, font=("Arial", 12), borderwidth=2, height=2, width=80, wrap="word")
        self.user_type_box.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.user_type_box.bind("<Key>", self.begin_timing)
        self.user_type_box.bind("<KeyRelease>", self.check_if_done)

        # Define reset button
        self.reset_btn = Button(self.frame, text="Reset", command=self.restart_test)
        self.reset_btn.grid(row=6, column=1, columnspan=1, padx=10, pady=10)

    # Function to take words list and randomise it so it can't be learnt
    def random_word_list(self):
        shuffled_words = WORD_LIST.copy()
        random.shuffle(shuffled_words)
        return ' '.join(shuffled_words)

    # Function that checks if typing has begun - if not, starts it and saves current time
    def begin_timing(self, event):
        if not self.timer_begun:
            self.start_time = time.time()
            self.timer_begun = True
        return None

    # Function that checks if the full, accurate phrase has been completed and calculates the WPM
    def check_if_done(self, event):
        curr_typed_view = self.user_type_box.get("1.0", END).strip()
        if curr_typed_view == self.word_list.strip():
            end_time = time.time()
            time_taken = end_time - self.start_time
            words_per_min = round((len(WORD_LIST) / time_taken) * 60)
            self.typing_speed = words_per_min
            self.speed_label.config(text=f"Typing speed: {self.typing_speed}")
            messagebox.showinfo("Test completed!", "You have finished the typing speed test!")
            self.user_type_box.config(state=DISABLED)
        return None

    # Function to restart the test
    def restart_test(self):
        self.typing_speed = "N/A"
        self.word_list = self.random_word_list()
        self.timer_begun = False
        self.start_time = 0
        self.user_type_box.config(state=NORMAL)
        self.user_type_box.delete("1.0", END)
        self.words_to_type.config(state=NORMAL)
        self.words_to_type.delete("1.0", END)
        self.words_to_type.insert(END, self.word_list)
        self.words_to_type.config(state=DISABLED)
        self.speed_label.config(text=f"Typing speed: {self.typing_speed}")


# Run the app
if __name__ == "__main__":
    window = Tk()
    app = TypingSpeedApp(window)
    window.mainloop()
