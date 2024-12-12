from sqlalchemy import create_engine, Column, String, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class UserContent(Base):
    __tablename__ = 'user_content'

    user_id = Column(String, primary_key=True)
    prompt = Column(String)
    video_paths = Column(JSON)
    image_paths = Column(JSON)
    status = Column(String, default="Processing")
    generated_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///content.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)