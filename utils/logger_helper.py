import logging
import sys
from typing import Optional

# 这个是给需要调方法来获取logger的场景用的，可以传入想要的参数
def get_logger(
    name: Optional[str] = None,
    log_format: str = '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
    log_file: Optional[str] = "app.log",
    level: int = logging.INFO
) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger   # 已配置过，直接返回，避免重复添加 handler

    formatter = logging.Formatter(log_format)

    # 控制台输出
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件输出（可选）
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# 这个是懒人logger，直接导入获取即可，无需调方法+传参
LOG_FILE = "app.log"  # 日志文件路径，想写就改，想不写就设置为 None
LOG_LEVEL = logging.INFO

logger = logging.getLogger("myapp")
logger.setLevel(LOG_LEVEL)

# 避免重复添加 handler
if not logger.handlers:
    # 控制台 handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # 文件 handler（可选）
    if LOG_FILE:
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)