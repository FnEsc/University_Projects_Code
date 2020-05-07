import tensorflow as tf
import cv2, os, re
import numpy as np

path = './testimages/'


def getimagesnames(path=path):
    imagesnames = []
    filenames = os.listdir(path)
    for i in filenames :
        if re.findall('^\d+\.jpg$', i) != []:
            imagesnames.append(i)
    return imagesnames


def predict(meta='./temp/model.meta', model='./temp/model', outName='out:0', dataName='input:0', path=path):
    '''
    将新图片实时放入已保存好的模型中进行测试
    :param meta: 已保存好的计算图文件
    :param model: 已保存好的模型文件
    :param outName: 网络输出的tensor名
    :param dataName: 网络输入的tensor名
    :param path: 待测试图片路径
    :return: 直接打印分类结果，无返回值
    '''

    tf.reset_default_graph()
    imagesnames = getimagesnames()
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(meta)  # 调用计算图文件
        saver.restore(sess, model)  # 调用模型
        graph = tf.get_default_graph()  # 获得计算图
        x_data = graph.get_tensor_by_name(dataName)     # 通过tensor名获取网络输入节点
        y = graph.get_tensor_by_name(outName)           # 通过tensor名获取网络输出节点
        for i in imagesnames:
            data = cv2.imread(path+i)[:, :, 0]/255  # 读入图片并进行归一化
            data = data.reshape([1, 28*28])         # 维度转换
            y_pre = sess.run(y, feed_dict={x_data: data})   # 将实时读入的图片放入模型中进行预测
            print('Image ' + i + ' is', np.argmax(y_pre))      # 打印结果


if __name__ == '__main__':
    predict()  # 预测


