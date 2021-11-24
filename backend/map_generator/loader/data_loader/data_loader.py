from loader.data_loader import *

'''
DataLoader
===========

데이터 파일 타입과 데이터 파일의 경로를 입력하면 해당 데이터 클래스를 반환하는 클래스
'''


class DataLoader:
    def __init__(self, file_type, file_path, **data_kw):
        self.data = None

        if file_type == 'nc':
            self.data = NetCDF_loader(file_path)
