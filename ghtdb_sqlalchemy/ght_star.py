import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, String, Text, Boolean, BigInteger, DateTime, Numeric
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.associationproxy import association_proxy
import datetime
from .base import Base
from dateutil import parser
    

class GHTStar(Base):
    __tablename__ = 'watchers'
    
    repo_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True))


    def __repr__(self):
        return 'GH star: %s - %s - %s' % \
                    (self.repo_id, self.user_id, self.created_at) 


    
