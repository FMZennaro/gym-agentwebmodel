
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np





class AWM_Lvl3_Env(gym.Env):
    """
    Description:
        The Agent Web Model server at level1.
    Observation: 
        Type: MultiBinary(n_files)
            0   non connected
            1   connected
    Actions:
        Type: Dict('command':Discrete(3),'targetfile':Discrete(n_files),'pname':Discrete(n_pnames),'pvalue':Discrete(n_pvalues))
            Discrete(3):
                0    none
                1    read()
                2    deepread()
                3    search()
            Discrete(n_files)
                n    target file
            Discrete(n_pnames)
                n    parameter name
            Discrete(n_pvalue)
                n    parameter value
    Reward: 
        -1 for each action, +100 for capturing the flag.
    Starting State:
        A single known file (file 0,index.html).
    Episode Termination:
        Flag captured.
    """
    
    metadata = {'render.modes': ['human', 'ansi']}
    
    CMD_NONE = 0
    CMD_READ = 1
    CMD_DEEPREAD = 2
    CMD_SEARCH = 3

    def __init__(self,n_files,n_pnames,n_pvalues,webserver):
        
        self.n_files = n_files
        self.n_pnames = n_pnames
        self.n_pvalues = n_pvalues
        
        self.webserver = webserver
                
        # Observation space
        self.observation_space = spaces.MultiBinary(self.n_files)
        
        # Action space
        self.action_space = spaces.Dict({
            "command":spaces.Discrete(4),
            "targetfile":spaces.Discrete(self.n_files),
            "pname":spaces.Discrete(self.n_pnames),
            "pvalue":spaces.Discrete(self.n_pvalues)
            })
        
        self.seed()
        self.viewer = None
        self.steps_beyond_done = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.done = False
        return [0]
    
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        
        observation,reward,done,msg = self.webserver(action)
        self.done = done
        
        return observation,reward,done,msg
       
    def render(self, mode='human'):
        raise NotImplementedError
        
    def close(self):
        return
    
    

