from tkinter import StringVar, Tk, ttk
from tkinter.messagebox import showinfo
import routes
from sqlalchemy.exc import InternalError, DataError


class App(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Employee Login')
        self.geometry('800x500')

        # Main Label
        self.label = ttk.Label(
            self, text='Enter Employee ID', font='none 30 bold')
        self.label.pack()

        # ID Entry
        self.idEntry = StringVar()
        self.idInput = ttk.Entry(
            self, textvariable=self.idEntry, font='none 30 normal')
        self.idInput.focus()
        self.idInput.pack()

        # Submit to verify user
        self.submit = ttk.Button(self, text='Submit', width=30)
        self.submit.bind('<Button-1>', lambda event: self.Submit())
        self.submit.pack()

        self.bind('<Return>', lambda event: self.Submit())

    def Submit(self):
        try:
            showinfo(title='Conformation',
                     message=f'Employee {routes.read(self.idEntry.get())} was Submitted')
            self.idInput.destroy()
            self.submit.destroy()
            self.label['text'] = 'Please Clock in'
        except AttributeError:
            showinfo(
                title='Error', message=f'There is no user with the ID {self.idEntry.get()}')
        except InternalError:
            showinfo(
                title='Error', message=f'There is no user with the ID {self.idEntry.get()}')
        except DataError:
            showinfo(
                title='Error', message=f'There is no user with the ID {self.idEntry.get()}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
