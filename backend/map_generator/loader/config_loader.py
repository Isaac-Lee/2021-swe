import yaml
"""

ConfigLoader
===========

Config 파일을 읽어들이는 클래스 입니다.

Attributes:
    config(dict): 읽어온 config 파일의 정보
"""


class ConfigLoader:
    def __init__(self, file_type, file_path=str):
        self.config = {}
        if file_type == 'yaml':
            with open(file_path, 'r') as f:
                self.config = yaml.load(f, Loader=yaml.FullLoader)

    def get_config(self, option=None):
        """
        Args:
            option (str): config 파일 안에 원하는 특정 config를 불러오고 싶으면 작성

        Returns:
            dict: config 정보를 담은 딕셔너리
        """
        config = self.config
        if option is not None:
            config = self.config[option]
        return config

    def print_config(self):
        """
        Args: None

        Returns: None
        """
        config = self.config
        for k in config:
            if type(config[k]) and type(str):
                print(k)
                for v in config[k]:
                    if type(config[k][v]) == type(str):
                        print("--", v)
                        for i in config[k][v]:
                            print("----", i, ":", str(config[k][v][i]))
                    else:
                        print("--", v, ":", str(config[k][v]))
            else:
                print(k, ":", str(config[k]))


if __name__ == '__main__':
    config_file_path = "./config/config.yaml"

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config_loader.print_config()
    config = config_loader.get_config()