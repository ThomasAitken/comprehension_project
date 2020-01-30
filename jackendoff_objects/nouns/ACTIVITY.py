from .EVENT import Event

class Activity(Event):
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)