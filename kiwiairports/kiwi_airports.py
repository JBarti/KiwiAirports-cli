"""kiwi_airports main application module

Contains the KiwiAirports class which implements the 
top level funcitonalities of the kiwi_airports-cli,
such as connecting each provided option to a parser.

Handles formating the output into a readable format
viable for later on processing.
"""
from sys import argv, exc_info
import requests
from terminaltables import AsciiTable
from options import *


class KiwiAirports:
    option_functions = {
        'help': help,
        'cities': cities,
        'iata': iata,
        'names': names,
        'lat': lat,
        'lon': lon,
        'full': 'defined in class'
    }

    airport_data = requests.get(
        'https://api.skypicker.com/locations?type=subentity&term=GB&location_types=airport'
    ).json()['locations']

    def run_commands(self, option_list):
        table_data = [[] for x in range(len(self.airport_data))]
        if 'help' in option_list:
            self.option_functions['help']()
        if 'full' in option_list:
            option_list = ['names', 'cities', 'iata', 'lat', 'lon']
        if not option_list:
            option_list = ['names', 'iata']
        if 'names' not in option_list:
            option_list.insert(0, 'names')
        for option in option_list:
            data = self.option_functions[option](self.airport_data)
            table_data[0].append(option.upper())
            for row_num in range(1, len(table_data)):
                table_data[row_num].append(data.pop(0))
        return table_data


if __name__ == '__main__':
    app = KiwiAirports()

    try:
        formated_options = format_opts(argv)
    except ValueError:
        print('{} {}'.format('ValueError:', exc_info()[1]))
        exit()

    output_data = app.run_commands(formated_options)
    output_table = AsciiTable(output_data)
    print(output_table.table)
