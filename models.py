from sqlalchemy import Column, String, Integer, DateTime, Boolean

from database import Base


class Tickets(Base):
    __tablename__ = 'tickets2'

    id = Column(String(64), primary_key=True, nullable=False, unique=True)
    title = Column(String(255))
    creator = Column(String(100))
    assignee = Column(String(100))
    urgency = Column(String(20))
    impact = Column(String(20))
    priority = Column(String(20))
    source = Column(String(111))
    reporter = Column(String(255))
    quantity = Column(Integer)
    jira_link = Column(String(255))
    org_1 = Column(String(100))
    org_2 = Column(String(100))
    event_type_1 = Column(String(50))
    event_type_2 = Column(String(50))
    event_type_3 = Column(String(50))
    event_type_4 = Column(String(50))
    reported_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    completed = Column(Boolean, default=False)
    escalated = Column(Boolean, default=False)
    lead_time = Column(String(50))