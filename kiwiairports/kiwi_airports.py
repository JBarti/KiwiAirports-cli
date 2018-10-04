from sys import argv
from terminaltables import AsciiTable
from arguments import format

class KiwiAirports:
    commands = {
        'help': 1,
        'cities': 1,
        'coords': 1,
        'iata': 1,
        'names': 1,
        'full': 1
    }

    def run_command(self, command_list):
        pass


if __name__ == '__main__':
    app = KiwiAirports()
    table_data = [
        ['heding1', 'heading2'],
        [10, 20],
        ['column2', 'column3']
    ]

    table = AsciiTable(table_data)
    print(table.table)
    try:
        format(argv)
    except ValueError:
        print(err)

