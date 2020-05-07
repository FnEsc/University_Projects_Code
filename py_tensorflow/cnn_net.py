import tensorflow as tf
'''
CnnNet 类
该类主要实现四个方面的方法：
1.核心函数定义；
2.网络结构搭建；
3.模型训练；
4.模型预测。
基本遵照先后顺序进行编排。
'''


def weightVariable(self,shape):     #权值数组W
    return tf.Variable(tf.random_normal(shape, stddev=0.1))  # 标准差

# def biasVariable(self,shape):       #偏置项数组b
#
# def conv2d(self,x, W):     #卷积
#
# def maxPool(self,x):       #max池化
#
# def dropout(self,x,keep):  #随机让某些权重不更新，保持某个数

def cnnLayer(self):
    """
    cnn神经网络结构
    :return:网络输出值
    """
    #===第一次卷积====

    #===第二次卷积====

    #===第三次卷积====

    #===全连接层====

    #===全连接层====


def cnnTrain(self,maxiter=1000,accu=0.99,batch_size=100):
    """
    依据训练样本的模型输出与样本实际值进行模型训练
    :param maxiter: 最大迭代次数
    :param accu: 精度阈值，当训练精度大于accu时则停止训练
    :param batch_size: 每轮训练的样本数
    :return: 无返回，但是当模型精度满足要求后会将模型保存
    """

    #比较标签是否相等，再求的所有数的平均值，tf.cast(强制转换类型)
    #每次取batch_size张图片
    #正式训练
    #获取训练精度
    #保存模型

def predict(self,test_x=test_x):
    """
    预测函数，导入已训练好的模型后再将新样本数据放入，进行模型预测
    :param test_x: 测试样本的自变量
    :return: 模型对测试样本的预测结果
    1: 预测结果（数字标签：0,1,2,3,4,5,...）
    pre: 样本属于各类别的概率，形如：[[0.1, 0.1, 0.0, 0.0, 0.0, 0.8]]
    """
    #网络输出
    #启动模型保存类Saver
    #调用之前保存的模型
    #获取计算图
    #通过tensor的名称获取相应tensor，注意到底是 x_data 还是x_data_1
    #放入测试集样本
