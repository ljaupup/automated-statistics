import re

conflict_college = ['理学院', '管理', '公共管理']

college_list = ['土木', '环境', '建科', '材料',
                # '管理',
                '机电', '冶金', '信控',
                '艺术',
                # '理学',
                '文学', '资源',
                # '公管',
                '化工', '体育', '安德', '城市', '马院']

# college_list = ['信控']

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
    for info in chat_infos:
        if college in info:
            print(college + "---" + info)
            chat_infos_check.append(info)
    print("*******************************")
print(len(chat_infos_check))

# 去除chat_infos中包含的chat_infos_check的项
for info in chat_infos_check:
    chat_infos.remove(info)
print(len(chat_infos))

# 处理conflict_college中的学院
for info in chat_infos:
    for i in range(3):
        if conflict_college[0] not in info:
            continue
        if conflict_college[i] in info:
            continue
        else:
            print(conflict_college[i - 1] + "---" + info)
            break

# for info in chat_infos:
#     print(info)
