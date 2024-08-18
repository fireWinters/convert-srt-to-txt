'''
Author: Diana Tang
Date: 2024-08-16 18:23:05
LastEditors: Diana Tang
Description: some description
FilePath: /transformSrtFile/# 示例关键词列表 copy.py
'''
// 示例关键词列表
const keywords = new Set(["原研药", "退市", "西力欣"]);  // 使用 Set 存储关键词

// 用户发布的动态示例
const userPosts = {
    "user1": "这是一条关于原研药的动态。",
    "user2": "我今天在研究退市的情况。",
    "user3": "这只是一个普通的动态。",
    "user4": "西力欣这个药品效果怎么样？",
    "user5": "西力欣是抗生素吗？"
};

// 锁定用户ID的列表
let flaggedUsers = [];

// 检索动态并锁定包含关键词的用户ID
for (const [userId, post] of Object.entries(userPosts)) {
    const words = new Set(post.split(/\s+/));  // 将动态拆分为单词集合
    for (let word of words) {
        if (keywords.has(word)) {  // 检查关键词集合中是否存在该单词
            flaggedUsers.push(userId);
            break;  // 一旦找到匹配的关键词，跳出循环
        }
    }
}

// 输出结果
console.log("锁定的用户ID:", flaggedUsers);



// 考虑V8引擎对for循环优化这一背景，优化代码如下：

// 示例关键词列表
const keywords = ["原研药", "退市", "西力欣"];  // 使用数组存储关键词，提升遍历速度

// 用户发布的动态示例
const userPosts = {
    "user1": "这是一条关于原研药的动态。",
    "user2": "我今天在研究退市的情况。",
    "user3": "这只是一个普通的动态。",
    "user4": "西力欣这个药品效果怎么样？",
    "user5": "西力欣是抗生素吗？"
};

// 锁定用户ID的列表
let flaggedUsers = [];

// 检索动态并锁定包含关键词的用户ID
for (const userId in userPosts) {
    const post = userPosts[userId];
    const words = post.split(/\s+/);  // 将动态拆分为单词数组

    outerLoop: for (let i = 0, len = words.length; i < len; i++) {  // 使用缓存的长度进行循环
        for (let j = 0, klen = keywords.length; j < klen; j++) {
            if (words[i] === keywords[j]) {  // 直接比较字符串
                flaggedUsers.push(userId);
                break outerLoop;  // 跳出外部循环
            }
        }
    }
}

// 输出结果
console.log("锁定的用户ID:", flaggedUsers);
