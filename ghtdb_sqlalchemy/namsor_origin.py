import sqlalchemy as sa
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text, Numeric
from .base import Base
from sqlalchemy.orm import relationship


class NamSorOrigin(Base):
    __tablename__ = 'bv_namsor_origin_2_0_10'
    
    id = Column(Integer, primary_key=True)
    name_id = Column(Integer, ForeignKey("bv_names.id"))
    country_origin = Column(String)
    country_origin_alt = Column(String)
    probability_calibrated = Column(Numeric)
    probability_alt_calibrated = Column(Numeric)
    region_origin = Column(String)
    score = Column(Numeric)
    sub_region_origin = Column(String)
    top_region_origin = Column(String)
    
    gh_name = db.relationship('Name', backref='bv_namsor_origin_2_0_10')
    
    def __init__(self, 
                name_id,
                country_origin,
                country_origin_alt,
                probability_calibrated,
                probability_alt_calibrated,
                region_origin,
                score,
                sub_region_origin,
                top_region_origin):
        self.name_id = name_id
        self.country_origin = country_origin
        self.country_origin_alt = country_origin_alt
        self.probability_calibrated = probability_calibrated
        self.probability_alt_calibrated = probability_alt_calibrated
        self.region_origin = region_origin
        self.score = score
        self.sub_region_origin = sub_region_origin
        self.top_region_origin = top_region_origin

    def __repr__(self):
        return 'Name origin: %d - %s' % \
                    (self.name_id, self.country_origin) 
    

