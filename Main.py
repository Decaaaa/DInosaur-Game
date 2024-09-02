import numpy as np
#from tensorflow import keras
from keras.models import Sequential 
from keras.layers import Dense, Flatten 
from keras.optimizers.legacy import Adam

from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy

import gym_dino
import gym 

#import time
import pyautogui

def build_model(states, actions):
    model = Sequential()
    #model.add(Flatten(input_shape = (86, 1760, s tates)))
    model.add(Flatten(input_shape = (1, states)))
    #model.add(Dense(86*1760, input_shape=(86,1760,1), activation = 'relu'))
    #model.add(Dense(600*86, input_dim=600*86, activation='relu'))
    model.add(Dense(24, activation = 'relu')) 
    model.add(Dense(24, activation = 'relu'))
    model.add(Dense(actions, activation = 'tanh'))
    return model

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory = memory, policy = policy, 
                   nb_actions = actions, nb_steps_warmup = 100) # , target_model_updates = 1e-2)
    return dqn

env = gym.make('dino-v0')
model = build_model(4, 2)
dqn = build_agent(model, 2)
dqn.compile(Adam(learning_rate = 1e-3), metrics = ['mae'])
pyautogui.press("up")
dqn.fit(env, nb_steps = 50000, visualize = False, verbose = 1)
dqn.save_weights('dqn_weight.h5f', overwrite = True)
#dqn.load_weights('dqn_weight.h5f')
 #_ = dqn.test(env, nb_episodes = 5, visualize = False)
