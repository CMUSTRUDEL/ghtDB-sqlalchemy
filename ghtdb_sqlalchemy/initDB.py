from ghtdb_sqlalchemy.base import Base

def initDB(engine):
    metadata = Base.metadata
    metadata.create_all(engine) 
    print ('Database structure created')
    
    
