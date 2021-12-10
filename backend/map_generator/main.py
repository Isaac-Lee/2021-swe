from loader.config_loader.config_loader import ConfigLoader
from util.file_name_finder import find_file_name

import yaml
import sys
import netCDF4
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    config_file_path = "./map_generator/config/config.yaml"

    print("get custom options")
    keyword_name = sys.argv[1]
    shooting_period = sys.argv[2]
    shooting_time = sys.argv[3]
    title = sys.argv[4]
    font = int(sys.argv[5])
    latitude_font = int(sys.argv[6])
    longitude_font = int(sys.argv[7])

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config = config_loader.get_config()

    keyword = config["keywords"][keyword_name]
    title_name = keyword["keyword_name"]
    group_names = keyword["group_names"]
    group_depth = keyword["group_depth"]
    variable_name = keyword["variable_name"]
    valid_min = keyword["valid_min"]
    valid_max = keyword["valid_max"]
    units = keyword["units"]

    print("read data")
    data_file_name = find_file_name(shooting_period, shooting_time, keyword_name)
    result_file_name = f'{keyword_name}_{shooting_period}_{shooting_time}_{title}_{font}_{latitude_font}_{longitude_font}'

    # debug 용
    # data_file_name = "GK2B_GOCI2_L2_20211110_011530_LA_S007_AC"

    Data = netCDF4.Dataset(f'./map_generator/data/{data_file_name}')

    group = Data.groups[group_names[0]]
    for i in range(1, group_depth):
        group = group.groups[group_names[i]]
    var = group.variables[variable_name]

    data = np.array(var)
    data[data < valid_min] = np.nan
    data[data > valid_max] = np.nan

    print("make image")
    fig, ax = plt.subplots()
    fig.set_figheight(6.8)
    fig.set_figwidth(7.5)
    ax.set_title(title, fontsize=font, pad=10)
    plt.xticks(fontsize=longitude_font)
    plt.yticks(fontsize=latitude_font)
    plt.imshow(data)

    ax.xaxis.set_label_position("top")
    ax.set_xlabel(f"{title_name} unit: {units}")

    print("save image")
    plt.savefig("./map_generator/img/%s.jpg" % result_file_name, dpi=150)

    print("return image")
