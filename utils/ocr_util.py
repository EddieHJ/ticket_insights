from paddleocr import PaddleOCR
import os, json
from utils.dir_util import ensure_dir


def get_ocr_result(filepath: str):
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        # text_detection_model_dir="C:/Users/Admin/.paddlex/official_models/PP-OCRv5_server_det",
        # text_recognition_model_dir="C:/Users/Admin/.paddlex/official_models/PP-OCRv5_server_rec"

    )  # 文本检测+文本识别

    result = ocr.predict(filepath)

    output_path = ensure_dir("ocr_output")

    for res in result:
        res.print()
        res.save_to_img(output_path)
        res.save_to_json(output_path)

    # 获取图片的basename
    basename = os.path.splitext(os.path.basename(filepath))[0]

    # 拼接成Paddle解析后导出的json文件名
    json_filename = basename + "_res.json"

    # 读取Paddle生成的json文件
    json_file = os.path.join(output_path, json_filename)
    with open(f"{json_file}", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # 返回json文件里的正文list
    return data["rec_texts"]
