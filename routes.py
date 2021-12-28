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


employee = Employee(
    id=1866219,
    firstName='Donnahue',
    lastName='George'
)

recreate_database()
