from datetime import datetime
import cv2, os
import numpy as np
from utils.dir_util import ensure_dir


def get_opencv_result(filepath: str) -> str:
    save_dir = ensure_dir("opencv_output")
    os.makedirs(save_dir, exist_ok=True)

    # 1. 读取图片
    image = cv2.imread(filepath)
    # 2. 定义灰色的 BGR 范围（根据你调好的范围）
    lower = np.array([228, 228, 228])
    upper = np.array([236, 236, 236])
    # 3. 生成掩码
    mask = cv2.inRange(image, lower, upper)
    # 4. 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    dialog_index = 0

    filepath_out = None

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 50 and h > 30:  # 过滤小噪点
            roi = image[y:y + h, x:x + w]  # 裁剪矩形区域
            # 获取当前时间戳，格式 YYYYMMDDHHMMSS
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            # 拼接文件名：dialog_时间戳_index.png
            filename = f"dialog_{timestamp}_{dialog_index}.png"
            filepath_out = os.path.join(save_dir, filename)
            # 保存文件
            cv2.imwrite(filepath_out, roi)
            dialog_index += 1

    # 返回红框文件（带路径的str）
    return filepath_out


