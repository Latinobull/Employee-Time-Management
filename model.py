from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'Employee_Time'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    startShift = Column(Time)
    startBreak = Column(Time)
    endBreak = Column(Time)
    endShift = Column(Time)

    def __repr__(self) -> str:
        return "<Employee(firstName='{}',lastName='{}', startShift={}, startBreak={},endBreak={},endShift={})> "\
            .format(self.firstName, self.lastName, self.startShift, self.startBreak, self.endBreak, self.endShift)
