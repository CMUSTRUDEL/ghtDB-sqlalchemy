import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, String, Text, Boolean, BigInteger, DateTime
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.associationproxy import association_proxy
import datetime
from .base import Base
from dateutil import parser
    

class GHTUser(Base):
    __tablename__ = 'ght_users'
    
    id = Column(Integer, primary_key=True)
    login = Column(String(255))
    company = Column(String(255))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    usr_type = Column('type', String(255))
    fake = Column(Boolean)
    deleted = Column(Boolean)
    longitude = Column('long', Numeric(11,8))
    latitude = Column('lat', Numeric(11,8))
    country_iso = Column('country_code', String(3))
    state = Column(String(255))
    city = Column(String(255))
    location = Column(String(255))


    def __repr__(self):
        return 'GH user: %s - %s' % \
                    (self.id, self.login) 


    
