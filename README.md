# gym-agentwebmodel
Implementation of Agent Web Model for OpenAI gym.

### Requirements
The following code requires *numpy* and [OpenAI gym](https://github.com/openai/gym); [stable-baselines](https://github.com/hill-a/stable-baselines) (together with [tensorflow](https://github.com/tensorflow/tensorflow) and [tensorboard](https://github.com/tensorflow/tensorboard)) is used to train reinforcement learning agents; [networkx](https://networkx.org/documentation/stable/tutorial.html) is not required, but recommended.

### Installation
Clone this git and run `pip install -e gym-agentwebmodel` to make this environment available to *OpenAI gym*.

### Content
The *gym-agentwebmodel* contains the implementation of the first three levels of hacking challenges described in [1].

For each level $x$ we provide:
- *AWM_Lvl$x$_Env*: this class provides a conceptual implementation of the first level of the Agent Web Model. This implementation favors interpretabilty, clarity and versatility. Level parameters may be set at instantiation time, and action and responsed are verbose. We recommend its use for exploring and understanding the problem, and for custom RL applications. The use of this class is exemplified in the *AWMLevel$x$-Example.ipynb* files.

- *AWM_Lvl$x$_Env_v1*: this class provides a practical implementation of the first level of the Agent Web Model. This implementation favors interoperability, hard-coding and learning. A specific choice of level parameters is encoded in the class, and action and responsed are reduced to integers. We recommend its use for training standard RL agents, such as *stable-baselines* agents. The use of this class is exemplified in the *AWMLevel$x$-Learning.ipynb* files.


### Use
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

For more examples on how to use the basic environment, see *AWMLevel1-Example.ipynb*, *AWMLevel2-Example.ipynb*, and *AWMLevel3-Example.ipynb*. For more examples on how to use the learning environment, see *AWMLevel1-Learning.ipynb*, *AWMLevel2-Learning.ipynb*, and *AWMLevel3-Learning.ipynb*.

### References
\[1\] Erdodi, L. and Zennaro, F.M., 2020. The Agent Web Model--Modelling web hacking for reinforcement learning. arXiv preprint arXiv:2009.11274.
