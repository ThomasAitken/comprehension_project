class GenericEntity(object):

    #abstract can take 3 values: 1 = True, 0 = False, -1 = concrete and abstract possibilities
    #count/mass is just binary... bounded or unbounded.
    def __init__(self, abstract: int, count: bool):
        self.abstract=abstract
        self.count=count
