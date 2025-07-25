import os

def get_file_path(file_name):
    return os.path.join(os.getcwd(), 'myfile', file_name)

def get_string_from_file(file_name):
    try:
        with open(get_file_path(file_name), 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: The file {file_name} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

def write_string_to_file(file_name, str):
    try:
        with open(get_file_path(file_name), 'w') as file:
            for char in str:
                file.write(char)
    except FileNotFoundError:
        print(f'Error: The file {file_name} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')