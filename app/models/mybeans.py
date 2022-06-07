from sqlalchemy import Column, Integer, Float, String, ForeignKey, TIMESTAMP, Date, text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue

from app.database import Base
from app.models.beans import Beans

class Mybeans(Base):
    __tablename__ = "mybeans"

    id = Column(Integer, primary_key=True)
    beans_id = Column(Integer, ForeignKey("beans.id"), nullable=False)
    weight = Column(Float, nullable=False)
    roast_level = Column(String(30))
    roasted_date = Column(Date)
    grind_size = Column(String(30))
    grinded_date = Column(Date)
    got_date = Column(Date, nullable=False)
    created_date = Column(TIMESTAMP, nullable=False, server_default=text('current_timestamp'))
    updated_date = Column(TIMESTAMP, nullable=False, server_default=text('current_timestamp on update current_timestamp'))