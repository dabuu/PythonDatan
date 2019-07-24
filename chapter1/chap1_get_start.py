# coding:utf-8
"""
@file: chap1_get_start.py.py
@time: 7/24/2019 9:56 PM
@contact: dabuwang
@desc:
案例场景：每个销售型公司都有一定的促销费用，促销费用可以带
来销售量的显著提升；当给出一定的促销费用时，预计会带来多大的商
品销售量？
data.txt存储了建模所需的原始数据，字段变量：第一列是促销费用，第二列是商品销售量。
"""

import re
import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt


def main(pre_cost):
    fn = open('data.txt', 'r')
    all_data = fn.readlines()
    fn.close()

    x, y = [], []
    for line in all_data:
        tx, ty = re.split('\t', line)
        x.append(float(tx.strip()))
        y.append(float(ty.strip()))
    # 将x和y由列表类型转换为数组类型，同时数组的形状是100行1列
    x = numpy.array(x).reshape([100,1])
    y = numpy.array(y).reshape([100,1])

    # plt.scatter(x, y)
    # plt.show()

    # 选择线性回归训练模型
    model = linear_model.LinearRegression()
    model.fit(x,y)
    # 模型评估
    model_coef = model.coef_ # 获取模型的自变量的系数并赋值为model_coef
    model_inter = model.intercept_ # 获取模型的截距并赋值为model_intercept
    r2 = model.score(x,y) # 模型的决定系数R的平方
    print model_coef, model_inter, r2
    # [[2.09463661]] [13175.36904199] 0.7876414684758954

    new_x = [[pre_cost]]   # 输入促销费用,  *注*：这里跟书里不一致
    pre_y = model.predict(new_x)    # 模型计算预期销售额
    print "pre_y: %s" % repr(pre_y)


if __name__ == '__main__':
    main(84610)