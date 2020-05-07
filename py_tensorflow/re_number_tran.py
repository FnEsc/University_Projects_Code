from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
tf.reset_default_graph()    # 重置计算图

sess = tf.Session()
saver = tf.train.import_meta_graph('temp/model.meta')   # 导入计算图
saver.restore(sess, 'temp/model')   # 将已保存模型参数放入当前会话（计算图）
graph = tf.get_default_graph()  # 获取当前计算图
x = graph.get_tensor_by_name('input:0')     # 通过名称获取tensor，网络输入节点
y = graph.get_tensor_by_name('out:0')       # 通过名称获取tensor，网络输出节点

res = sess.run(y, feed_dict={x: mnist.test.images})   # 调用模型，用已经训练完成的神经网去辨别测试集
sess.close()    # 关闭会话

acc_te = np.argmax(res, axis=1) == np.argmax(mnist.test.labels, axis=1)
acc_te = sum(acc_te) / len(acc_te)  # 测试集精度
print('acc_te:', acc_te)    # 得到的测试集精度应该和训练当时的一样


