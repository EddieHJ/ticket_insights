from datetime import datetime

from sqlalchemy import select, desc, func
from pydantic import BaseModel
from models import Tickets
from utils.db_util import db_dependency


# Pydantic模型
class TicketsRangeAndEventType4Query(BaseModel):
    start_date: datetime
    end_date: datetime
    event_type_3: str

class TicketsRangeAndEventType4Query1(BaseModel):
    start_date_1: datetime
    end_date_1: datetime
    event_type_3_first: str

class TicketsRangeAndEventType4Query2(BaseModel):
    start_date_2: datetime
    end_date_2: datetime
    event_type_3_second: str

class TicketRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_ticket_by_id(self, ticket_id: str):
        stmt = select(Tickets).where(Tickets.id == ticket_id)
        return self.db.execute(stmt).scalars().one_or_none()

    def get_tickets_by_date_and_type(self, params: TicketsRangeAndEventType4Query):
        stmt = (
            select(Tickets.event_type_4, func.count().label("count"))
            .where(
                Tickets.event_type_3 == params.event_type_3,
                Tickets.reported_at >= params.start_date,
                Tickets.reported_at <= params.end_date,
            )
            .group_by(Tickets.event_type_4)
            .order_by(desc("count"))
        )

        rows = self.db.execute(stmt).all()
        return [{"event_type_4": row[0], "count": row[1]} for row in rows]