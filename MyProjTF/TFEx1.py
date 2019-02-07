import tensorflow as tf
g = tf.Graph()
output = 0

with g.as_default():
    w = tf.Variable([.3], tf.float32)
    b = tf.Variable([-0.3], tf.float32)
    x = tf.placeholder(tf.float32)

    y = w*x + b

with tf.Session(graph=g) as tfs:
    tf.global_variables_initializer().run()
    output = tfs.run(y, {x: [1, 2, 3, 4]})

print('Output: ', output)