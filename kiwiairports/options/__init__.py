"""kiwi_airport data parsing package

This package provides functions for parsing
json data retrieved by Kiwi's skypicker api.
The funcitons are suited for the kiwi_airport-cli
created for application at the Kiwi Python weekend program.
"""
from .help import help
from .cities import cities
from .iata import iata
from .coords import lat, lon
from .names import names


def format_opts(options):
    """Console line option parser

    Checks if the options passed to the application.
    Removes duplicate options.
    Removes the double dashh (--option) before the option parameter.

    Args:
        options -- sys.argv from kiwi_airports.py (list of all sent options)

    Raises:
        ValueError -- in case of an invalid option the function
                      raises a ValueErrror

    Returns:
        list -- formated options passed to the funciton
    """

    available_opts = ['help', 'cities', 'coords', 'iata', 'names', 'full']
    options = options[1::]
    formated_options = []
    for opt in options:
        if opt[2::] in available_opts:
            if opt[2::] == 'coords':
                formated_options.append('lat')
                formated_options.append('lon')
            else:
                formated_options.append(opt[2::])
        else:
            raise ValueError('No such command "{}"'.format(opt[2::]))
    return list(set(formated_options))
