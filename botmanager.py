import yaml
import json
from loguru import logger
global_setting = yaml.safe_load(open('./yamls/General.yaml', 'r', encoding='UTF-8'))
rand_sents = json.load(open('./jsons/zh-cn/rand_sents.json','r',encoding='UTF-8'))
rand_sents1 = json.load(open('./jsons/en-us/rand_sents_en.json','r',encoding='UTF-8'))
rand_sents2 = json.load(open('./jsons/fr-fr/rand_sents_fr.json','r',encoding='UTF-8'))
def bot_config(name: str):
    try:
        return global_setting[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None
def sents_config(name: str):
    try:
        return rand_sents[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None    
def sents_config_en(name: str):
    try:
        return rand_sents1[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None         
def sents_config_fr(name: str):
    try:
        return rand_sents2[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None                 