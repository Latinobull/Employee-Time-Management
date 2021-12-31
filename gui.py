from tkinter import StringVar, Tk, ttk
from tkinter.messagebox import showinfo
import routes
from sqlalchemy.exc import InternalError, DataError
import time


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

    def clock(self):

        t = time.localtime()
        fullTime = time.strftime('%H:%M:%S', t)
        self.label['text'] = f'Please Clock in {fullTime}'
        self.label.after(1000, self.clock)

    def clockInFunction(self):
        print('I have been clocked in')

    def clockOutFunction(self):
        print('I have been clocked out')

    def breakInFunction(self):
        print('I have been clocked in for break ')

    def breakOutFunction(self):
        print('I have been clocked out for break')

    def Submit(self):

        try:
            showinfo(title='Conformation',
                     message=f'Employee {routes.read(self.idEntry.get())} was Submitted')
            self.idInput.destroy()
            self.submit.destroy()
            # Clock in Entry
            self.clockIn = ttk.Button(self, text='Clock in', width=30,)
            self.clockIn['command'] = self.clockInFunction
            self.clockIn.pack()
            # Break out entry
            self.breakOut = ttk.Button(self, text='Break Out', width=30)
            self.breakOut['command'] = self.breakOutFunction
            self.breakOut.pack()
            # Break in entry
            self.breakIn = ttk.Button(self, text='Break In', width=30)
            self.breakIn['command'] = self.breakInFunction
            self.breakIn.pack()
            # Clock out Entry
            self.clockOut = ttk.Button(self, text='Clock Out', width=30)
            self.clockOut['command'] = self.clockOutFunction
            self.clockOut.pack()
            self.clock()

        except AttributeError:
            showinfo(
                title='Error', message=f'There is no user with the ID {self.idEntry.get()}')

        except DataError:
            showinfo(
                title='Error', message=f'There is no user with the ID {self.idEntry.get()}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
