from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from model import Base, Employee
from flask_seeder import Seeder, Faker, generator

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def fakeEmployees():
    employees = [Employee(
        id=1866219,
        firstName='Donnahue',
        lastName='George'
    ), Employee(id=1234567,
                firstName='Test',
                lastName='Employee')]
    for employee in employees:
        s.add(employee)
        print(employee)
    s.commit()


class Seed(Seeder):
    def run():
        faker = Faker(
            cls=Employee,
            init={
                'id': generator.Integer(start=1000000, end=2020000),
                'firstName': generator.Name(),
                'lastName': generator.Name()
            })
        for user in faker.create(10):
            print(f'Adding user {user}')
            s.add(user)
            s.commit()
    run()


def read(userId):
    r = s.query(Employee).filter_by(id=userId).first()
    print(r.firstName + ' ' + r.lastName)
    s.commit()
    return r.firstName


def updateClockIn(userId, currentTime):
    read = s.query(Employee).filter_by(id=userId)
    read.update(
        {Employee.startShift: str(currentTime)})
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
