# function to write a string into a file
def write_string_to_file(string_data, file_path):
    """
    Writes a given string into a file specified by the file_path.
    If the file does not exist, it will be created.
    If the file exists, it will be overwritten.

    :param file_path: Path to the file where the string will be written.
    :param string_data: The string data to write into the file.
    """
    with open(file_path, 'w') as file:
        file.write(string_data)