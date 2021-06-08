import os
import argparse


def get_project_directory():
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))


def pars_arguments():
    parser = argparse.ArgumentParser(description="Process access.log")

    parser.add_argument('--input',
                        action='store',
                        dest='input',
                        default='input',
                        help='Path to logfile or directory with logfile')
    parser.add_argument('--output',
                        action='store',
                        dest='output',
                        default='output/result.json',
                        help='Path to result json file')
    return parser.parse_args()


def get_files_list(path_to_file):
    _path = os.path.join(get_project_directory(), path_to_file.input)
    if os.path.isdir(_path):
        _files_list = os.listdir(_path)
        logfiles_list = [
            os.path.join(_path, logfile) for logfile in _files_list
            if logfile.endswith(".log") or logfile.endswith(".txt")
        ]

        return logfiles_list

    elif os.path.isfile(_path):
        if _path.endswith(".log") or _path.endswith(".txt"):

            return [_path]

        else:
            raise Exception("File must be '.log' or '.txt'")
    else:
        raise Exception("Path is not valid")
