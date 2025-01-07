import re
from pprint import pprint

import json

with open(r'json/250105.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    for info in v:
        # info中有的可能存在\n或者长空格，将其进行分割
        info = re.split(r'\n|\s+', info)


sort_data = {}
# 将data中的键值赋给新的字典sort_data
for k, v in data.items():
    sort_data[k] = {}

master_pattern = r"'硕|研'"

for k, v in data.items():
    for info in v:
#         如果在info中包含“硕”或“研”的字样，将其添加到字典中
        if "硕" in info or "研" in info:
            sort_data[k]["研究生"] = info

pprint(sort_data)
