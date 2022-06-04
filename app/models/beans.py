from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Beans(Base):
    __tablename__ = "beans"

    id = Column(Integer, primary_key=True)
    shop = Column(String(50))
    country = Column(String(50))
    origin = Column(String(120))

    mybeans = relationship("Mybeans")