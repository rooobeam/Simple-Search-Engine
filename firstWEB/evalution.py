import re


def extract(relat_d):
    result = []
    pattern = re.compile(r'N(\d{2})')  # 匹配 'N' 后的两个数字

    for sublist in relat_d:
        extracted_numbers = []
        for path in sublist:
            match = pattern.search(path)
            if match:
                extracted_numbers.append(int(match.group(1)))
        result.append(extracted_numbers)

    return result


def evaluate(relat_d, d_total, ind):
    d_ind = extract(relat_d)
    ans_ind = [10, 9, 4, 5, 10, 1, 4, 7, 19, 19, 4, 14, 12, 16, 19, 13]


    # 算TP TN FN FP
    i = ind
    TP = d_ind[0].count(i+1)  # 预测为正例且正确(TP)
    FP = len(d_ind[0]) - TP  # 预测为正例但错误（FP）
    FN = ans_ind[i] - TP  # 预测为负例但错误（FN）
    TN = d_total - TP - FP - FN  # 预测为负例且正确（TN）

    # 计算准确率
    acc = ((TP + TN) / (TP + TN + FP + FN))

    # 计算精确率
    prec = (TP / (TP + FP))

    # 计算召回率
    recal = (TP / (TP + FN))

    # 计算 F1 分数
    f1_s = (2 * (prec * recal) / (prec + recal+0.00000000001))

    return [acc, prec, recal, f1_s]
