import sys
sys.path.append('/home/crastollgorton/comprehension_project')

from jackendoff_objects.nouns.EVENT import Event
from jackendoff_objects.nouns.PERSON import Person

class Action(Event):

    #'impact' refers to world-changing facet of actions... Some actions are merely responses/dispositions: "I love", "I am impressed". Nothing changes, impact=False
    #kwargs because could be more than one agent or other living or non-living participants
    def __init__(self, impact: bool, agent: Person, **kwargs):
        # self.impact = impact
        self.agent = agent

    def update_states(self, agent: Person, **kwargs):

    

    

