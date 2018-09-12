import tensorflow as tf

m1 = tf.constant([[3, 3]])
m2 = tf.constant([[2],
                 [2]])

product = tf.matmul(m1, m2)

###methon1
sess = tf.Session()
result1 = sess.run(product)
print(result1)
sess.close()

###methon2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
