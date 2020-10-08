import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf 
from collections import deque
import random

class AiTrader:

    model : object = None

    def __init__(self, state_size, action_space=3, model_name='AITrader'):
        self.state_size = state_size
        self.action_space = action_space
        self.memory = deque(maxlen=2000)
        self.inventory = []
        self.model_name = model_name
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_final = 0.01
        self.epsilon_decay = 0.995

    def hook(self):

    def model_builder(self):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(units=32, activation='relu', input_dim=self.state_size))
        model.add(tf.keras.layers.Dense(units=64, activation='relu'))
        model.add(tf.keras.layers.Dense(units=128, activation='relu'))
        model.add(tf.keras.layers.Dense(units=self.action_space, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=0.001))
        self.model = model
    
    def batch_model(self,batch_size): # 샘플만 뽑아 쓰는거야
        batch = []
        for i in range(len(self.memory) - batch_size + 1, len(self.memory)):
            batch.append(self.memory[i])
        for state, action, reward, next_state, done in batch:
            reward = reward
            if not done:
                reward = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target = self.model.predict(state)
            target[0][action] = reward
            self.model.fit(state, target, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_final:
            self.epsilon *= self.epsilon_decay

    def trade(self,state):
        if random.random() <= self.epsilon:
            return random.randrange(self.action_space)
        actions = self.model.predict(state)
        return np.argmax(actions[0])

    def create_sample(self):


    def eval_model(self):

if __name__ == '__main__':
    ait = AiTrader()
    ait.hook()
    