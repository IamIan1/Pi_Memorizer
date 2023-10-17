import tkinter as tk
import json

class NumberGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pi Memorizer")
        self.master.minsize(300, 300)  # Set minimum size to 200x200

        self.target_string = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
        self.entered_digits = tk.StringVar()
        self.current_input = tk.StringVar()
        self.current_correction = tk.StringVar()
        self.clear_progress_var = tk.BooleanVar()
        self.clear_progress_var.set(False)
        self.digits_count = 0

        # Color scheme
        self.bg_color = "#2E294E"  # Background color
        self.text_color = "#FFFFFF"  # Text color
        self.button_color = "#FF847C"  # Button color

        self.label = tk.Label(master, text="Enter the digits of pi:", fg=self.text_color, bg=self.bg_color, font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.progress_label = tk.Label(master, textvariable=self.entered_digits, wraplength=400, fg=self.text_color, bg=self.bg_color, font=("Helvetica", 14))
        self.progress_label.pack(pady=5)

        self.counter_label = tk.Label(master, text="Digits Entered: 0", fg=self.text_color, bg=self.bg_color, font=("Helvetica", 12))
        self.counter_label.pack(pady=5)

        self.entry = tk.Entry(master, textvariable=self.current_input, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.clear_progress_checkbox = tk.Checkbutton(master, text="Clear Progress", variable=self.clear_progress_var, fg=self.text_color, bg=self.bg_color, font=("Helvetica", 12))
        self.clear_progress_checkbox.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_input, bg="#FF847C", fg="#000000", font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", wraplength=400, fg=self.text_color, bg=self.bg_color, font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        # Bind events
        self.master.bind('<FocusIn>', self.fill_entry_box)
        self.master.bind('<Return>', lambda event=None: self.check_input())

        # Bind closing event to save progress
        self.master.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        # Load progress from file
        self.load_progress()

        # Configure background color
        master.configure(bg=self.bg_color)

    def fill_entry_box(self, event):
        self.current_input.set("")

    def check_input(self):
        user_input = self.current_input.get()
        if user_input.replace('.', '', 1).isdigit() and (user_input.count('.') <= 1):
            full_input = self.entered_digits.get() + user_input
            if full_input == self.target_string[:len(full_input)]:
                self.entered_digits.set(full_input)
                self.digits_count = sum(c.isdigit() for c in full_input)  # Exclude '.' from count
                self.counter_label.config(text=f"Digits Entered: {self.digits_count}")
                if len(full_input) == len(self.target_string):
                    self.result_label.config(text="Congratulations! You've learned 1000 digits!")
                else:
                    self.result_label.config(text="Continue!")
            else:
                if len(user_input) > len(self.target_string):
                    user_input = user_input[:len(self.target_string) - len(self.entered_digits.get())]
                correct_part = self.target_string[len(self.entered_digits.get()):len(full_input)]
                self.current_correction.set(f"Try {correct_part} next time!")
                self.result_label.config(text=f"{self.current_correction.get()}")
                if self.clear_progress_var.get():
                    self.entered_digits.set("")
                    self.digits_count = 0  # Reset count to zero
                    self.counter_label.config(text=f"Digits Entered: {self.digits_count}")
            self.current_input.set("")
        else:
            self.result_label.config(text="Input must be numerical (or '.')")

    def save_and_exit(self):
        # Save progress upon closing
        progress_data = {"entered_digits": self.entered_digits.get()}
        with open("progress.json", "w") as json_file:
            json.dump(progress_data, json_file)
        # Close the program
        self.master.destroy()

    def load_progress(self):
        try:
            with open("progress.json", "r") as json_file:
                progress_data = json.load(json_file)
                self.entered_digits.set(progress_data.get("entered_digits", ""))
                self.digits_count = sum(c.isdigit() for c in self.entered_digits.get())  # Exclude '.' from count
                self.counter_label.config(text=f"Digits Entered: {self.digits_count}")
        except (json.JSONDecodeError, FileNotFoundError):
            # If the file doesn't exist or is invalid, start with an empty progress
            self.entered_digits.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGameApp(root)
    root.mainloop()
