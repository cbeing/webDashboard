from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
import json

fConfig = open('config.json', 'r')
config = json.load(fConfig)
fConfig.close()

engine = create_engine('mysql://'+config['user']+':'+config['password']+'@'+config['host']+'/'+config['database_name']+'?unix_socket=/var/run/mysqld/mysqld.sock', convert_unicode=True, poolclass=NullPool)
db_session = scoped_session(sessionmaker(autocommit=False, 
      autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  #We only need init_db to create the database and tables
  import classes 
  Base.metadata.create_all(bind=engine)
