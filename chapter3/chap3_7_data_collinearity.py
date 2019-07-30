# coding:utf-8
"""
@file: chap3_7_data_collinearity.py
@time: 7/30/2019 11:08 PM
@contact: dabuwang
@desc: 运营数据的共线性问题:
所谓共线性（又称多重共线性）问题指的是输入的自变量之间存在较高的线性相关度。共线性问题会导致回归模型的稳定性和准确性大大降低.

## 解决共线性的5种常用方法
（1）增大样本量（2）岭回归法（Ridge Regression）（3）逐步回归法（Stepwise Regression）（4）主成分回归（Principal Components Regression）（5）人工去除
"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression


def data_collinearity_handle():
    # 读取数据
    data = np.loadtxt('data5.txt', delimiter='\t')  # 读取数据文件
    x = data[:, :-1]  # 切分自变量
    y = data[:, -1]  # 切分预测变量
    print x
    print y

    # 使用岭回归算法进行回归分析
    model_ridge = Ridge(alpha=1.0)  # 建立岭回归模型对象
    model_ridge.fit(x, y)  # 输入x/y训练模型
    print (model_ridge.coef_)  # 打印输出自变量的系数
    print (model_ridge.intercept_)  # 打印输出截距

    # 使用主成分回归进行回归分析
    model_pca = PCA()  # 建立PCA模型对象
    data_pca = model_pca.fit_transform(x)  # 将x进行主成分分析
    ratio_cumsm = np.cumsum(model_pca.explained_variance_ratio_)  # 得到所有主成分方差占比的累积数据
    print (ratio_cumsm)  # 打印输出所有主成分方差占比累积

    rule_index = np.where(ratio_cumsm > 0.8)  # 获取方差占比超过0.8的所有索引值
    min_index = rule_index[0][0]  # 获取最小索引值
    data_pca_result = data_pca[:, :min_index + 1]  # 根据最小索引值提取主成分
    model_liner = LinearRegression()  # 建立回归模型对象
    model_liner.fit(data_pca_result, y)  # 输入主成分数据和预测变量y并训练模型
    print (model_liner.coef_)  # 打印输出自变量的系数
    print (model_liner.intercept_)  # 打印输出截距


if __name__ == '__main__':
    data_collinearity_handle()
