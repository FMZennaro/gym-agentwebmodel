
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
    
    CMD_NONE = 0; CMD_READ = 1; CMD_DEEPREAD = 2; CMD_SEARCH = 3
    metadata = {'render.modes': ['human', 'ansi']}

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
    
    
class AWM_Lvl3_Env_v1(gym.Env):
    """
    Description:
        The Agent Web Model server at level1.
    Observation: 
        Type: MultiBinary(n_files)
            0   non connected
            1   connected
    Actions:
        Type: MultiDiscrete(command,targetfile,pname,pvalue)
            command: Discrete(3):
                0    none
                1    read()
                2    deepsearch()
                3    search()
            targetfile: Discrete(4)
                n    target file
            pname: Discrete(5)
                n    parameter name
            pvalue: Discrete(5)
                n    parameter value
    Reward: 
        -1 for each action, +100 for capturing the flag.
    Starting State:
        A single known file (file 0,index.html).
    Episode Termination:
        Flag captured.
    """
    
    CMD_NONE = 0; CMD_READ = 1; CMD_DEEPREAD = 2; CMD_SEARCH = 3
    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self):
        
        self.n_files = 4
        self.n_pnames = 5
        self.n_pvalues = 5
        
        self.flag = np.random.randint(self.n_files)
        self.state = np.zeros(self.n_files,dtype=np.bool)
        self.state[0] = 1
        self.done = False
        
        # Observation space
        self.observation_space = spaces.MultiBinary(self.n_files)
        
        # Action space
        self.action_space = spaces.MultiDiscrete([4,self.n_files,self.n_pnames,self.n_pvalues])
        
        self.seed()
        self.viewer = None
        self.steps_beyond_done = None
        
    def webserver(self,action):        
        command = action[0]
        targetfile = action[1]
        pname = action[2]
        pvalue = action[3]

        if(self.state[targetfile] == 0):
            return self.state, -1, self.done, {'msg':'Targetfile unreachable'}
        
        if(command==0): 
            return self.state,-1,self.done,{'msg':'None action'}

        elif(command==1):
            if(targetfile==0):
                if(pname==3 and pvalue==2): 
                    self.state[3] = 1
                    return self.state,-1,self.done,{'msg':'Read action'}
                else:
                    self.state[1] = 1
                    self.state[2] = 1
                    return self.state,-1,self.done,{'msg':'Read action'}
            elif(targetfile==1): 
                return self.state,-1,self.done,{'msg':'Read action'}
            elif(targetfile==2): 
                return self.state,-1,self.done,{'msg':'Read action'}
            elif(targetfile==3): 
                return self.state,-1,self.done,{'msg':'Read action'}

        elif(command==2): 
            return self.state,-1,self.done,{'msg':'Deepread action'}

        elif(command==3):
            if(targetfile==self.flag):
                if(pname==1 and pvalue==1): 
                    self.done = True
                    return self.state,100,self.done,{'msg':'Flag retrieved'}
                else: 
                    return self.state,-1,self.done,{'msg':'No flag'}
            else: 
                return self.state,-1,self.done,{'msg':'No flag'}

        else: 
            return self.state,-1,self.done,{'msg':'Wrong command'}

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.flag = np.random.randint(self.n_files)
        self.state = np.zeros(self.n_files,dtype=np.bool)
        self.state[0] = 1
        self.done = False
        return self.state
    
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        
        return self.webserver(action)
       
    def render(self, mode='human'):
        raise NotImplementedError
        
    def close(self):
        return
    
    

