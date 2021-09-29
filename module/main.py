import sys
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.basemap import Basemap

from map_generator.colormap_maker import get_continuous_cmap
from map_generator.grid_line import get_para_meri
from map_generator.loader.config_loader import ConfigLoader
from map_generator.loader.data_loader import DataLoader
from map_generator.map_generator import create_map, create_map_with_2d

if __name__ == '__main__':
    print("Reading Config...")
    # config_path / data_path / [ 데이터 id(?) ] / [ 데이터 파일 타입] / { 지도로 그리려는 데이터들... }
    config_file_path = sys.argv[1]
    data_file_path = sys.argv[2]
    data_id = sys.argv[3]
    data_file_type = sys.argv[4]
    data_field_info = sys.argv[5:]

    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config = config_loader.get_config()

    # data config load / data load
    data_config = config_loader.get_config('data')[data_id]
    data_config = data_config[data_file_type]
    loader = DataLoader(data_file_type, data_file_path, data_id, **data_config)
    data = loader.data

    lat_field_name = data_config['lat_field_name']
    lon_field_name = data_config['lon_field_name']
    z_field_name = data_config['z_axis_field_name']
    z_field_idx = data_config['z_axis_field_idx']

    print("Get Config Info...")
    # map 관련 config load
    basemap_config = config_loader.get_config('basemap')
    colormap_config = config_loader.get_config('colormap')
    grid_config = config_loader.get_config('grid')
    parallels_grid = config_loader.get_config('parallels_grid')
    meridians_grid = config_loader.get_config('meridians_grid')
    grid_text = config_loader.get_config('grid_text')
    cbar_config = config_loader.get_config('colorbar')
    cbar_label_config = config_loader.get_config('colorbar_label')
    cbar_text_config = config_loader.get_config('colorbar_text')
    title_config = config_loader.get_config('title')
    image_config = config_loader.get_config('image')
    text_config = config_loader.get_config('text')

    print("Read Data Info...")
    # TODO data_info key를 이용해서 각각의 정보를 불러오기
    # draw map for each data
    for data_field_key in data_field_info:
        print("Get Data Info...")

        data_field = data_config['data_field_info'][data_field_key]
        data_info = data_field['data_info']
        data_field_name = data_info['data_field_name']
        valid_min = data_info['valid_min']
        valid_max = data_info['valid_max']

        basemap_type = data_field['basemap_type']
        colormap_type = data_field['colormap_type']
        map_categories = data_field['map_categories']
        result_file_name = data_field['result_file_name']

        data.remove_invalid_value(lat_field_name, lon_field_name, **data_info)
        lats = data.get_data_array(lat_field_name)
        lons = data.get_data_array(lon_field_name)
        var_data_array = data.get_data_array(data_field_name)

        # time 등과 같이 데이터에 시간 차원이 들어가 있는 경우, 특정 시간을 정하기 위한 코드 부분
        if z_field_name is not None:
            z = data.get_data(z_field_name)
            z_idx = data_config['z_axis_field_idx']
            var_data_array = var_data_array[z_idx]
        else:
            z = None

        print("Making plot and map...")
        # =====이미지 생성 부분=====
        fig, ax = plt.subplots()
        fig.dpi = 200

        basemap_config = config_loader.get_config('basemap')
        basemap_kwarg = basemap_config[basemap_type]
        m = Basemap(**basemap_kwarg, ax=ax)
        m.drawcoastlines()
        m.drawcountries()

        colormap_categories = colormap_config['categories']
        color_list = colormap_categories[colormap_type]['color_list']
        colormap = get_continuous_cmap(color_list)

        print("Draw a grid line...")
        # set map grid
        if grid_config['disable']:
            pass
        else:
            parallels, meridians = get_para_meri(**grid_config)
            m.drawparallels(parallels, **parallels_grid, **grid_text)
            m.drawmeridians(meridians, **meridians_grid, **grid_text)

        # map 컬러 넣기
        if map_categories == '1d':
            # 1차원 scatter plot 그리기
            # colormap = create_map_with_1d(m, lons, lats, var_data_array, colormap=colormap)
            colormap = m.scatter(lons, lats, latlon=True, c=var_data_array, s=1, cmap=colormap)
        elif map_categories == '2d':
            # 2차원 interpolation plot 그리기
            colormap = create_map_with_2d(data_file_type, m, lats, lons, var_data_array, colormap)

        print("Make a colorbar...")
        cbar_orientation = cbar_config['orientation']
        divider = make_axes_locatable(plt.gca())
        if cbar_orientation == 'horizontal':
            cax = divider.append_axes("bottom", size="8%", pad=0.5)
        elif cbar_orientation == 'vertical':
            cax = divider.append_axes("right", size="8%", pad=0.5)
        cbar = fig.colorbar(colormap, orientation=cbar_orientation, cax=cax)
            

        print("Setting colorbar...")
        unit = data_field['units']
        position = cbar_label_config['position']

        if cbar_label_config['disable']:
            pass
        else:
            print("Colorbar Label setting...")
            cbar_label_text_config = cbar_label_config['text']
            if cbar_orientation == 'horizontal':
                cbar.ax.get_xaxis().labelpad = 10
                cbar.ax.set_xlabel(unit, **cbar_label_text_config)
                cbar.ax.xaxis.set_label_position(position)
            elif cbar_orientation == 'vertical':
                cbar.ax.get_yaxis().labelpad = 15
                cbar.ax.set_ylabel(unit, rotation=270, **cbar_label_text_config)
                cbar.ax.yaxis.set_label_position(position)

        if cbar_text_config['disable']:
            pass
        else:
            print("Colorbar Text setting...")
            text_list = cbar_text_config['text_list']
            cbar_text_text_config = cbar_text_config['text']
            if cbar_orientation == 'horizontal':
                for j, label in enumerate(text_list):
                    cbar.ax.text(((j * 2 + 1) * max(var_data_array)) / (len(text_list) * 2) - 3, 25,
                                 label, ha='center', va='center', **cbar_text_text_config)
            elif cbar_orientation == 'vertical':
                for j, label in enumerate(text_list):
                    cbar.ax.text(25, ((j * 2 + 1) * max(var_data_array)) / (len(text_list) * 2) - 3,
                                 label, ha='center', va='center', **cbar_text_text_config)

        print("Setting a title...")
        title_config = config_loader.get_config('title')

        if title_config['disable']:
            pass
        else:
            long_name = data_field_name
            title_config = title_config['config']
            if z is None:
                ax.set_title(long_name, **title_config)
            else:
                # TODO time이나 사용자가 원하는 자료를 표시
                pass
            ax.xaxis.set_label_position("top")
            ax.set_xlabel("%s" % result_file_name)

        print("Setting a image...")
        if image_config['disable']:
            pass
        else:
            image_info_config = image_config['config']
            image_path = image_info_config['file_path']
            x_position = image_info_config['x_position']
            y_position = image_info_config['y_position']
            zoom = image_info_config['zoom']
            logo = np.array(Image.open(image_path))
            im = OffsetImage(logo, zoom=zoom)
            ab = AnnotationBbox(im, (x_position, y_position), xycoords='axes fraction', frameon=False)
            ax.add_artist(ab)

        print("Setting a text...")
        if text_config['disable']:
            pass
        else:
            text = text_config['text']
            x, y = text_config['xy']
            text_text_config = text_config['config']
            plt.annotate(text, xy=(x, y), xycoords='axes fraction', **text_text_config)

        print("Save image...")
        plt.savefig("./img/%s.jpg" % result_file_name, dpi=200)
        plt.show()

    loader.data.close_dataset()
    print("Finish Process.")
