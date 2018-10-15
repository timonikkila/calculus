from exceptions import InvalidParam

def calculate(query):
    try:
        return eval(query)
    except:
        raise InvalidParam("Could not parse query \"%s\"" % (query))
