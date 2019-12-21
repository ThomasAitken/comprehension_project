def is_abstract(object_x):
    if object_x.abstract == 1:
        return "True"
    elif object_x.abstract == 0:
        return "False"
    else:
        return "Both abstract and concrete meanings"

def is_count(object_x):
    if object_x.count:
        return "True"
    else:
        return "False"