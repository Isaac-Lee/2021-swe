from loader.config_loader.config_loader import ConfigLoader

import yaml
import sys
import netCDF4
from matplotlib import pyplot as plt

if __name__ == '__main__':
    config_file_path = "./map_generator/config/config.yaml"

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config = config_loader.get_config()

    print("get custom options")
    keyword = sys.argv[1]
    shooting_period = sys.argv[2]
    shooting_time = sys.argv[3]
    title = sys.argv[4]
    font = sys.argv[5]
    latitude_font = sys.argv[6]
    longitude_font = sys.argv[7]

    print("read data")
    # data_file_name = "GK2B_GOCI2_L2_"+shooting_period+"_"+shooting_time+"_"+"_LA_S007_"+keywords
    data_file_name = "GK2B_GOCI2_L2_20211110_011530_LA_S007_AC"
    Data = netCDF4.Dataset(f'./map_generator/data/{data_file_name}.nc')

    print("make image")
    plt.figure(figsize=(7.5, 6.8))
    plt.plot([1, 2, 3], [1, 2, 3])
    plt.title(title, fontname=font)
    plt.xlabel("Longitude (deg.)", fontname=longitude_font)
    plt.ylabel("Latitude (deg.)", fontname=latitude_font)

    # TODO
    # 추후에 모든 커스텀 값들 들어오면 해당 문자열로 만들기
    result_file_name = f'{keyword}_{shooting_period}_{shooting_time}_{title}_{font}'

    print("Save image...")
    plt.savefig("./map_generator/img/%s.jpg" % result_file_name, dpi=150)

    print("return image")
