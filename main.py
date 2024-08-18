'''
Author: Diana Tang
Date: 2024-08-16 15:28:01
LastEditors: Diana Tang
Description: transfer srt file to text file 
FilePath: /transformSrtFile/main.py
'''
import re

def deleteTimestamp(lines):

    # 定义正则表达式，匹配时间戳和文字内容
    pattern = r'(\d{2}:\d{2}:\d{2},\d{3}) --> .*'

    # 遍历文件内容，将符合时间戳格式的行删除，否则保留,并返回处理后的文本
    for line in lines:
        # 使用re.sub()函数替换时间戳为空字符串
        new_line = re.sub(pattern, '', line)
        # 返回处理后的文本
        yield new_line



def remove_timestamp(srt_file):
    with open(srt_file, 'r') as f:
        lines = f.readlines()
    no_timestamp_lines = []
    newLines= deleteTimestamp(lines)
    for line in newLines:
        stripped_line = line.strip()
        if stripped_line.startswith('-->'):
            continue
        no_timestamp_lines.append(stripped_line)
    with open('new_file1.txt', 'w') as f:
        f.writelines(no_timestamp_lines)

# 调用函数，读取srt文件并生成新的txt文件
remove_timestamp('./srt/[6.1]--Vue2原理分析①.srt')
#在一个文件夹下有多个srt文件，遍历所有的文件，转换成新的txt文件，文件名称和源文件相同，将这些文件放在txt文件夹下
import os
def remove_timestamp_all_files():
    for root, dirs, files in os.walk('./srt'):
        for file in files:
            if file.endswith('.srt'):
                remove_timestamp(os.path.join(root, file))




