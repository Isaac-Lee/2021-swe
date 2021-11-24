from loader.config_loader.config_loader import ConfigLoader

import yaml
from matplotlib import pyplot as plt

if __name__ == '__main__':
    debug = True
    config_file_path = "config/config.yaml"

    print("read config")
    config_loader = ConfigLoader(file_type='yaml', file_path=config_file_path)
    config_loader.print_config()
    config = config_loader.get_config()

    print("read data")
    result_file_name = "test_file"

    print("make image")
    plt.figure(figsize=(75, 68))
    fig, ax = plt.subplots()



    if debug:
        print("Save image...")
        plt.savefig("./img/%s.jpg" % result_file_name, dpi=150)
        plt.show()

    print("return image")
