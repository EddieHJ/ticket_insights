from fastapi import APIRouter

from utils import excel_processor

router = APIRouter(
    prefix="/convert",
    tags=["转换Excel"],
)

input_path = 'DATA/input.xlsx'
output_path = 'DATA/output.xlsx'

@router.post("/convert_excel")
async def convert_endpoint():
    try:
        excel_processor.convert_raw_to_output(input_path, output_path)
        return {"msg": "转换成功", "output": output_path}

    except Exception as e:
        return {"msg": "转换失败", "error": str(e)}

@router.get("/test")
async def test():
    return "hello world"