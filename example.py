def example(any):
    return type(any)

print(example(True))

def sayMsg(msg):
    if isinstance(msg,(str)) == False:
        return "not is string!"
    else:
        return msg

print(sayMsg(True))