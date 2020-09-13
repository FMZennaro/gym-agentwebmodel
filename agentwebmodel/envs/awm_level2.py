
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np





class AWM_Lvl2_Env(gym.Env):
    """
    Description:
        The Agent Web Model server at level1.
    Observation: 
        Type: MultiBinary(n_files)
            0   non connected
            1   connected
    Actions:
        Type: Dict('command':Discrete(3),'targetfile':Discrete(n_files))
            Discrete(3):
                0    none
                1    read()
                2    deepread()
                3    search()
            Discrete(n_files)
                n    target file
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

    def __init__(self,A,B,flag):
        assert (A.shape[0] == A.shape[1]), 'The public links adjacency matrix of the files must be square'
        assert (B.shape[0] == B.shape[1]), 'The hidden links adjacency matrix of the files must be square'
        assert (A.shape[0] == B.shape[0]), 'The public links and the hidden links adjacency matrix must have the same shape'
        assert (flag >= A.shape[0]), 'The file with the flag is beyond the count of the files'
        assert (flag < 0), 'The file with the flag can not be negative'
        
        self.A = A.astype(np.bool)
        self.B = B.astype(np.bool)
        self.n_files = A.shape[0]
        self.flag = flag
                
        # Observation space
        self.observation_space = spaces.MultiBinary(self.n_files)
        
        # Action space
        self.action_space = spaces.Dict({
            "command":spaces.Discrete(4),
            "targetfile":spaces.Discrete(self.n_files)
            })
        
        self.seed()
        self.viewer = None
        self.steps_beyond_done = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.state = np.zeros(self.n_files,dtype=np.bool)
        self.state[0] = 1
        self.done = False
        return np.where(self.state==1)[0]
    
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        
        command = action['command']
        targetfile = action['targetfile']
        
        assert targetfile <= self.n_files, 'Target file non-existing'
        assert self.state[targetfile] == 1, 'Target file not known to the attacker'

        if(command == self.CMD_NONE):
            return None, -1, self.done, {'msg':'None'}
        
        elif(command == self.CMD_READ):
            self.state = np.logical_or(self.state,self.A[targetfile,:])
            return np.where(self.A[targetfile,:]==1)[0], -1, self.done, {'msg':'Files openly connected to file {0}'.format(targetfile)}
        
        elif(command == self.CMD_DEEPREAD):
            self.state = np.logical_or(self.state,self.B[targetfile,:])
            return np.where(self.B[targetfile,:]==1)[0], -1, self.done, {'msg':'Files implicitly connected to file {0}'.format(targetfile)}
        
        elif(command == self.CMD_SEARCH):
            if(targetfile==self.flag):
                self.done = True
                return True, 100, self.done, {'msg':'Flag found in file {0}'.format(targetfile)}
            else:
                return False, -1, self.done, {'msg':'No flag in file {0}'.format(targetfile)}
       
    def render(self, mode='human'):
        raise NotImplementedError
        
    def close(self):
        return
    
    

