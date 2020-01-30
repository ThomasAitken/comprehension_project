#Named hurricanes, battles, wars, sports events, etc.

class Event(object):
    
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    
    def get_property(self, property: str):
        value = vars(self).get(property, "Unknown")
        return value