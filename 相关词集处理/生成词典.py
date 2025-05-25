import pickle
from gensim.models import FastText
import jieba

# 读取包含中文词项的pkl文件
input_pkl_path = "F:\\有用\\各个学期文件汇总\\大二下\\搜索引擎\\大作业\\total_data.pkl"  # 输入pkl文件路径
output_pkl_path = 'dictionary1.pkl'  # 输出pkl文件路径
with open(input_pkl_path, 'rb') as file:
    word_list = pickle.load(file)

# 假设word_list是一个列表，每个元素是一个词
# 使用FastText训练模型
model = FastText(
    sentences=[word_list],
    vector_size=200,  # 向量维度
    window=10,       # 窗口大小
    min_count=1,     # 最小词频
    sg=1,            # 使用Skip-gram
    workers=4,       # 使用4个CPU核心进行训练
    epochs=10        # 训练次数
)

# 自定义的判断函数
def is_similar(word1, word2):
    if word1 in word2 or word2 in word1:
        return True
    segs1 = set(jieba.cut(word1))
    segs2 = set(jieba.cut(word2))
    if len(segs1 & segs2) > 0:
        return True
    return False

# 生成词典，每个键是词项，值是与其最相关的且不重复的前五个词项
similarity_dict = {}
for word in word_list:
    if word in model.wv:
        # 找到与word最相似的topn=20个词项
        similar_words = model.wv.most_similar(word, topn=20)
        # 去重，确保只有五个词项
        seen = set()
        top_5_similar = []
        for similar_word, _ in similar_words:
            if similar_word not in seen and is_similar(word, similar_word):
                top_5_similar.append(similar_word)
                seen.add(similar_word)
            if len(top_5_similar) == 5:
                break
        if top_5_similar:
            similarity_dict[word] = top_5_similar
        else:
            similarity_dict[word] = None
    else:
        similarity_dict[word] = None

# 将结果保存到新的 pkl 文件中
with open(output_pkl_path, 'wb') as file:
    pickle.dump(similarity_dict, file)

print("结果已保存到", output_pkl_path)
