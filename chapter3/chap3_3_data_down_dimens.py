# coding:utf-8
"""
@file: chap3_3_data_down_dimens.py
@time: 7/28/2019 9:49 PM
@contact: dabuwang
@desc: 大数据时代的数据降维
"""

def data_down_dimens_demo():
    """
    本示例中，将分别使用sklearn的DecisionTreeClassifier来判断变量重要性并选择变量，通过PCA进行维度转换。
    :return:
    """
    import numpy as np
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.decomposition import PCA
    # 读取数据文件
    data = np.loadtxt('data1.txt')  # 读取文本数据文件
    x = data[:, :-1]  # 获得输入的x
    y = data[:, -1]  # 获得目标变量y
    print (x[0], y[0])  # 打印输出x和y的第一条记录

    # 使用sklearn的DecisionTreeClassifier判断变量重要性
    model_tree = DecisionTreeClassifier(random_state=0)  # 建立分类决策树模型对象
    model_tree.fit(x, y)  # 将数据集的维度和目标变量输入模型
    feature_importance = model_tree.feature_importances_  # 获得所有变量的重要性得分
    print (feature_importance)  # 打印输出
    """从变量重要性得分看出，第4/5/7三个变量的重要性最高，分别约为0.12、0.48、0.17，三者得分之和约等于77%，这意味着仅仅这3个变量
已经具有非常显著的并且足以代表所有变量参与模型计算的能力。因此，可以选择这3个变量参与后续模型计算。
    """

    # 使用sklearn的PCA进行维度转换
    model_pca = PCA()  # 建立PCA模型对象
    model_pca.fit(x)  # 将数据集输入模型
    model_pca.transform(x)  # 对数据集进行转换映射
    components = model_pca.components_  # 获得转换后的所有主成分
    components_var = model_pca.explained_variance_  # 获得各主成分的方差
    components_var_ratio = model_pca.explained_variance_ratio_  # 获得各主成分的方    差占比
    print (components[:2])  # 打印输出前2个主成分
    print (components_var[:2])  # 打印输出前2个主成分的方差
    print (components_var_ratio)  # 打印输出所有主成分的方差占比
    """
    所有主成分的方差占比是选择主成分数量的关键，因为PCA降维的基本思想是根据方差占比来选择主成分的数量。通过该结
果可以看出，前6项主成分的方差占比之和components_var_ratio[:5].sum（）约等于77%，取前6项主成分基本可以
作为转换后的主成分参与后续模型计算。
    """

if __name__ == '__main__':
    data_down_dimens_demo()