from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import db_uri

engine = create_engine(db_uri.DB_URI, pool_recycle=100, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					autoflush=True,
					bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import models
	Base.metadata.create_all(bind=engine)

