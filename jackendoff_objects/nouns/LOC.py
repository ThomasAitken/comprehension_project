#Non-GPE locations, mountain ranges, bodies of water.

class Loc(object):
    
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    
    def get_property(self, property: str):
        value = vars(self).get(property, "Unknown")
        return value
