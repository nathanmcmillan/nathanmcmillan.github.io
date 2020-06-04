directory = 'code'


def compiler(name):
    with open(directory + '/' + name, 'r') as file:
        source = file.readlines()
    return ''.join(source)
