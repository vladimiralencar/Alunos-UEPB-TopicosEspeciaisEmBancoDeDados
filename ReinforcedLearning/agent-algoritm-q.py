import numpy as np
import gym

env = gym.make('Taxi-v2') # FrozenLake-v0
env.reset()
env.render()

Q = np.zeros([env.observation_space.n, env.action_space.n])
G = 0
alpha = 618

#state, reward, done, info = env.step(env.action_space.sample())


for episode in range(1,1001):
    done = False
    G, reward = 0,0
    state = env.reset()
    while done != True:
            action = np.argmax(Q[state]) 
            state2, reward, done, info = env.step(action) 
            Q[state,action] += alpha * (reward + np.max(Q[state2]) - Q[state,action]) 
            G += reward
            state = state2   
    if episode % 50 == 0:
        print('Episode {} Total Reward: {}'.format(episode,G))


