import os
import tensorflow as tf
merged = tf.summary.merge_all(key='summaries')
if not os.path.exists('tensorboard_logs/'):
    os.makedirs('tensorboard_logs/')

my_writer = tf.summary.FileWriter('C:\Users\lenovo\Documents\tensorboard\', sess.graph)

def TB(cleanup=False):
    import webbrowser
    webbrowser.open('http://127.0.1.1:6006')
    !tensorboard --logdir = 'C:\Users\lenovo\Documents\tensorboard\'

    if cleanup:
        !rm -R tensorboard/

TB(1)