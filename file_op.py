import os
import shutil
import time
from datetime import datetime, timedelta
import winreg
from text_processing import t_p
from json_processing import j_p

# 打印昨天的日期，yyMMdd格式
date = datetime.now().date() - timedelta(days=1)
date = date.strftime('%y%m%d')


def copy_txt(file_path: str, date: str):
    """
    将文件路径拖动到cmd窗口，然后回车，即可将文件复制到指定目录
    :param date: 日期yyMMdd
    :param file_path: 文件路径
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 检查以date命名的文件是否存在
    if not os.path.exists(r'src/{}.txt'.format(date)):
        # 创建文件
        with open(r'src/{}.txt'.format(date), 'w', encoding='utf-8') as f:
            f.write(text)
        print('文件创建成功！')
        return r'src/{}.txt'.format(date)
    else:
        ask = input('文件已存在，是否覆盖？（y/N）')
        if ask == 'N':
            print('文件未覆写！')
            return r'src/{}.txt'.format(date)
        elif ask == 'y':
            t_s = int(time.time() * 1000)
            f_p = r'src/{}_{}.txt'.format(date, t_s)
            with open(f_p, 'w', encoding='utf-8') as f:
                f.write(text)
            print('文件覆写成功！')
            return f_p


def get_desktop_path_windows():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
    try:
        desktop_path, _ = winreg.QueryValueEx(key, "Desktop")
        return desktop_path
    except FileNotFoundError:
        return None
    finally:
        winreg.CloseKey(key)


if __name__ == '__main__':
    target_f_p = input('请将目标文件拖入对话框：')
    chat_txt_f_p = copy_txt(target_f_p, date)
    json_f_p = r'json/{}.json'.format(date)
    # 使用t_p函数处理txt文件，将结果写入json文件
    t_p(chat_txt_f_p, json_f_p)
    # 获取桌面路径
    desktop_path = get_desktop_path_windows()
    # 使用j_p函数处理json文件，将结果写入桌面
    j_p(json_f_p, desktop_path)
