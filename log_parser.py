#! /usr/bin/python3

import re
import os
import json
import configuration

from collections import Counter
from utils import get_project_directory, pars_arguments, get_files_list


class LogParser:
    def __init__(self, files_list):
        self.files_list = files_list
        self.count = 0
        self.ip_counter = Counter()
        self.methods_counter = Counter()
        self.top_duration = []
        self.top_client_errors = Counter()
        self.top_server_errors = Counter()

    def count_top_ip(self, line):
        ip = re.search(configuration.IP_ADDRESS_REGEX, line).group()
        self.ip_counter[ip] += 1

    def count_methods_requests(self, line):
        method = re.search(configuration.METHODS_REGEX, line)
        if method:
            methods = method.group()
            self.methods_counter[methods] += 1

    def count_duration_requests(self, line):
        time_request = re.search(configuration.DURATION_REQUEST_REGEX, line)
        if time_request:
            time_requests = time_request.groups()
            self.top_duration.append(time_requests)

    def count_client_errors(self, line):
        client_error = re.search(configuration.CLIENT_ERROR_REGEX, line)
        if client_error:
            client_errors = client_error.groups()
            self.top_client_errors[" ".join(client_errors)] += 1

    def count_server_errors(self, line):
        server_error = re.search(configuration.SERVER_ERROR_REGEX, line)
        if server_error:
            server_errors = server_error.groups()
            self.top_server_errors[" ".join(server_errors)] += 1

    def sorted_top_duration_list(self):
        return sorted(self.top_duration, reverse=True, key=lambda tup: int(tup[-1]))[:10]

    def count_all(self):
        for file in self.files_list:
            with open(file, 'r') as f:
                for index, line in enumerate(f.readlines()):
                    self.count += 1
                    self.count_top_ip(line)
                    self.count_methods_requests(line)
                    self.count_duration_requests(line)
                    self.count_client_errors(line)
                    self.count_server_errors(line)

    def get_json_data(self):
        data = {
                    "Requests count": self.count,
                    "Requests count for type:": self.methods_counter,
                    "TOP 10 IP": dict(self.ip_counter.most_common(10)),
                    "TOP 10 most long reqests": [' '.join(e) for e in self.sorted_top_duration_list()],
                    "TOP 10 client errors": dict(self.top_client_errors.most_common(10)),
                    "TOP 10 server errors": dict(self.top_server_errors.most_common(10))
                }
        return data

    def creat_result_file(self):
        filename = pars_arguments().output
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(os.path.join(get_project_directory(), filename), "w") as file:
            data = json.dumps(self.get_json_data(), indent=4)
            file.write(data)


if __name__ == "__main__":
    files = get_files_list(pars_arguments())
    log_parser = LogParser(files)
    log_parser.count_all()
    log_parser.creat_result_file()
