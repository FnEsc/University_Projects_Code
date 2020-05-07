# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
# mnist.train.images        # 训练集图片的灰度值
# mnist.train.images.shape
# mnist.train.labels.shape
#
# mnist.test.images.shape   # 测试集图片的灰度值
#
# # real: 0  [1,  0,  0,  0,0,0,0,0,0,0]
# # p1  : 1  [0.1,0.5,0.4,0,0,0,0,0,0,0]
# # p2  : 2  [0.5,0.1,0.4,0,0,0,0,0,0,0]
#
# # from PIL import Image
# # import numpy as np
# # img = Image.open('0.jpg')
# # data = np.asarray(img)
# # data.shape

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
tf.reset_default_graph()          # 将当前计算图重置
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
x_data = tf.placeholder(tf.float32, [None, 784], name='input')
y_data = tf.placeholder(tf.float32, [None, 10])

w = tf.Variable(tf.zeros([784, 10]))   # 网络权值
b = tf.Variable(tf.zeros([10]))        # 网络阈值
y = tf.nn.softmax(tf.matmul(x_data, w) + b, name='out')   # 网络输出值

init = tf.global_variables_initializer()
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_data * tf.log(y), axis=1))   # 损失函数
optimizer = tf.train.GradientDescentOptimizer(0.02)
train = optimizer.minimize(cross_entropy)
saver = tf.train.Saver()   # 保存类
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        x_s, y_s = mnist.train.next_batch(300)
        if i%100 == 0:
            acc = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_data, axis=1))
            acc = sess.run(acc, feed_dict={x_data:x_s, y_data:y_s})
            print(i,' step train acc: ',sum(acc)/len(acc))
        sess.run(train, feed_dict={x_data: x_s, y_data: y_s})
    pre = sess.run(y, feed_dict={x_data: mnist.test.images})           # 将测试集样本放入训练后的网络

    acc = np.argmax(pre, axis=1) == np.argmax(mnist.test.labels, axis=1)  # 比较预测值和实际值
    acc_te = sum(acc)/len(acc)      # 测试集精度
    saver.save(sess, 'temp/model')  # 保存模型



