from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from model import Base, Employee

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def fakeEmployee():
    employee = Employee(
        id=1866219,
        firstName='Donnahue',
        lastName='George'
    )
    s.add(employee)
    s.commit()


def read(userId):
    r = s.query(Employee).filter_by(id=userId).first()
    print(r.firstName + ' ' + r.lastName)
    s.commit()
    return r.firstName


def updateClockIn(userId, currentTime):
    read = s.query(Employee).filter_by(id=userId)
    read.update(
        {Employee.startShift: currentTime})
    s.commit()
    print(read)


def updateClockOut(userId, currentTime):
    read = s.query(Employee).filter_by(id=userId)
    read.update(
        {Employee.endShift: currentTime})
    s.commit()
    print(read)


def updateBreakOut(userId, currentTime):
    read = s.query(Employee).filter_by(id=userId)
    read.update(
        {Employee.startBreak: currentTime})
    s.commit()
    print(read)


def updateBreakIn(userId, currentTime):
    read = s.query(Employee).filter_by(id=userId)
    read.update(
        {Employee.endBreak: currentTime})
    s.commit()
    print(read)
