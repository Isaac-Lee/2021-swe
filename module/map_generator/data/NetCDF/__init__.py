import numpy as np
import pandas as pd
from netCDF4 import Dataset

from MapGenerator.data import Data


class NetCDF(Data):
    """

    NetCDF
    ===========

    NetCDF 파일을 읽고, 처리, 저장하는 클래스

    Attributes:
        path(str): 데이터 파일의 경로
        data(netCDF4.Dataset): NetCDF 데이터
        df(pandas.Dataframe): NetCDF 데이터를 처리해서 pandas Dataframe 형태로 저장한 데이터

    Todo:
        * S5P에 오버피팅 되어있는 클래스 수정
        * nc 파일들간에도 데이터가 저장되어있는 구조가 달라서 구분이 필요함
        * 추후에 그려야 하는 데이터가 늘어나면 그때 다시 작성
    """
    def __init__(self, file_path=str, data_id=str):
        super().__init__()
        self.path = file_path
        if data_id == 'no2':
            self.data = NetCDFno2(file_path)
        else:
            self.data = None
        self.df = None

    def remove_invalid_value(self, lat_field_name, lon_field_name,
                             data_field_name, valid_min, valid_max):
        """
                반드시 get_data_array() 함수 실행전에 실행되어야 합니다.

                 Args:
                    lat_field_name (str): latitude 필드 이름
                    lon_field_name (str): longitude 필드 이름
                    data_field_name (str): data 필드 이름
                    valid_min (int): 최소 유효값
                    valid_max (int): 최대 유효값

                Returns: None
                """
        self.df = pd.DataFrame({lat_field_name: self.__get_data_array(lat_field_name),
                                lon_field_name: self.__get_data_array(lon_field_name),
                                data_field_name: self.__get_data_array(data_field_name)})
        self.df = self.df[self.df[data_field_name] >= valid_min]
        self.df = self.df[self.df[data_field_name] <= valid_max]

    def __get_data_array(self, field_name):
        return self.data.get_data_array(field_name)

    def get_data_array(self, field_name):
        """
         Args:
            field_name (str): 원하는 데이터의 필드 이름

        Returns:
            numpy.array: 원하는 데이터의 Numpy 배열(1차원)
        """
        return self.df[field_name]

    def get_data(self, data_set=None, field_name=str):
        """
        데이터 셋에서 원하는 필드의 데이터를 찾아서 raw한 형태로 반환합니다.

         Args:
             data_set(str): 원하는 필드가 들어있는 netCDF4.Dataset
             field_name (str): 원하는 데이터의 필드 이름

        Returns:
            netCDF4.Dataset: 원하는 데이터의 Dataset
        """
        if data_set is None:
            current_data_set = self.data
        else:
            current_data_set = data_set
        if len(current_data_set.variables) <= 0:
            for key in current_data_set.groups:
                if self.get_data(current_data_set.groups[key], field_name) is None:
                    continue
                else:
                    return self.get_data(current_data_set.groups[key], field_name)
        else:
            if field_name in current_data_set.variables:
                return current_data_set[field_name]
            else:
                for key in current_data_set.groups:
                    if self.get_data(current_data_set.groups[key], field_name) is None:
                        continue
                    else:
                        return self.get_data(current_data_set.groups[key], field_name)
                for key in current_data_set.variables:
                    if self.get_data(current_data_set.variables[key], field_name) is None:
                        continue
                    else:
                        return self.get_data(current_data_set.variables[key], field_name)

    def close_dataset(self):
        self.data.close()

    def show_shape(self, field_name=str):
        """

        데이터의 shape을 보여줍니다.

         Args:
             field_name (str): 원하는 데이터의 필드 이름

        Returns:
            tuple: 원하는 데이터의 shape
        """
        return self.get_data(field_name=field_name)[:].shape


class NetCDFno2(NetCDF):
    """
    NetCDFNO2
    ===========

    NetCDF 파일 중 NO2와 관련된 데이터를 읽고, 처리, 저장하는 클래스

    Attributes:
        data(netCDF4.Dataset): NetCDF 데이터
    """
    def __init__(self, file_path=str):
        super().__init__()
        self.data = Dataset(file_path)

    def get_data_array(self, field_name=str):
        """
        raw한 데이터를 받아서 데이터를 1차원 또는 2차원 array로 반환하는 함수
        """
        data = super().get_data(field_name=field_name)[:][0]
        new_data = np.ravel(data, order='C')
        return new_data