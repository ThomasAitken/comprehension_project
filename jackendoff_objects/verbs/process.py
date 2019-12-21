class Process(object):

    #'impact' refers to world-changing facet of actions... Some actions are merely responses/dispositions: "I love", "I am impressed". Nothing changes, impact=False
    def __init__(self, impact: bool):
        self.impact = impact
