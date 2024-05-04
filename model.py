from xmlrpc.client import Boolean
from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta
from sqlalchemy import DateTime


class MessageHistory(Base):
    __tablename__ = 'message_history'

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.now())