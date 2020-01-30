#	Nationalities or religious or political groups.

class Norp(object):
    
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    
    def get_property(self, property: str):
        value = vars(self).get(property, "Unknown")
        return value