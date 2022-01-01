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

    # Displaying BUTTONS FOR BREAK
    def clock(self):

        t = time.localtime()
        self.currentTime = time.strftime('%H:%M:%S', t)
        self.label['text'] = f'Please Clock in {self.currentTime}'
        self.label.after(1000, self.clock)

    def clockInFunction(self):
        showinfo(title='Confirmation',
                 message=f'You have clocked in at {self.currentTime}')
        routes.updateClockIn(userId, self.currentTime)
        self.destroy()

    def clockOutFunction(self):
        showinfo(title='Confirmation',
                 message=f'You have clocked it at {self.currentTime}')
        self.destroy()

    def breakInFunction(self):
        showinfo(title='Confirmation',
                 message=f'You have clocked in for break at {self.currentTime}')
        self.destroy()

    def breakOutFunction(self):
        showinfo(title='Confirmation',
                 message=f'You have clocked out for break at {self.currentTime}')
        self.destroy()

    def Submit(self):
        global userId
        userId = self.idEntry.get()
        try:
            showinfo(title='Conformation',
                     message=f'Employee {routes.read(userId)} was Submitted')
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
