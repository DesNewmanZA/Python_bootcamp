# Import needed modules
import tkinter

# Define constants
TIME_WINDOW = 5
SESSION_TIME = 120


# Define app class
class WritersBlockApp:
    # Initialise the app's starting state and layout
    def __init__(self, master):
        # Window definition
        self.master = master
        self.master.title("Writer's block assistant")
        self.master.minsize(width=800, height=700)
        self.master.resizable(False, False)

        # Introductory text
        self.intro_label = tkinter.Label(text="Start typing to cure your writer's block. If you stop writing for more "
                                              "than 5 seconds, your work will be erased.", font=('Arial', 16, 'bold'),
                                         wraplength=600)
        self.intro_label.pack(pady=(20, 5))

        self.intro_label2 = tkinter.Label(text="If you type for two minutes or more, your work is safe!",
                                          font=('Arial', 16, 'bold'), wraplength=600)
        self.intro_label2.pack(pady=(5, 20))

        # Session time left label
        self.session_left_label = tkinter.Label(text="Session remaining: N/A", font=('Arial', 13))
        self.session_left_label.pack(pady=(5, 5))

        # Danger time left label
        self.time_left_label = tkinter.Label(text="Time left: N/A", font=('Arial', 13))
        self.time_left_label.pack(pady=(5, 5))

        # Writing area
        self.text_area = tkinter.Text(font=('Arial', 12), wrap="word")
        self.text_area.pack()
        self.text_area.bind("<Key>", self.timer)

        # Define restart button
        self.restart_btn = tkinter.Button(master, text="Restart", command=self.restart, font=('Arial', 12))
        self.restart_btn.pack(pady=10)

        # Define session parameters
        self.session = True
        self.session_started = False
        self.session_left = SESSION_TIME
        self.session_timer = None

        # Define timer parameters
        self.counter = TIME_WINDOW
        self.timer = None

    # Define timer function
    def timer(self, event=None):
        # If session has already finished, don't restart timer
        if not self.session:
            return

        # If first press, start the session
        if not self.session_started:
            self.session_started = True
            self.update_session_label()
            self.session_counter_tick()

        # Start out with the time window and update the label
        self.counter = TIME_WINDOW
        self.update_label()

        # If there's an existing timer, remove it
        if self.timer:
            self.master.after_cancel(self.timer)

        # Restart an incrementing timer
        self.timer = self.master.after(1000, self.counter_tick)

    # Function to increment timer and remove text when time exceeded
    def counter_tick(self):
        # Increment down by one and adjust the label each time
        self.counter -= 1
        self.update_label()

        # If time is up, delete the text and display a message
        if self.counter <= 0:
            self.text_area.delete("1.0", tkinter.END)
            self.time_left_label.config(text="Out of time! Try again!")
        # Else continue to increment
        else:
            self.timer = self.master.after(1000, self.counter_tick)

    # Function to update timer label
    def update_label(self):
        self.time_left_label.config(text=f"Time left: {self.counter} seconds")

    # Function to update session label
    def update_session_label(self):
        self.session_left_label.config(text=f"Session remaining: {self.session_left} seconds")

    # Session counter
    def session_counter_tick(self):
        # Increment by 1
        self.update_session_label()
        self.session_left -= 1

        # If session done
        if self.session_left <= 0:
            # Cancel danger timer
            if self.timer:
                self.master.after_cancel(self.timer)
            self.time_left_label.config(text="Well done! You typed for 2 minutes!")
            self.session = False
            return
        else:
            self.session_timer = self.master.after(1000, self.session_counter_tick)

    # Restart button action
    def restart(self):
        # Cancel timers if running
        if self.timer:
            self.master.after_cancel(self.timer)
            self.timer = None
        if self.session_timer:
            self.master.after_cancel(self.session_timer)
            self.session_timer = None

        # Reset counters and flags
        self.counter = TIME_WINDOW
        self.session_left = SESSION_TIME
        self.session = True
        self.session_started = False

        # Clear text area and enable it
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tkinter.END)

        # Reset labels
        self.time_left_label.config(text="Time left: N/A")
        self.session_left_label.config(text="Session remaining: N/A")


# Run app
if __name__ == "__main__":
    root = tkinter.Tk()
    app = WritersBlockApp(root)
    root.mainloop()
