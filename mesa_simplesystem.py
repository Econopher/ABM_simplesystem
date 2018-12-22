from mesa import Agent, Model
from mesa.time import RandomActivation
# from mesa import space
import numpy as np
import matplotlib.pyplot as plt
import random


class MoneyAgent(Agent):
    def __init__(self, uniue_id, model):
        super().__init__(uniue_id, model)
        # create a list of wealth distribution_of_wealth of agents
        distribution_of_wealth = [i for i in range(100)]
        # scatter the wealth between agents randomly
        self.wealth = np.random.choice(distribution_of_wealth, size=None,
                                       p=None)

    def step(self):
        if self.wealth == 0:
            return
        else:
            other_agent = random.choice(self.model.schedule.agents)
            # creat the trade range between agents
            trade_value = [i for i in range(10)]

            if self.wealth <= 50:
                np.random.seed(123)
                prob_poor_agents = [0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0, 0]
                other_agent.wealth += np.random.choice(trade_value, size=1,
                                                       p=prob_poor_agents)
                self.wealth -= np.random.choice(trade_value)
            else:
                np.random.seed(124)
                prob_rich_agents = [0, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.3]
                other_agent.wealth += np.random.choice(trade_value, size=1,
                                                       p=prob_rich_agents)
                self.wealth -= np.random.choice(trade_value)


class MoneyModel(Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()


model = MoneyModel(10)
for i in range(10):
    model.step()


agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)
plt.show()
