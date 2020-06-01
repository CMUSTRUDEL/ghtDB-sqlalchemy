import sqlalchemy as sa
from sqlalchemy import Column, Table
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text
    

class Name(Base):
    __tablename__ = 'bv_names'
    
    id = Column(Integer, primary_key=True)
	name = Column(Text)

    
    def __init__(self, 
                name):
 
        self.name = name

    def __repr__(self):
        return 'GH name: %s' % \
                    (self.name) 
    

