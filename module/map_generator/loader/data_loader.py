from MapGenerator.data.H5 import H5
from MapGenerator.data.NetCDF import NetCDF
from MapGenerator.data.CSV import CSV

'''
DataLoader
===========

데이터 파일 타입과 데이터 파일의 경로를 입력하면 해당 데이터 클래스를 반환하는 클래스
'''


class DataLoader:
    def __init__(self, file_type, file_path, data_id, **data_kw):
        self.data = None

        if file_type == 'nc':
            self.data = NetCDF(file_path, data_id)

        elif file_type == 'h5':
            self.data = H5(file_path, data_id)

        elif file_type == 'csv':
            self.data = CSV(file_path, **data_kw)


"""
class NetcdfLoader(DataLoader):
    def load(self, src, **kwargs):
        data_field_name = kwargs.get('data_field_name',None)
        nc = NetCDF(src)
        data = nc[data_field_name][:]
        nc.close()
        return data
"""
