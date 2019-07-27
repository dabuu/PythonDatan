# coding:utf-8
"""
@file: chap2_2_get_data.py
@time: 7/25/2019 10:49 PM
@contact: dabuwang
@desc:
how to get data from file, xls, mysql, MongoDB, and api?
- file:
1. file open
2. numpy load txt


"""


def get_data_from_file():
    """
    NA
    """

    # region file open
    """
    2 ways: open, io.open
    """
    # open(file, mode, buffering=)
    # import io
    # io.open(file, mode, encoding=)
    # endregion file open

    # region numpy open
    """
    3 ways: loadtxt, load, fromfile
    """
    # way 1:
    import numpy as np
    np_file_name = 'numpy_data.txt'
    data_np = np.loadtxt(np_file_name, dtype="float32", delimiter=' ')
    print data_np

    # way 2:
    # 先将自定义的数据 保存为npy数据文件
    np.save('load_data_dabu', np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    npy_file_name = 'load_data_dabu.npy'
    data_npy = np.load(npy_file_name)
    print data_npy

    # way 3:
    # reuse data: data_np
    to_file_name = 'binary_tofile'
    data_np.tofile(to_file_name)  # 将二维数据 写入二进制文件
    from_file_data = np.fromfile(to_file_name, dtype='float32')  # 从二进制文件读出数据，但数据形状信息丢失，无法还原出矩阵
    print from_file_data

    # endregion numpy open

    # region pandas open
    """
    使用Pandas的read_csv、read_fwf、read_table读取数据
    """
    import pandas as pd
    # way1 : read_csv
    csv_data = pd.read_csv("csv_data.csv", names=['col1', 'col2', 'col3', 'col4', 'col5'])
    print csv_data
    # way2 : read_fwf
    fwf_data = pd.read_fwf("fwf_data", widths=[5, 5, 5, 5], names=['col1', 'col2', 'col3', 'col4'])
    print fwf_data
    # way3 : read_table
    table_data = pd.read_table("table_data.txt", sep=';', names=['col1', 'col2', 'col3', 'col4', 'col5'])
    print table_data

    # endregion pandas open


def get_data_from_excel():
    import xlrd
    xlsx = xlrd.open_workbook('demo.xlsx')
    print ('All sheets: %s' % xlsx.sheet_names())
    print '=' * 20  # 内容分割

    # 查看sheet1的数据概况
    sheet1 = xlsx.sheets()[0]  # 获得第一张sheet，索引从0开始
    sheet1_name = sheet1.name  # 获得名称
    sheet1_cols = sheet1.ncols  # 获得列数
    sheet1_nrows = sheet1.nrows  # 获得行数
    print ('Sheet1 Name: %s\nSheet1 cols: %s\nSheet1 rows: %s') % (sheet1_name, sheet1_cols, sheet1_nrows)
    print ('=' * 20)  # 内容分割线
    # 查看sheet1的特定切片数据
    sheet1_nrows4 = sheet1.row_values(4)  # 获得第4行数据
    sheet1_cols2 = sheet1.col_values(2)  # 获得第2列数据
    cell23 = sheet1.row(2)[3].value  # 查看第3行第4列数据
    print ('Row 4: %s\nCol 2: %s\nCell 1: %s\n' % (sheet1_nrows4, sheet1_cols2, cell23))
    print ('=' * 20)  # 内容分割线
    # 查看sheet1的数据明细
    for i in range(sheet1_nrows):  # 逐行打印sheet1数据
        print (sheet1.row_values(i))


def get_data_from_mysql():
    """
    just connect to mysql db & execute sql cmd
    """
    pass


def get_data_from_mongdb():
    """
    need mongdb entity, just copy code
    :return:
    """

    from pymongo import MongoClient  # 导入库
    client = MongoClient()  # 建立连接
    client = MongoClient('10.66.202.134', 27017)  # 环境变量初始化
    db = client.test_py  # 选择test_py库
    orders = db.ordersets  # 选择orders集合
    terms = [{"user": "tony", "id": "31020", "age": "30", "products": ["215120", "245101", "128410"],
              "date": "2017-04-06"},
             {"user": "lucy", "id": "32210", "age": "29", "products": ["541001", "340740", "450111"],
              "date": "2017-04-06"}]  # 定义一条数据集合用于插入
    orders.insert_many(terms)  # 插入数据
    print (orders.find_one())  # 获取一文档数据
    print ('========================================')
    for i in orders.find():  # 获取所有文档数据并展示
        print (i)

    orders.find({"user": "lucy"})  # 所有数据，注意使用迭代方法查看数据
    orders.find_one({"user": "lucy"})  # 单条数据
    orders.find({"user": "lucy"}).sort("user")


def get_data_from_api():
    """
    skip,  get json | xml data from baidu map's API.s
    """
    pass

if __name__ == '__main__':
    # get_data_from_file()
    get_data_from_excel()
    ## get_data_from_mysql()
    ## get_data_from_mongdb()
    ## get_data_from_api()
