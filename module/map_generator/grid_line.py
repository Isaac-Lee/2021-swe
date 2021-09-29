import numpy as np


def get_para_meri(disable, lat_min, lat_max, lat_tick,
                  lon_min, lon_max, lon_tick):
    parallels = np.arange(lat_min, lat_max + 1, lat_tick)
    meridians = np.arange(lon_min, lon_max + 1, lon_tick)
    return parallels, meridians
