from matplotlib import pyplot as plt, tri
import numpy as np


def create_map(map_type, **kw):
    if map_type == '1d':
        return create_map_with_1d(**kw)
    elif map_type == '2d':
        return create_map_with_2d(**kw)


def create_map_with_1d(basemap, lat, lon, data, colormap, **kw):
    colormap = basemap.scatter(lon, lat, latlon=True, c=data, s=1, cmap=colormap)
    return colormap


def create_map_with_2d(file_type, basemap, lat, lon, data, colormap):
    # TODO 각각 다른 형태의 데이터의 경우 다르게 처리해야함.
    # h5, netcdf 추가
    if file_type in ['csv', 'h5', 'nc']:
        x = lon
        y = lat

        lon_min, lon_max = min(lon), max(lon)
        lat_min, lat_max = min(lat), max(lat)
        x_point = int(np.sqrt(len(data))) + 1
        y_point = int(np.sqrt(len(data))) + 1
        xi = np.linspace(lon_min-2, lon_max+2, x_point)
        yi = np.linspace(lat_min-2, lat_max+2, y_point)

        triang = tri.Triangulation(y, x)
        interpolator = tri.LinearTriInterpolator(triang, data)
        Xi, Yi = np.meshgrid(xi, yi)
        vari = interpolator(Yi, Xi)
        xi, yi = basemap(Xi, Yi)
        colormap = basemap.contourf(xi, yi, vari, levels=100, cmap=colormap)
    else:
        if np.ndim(lon) == 1 and np.ndim(lat) == 1:
            lons, lats = np.meshgrid(lon, lat)
        else:
            lons, lats = lon, lat
        x, y = basemap(lons, lats)
        colormap = basemap.contourf(x, y, data, levels=100, cmap=colormap)
    return colormap
