from tkinter import Tk, ttk
from tkinter.messagebox import showinfo


class App(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Employee Login')
        self.geometry('800x500')

        self.label = ttk.Label(self, text='Enter Employee ID')
        self.label.pack()

        self.button = ttk.Button(self, text='Submit')
        self.button['command'] = self.Submit
        self.button.pack()

    def Submit(self):
        showinfo(title='Conformation', message='It was submitted correctly')


if __name__ == '__main__':
    app = App()
    app.mainloop()
