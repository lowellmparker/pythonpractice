import tkinter as tk


def say_hi():
    print("you just clicked the button!")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.hi_there = tk.Button(self)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there["text"] = "Hello World \n (click me)"
        self.hi_there["command"] = say_hi
        self.hi_there.pack(side="top")

        self.quit.pack(side="bottom")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
