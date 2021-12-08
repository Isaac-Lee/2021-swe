from util.time_converter import kst2utc

import re
import os

def find_file_name(shooting_period, shooting_time, keyword_name):
    kst = kst2utc(shooting_period, shooting_time)
    pattern = f"GK2B_GOCI2_L2_{kst}[0-9]+_LA_S007_{keyword_name}"
    data_name_pattern = re.compile(pattern)
    dir = './map_generator/data'
    files = os.listdir(dir)

    for file in files:
        m = data_name_pattern.match(file)
        if m is not None:
            return file

    pattern = f"GK2B_GOCI2_L2_{kst}****_LA_S007_{keyword_name}"
    raise Exception(f'no file matched: {pattern}')

if __name__ == '__main__':
    dir = '../data'
    files = os.listdir(dir)

    pattern = "GK2B_GOCI2_L2_20211110_01[0-9]{4}_LA_S007_AC.nc"
    data_name_pattern = re.compile(pattern)

    for file in files:
        m = data_name_pattern.match(file)
        if m is not None:
            print("matched file: ", file)
        print(file, m)