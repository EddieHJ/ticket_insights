import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件中的变量

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def analyze_ticket_periods(tickets1: list[dict], tickets2: list[dict]) -> str:
    """
    用于分析两段时间的 IT 工单数据差异，并生成自然语言总结报告。
    参数：
        tickets1: 第一段时间的工单统计数据（event_type_4 + count）
        tickets2: 第二段时间的工单统计数据（event_type_4 + count）
    返回：
        GPT 返回的自然语言分析结果
    """
    prompt = f"""
我有两段时间内的 IT 工单统计数据，结构如下：

第一段时间的数据：
{json.dumps(tickets1, ensure_ascii=False, indent=2)}

第二段时间的数据：
{json.dumps(tickets2, ensure_ascii=False, indent=2)}

每条记录的 event_type_4 是子事件类型，count 是该类型的工单数量。

请你对比这两段时间内的各类事件数量差异，直接直观的指出各个类型数量的变化即可，每个类型起个数字序号。以以下方式体现：
1、给出类型的名字
2、给出第一段时间的数量，给出第二段时间的数量
3、直观的给出数量变化


    """.strip()

    completion = client.chat.completions.create(
        model="qwen-turbo-2025-04-28",
        messages=[{"role": "user", "content": prompt}],
        timeout=120
    )

    return completion.choices[0].message.content
