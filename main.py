from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import excel_process, import_to_db, analyze

import models
from database import engine

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据库表
models.Base.metadata.create_all(bind=engine)

app.include_router(excel_process.router)
app.include_router(import_to_db.router)
app.include_router(analyze.router)


