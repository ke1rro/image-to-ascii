
FILE_FORMATS = ['png', 'jpg', 'jpeg']


def get_file_format():
    for index, frmt in enumerate(FILE_FORMATS):
        print(f'{index + 1}: {frmt}')
    chosen_format = int(input('Choose file format '))
    return FILE_FORMATS[chosen_format - 1]
