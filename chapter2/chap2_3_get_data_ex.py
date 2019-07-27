# coding:utf-8
"""
@file: chap2_3_get_data_ex.py.py
@time: 7/27/2019 10:57 AM
@contact: dabuwang
@desc: 内容延伸：读取非结构化网页、文本、图像、视频、语音
"""


def get_data_from_web():
    """
    skip, get http_web_page by requests
    """
    pass


def get_data_from_nonformat_text():
    """
    need code to special aim, "traffic_log_for_dataivy" is an example about non-format txt.
    """
    pass


def get_data_from_jpg():
    """
    there are 2ways: PIL, opencsv
    """
    file = 'cat.jpg'

    # # way 1: use PIL
    # from PIL import Image
    # img = Image.open(file)
    # # img.show()
    # print ('img format: ', img.format)  # 打印图像格式
    # print ('img size: ', img.size)  # 打印图像尺寸
    # print ('img mode: ', img.mode)  # 打印图像色彩模式
    #
    # img_gray = img.convert('L')  # 转换为灰度模式
    # img_gray.show()  # 展示图像

    # way 2: use cv2
    import cv2 as cv
    img = cv.imread(file)

    cv.imshow('image', img)
    cv.waitKey(0)


def get_data_from_video():
    import cv2  # 导入库
    cap = cv2.VideoCapture("tree.avi")  # 获得视频对象
    status = cap.isOpened()  # 判断文件是否正确打开
    if status:  # 如果正确打开，则获得视频的属性信息
        frame_width = cap.get(3)  # 获得帧宽度
    frame_height = cap.get(4)  # 获得帧高度
    frame_count = cap.get(7)  # 获得总帧数
    frame_fps = cap.get(5)  # 获得帧速率
    print ('frame width: ', frame_width)  # 打印输出
    print ('frame height: ', frame_height)  # 打印输出
    print ('frame count: ', frame_count)  # 打印输出
    print ('frame fps: ', frame_fps)  # 打印输出
    success, frame = cap.read()  # 读取视频第一帧
    while success:  # 如果读取状态为True
        cv2.imshow('vidoe frame', frame)  # 展示帧图像
        success, frame = cap.read()  # 获取下一帧
        k = cv2.waitKey(1000 / int(frame_fps))  # 每次帧播放延迟一定时间，同时等待输入指令
        if k == 27:  # 如果等待期间检测到按键ESC
            break  # 退出循环

    cv2.destroyAllWindows()  # 关闭所有窗口
    cap.release()  # 释放视频文件对象


def get_data_from_audio():
    """
    1. 使用Python的audioop、aifc、wav等库
    2. 调用科大讯飞、百度语音等解决方案提供的API实现语音分析处理
    skip
    """
    pass


if __name__ == '__main__':
    # get_data_from_jpg()
    get_data_from_video()
