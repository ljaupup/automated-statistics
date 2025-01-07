import re
from datetime import datetime, timedelta

import json


def j_p(json_f_p, desktop_path):
    with open(json_f_p, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for k, v in data.items():
        info_list = []
        for info in v:
            # 将长空格替换为一个\n
            info_de_space = re.sub(r'    +', '\n', info)
            # print(info_de_space)
            # info中有的可能存在\n或者长空格，将其进行分割
            if '\n' in info:
                info_list = info_de_space.split('\n')
                v.remove(info)
                if ':' in info_list[0] or "：" in info_list[0]:
                    v.extend(info_list[1:])
                else:
                    v.extend(info_list)
                break

    # with open(r'd:/DESKTOP/250105.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    sort_data = {}
    # 将data中的键值赋给新的字典sort_data
    for k, v in data.items():
        sort_data[k] = {"本科生": [], "研究生": []}

    for k, v in data.items():
        for info in v:
            # 如果在info中包含“硕”或“研”的字样，将其添加到字典中
            if "硕" in info or "研" in info:
                sort_data[k]["研究生"].append(info)
            else:
                sort_data[k]["本科生"].append(info)

    # 若sort_data中的“研究生”的值为空，则删除该键值
    for k, v in list(sort_data.items()):
        if not v["研究生"]:
            del sort_data[k]["研究生"]

    for k, v in sort_data.items():
        undergraduate = sort_data[k]["本科生"]
        # 根据列表undergraduate中的元素的级字前的两个数字进行排序

    # 前一天的日期
    date = datetime.now().date() - timedelta(days=1)
    date = date.strftime('%Y-%m-%d')
    with open(r'{}\{}值班记录.json'.format(desktop_path, date), 'w', encoding='utf-8') as f:
        json.dump(sort_data, f, ensure_ascii=False, indent=4)
    print('{}值班记录.json 文件已生成在桌面，请查看！'.format(date))
