import sqlalchemy as sa
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, Boolean, BigInteger, DateTime, Text, Numeric
from .base import Base
from sqlalchemy.orm import relationship


class BVCommitters(Base):
    __tablename__ = 'bv_committers'
    
    id = Column(Integer, primary_key=True)
    login = Column(Text)
    name = Column(Text)
    email = Column(Text)
    created_at = Column(DateTime)
    user_type = Column('type', String)
    fake = Column(Boolean)
    deleted = Column(Boolean)
    num_commits = Column(Integer)
    num_repos_committed = Column(Integer)
    last_date_committed = Column(DateTime)
    gender = Column(String)
    gender_scale = Column(Numeric)
    gender_score = Column(Numeric)
    gender_probability_calibrated = Column(Numeric)

    def __init__(self,
                 login,
                 name,
                 email,
                 created_at,
                 user_type,
                 fake,
                 deleted,
                 num_commits,
                 num_repos_committed,
                 last_date_committed,
                 likely_gender,
                 gender_scale,
                 score,
                 probability_calibrated):

        self.login = login
        self.name = name
        self.email = email
        self.created_at = created_at
        self.user_type = user_type
        self.fake = fake
        self.deleted = deleted
        self.num_commits = num_commits
        self.num_repos_committed = num_repos_committed
        self.last_date_committed = last_date_committed
        self.gender = likely_gender
        self.gender_scale = gender_scale
        self.gender_score = score
        self.gender_probability_calibrated = probability_calibrated

    def __repr__(self):
        return 'GHTCommitter: %d %s' % \
                    (self.id, self.login)
    

