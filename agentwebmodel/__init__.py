from gym.envs.registration import register

register(
    id='awm_level1-v0',
    entry_point='agentwebmodel.envs:AWM_Lvl1_Env',
)
register(
    id='awm_level1-v1',
    entry_point='agentwebmodel.envs:AWM_Lvl1_Env_v1',
)
register(
    id='awm_level2-v0',
    entry_point='agentwebmodel.envs:AWM_Lvl2_Env',
)
register(
    id='awm_level2-v1',
    entry_point='agentwebmodel.envs:AWM_Lvl2_Env_v1',
)
register(
    id='awm_level3-v0',
    entry_point='agentwebmodel.envs:AWM_Lvl3_Env',
)
register(
    id='awm_level3-v1',
    entry_point='agentwebmodel.envs:AWM_Lvl3_Env_v1',
)
