import pickle

def process_dict_to_list(input_pkl_path, output_pkl_path):
    # 读取包含词典的pkl文件
    with open(input_pkl_path, 'rb') as file:
        data_dict = pickle.load(file)

    # 将词典中的每个键和它的全部值组成一个列表
    result_list = [[key] + values for key, values in data_dict.items()]

    # 将结果保存到新的pkl文件中
    with open(output_pkl_path, 'wb') as file:
        pickle.dump(result_list, file)

    print("结果已保存到", output_pkl_path)

# 示例用法
input_pkl_path = "F:\\有用\\各个学期文件汇总\\大二下\\搜索引擎\\大作业\\dddictionary.pkl"  # 输入pkl文件路径
output_pkl_path = 'list.pkl'  # 输出pkl文件路径
process_dict_to_list(input_pkl_path, output_pkl_path)


#有空值的转法
import pickle

# 从用户提供的pkl文件中读取字典
with open("F:\\有用\\各个学期文件汇总\\大二下\\搜索引擎\\大作业\\dictionary1.pkl", 'rb') as file:
    your_dict = pickle.load(file)

# 构建大列表
big_list = []
for key, value in your_dict.items():
    if value:  # 如果值存在
        big_list.append([key, *value])  # 使用*操作符展开值列表
    else:
        big_list.append([key])

# 将大列表保存到pkl文件中
with open('output_list.pkl', 'wb') as file:
    pickle.dump(big_list, file)

# 返回大列表
print(big_list)
