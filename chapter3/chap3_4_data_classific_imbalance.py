# coding:utf-8
"""
@file: chap3_4_data_classific_imbalance.py
@time: 7/28/2019 10:19 PM
@contact: dabuwang
@desc: 所谓的不均衡指的是不同类别的样本量差异非常大。样本类别分布不均衡主要出现在分类相关的建模问题上。样本类别分布不均衡从数据
规模上可以分为大数据分布不均衡和小数据分布不均衡两种。

·大数据分布不均衡；这种情况下整体数据规模大，只是其中的小样本类的占比较少。但是从每个特征的分布来看，小样本也覆盖了大部
分或全部的特征。例如拥有1000万条记录的数据集中，其中占比50万条的少数分类样本便于属于这种情况。
·小数据分布不均衡；这种情况下整体数据规模小，并且占据少量样本比例的分类数量也少，这会导致特征分布的严重不平衡。例如拥有
1000条数据样本的数据集中，其中占有10条样本的分类，其特征无论如何拟合也无法实现完整特征值的覆盖，此时属于严重的数据样本分布不均衡。

样本分布不均衡将导致样本量少的分类所包含的特征过少，并很难从中提取规律；即使得到分类模型，也容易产生过度依赖于有限的数据
样本而导致过拟合的问题，当模型应用到新的数据上时，模型的准确性和健壮性将很差。
样本分布不均衡主要在于不同类别间的样本比例差异。以笔者的工作经验看，如果不同分类间的样本量差异达到超过10倍就需要引起警觉
并考虑处理该问题，超过20倍就一定要解决了。

解决样本不均衡的方法：
1. 通过过抽样和欠抽样解决样本不均衡
2. 通过正负样本的惩罚权重解决样本不均衡
3. 通过组合/集成方法解决样本不均衡
4. 通过特征选择解决样本不均衡
"""

import pandas as pd
from imblearn.over_sampling import SMOTE  # 过抽样处理库SMOTE
from imblearn.under_sampling import RandomUnderSampler  # 欠抽样处理库RandomUnderSampler
from sklearn.svm import SVC  # SVM中的分类算法SVC
from imblearn.ensemble import EasyEnsemble  # 简单集成方法EasyEnsemble


def data_imbalance_handle():
    # 导入数据文件
    df = pd.read_table('data2.txt', sep=' ', names=['col1', 'col2', 'col3', 'col4', 'col5', 'label'])  # 读取数据文件
    x = df.iloc[:, :-1]  # 切片，得到输入x
    y = df.iloc[:, -1]  # 切片，得到标签y
    groupby_data_orgianl = df.groupby('label').count()  # 对label做分类汇总
    print (groupby_data_orgianl)  # 打印输出原始数据集样本分类分布
    print "="*20
    # 使用SMOTE方法进行过抽样处理
    model_smote = SMOTE()  # 建立SMOTE模型对象
    x_smote_resampled, y_smote_resampled = model_smote.fit_sample(x, y)  # 输入数据并作过抽样处理
    x_smote_resampled = pd.DataFrame(x_smote_resampled,
                                     columns=['col1', 'col2', 'col3', 'col4', 'col5'])  # 将数据转换为数据框并命名列名
    y_smote_resampled = pd.DataFrame(y_smote_resampled, columns=['label'])  # 将数据转换为数据框并命名列名
    smote_resampled = pd.concat([x_smote_resampled, y_smote_resampled], axis=1)  # 按列合并数据框
    groupby_data_smote = smote_resampled.groupby('label').count()  # 对label做分类汇总
    print (groupby_data_smote)  # 打印输出经过SMOTE处理后的数据集样本分类分布
    print "=" * 20
    # 使用RandomUnderSampler方法进行欠抽样处理
    model_RandomUnderSampler = RandomUnderSampler()  # 建立RandomUnderSampler模型对象
    x_RandomUnderSampler_resampled, y_RandomUnderSampler_resampled = model_RandomUnderSampler.fit_sample(x,
                                                                                                         y)  # 输入数据并作欠抽样处理
    x_RandomUnderSampler_resampled = pd.DataFrame(x_RandomUnderSampler_resampled,
                                                  columns=['col1', 'col2', 'col3', 'col4', 'col5'])  # 将数据转换为数据框并命名列名
    y_RandomUnderSampler_resampled = pd.DataFrame(y_RandomUnderSampler_resampled, columns=['label'])  # 将数据转换为数据框并命名列名
    RandomUnderSampler_resampled = pd.concat([x_RandomUnderSampler_resampled, y_RandomUnderSampler_resampled],
                                             axis=1)  # 按列合并数据框
    groupby_data_RandomUnderSampler = RandomUnderSampler_resampled.groupby('label').count()  # 对label做分类汇总
    print (groupby_data_RandomUnderSampler)  # 打印输出经过RandomUnderSampler处理后的数据集样本分类分布
    print "=" * 20
    # 使用SVM的权重调节处理不均衡样本
    model_svm = SVC(class_weight='balanced')  # 创建SVC模型对象并指定类别权重
    model_svm.fit(x, y)  # 输入x和y并训练模型

    # 使用集成方法EasyEnsemble处理不均衡样本
    model_EasyEnsemble = EasyEnsemble()  # 建立EasyEnsemble模型对象
    x_EasyEnsemble_resampled, y_EasyEnsemble_resampled = model_EasyEnsemble.fit_sample(x, y)  # 输入数据并应用集成方法处理
    print (x_EasyEnsemble_resampled.shape)  # 打印输出集成方法处理后的x样本集概况
    print (y_EasyEnsemble_resampled.shape)  # 打印输出集成方法处理后的y标签集概况
    print "=" * 20
    # 抽取其中一份数据做审查
    index_num = 1  # 设置抽样样本集索引
    x_EasyEnsemble_resampled_t = pd.DataFrame(x_EasyEnsemble_resampled[index_num],
                                              columns=['col1', 'col2', 'col3', 'col4', 'col5'])  # 将数据转换为数据框并命名列名
    y_EasyEnsemble_resampled_t = pd.DataFrame(y_EasyEnsemble_resampled[index_num], columns=['label'])  # 将数据转换为数据框并命名列名
    EasyEnsemble_resampled = pd.concat([x_EasyEnsemble_resampled_t, y_EasyEnsemble_resampled_t], axis=1)  # 按列合并数据框
    groupby_data_EasyEnsemble = EasyEnsemble_resampled.groupby('label').count()  # 对label做分类汇总
    print (groupby_data_EasyEnsemble)  # 打印输出经过EasyEnsemble处理后的数据集样本分类分布

if __name__ == '__main__':
    data_imbalance_handle()