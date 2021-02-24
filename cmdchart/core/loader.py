"""Loads data that will be transposed/transformed.
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"


def loader(data, value_slice, chart_type='bar', marker='X'):
    """Accept data and return chart in array

    args:
        data (dict): { "str": int, "str2": int2}
        value_slice (int): Break down value for chart

    kwargs:
        chart_type (str): bar

    return (list): chart list array
    """
    max_value = 0

    # Get maximum value
    for value in data.values():
        if value > max_value:
            max_value = value
    
    num_of_slices = (max_value)/value_slice

    y_axis = []
    for i in range(1, int(num_of_slices)+1):
        y_axis.insert(0, value_slice*i)

    x_axis = []
    for key in data.keys():
        x_axis.append(key)

    # Replace actual value for graph value
    for key, value in data.items():
        height = int(value / value_slice)
        data[key] = height

    x_axis_spacing = get_spacing(x_axis)

    # Build chart data array
    data_rows = []
    for num, value in enumerate(y_axis):
        data_row = []
        for col in data.values():
            if num+1 <= col:
                data_row.append('{}'.format(_add_char(x_axis_spacing, char=marker)))
            else:
                data_row.append('{}'.format(_add_char(x_axis_spacing)))
        data_rows.insert(0, data_row)

    chart_str = build_chart(y_axis, x_axis, data_rows)

    print(chart_str)

def build_chart(y_axis, x_axis, data_array, data_buffer=1, y_axis_buffer=1):
    final_str = ''

    # Get maximum length for x & y axis names
    y_axis_spacing = get_spacing(y_axis)
    x_axis_spacing = get_spacing(x_axis)

    # Loop through y_axis names and data_array
    for num in range(len((y_axis))):
        row_str = ''
        
        if len(str(y_axis[num])) < y_axis_spacing:
            space = y_axis_spacing - len(str(y_axis[num]))
            row_str += _add_char(space)

        row_str += '{}{}|'.format(y_axis[num], _add_char(y_axis_buffer))
        
        for value in data_array[num]:
            row_str += '{}{}{}'.format(_add_char(data_buffer), value, _add_char(data_buffer))

        row_str += '\n'

        final_str += row_str
    
    # Add break line before x axis names
    final_str += '{}{}\n'.format(_add_char(y_axis_spacing+2), _add_char((x_axis_spacing+data_buffer*2)*len(x_axis), char='-'))
    
    # Loop through x axis names
    row_str = ''
    final_str += _add_char(y_axis_spacing+2)
    for name in x_axis:
        row_str += '{}{}{}'.format(_add_char(data_buffer), name, _add_char(data_buffer))

    final_str += row_str

    return final_str


def get_spacing(check_list):
    column_width = 0
    for item in check_list:
        if len(str(item)) > column_width:
            column_width = len(str(item))
    return column_width


def _add_char(num, char=' '):
    """Creates a string value give a number and character.
    args:
        num (int): Amount to repeat character
    kwargs:
        char (str): Character value to lopp
    Returns (str): Iterated string value for given character
    """
    string = ''
    for i in range(num):
        string += char
    return string

if __name__ == '__main__':
    data = {
        "Jan": 100,
        "Feb": 200,
        "Mar": 100,
        "Apr": 500,
        "May": 400,
        "Jun": 300,
        "Jul": 200,
        "Aug": 100,
        "Sep": 100,
        "Oct": 100,
        "Nov": 900,
        "Dec": 800
    }

    loader(data, 100, chart_type='bar')