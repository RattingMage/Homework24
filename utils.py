import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_NAME = os.path.join(DATA_DIR, "apache_logs.txt")


def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data: list[str]) -> list[str]:
    col_number: int = int(param)
    return list(map(lambda row: row.split(" ")[col_number], data))


def unique_query(data: list[str], *args, **kwargs) -> list[str]:
    result: list = []
    seen: set = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result


def sort_query(param: str, data: list[str]) -> list[str]:
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: list[str]) -> list[str]:
    limit = int(param)
    return data[:limit]


def regex_query(param: str, data: list[str]) -> list[str]:
    pattern = re.compile(param)
    return list(filter(lambda row: re.search(pattern, row), data))


CMD_TO_FUNCTION = {
    "fileter": filter_query,
    "map": map_query,
    "unique": unique_query,
    "sort": sort_query,
    "limit": limit_query,
    "regex": regex_query
}


def build_query(cmd, param, data=None):
    if not data:
        with open(FILE_NAME) as file:
            data = list(map(lambda row: row.strip(), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
