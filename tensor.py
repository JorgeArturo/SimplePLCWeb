
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import numpy as np

#Write a multiplication between two tensors with random values
A = tf.constant(np.random.randint(0,10,(3,3)))
B = tf.constant(np.random.randint(0,10,(3,3)))
print(tf.matmul(A,B))

#Create an example using linear regression using rando values for the input 
#and the output, and then train the model
X = tf.constant(np.random.randint(0,10,(10,2)))
Y = tf.constant(np.random.randint(0,10,(10,1)))
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X,Y,epochs=10)
#show the summary of the model
model.summary()
#do a validation of the model
model.predict(X)
#predict a new value
model.predict(tf.constant(np.random.randint(0,10,(1,2))))
