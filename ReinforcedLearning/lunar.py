# conda install swig
# conda install swig # needed to build Box2D in the pip install
# pip install box2d-py # a repackaged version of pybox2d

import random
import gym
import matplotlib.pyplot as plt
#%matplotlib inline

env = gym.make('LunarLander-v2')

#env = gym.make('BipedalWalker-v2')

env.seed(23)

# Let's watch how an untrained agent moves around

state = env.reset()
#img = plt.imshow(env.render(mode='rgb_array'))
for j in range(4000):
	action = agent.act(state)
	#action = random.choice(range(4))
	env.render()
    #img.set_data(env.render(mode='rgb_array')) 
   # plt.axis('off')
  #  display.display(plt.gcf())
  #  display.clear_output(wait=True)
  	state, reward, done, _ = env.step(action)
    if done:
        break 
        
env.close()