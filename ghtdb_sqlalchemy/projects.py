import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, String, Text, Boolean, BigInteger, DateTime
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import relationship, backref
import datetime
# from .base import Base
# from dateutil import parser
    

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    owner_id = Column(Integer)
    name = Column(String(255))
    description = Column(String(255))
    language = Column(String(255))
    created_at = Column(DateTime)
    forked_from = Column(Integer)
    deleted = Column(Integer)
    updated_at = Column(DateTime)
    
    def __init__(self,
                 url,
                 owner_id,
                 name,
                 description,
                 language,
                 created_at,
                 forked_from,
                 deleted,
                 updated_at):
 
        self.url = url
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.language = language
        self.created_at = created_at
        self.forked_from = forked_from
        self.deleted = deleted
        self.updated_at = updated_at


    def __repr__(self):
        return 'Project: %s' % \
                    (self.url) 
    
