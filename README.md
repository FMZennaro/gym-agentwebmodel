# gym-agentwebmodel
Implementation of Agent Web Model for OpenAI gym

### Requirements
The following code requires *numpy* and *OpenAI gym*; *networkx* is not required, but recommended.

### Installation
Clone this git and run `pip install -e gym-agentwebmodel` to make this environment available to *OpenAI gym*.

### Usage
First, import *numpy*, *OpenAI gym* and *gym-agentwebmodel*:

```python
import numpy as np
import gym
import agentwebmodel
```
Then, you can simply instantiate a new environment and start using it:
```python
env = gym.make('awm_level1-v0',A=np.ones((2,2)),flagfile=1)
```

For more details on the interface of the environment, check *Levels.md*.

For more example on how to use the environment, see *AWMLevel1-Example.ipynb*, *AWMLevel2-Example.ipynb*, and *AWMLevel3-Example.ipynb*.

### Reference
\[1\] Erdodi, L. and Zennaro, F.M., 2020. The Agent Web Model--Modelling web hacking for reinforcement learning. arXiv preprint arXiv:2009.11274.
