from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    orm
)
from app.database import Base


class Question(Base):
    __tablename__ = "poll_question"

    id = Column(Integer, index=True, primary_key=True)
    question_text = Column(String(200), nullable=False)
    pub_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    choices = orm.relationship("Choice", backref="question")


class Choice(Base):
    __tablename__ = "poll_choice"

    id = Column(Integer, index=True, primary_key=True)
    choice_text = Column(String(200), nullable=False)
    votes = Column(Integer, default=0, nullable=False)
    question_id = Column(Integer, ForeignKey("poll_question.id"))
