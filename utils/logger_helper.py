import logging
import sys
from typing import Optional


DEFAULT_FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s'
DEFAULT_LOG_FILE = 'app.log'
DEFAULT_LEVEL = logging.INFO

def setup_root_logger(
    log_format: str = DEFAULT_FORMAT,
    log_file: Optional[str] = DEFAULT_LOG_FILE,
    level: int = DEFAULT_LEVEL
):
    """集中式使用：在主程序调用一次即可，全局模块共享"""
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding='utf-8') if log_file else logging.NullHandler()
        ]
    )


# 这个是给需要调方法来获取logger的场景用的，可以传入想要的参数
def get_logger(
    name: Optional[str] = None,
    log_format: str = DEFAULT_FORMAT,
    log_file: Optional[str] = DEFAULT_LOG_FILE,
    level: int = DEFAULT_LEVEL
) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 独立 logger 模式：只添加一次 handler，防止重复
    if not logger.handlers:
        formatter = logging.Formatter(log_format)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_file:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    logger.propagate = False  # 防止冒泡导致重复输出
    return logger

