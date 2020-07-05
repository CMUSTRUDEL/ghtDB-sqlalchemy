import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.associationproxy import association_proxy
import datetime
from .base import Base
from dateutil import parser
    

class TwitterUser(Base):
    __tablename__ = 'mongo_users'
    
    id = Column(Integer, primary_key=True)
    tw_id = Column(String(255))
    mongo_collection = Column(Integer)
    ght_id = Column(BigInteger)
    tw_name = Column(Text)
    tw_screen_name = Column(Text)
    tw_created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    tw_followers = Column(Integer)
    tw_listed = Column(Integer)
    tw_favourites = Column(Integer)
    tw_utc = Column(Text)
    tw_time_zone = Column(Text)
    tw_location = Column(Text)
    # tw_profile_location = Column(Text)
    tw_statuses = Column(Integer)
    tw_friends = Column(Integer)
    tw_url = Column(Text)
    tw_desc = Column(Text)
    tw_lang = Column(Text)
    tw_img_url = Column(Text)

    
    def __init__(self, 
                tw_id, 
                mongo_collection,
                ght_id, 
                tw_name, 
                tw_screen_name,
                tw_created_at,
                tw_followers, 
                tw_listed, 
                tw_favourites,
                tw_utc, 
                tw_time_zone,
                tw_location, 
                # tw_profile_location,
                tw_statuses, 
                tw_friends, 
                tw_url,
                tw_desc, 
                tw_lang,
                tw_img_url):
 
        self.tw_id = tw_id
        self.mongo_collection = mongo_collection
        self.ght_id = ght_id
        self.tw_name = tw_name
        self.tw_screen_name = tw_screen_name
        # self.tw_created_at = tw_created_at
        self.tw_followers = tw_followers
        self.tw_listed = tw_listed
        self.tw_favourites = tw_favourites
        self.tw_utc = tw_utc
        self.tw_time_zone = tw_time_zone
        self.tw_location = tw_location
        # self.tw_profile_location = tw_profile_location
        self.tw_statuses = tw_statuses
        self.tw_friends = tw_friends
        self.tw_url = tw_url
        self.tw_desc = tw_desc
        self.tw_lang = tw_lang
        self.tw_img_url = tw_img_url
        
        if tw_created_at is not None:
            st = parser.parse(tw_created_at)
            self.tw_created_at = datetime.datetime(st.year, st.month, st.day, st.hour, st.minute, st.second)
        else:
            self.tw_created_at = None


    def __repr__(self):
        return 'Twitter user: %s - %s' % \
                    (self.tw_id, self.tw_name) 
    

