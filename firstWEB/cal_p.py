import pickle
import math


def cal_proportion_d(token, file_lis, token_relat_lis):
    # with open(file_path, 'rb') as lis_file:
    #     data = pickle.load(lis_file)
    # 词总数
    words_num = len(file_lis)
    # 词种类数
    words_sorts = len(set(file_lis))
    # c(token)
    # count_of_token = file_lis.count(token)
    relat_key_lis = []
    for lis in token_relat_lis:
        relat_key_lis.append(lis[0])
    count_of_token = 0
    if token in relat_key_lis:
        a = token_relat_lis[relat_key_lis.index(token)]
        for term in token_relat_lis[relat_key_lis.index(token)]:
            count_of_token += file_lis.count(term)

    a = 0.05
    b = 1
    c = 0.05
    p = (count_of_token + a) / (c * words_num + b * words_sorts)
    return p


def cal_proportion_q(lis, d_path):
    p_table = {}
    appear_times = {}

    q_len = len(lis)
    for term in lis:
        if term in p_table:
            p_table[term] += 1
        else:
            p_table[term] = 1

    for term in p_table:
        appear_times[term] = count_in_d(term, d_path)

    for term in p_table:
        p_table[term]=(p_table[term]/q_len) * math.log2(len(d_path)/(appear_times[term]+1))

    return p_table


def read_pkl_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except pickle.UnpicklingError:
        print("Error: The file is not a valid pickle file.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def count_in_d(term, d_path):
    n = 0
    for path in d_path:
        data = read_pkl_file(path)
        if term in data:
            n += 1
    return n
