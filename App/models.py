from sqlalchemy import Column, Integer, String, Boolean
from App.database import Base

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    internal_time = (Integer)
    name = (String)