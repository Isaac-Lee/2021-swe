from loader.config_loader.config_loader import ConfigLoader

import yaml
import sys
import netCDF4
from matplotlib import pyplot as plt

if __name__ == '__main__':
    config_file_path = "./map_generator/config/config.yaml"

    print("get custom options")
    keyword = sys.argv[1]
    shooting_period = sys.argv[2]
    shooting_time = sys.argv[3]
    title = sys.argv[4]
    font = int(sys.argv[5])
    latitude_font = int(sys.argv[6])
    longitude_font = int(sys.argv[7])

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config = config_loader.get_config()

    title_name = config["keywords"][keyword]["keyword_name"]


    print("read data")

    # data_file_name = "GK2B_GOCI2_L2_"+shooting_period+"_"+shooting_time+"_LA_S007_"+keyword
    result_file_name = f'{keyword}_{shooting_period}_{shooting_time}_{title}_{font}'

    # debug용
    data_file_name = "GK2B_GOCI2_L2_20211110_011530_LA_S007_AC"
    Data = netCDF4.Dataset(f'./map_generator/data/{data_file_name}.nc')
    data_x_axis = []
    data_y_axis = []


    print("make image")
    fig, ax = plt.subplots()
    fig.set_figheight(6.8)
    fig.set_figwidth(7.5)
    ax.set_title(title, fontsize=font, pad=10)
    plt.xticks(fontsize=longitude_font)
    plt.yticks(fontsize=longitude_font)

    ax.xaxis.set_label_position("top")
    ax.set_xlabel("%s" % title_name)

    print("Save image...")
    plt.savefig("./map_generator/img/%s.jpg" % result_file_name, dpi=150)

    print("return image")
