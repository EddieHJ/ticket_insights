import pandas as pd

def clean_excel(df: pd.DataFrame) -> pd.DataFrame:
    df[['组织1', '组织2']] = df['组织'].str.extract(r'([^/]+)?/?([^/]*)?')
    df['组织1'] = df['组织1'].str.strip()
    df['组织2'] = df['组织2'].str.strip()

    event_type_split = df['事件类型'].str.split('/', expand=True)
    for i in range(4):
        df[f'事件类型{i + 1}'] = event_type_split[i].str.strip()

    # 计算 Lead Time
    df['报单时间'] = pd.to_datetime(df['报单时间'])
    df['完成时间'] = pd.to_datetime(df['完成时间'])
    df['Lead Time'] = (df['完成时间'] - df['报单时间']).dt.total_seconds() // 60

    # 按顺序保留需要的字段
    desired_columns = [
        '任务ID', '标题', '创建者', '执行者', '紧急程度', '影响级', '优先级',
        '事件来源', '联系人', '单量', 'Jira工单',
        '组织1', '组织2',
        '事件类型1', '事件类型2', '事件类型3', '事件类型4',
        '报单时间', '完成时间', '是否完成', '借助伙伴资源',
        'Lead Time'
    ]

    df_final = df[desired_columns]

    return df_final