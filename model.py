from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'Employee_Time'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    startShift = Column(String)
    startBreak = Column(String)
    endBreak = Column(String)
    endShift = Column(String)

    def __repr__(self) -> str:
        return "<Employee(firstName='{}',lastName='{}', startShift={}, startBreak={},endBreak={},endShift={})> "\
            .format(self.firstName, self.lastName, self.startShift, self.startBreak, self.endBreak, self.endShift)
