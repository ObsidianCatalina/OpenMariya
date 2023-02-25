from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from modules import langmanager
import botmanager

su = botmanager.bot_config('su')
channel = Channel.current()
channel.name("Factory Test -REC")
channel.description("Recovery Bot All setting")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("rec --all")],
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage):
    if event.sender.id in su:
        langmanager.zh_cn = 1
        langmanager.zh_hk = 0
        langmanager.en_us = 0
        langmanager.fr_fr = 0
        langmanager.ru_ru = 0
        langmanager.es_es = 0
        langmanager.ja_jp = 0
        langmanager.ko_kr = 0
        await app.send_message(
            group,
            MessageChain(At(event.sender.id), " All settings is restored to normal!")
        )
    else:
        await app.send_message(group, MessageChain(At(event.sender.id), " You don't have factory test usufruct"))
