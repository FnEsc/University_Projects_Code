from sklearn.datasets import load_iris
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

iris = load_iris()
target = tf.one_hot(iris.target, 3)

with tf.Session() as sess:
    target = sess.run(target)

x_tr, x_te, y_tr, y_te = train_test_split(np.float32(iris.data), np.float32(target)), 2, 3, 4

# 待完善

