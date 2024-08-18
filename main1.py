'''
Author: Diana Tang
Date: 2024-08-16 16:56:53
LastEditors: Diana Tang
Description: some description
FilePath: /transformSrtFile/main1.py
'''
import os
import re

# 源文件夹路径
source_folder = './srtFiles'

# 目标文件夹路径
target_folder = './txtFiles'

# 获取源文件夹下的所有文件名
file_names = os.listdir(source_folder)

def deleteTimestamp(lines):

    # 定义正则表达式，匹配时间戳和文字内容
    pattern = r'(\d{2}:\d{2}:\d{2},\d{3}) --> .*'

    # 遍历文件内容，将符合时间戳格式的行删除，否则保留,并返回处理后的文本
    for line in lines:
        # 使用re.sub()函数替换时间戳为空字符串
        new_line = re.sub(pattern, '', line)
        # 返回处理后的文本
        yield new_line
# # 遍历文件名列表，将文件名作为txt文件名，将SRT文件内容写入txt文件
# for file_name in file_names:
#     if file_name.endswith('.srt'):
#         source_file = os.path.join(source_folder, file_name)
#         target_file = os.path.join(target_folder, file_name)
#         with open(source_file, 'r', encoding='utf-8') as f:
#             lines = f.readlines()
#             deleteTimestamp(lines)
#         with open(target_file, 'w', encoding='utf-8') as f:
#             f.writelines(lines)
#将SRT文件改成txt文件
import os

def convert_srt_to_txt(folder_path,target_path):
    # 遍历指定文件夹下的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为 .srt 结尾的文件
        if filename.endswith('.srt'):
            # 构建文件的完整路径
            srt_file_path = os.path.join(folder_path, filename)
            
            # 创建新的 .txt 文件路径
            txt_file_path = os.path.join(target_path, filename.replace('.srt', '.txt'))
            # 定义一个变量用来保存处理后的文本
            new_lines = []
            # 打开 .srt 文件并读取内容
            with open(srt_file_path, 'r', encoding='utf-8') as srt_file:
                lines = srt_file.readlines()
                new_lines=deleteTimestamp(lines)
            # 将内容写入新的 .txt 文件
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.writelines(new_lines)
            
            print(f"Converted {filename} to {filename.replace('.srt', '.txt')}")

# 调用函数并传入目标文件夹路径
folder_path = './srtFiles'  # 请将此路径替换为你实际的文件夹路径
target_path='./txtFiles'
convert_srt_to_txt(folder_path,target_path)
