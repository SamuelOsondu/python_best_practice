from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()

        self.state("zoomed")
        self.title("DANGEROUS WRITER")
        self.config(bg="grey")

        self.text_box = Text(height=37, width=130)
        self.text_box.pack(pady=55)

        self.text_box.insert(INSERT, "Start typing here...")
        self.on_click_id = self.text_box.bind('<Button-1>', self.on_click)
        self.click_id = None

    def on_click(self, event):
        self.text_box.configure(state=NORMAL)
        self.text_box.delete("1.0", END)

        self.text_box.unbind('<Button-1>', self.on_click_id)
        self.note_click()

    def note_click(self):
        self.text_box.bind("<Key>", self.after_click)

    def after_click(self, event):
        if self.click_id is not None:
            self.text_box.after_cancel(self.click_id)
            print("Im active")

        self.click_id = self.text_box.after(1000, self.time_elapsed)

    def time_elapsed(self):
        self.text_box.delete("1.0", END)
        self.text_box.config(bg="red")
        print("its passed 360s Sam!")


app = App()
app.mainloop()
