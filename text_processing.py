import re
from pprint import pprint

college_log= {}

conflict_college = ['理学', '管理', '公共管理']

college_list = ['土木', '环境', '建科', '材料',
                '机电', '冶金', '信控', '艺术',
                '文学', '资源', '化工', '体育',
                '安德', '城市', '马院']


with open(r'src/250102.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r"(.+?): \d{2}-\d{2} \d{2}:\d{2}:\d{2}\n"

# 将匹配到的部分替换为空字符串
text_de_time = re.sub(pattern, "", text)

# print(text_de_time)

chat_infos = [i.strip() for i in text_de_time.split("\n\n")]
chat_infos_check = []

# 排除conflict_college之外的学院
print(len(chat_infos))
for college in college_list:
    if college not in college_log:
        college_log[college] = []
    for info in chat_infos:
        if college in info:
            # print(college + "---" + info)
            chat_infos_check.append(info)
            college_log[college].append(info)
    # print("*******************************")
print(len(chat_infos_check))

# 去除chat_infos中包含的chat_infos_check的项
for info in chat_infos_check:
    chat_infos.remove(info)
print(len(chat_infos))

conflict_college_patterns = {
    '理学': re.compile(r'^理学院'),
    '管理': re.compile(r'^管理'),
    '公管': re.compile(r'^公共管理(学院)?|^公管(学院)?')
}

for info in chat_infos:
    for keyword, pattern in conflict_college_patterns.items():
        if keyword not in college_log:
            college_log[keyword] = []
        if pattern.search(info):
            # print(keyword + "---" + info)
            college_log[keyword].append(info)

pprint(college_log)

sort_list = ['土木', '环境', '建科', '材料', '管理',
             '机电', '冶金', '信控', '艺术', '理学',
             '文学', '资源', '公管', '化工', '体育', '安德', '城市']
# 将college_log按sort_list排序
sorted_college_log = {k: college_log[k] for k in sort_list if k in college_log}
pprint(sorted_college_log)