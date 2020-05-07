import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

tf.reset_default_graph()          # 将当前计算图重置

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# print(mnist.train.images.shape, mnist.train.labels.shape)  # 训练集数据的维度
# print(mnist.validation.labels[0:10, :])  # 验证集数据前10个样本的标签

# x_data = mnist.train.images[:300, :]
# y_data = mnist.train.labels[:300, :]
x_data = tf.placeholder(tf.float32, [None, 784], name='input')
y_data = tf.placeholder(tf.float32, [None, 10])
#
w = tf.Variable(tf.zeros([784, 10]))  # 网络权值
b = tf.Variable(tf.zeros([10]))       # 网络阈值
y = tf.nn.softmax(tf.matmul(x_data, w) + b, name='out')  # 网络输出值

init = tf.global_variables_initializer()
cross_entyopy = tf.reduce_mean(-tf.reduce_sum(y_data * tf.log(y), axis=1))  # 损失函数，交叉熵的公式
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entyopy)

saver = tf.train.Saver()   # 保存类

with tf.Session() as sess:
    sess.run(init)
    # for i in range(100):
    #     sess.run(train)
    #     acc = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_data, 1))
    #     acc = sess.run(acc)
    #     print(sum(acc)/len(acc))
    # 开始多批处理，注意先把上面的mnist的限制取消并设置占位符

    for i in range(1000):
        x_s, y_s = mnist.train.next_batch(300)
        # acc = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_data, axis=1))
        # acc = sess.run(acc, feed_dict={x_data:x_s, y_data: y_s})
        # print(sum(acc) / len(acc))
        if i%100 == 0:
            acc = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_data, axis=1))
            acc = sess.run(acc, feed_dict={x_data: x_s, y_data: y_s})
            print('the No.' + str(i) + ' time acc', sum(acc)/len(acc))
        sess.run(train, feed_dict={x_data: x_s, y_data: y_s})

    pre = sess.run(y, feed_dict={x_data: mnist.test.images})  # 将测试集样本放入训练后的网络

    acc = np.argmax(pre, axis=1) == np.argmax(mnist.test.labels, axis=1)  # 比较预测值和实际值
    acc_te = sum(acc) / len(acc)  # 测试集精度
    print('acc_te:', acc_te)

    saver.save(sess, 'temp/model')  # 保存模型
    print('save temp/model')



