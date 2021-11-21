from loader.config_loader import ConfigLoader
import yaml

if __name__ == '__main__':
    config_file_path = "./config/config.yaml"

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config_loader.print_config()
    config = config_loader.get_config()

    print("return image")