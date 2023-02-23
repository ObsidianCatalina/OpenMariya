import yaml
import json
from loguru import logger
global_setting = yaml.safe_load(open('./yamls/General.yaml', 'r', encoding='UTF-8'))
def bot_config(name: str):
    try:
        return global_setting[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None