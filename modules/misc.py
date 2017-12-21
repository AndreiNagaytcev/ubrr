import configparser
def read_properties(filename):
    config_parser = configparser.ConfigParser()
    config_parser.read(filename)
    return config_parser