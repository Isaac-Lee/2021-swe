import netCDF4
import numpy as np
from matplotlib import pyplot as plt

data_file_name = "GK2B_GOCI2_L2_20211110_011530_LA_S007_AOD"
Data = netCDF4.Dataset(f'../data/{data_file_name}.nc')

group = Data.groups['geophysical_data']
var = group.variables['Aerosol_Optical_Depth']
valid_min = -32767.0
valid_max = 32767.0
data = np.array(var)
data[data < valid_min] = np.nan
data[data > valid_max] = np.nan

print(data)

plt.figure(figsize=(7.5, 6.8))
plt.imshow(data)
plt.show()