from utils.ocr_util import get_ocr_result
# from utils.opencv_util import get_opencv_result

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.opencv_util import get_opencv_result


def get_recog_results(filepaths: list[str]) -> dict:
    reporters: list[str] = []
    opencv_result_list: list[str] = []
    sentences: list[str] = []

    for filepath in filepaths:
        # 先获取reporter
        reporter = get_ocr_result(filepath)[0]
        print(f"reporter: {reporter}")

        reporters.append(reporter)

        opencv_result = get_opencv_result(filepath)
        opencv_result_list.append(opencv_result)

    for opencv_result in opencv_result_list:
        ocr_result: list[str] = get_ocr_result(opencv_result)

        # 将ocr识别的ocr_result list拼接在一起
        ocr_sentence = " ".join(ocr_result)
        sentences.append(ocr_sentence)

    return {"reporters": reporters, "sentences": sentences}


test_list = ["../rag/test5.jpg", "../rag/test6_multi.png"]
print(get_recog_results(test_list))
