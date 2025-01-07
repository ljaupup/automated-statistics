import re
from pprint import pprint

import json

with open(r'json/250105.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    info_list = []
    for info in v:
        # 将长空格替换为一个\n
        info_de_space = re.sub(r'    +', '\n', info)
        print(info_de_space)
        # info中有的可能存在\n或者长空格，将其进行分割
        if '\n' in info:
            info_list = re.split(r'\n+', info_de_space)
            v.remove(info)
            break
    v.extend(info_list[1:])

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

pprint(sort_data)

# 若sort_data中的“研究生”的值为空，则删除该键值
for k, v in list(sort_data.items()):
    if not v["研究生"]:
        del sort_data[k]["研究生"]

with open(r'd:/DESKTOP/250105_sort.json', 'w', encoding='utf-8') as f:
    json.dump(sort_data, f, ensure_ascii=False, indent=4)
