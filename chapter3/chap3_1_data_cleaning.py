# coding:utf-8
"""
@file: chap3_1_data_cleaning.py
@time: 7/28/2019 10:21 AM
@contact: dabuwang
@desc: how to clean data:
数据清洗：缺失值、异常值和重复值的处理： 清洗，是对数据集进行丢弃、填充、替换、去重等操作，实现去除异常、纠正错误、补足缺失的目的。
"""

import pandas as pd # 导入Pandas库
import numpy as np # 导入Numpy库
from sklearn.preprocessing import Imputer # 导入sklearn.preprocessing中的Imputer库


def clean_missing_data():
    # 生成缺失数据
    df = pd.DataFrame(np.random.randn(6, 4), columns=
    ['col1', 'col2', 'col3', 'col4'])  # 生成一份数据
    print "="*20 + "生成缺失日志"
    df.iloc[1:2, 1] = np.nan  # 增加缺失值
    df.iloc[4, 3] = np.nan  # 增加缺失值
    print (df)

    # 查看哪些值缺失
    nan_all = df.isnull()  # 获得所有数据框中的N值
    print "="*20 + "查看哪些值缺失"
    print (nan_all)  # 打印输出
    # 查看哪些列缺失
    nan_col1 = df.isnull().any()  # 获得含有NA的列
    nan_col2 = df.isnull().all()  # 获得全部为NA的列
    print "=" * 20 + "查看哪些列缺失"
    print (nan_col1)  # 打印输出
    print (nan_col2)  # 打印输出

    # 丢弃缺失值
    df2 = df.dropna() # 直接丢弃含有NA的行记录
    print "=" * 20 + "丢弃缺失值"
    print (df2) # 打印输出

    # 使用sklearn将缺失值替换为特定值
    # 首先通 过Imputer方法创建一个预处理对象，其中strategy为默认缺失值的字符串，默认为NaN；示例中选择缺失值替换方法是均值（默认），还可以
    # 选择使用中位数和众数进行替换，即strategy值设置为median或 most_frequent；后面的参数axis用来设置输入的轴，默认值为0，即使用
    # 列做计算逻辑。然后使用预处理对象的fit_transform方法对df（数据框对象）进行处理，该方法是将fit和transform组合起来使用。
    nan_model = Imputer(missing_values='NaN', strategy='mean', axis=0) # 建立替换规则：将值为Nan的缺失值用均值做替换
    nan_result = nan_model.fit_transform(df) # 应用模型规则
    print "=" * 20 + "使用sklearn将缺失值替换为特定值"
    print (nan_result) # 打印输出

    # 使用Pandas将缺失值替换为特定值
    nan_result_pd1 = df.fillna(method='backfill') # 用后面的值替换缺失值
    nan_result_pd2 = df.fillna(method='bfill', limit=1) # 用后面的值替换缺失值,限制每列只能替换一个缺失值
    nan_result_pd3 = df.fillna(method='pad') # 用前面的值替换缺失值
    nan_result_pd4 = df.fillna(0) # 用0替换缺失值
    nan_result_pd5 = df.fillna({'col2': 1.1, 'col4': 1.2}) # 用不同值替换不同列的缺失值
    nan_result_pd6 = df.fillna(df.mean()['col2':'col4']) # 用平均数代替,选择各自列的均值替换缺失值
    # 打印输出
    print "=" * 20 + "使用Pandas将缺失值替换为特定值"
    print (nan_result_pd1)
    print (nan_result_pd2)
    print (nan_result_pd3)
    print (nan_result_pd4)
    print (nan_result_pd5)
    print (nan_result_pd6)


def clean_except_data():
    # 生成异常数据
    df = pd.DataFrame({'col1': [1, 120, 3, 5, 2, 12, 13],
                       'col2': [12, 17, 31, 53, 22, 32, 43]})
    print (df)  # 打印输出
    # 通过Z-Score方法判断异常值
    df_zscore = df.copy()  # 复制一个用来存储Z-score得分的数据框
    cols = df.columns  # 获得数据框的列名
    for col in cols:  # 循环读取每列
        df_col = df[col]  # 得到每列的值
        z_score = (df_col - df_col.mean()) / df_col.std()  # 计算每列的Z-score得分
        df_zscore[col] = z_score.abs() > 2.2  # 判断Z-score得分是否大于2.2，如果是    则为True，否则为False
    print (df_zscore)  # 打印输出


def clean_dup_data():
    import pandas as pd  # 导入Pandas库
    # 生成重复数据
    data1 = ['a', 3]
    data2 = ['b', 2]
    data3 = ['a', 3]
    data4 = ['c', 2]
    df = pd.DataFrame([data1, data2, data3, data4], columns=['col1', 'col2'])
    print (df)
    # 判断重复数据
    isDuplicated = df.duplicated()  # 判断重复数据记录
    print (isDuplicated)  # 打印输出
    # 删除重复值
    new_df1 = df.drop_duplicates()  # 删除数据记录中所有列值相同的记录
    new_df2 = df.drop_duplicates(['col1'])  # 删除数据记录中col1值相同的记录
    new_df3 = df.drop_duplicates(['col2'])  # 删除数据记录中col2值相同的记录
    new_df4 = df.drop_duplicates(['col1', 'col2'])  # 删除数据记录中指定列（col1 / col2）值相同的记录
    print (new_df1)  # 打印输出
    print (new_df2)  # 打印输出
    print (new_df3)  # 打印输出
    print (new_df4)  # 打印输出

if __name__ == '__main__':
    # clean_missing_data()
    # clean_except_data()
    clean_dup_data()