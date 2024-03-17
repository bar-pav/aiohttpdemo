import pathlib

import yaml


BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'config.yaml'


def get_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


config = get_config(config_path)
