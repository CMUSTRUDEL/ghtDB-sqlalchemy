import sqlalchemy as sa
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text, Numeric
from .base import Base
from sqlalchemy.orm import relationship


class NamSorGender(Base):
    __tablename__ = 'bv_namsor_gender_geo_manual_first_last_2_0_10'
    
    id = Column(Integer, primary_key=True)
    name_id = Column(Integer, ForeignKey("bv_names.id"))
    likely_gender = Column(String)
    gender_scale = Column(Numeric)
    score = Column(Numeric)
    probability_calibrated = Column(Numeric)

    gh_name = relationship('Name', backref='bv_namsor_gender_geo_manual_first_last_2_0_10')
    
    def __init__(self, 
                name_id,
                likely_gender,
                gender_scale,
                score,
                probability_calibrated):
        self.name_id = name_id
        self.likely_gender = likely_gender
        self.gender_scale = gender_scale
        self.score = score
        self.probability_calibrated = probability_calibrated


    def __repr__(self):
        return 'Name gender: %d - %s' % \
                    (self.name_id, self.likely_gender) 
    

