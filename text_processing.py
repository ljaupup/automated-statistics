import re

conflict_college = ['公共管理', '管理', '理学院']

college_list = ['土木', '环境', '建科', '材料',
                '管理', '机电', '冶金', '信控',
                '艺术', '理学', '文学', '资源',
                '公管', '化工', '体育', '安德', '城市']

with open(r'src/250102.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r"(.+?): \d{2}-\d{2} \d{2}:\d{2}:\d{2}\n"

# 将匹配到的部分替换为空字符串
text_de_time = re.sub(pattern, "", text)

# print(text_de_time)

chat_infos = [i.strip() for i in text_de_time.split("\n\n")]

for info in chat_infos:
    print(info)
    print("-" * 50)
