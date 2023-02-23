import yaml
import os
from aiohttp import ClientSession
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image, At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from loguru import logger
zh_cn = 1
en_us = 0
channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = en_us")],
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage):
 global en_us
 global zh_cn
 if en_us==0:    
    en_us=1
    zh_cn=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," Now bot default language is English(United States)")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," Bot default language is English(United States) now,Don't need Change"))   
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = zh_cn")],
    )
)
async def linux(app: Ariadne, group: Group,event: GroupMessage):
  global en_us
  global zh_cn
  if zh_cn ==0:
    en_us=0
    zh_cn=1
    await app.send_message(group,MessageChain(At(event.sender.id)," Bot默认语言已更改为中文(中国大陆)")) 
  else:
    await app.send_message(group,MessageChain(At(event.sender.id)," 默认语言已是中文(中国大陆)，无需更改")) 