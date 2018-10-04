def format(arguments):
    available_args = ['help', 'cities', 'coords', 'iata', 'names', 'full']
    arguments = arguments[1::]
    for arg in arguments:
        print(arg[2::])
        if arg[2::] in available_args:
            arg = arg[2::]
        else: 
            raise ValueError('No such command "{}"'.format(arg[2::]))
