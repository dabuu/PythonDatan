# coding:utf-8
"""
@file: chap3_5_data_in_conflict.py
@time: 7/30/2019 10:40 PM
@contact: dabuwang
@desc:
## 为什么会出现多数据源的冲突
1.内部工具与第三方工具数据冲突
对比指标不同,测量的时机不同,网络丢包的问题,去重机制的问题,用户中途退出的问题,页面跟踪加载问题,动机导致的数据夸大
2.内部同一个业务主体的同一类数据工具的数据测量冲突
指标定义不同,采集逻辑不同,系统过滤规则不同,更新时间不同,监测位置不同
3.内部同一个业务主体的不同数据工具的数据测量冲突
订单来源差异, 特殊商品订单跟踪,订单状态差异,数据同步问题,内部系统拆单问题

## 如何应对多数据源的冲突问题, 关注：差异性，稳定性。
1. 消除冲突并形成一份唯一数据
2. 不消除冲突也不作任何处理
3. 不消除冲突但是使用全部冲突数据

"""