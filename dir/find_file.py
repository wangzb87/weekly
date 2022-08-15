import datetime
import os
from pprint import pp, pprint
from re import A
from time import ctime, time
import config_filter
import shutil


all_file = []
now = datetime.datetime.now()
GMT_FORMAT = "%a %b %d %H:%M:%S %Y"


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            file_extension = os.path.splitext(fullname)[-1][1:]
            if file_extension not in config_filter.file_extension:
                continue
            file_ctime = ctime(os.path.getctime(fullname))
            fileter_time = datetime.datetime.strptime(file_ctime, GMT_FORMAT)
            if fileter_time < config_filter.create_time:
                continue

            file_mtime = ctime(os.path.getmtime(fullname))
            fileter_time = datetime.datetime.strptime(file_mtime, GMT_FORMAT)
            if fileter_time < config_filter.create_time:
                continue
            file_attr = (fullname, file_extension, file_ctime, file_mtime)
            all_file.append(file_attr)
    return all_file


def filter_by_extension(*args):
    # pprint(args)
    if args[0][1] in config_filter.file_extension:
        return True
    else:
        return False


def filter_by_create_time(*args):
    fileter_time = datetime.datetime.strptime(args[0][2], GMT_FORMAT)
    if fileter_time > config_filter.create_time and fileter_time <= now:
        return True
    else:
        return False


def filter_by_mtime(*args):
    fileter_time = datetime.datetime.strptime(args[0][3], GMT_FORMAT)
    if fileter_time > config_filter.update_time and fileter_time <= now:
        return True
    else:
        return False


if __name__ == "__main__":
    all_file = findAllFile(config_filter.path_e)
    # filtered_file = list(filter(filter_by_extension, all_file))
    # filtered_file = list(filter(filter_by_create_time, filtered_file))
    # filtered_file = list(filter(filter_by_mtime, filtered_file))

    # pprint(all_file)
    pprint(len(all_file))
    for file_attr in all_file:
        shutil.move(file_attr[0], "d:/dmove")

