from thing import GenericEntity
from generic_functions import is_abstract, is_count

class time(GenericEntity):

    def __init__(self):
        #time is an abstract mass noun
        super().__init__(1, False)

# TimeInstance = time()
# print(is_abstract(TimeInstance))
# print(is_count(TimeInstance))

