# import tensorflow as tf
# # 定义计算/计算图
# a = tf.constant([[1.],[2]])
# b = tf.constant([[3],[4]],dtype=tf.float64)
# res = a+b
# print(res)
#
# # 构建会话，执行计算
# sess = tf.Session()
# res1 = sess.run(res)
# sess.close()
# print(res1)
# [4,6]

# 任务一：拟合三维平面
import numpy as np
import tensorflow as tf

# print('hello world')
# 1. 利用Numpy生成100个样本点
data = np.load('line_fit_data.npy')
# 2. 构造一个线性模型
x_data = np.float32(data[:, 0:2])
y_data = np.float32(data[:, 2:])
w = tf.Variable(tf.zeros([2, 1]))
bias = tf.Variable(tf.zeros([1]))
y = tf.matmul(x_data, w) + bias   # 模型输出值

# 3. 最小化方差
loss = tf.reduce_mean(tf.square(y_data-y))
optimizer = tf.train.GradientDescentOptimizer(0.15)
train = optimizer.minimize(loss)
# 4. 初始化变量
init = tf.global_variables_initializer()
# 5. 启动会话
sess = tf.Session()
sess.run(init)
for i in range(100):
    y1 = sess.run(y)
    w1, bias1 = sess.run([w, bias])
    print(i, sess.run(loss), w1.T, bias1)
    sess.run(train)  # 6. 拟合平面(开始训练)
sess.close()

# y = 0.103*x1 + 0.197*x2 + 0.300

# from sklearn.linear_model import LinearRegression
# model = LinearRegression().fit(x_data,y_data)
# model.coef_
