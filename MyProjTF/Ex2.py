import tensorflow as tf
#sess = tf.Session()
myGraph = tf.Graph()
with myGraph.as_default():
    variable = tf.Variable(30, name = "navin")
    initialize = tf.global_variables_initializer()

with tf.Session(graph=myGraph) as sess:
    sess.run(initialize)
    print(sess.run(variable))