from io import BytesIO
from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from utils.db_util import db_dependency
from utils.excel_cleaner import clean_excel
from utils.db_importer import insert_rows_from_df

router = APIRouter(
    prefix="/import_to_db",
    tags=["导入数据库"],
)


@router.post("/upload")
async def upload_excel(db: db_dependency, file: UploadFile = File(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to read Excel")

    try:
        cleaned_df = clean_excel(df)
        count = insert_rows_from_df(cleaned_df, db)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to process data")

    return {"status": "success", "inserted": count}


