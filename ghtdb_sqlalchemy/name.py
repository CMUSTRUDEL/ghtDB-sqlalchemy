import sqlalchemy as sa
from sqlalchemy import Column, Table
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text
from .base import Base


class Name(Base):
    __tablename__ = 'bv_names'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    num_parts = Column(Integer)
    first_camel_case = Column(Boolean)
    last_camel_case = Column(Boolean)
        
    def __init__(self, 
                name,
                first_name,
                last_name,
                num_parts,
                first_camel_case,
                last_camel_case):
 
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.num_parts = num_parts
        self.first_camel_case = first_camel_case
        self.last_camel_case = last_camel_case

    def __repr__(self):
        return 'GH name: %s' % \
                    (self.name) 
    

