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
    np.save('load_data_dabu', np.array([[1,2,3],[4,5,6],[7,8,9]]))

    npy_file_name = 'load_data_dabu.npy'
    data_npy = np.load(npy_file_name)
    print data_npy

    # way 3:
    # reuse data: data_np
    to_file_name = 'binary_tofile'
    data_np.tofile(to_file_name)    # 将二维数据 写入二进制文件
    from_file_data = np.fromfile(to_file_name, dtype='float32') # 从二进制文件读出数据，但数据形状信息丢失，无法还原出矩阵
    print from_file_data

    # endregion numpy open

    pass

    # region file open
    # endregion file open

if __name__ == '__main__':
    get_data_from_file()