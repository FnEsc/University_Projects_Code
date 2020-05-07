import cv2
import numpy as np
import tensorflow as tf

img = cv2.imread('testimages/2.jpg')
img = cv2.resize(img, (64, 64))
img = np.float32(np.reshape(img, (1, 64, 64, 3)) / 255)
w0 = tf.Variable(tf.random_normal([5, 5, 3, 32]))  # 32个filter

conv1 = tf.nn.conv2d(img, w0, strides=[1, 1, 1, 1], padding='SAME')  # strides是步长，1批次图片的数量、4颜色通道，2、3是步长的大小
pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # ksize是池化块大小，取池化的最大值

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    res = sess.run(pool1)

data = res[0, :, :, 31]  # 目前只训练了一张，所以取第0张照片中用第32个filter池化后的照片
cv2.imwrite('test.jpg', data*255)





