import logging

from fastapi import APIRouter
from typing import Annotated

import pandas as pd
from fastapi import Depends
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import models
from models import Tickets
from database import SessionLocal

from utils.import_data_to_db import import_to_db
from utils.convert_and_import import combine_process_and_import
from utils.db_util import db_dependency

router = APIRouter(
    prefix="/import_to_db",
    tags=["导入数据库"],
)


@router.post("/import")
async def import_excel_to_db(db: db_dependency, file_path: str = "data/output.xlsx"):
    try:
        return import_to_db(db=db, file_path=file_path)
    except Exception as e:
        return {"msg": "导入失败", "error": str(e)}



@router.get("/convert_and_import")
async def convert_and_import(db: db_dependency, input_path: str = 'DATA/input.xlsx', output_path: str = 'DATA/output.xlsx'):

    try:
        return combine_process_and_import(input_path=input_path, output_path=output_path, db=db)
    except Exception as e:
        return {"msg": "导入失败", "error": str(e)}