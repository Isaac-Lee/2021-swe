import numpy as np
import pandas as pd
from netCDF4 import Dataset


class NetCDF_loader(Data):
    """

    NetCDF
    ===========

    NetCDF 파일을 읽고, 처리, 저장하는 클래스

    Attributes:
        path(str): 데이터 파일의 경로
        data(netCDF4.Dataset): NetCDF 데이터
        df(pandas.Dataframe): NetCDF 데이터를 처리해서 pandas Dataframe 형태로 저장한 데이터
    """

    def __init__(self, file_path=str):
        super().__init__()
        self.path = file_path
