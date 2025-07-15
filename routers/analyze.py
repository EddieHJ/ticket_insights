from typing import Annotated

from fastapi import APIRouter, Query, Depends, Path

from ai.ai_analyze import analyze_ticket_periods
from repository.crud import TicketRepository, TicketsRangeAndEventType4Query, TicketsRangeAndEventType4Query1, \
    TicketsRangeAndEventType4Query2
from utils.db_util import db_dependency

router = APIRouter(
    prefix="/tickets",
    tags=["工单分析"],
)


@router.get("/get_ticket/{ticket_id}", status_code=200)
async def get_ticket(db: db_dependency, ticket_id: str = Path(..., description="需要查找的工单号")):
    dao = TicketRepository(db)
    ticket = dao.get_ticket_by_id(ticket_id)
    return ticket


date_basemodel_1 = Annotated[TicketsRangeAndEventType4Query1, Depends()]
date_basemodel_2 = Annotated[TicketsRangeAndEventType4Query2, Depends()]


@router.get("/get_tickets_of_two_periods_and_by_type", status_code=200, summary="两段时间的AI对比分析")
async def get_tickets_of_two_periods_and_by_type(db: db_dependency, date1: date_basemodel_1,
                                                 date2: date_basemodel_2):
    dao = TicketRepository(db)
    first = TicketsRangeAndEventType4Query(start_date=date1.start_date_1, end_date=date1.end_date_1,
                                           event_type_3=date1.event_type_3_first)
    second = TicketsRangeAndEventType4Query(start_date=date2.start_date_2, end_date=date2.end_date_2,
                                            event_type_3=date2.event_type_3_second)

    tickets1 = dao.get_tickets_by_date_and_type(first)
    tickets2 = dao.get_tickets_by_date_and_type(second)

    print(tickets1, tickets2)

    ai_response = analyze_ticket_periods(tickets1, tickets2)

    return ai_response
