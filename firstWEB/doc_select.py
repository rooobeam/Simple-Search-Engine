import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

dataset = [1, 9, 6, 4, 2, 7, 8, 5, 4, 1, 6, 9, 0, 7]  # 设置要读取的数据集


def select_d(d_sim):
    x = np.array(d_sim).reshape(-1, 1)

    # /////设置簇数范围/////
    low = 2
    high = 8

    silhouetteScore = []
    predict = []
    ctr = []

    for i in range(low, high):
        kmeans = KMeans(n_clusters=i).fit(x)

        y = kmeans.fit_predict(x)  # 会得出每个sample属于哪一类
        predict.append(y)
        ctr.append(kmeans.cluster_centers_)

        silhouetteScore.append(silhouette_score(x, kmeans.labels_))  # 将各个指标储存

    # 输出轮廓系数最大时的最小簇
    max_sil = np.array(silhouetteScore).argmax()  # sil最大值
    arr = predict[max_sil]  # 选中sil最大时的预测结果
    ctr2 = ctr[max_sil]  # 选中sil最大时的中心点

    min_ctr = np.array(ctr2).argmin()

    result = []
    position = []
    for i in range(0, len(d_sim)):
        if arr[i] == min_ctr:
            result.append(d_sim[i])
            position.append(i)

    print(result, position)

    return result, position


if __name__ == "__main__":
    select_d(dataset)

