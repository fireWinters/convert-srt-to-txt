'''
Author: Diana Tang
Date: 2024-08-16 18:14:32
LastEditors: Diana Tang
Description: some description
FilePath: /transformSrtFile/# 示例关键词列表.py
'''
# 示例关键词列表
keywords = ["原研药", "退市", "西力欣"]

# 用户发布的动态示例
user_posts = {
    "user1": "这是一条关于原研药的动态。",
    "user2": "我今天在研究退市的情况。",
    "user3": "这只是一个普通的动态。",
    "user4": "西力欣这个药品效果怎么样？",
    "user5":'西力欣是抗生素吗？'
}

# 锁定用户ID的列表
flagged_users = []

# 检索动态并锁定包含关键词的用户ID
for user_id, post in user_posts.items():
    for keyword in keywords:
        if keyword in post:
            flagged_users.append(user_id)
            break  # 只要找到一个关键词，就不再继续检查其他关键词

# 输出结果
print("锁定的用户ID:", flagged_users)

#优化后算法
# 示例关键词列表
keywords = {"原研药", "退市", "西力欣"}  # 使用集合存储关键词

# 用户发布的动态示例
user_posts = {
    "user1": "这是一条关于原研药的动态。",
    "user2": "我今天在研究退市的情况。",
    "user3": "这只是一个普通的动态。",
    "user4": "西力欣这个药品效果怎么样？",
    "user5":'西力欣是抗生素吗？'
}

# 锁定用户ID的列表
flagged_users = []

# 检索动态并锁定包含关键词的用户ID
for user_id, post in user_posts.items():
    words = set(post.split())  # 将动态拆分为单词集合
    if keywords & words:  # 检查关键词集合和动态单词集合的交集
        flagged_users.append(user_id)

# 输出结果
print("锁定的用户ID:", flagged_users)