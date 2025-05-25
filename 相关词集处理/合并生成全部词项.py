import os
import pickle

def merge_pkls(folder_path, output_file):
    # 存储所有列表的变量
    merged_list = []

    # 遍历文件夹中的文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pkl'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as f:
                # 从 pkl 文件中加载列表数据
                data = pickle.load(f)
                # 将加载的列表添加到 merged_list 中
                merged_list.extend(data)

    # 将合并后的列表保存到输出文件中
    with open(output_file, 'wb') as f:
        pickle.dump(merged_list, f)

# 示例用法
folder_path = "F:\\pkl"  # 替换为你的文件夹路径
output_file = 'total_data.pkl'  # 输出文件的路径
merge_pkls(folder_path, output_file)
