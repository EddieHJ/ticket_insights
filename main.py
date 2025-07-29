from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import import_to_db, analyze

import models
from database import engine

from utils.logger_helper import get_logger


logger = get_logger(__name__, log_file="app.log")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时
    logger.info("💎 Starting FastAPI app...")
    yield
    # 应用关闭时
    logger.info("🛑 Shutting down FastAPI app...")

app = FastAPI(lifespan=lifespan)

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

app.include_router(import_to_db.router)
app.include_router(analyze.router)


