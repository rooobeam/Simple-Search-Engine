import pickle
from firstWEB import cal_p
import os
import glob
import math
from firstWEB import doc_select
from firstWEB import evalution
from firstWEB import input


def func(query):
    # 文档地址*******************************************************
    # 获取文档lis目录
    current_dir = r"D:\PyProject\STNO-UNICODE-lis"
    new_dir = r"D:\PyProject\STNO-UNICODE-p"
    # 遍历当前目录下的所有文件夹
    d_path = []
    for folder in os.listdir(current_dir):
        # folder——NO1
        folder_path = os.path.join(current_dir, folder)
        new_folder_path = os.path.join(new_dir, folder)
        # new_folder_path = r"D:\作业夹\大二\搜索引擎\python\STNO-UNICODE-lis\NO1"
        # folder_path = r"D:\作业夹\大二\搜索引擎\python\STNO-UNICODE-p\NO1"
        if os.path.isdir(folder_path):
            # 遍历文件夹中的所有文件

            for file_path in glob.glob(os.path.join(folder_path, '*')):
                # file_path——r"D:\作业夹\大二\搜索引擎\python\STNO-UNICODE\N01\XIN_CMN_20000206_0099.pkl"

                if os.path.isfile(file_path):
                    d_path = d_path+[file_path]

    # 获取相关词集
    relat_lis_path = r'D:\PyProject\word_cluster.pkl'
    token_relat_lis = cal_p.read_pkl_file(relat_lis_path)

    # 查询*******************************************************
    query, ind = input.chinese_word_cut(query)
    q_lis = [query]

    # 计算*******************************************************
    relat_d = []
    relat_p = []

    for q in q_lis:

        d_sim = []
        q_table = cal_p.cal_proportion_q(q, d_path)
        for d in d_path:
            token_sim = 0
            d_lis = cal_p.read_pkl_file(d)

            for token in q_table:
                por_d = cal_p.cal_proportion_d(token, d_lis, token_relat_lis)
                adjust = 0.5
                token_sim += q_table[token]*math.log10(adjust*q_table[token]/por_d)
            d_sim.append(token_sim)

        relat_p_i, d_ind = doc_select.select_d(d_sim)

        print(d_ind)
        relat_d.append([d_path[i] for i in d_ind])
        relat_p.append(relat_p_i)

    acc, prec, recal, f1_s = evalution.evaluate(relat_d, len(d_path), ind)

    combined = list(zip(relat_p[0], relat_d[0]))
    # print('before',relat_p)

    # 使用sorted函数对元组列表进行排序，这里我们根据元组的第一个元素（即A中的元素）排序
    # 注意，sorted函数返回的是新的列表，不会修改原来的列表
    sorted_combined = sorted(combined)

    # 通过解压缩的方式将排序后的元组列表分成两个列表
    relat_p[0], relat_d[0] = zip(*sorted_combined)
    # print('after',relat_p)
    # 因为zip返回的是迭代器，所以需要再次转换为列表
    relat_d = list(relat_d)



    print(acc, prec, recal, f1_s)
    return relat_d, acc, prec, recal, f1_s







