# coding:utf-8
"""
@file: chap3_2_data_signal.py
@time: 7/28/2019 9:22 PM
@contact: dabuwang
@desc: 将分类数据和顺序数据转换为标志变量
1）分类数据：分类数据指某些数据属性只能归于某一类别的非数值型数据，例如性别中的男、女就是分类数据。
用户性别：   男   女
0001        1   0
0002        0   1
2）顺序数据：顺序数据只能归于某一有序类别的非数值型数据，例如用户的价值度分为高、中、低，学历分为博士、研究生、学士，这些都属于顺序数据。

"""


def data_signal_exchange():
    import pandas as pd  # 导入pandas库
    from sklearn.preprocessing import OneHotEncoder  # 导入OneHotEncoder库
    # 生成数据
    df = pd.DataFrame({'id': [3566841, 6541227, 3512441],
                       'sex': ['male', 'Female', 'Female'],
                       'level': ['high', 'low', 'middle']})
    print (df)  # 打印输出原始数据框
    # 自定义转换主过程
    df_new = df.copy()  # 复制一份新的数据框用来存储转换结果
    for col_num, col_name in enumerate(df):  # 循环读出每个列的索引值和列名
        col_data = df[col_name]  # 获得每列数据
        col_dtype = col_data.dtype  # 获得每列dtype类型
        if col_dtype == 'object':  # 如果dtype类型是object（非数值型），执行条件
            df_new = df_new.drop(col_name, 1)  # 删除df数据框中要进行标志转换的列
            value_sets = col_data.unique()  # 获取分类和顺序变量的唯一值域
            for value_unique in value_sets:  # 读取分类和顺序变量中的每个值
                col_name_new = col_name + '_' + value_unique  # 创建新的列名，使    用“原标题 + 值”的方式命名
                col_tmp = df.iloc[:, col_num]  # 获取原始数据列
                new_col = (col_tmp == value_unique)  # 将原始数据列与每个值进行比    较，相同为True，否则为False
                df_new[col_name_new] = new_col  # 为最终结果集增加新列值
    print (df_new)  # 打印输出转换后的数据框

    # 使用sklearn进行标志转换
    df2 = pd.DataFrame({'id': [3566841, 6541227, 3512441],
                        'sex': [1, 2, 2],
                        'level': [3, 1, 2]})
    id_data = df2.values[:, :1]  # 获得ID列
    transform_data = df2.values[:, 1:]  # 指定要转换的列
    enc = OneHotEncoder()  # 建立模型对象
    df2_new = enc.fit_transform(transform_data).toarray()  # 标志转换
    df2_all = pd.concat((pd.DataFrame(id_data), pd.DataFrame(df2_new)), axis=1)  # 组合为数据框
    print (df2_all)  # 打印输出转换后的数据框


if __name__ == '__main__':
    data_signal_exchange()
