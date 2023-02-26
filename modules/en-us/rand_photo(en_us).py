from aiohttp import ClientSession
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image, At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import botmanager
import langmanager

url = botmanager.bot_config('setuapi')
ban_group = botmanager.bot_config('ban_group')
ban_user = botmanager.bot_config('ban_user')
channel = Channel.current()
channel.name("Random acg photo")
channel.description("Just Random acg photo")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("acgphoto")],
    )
)
async def setu(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "en_us":
        if group.id in ban_group:
            await app.send_message(
                group,
                MessageChain(At(event.sender.id),
                             " Sorry,This group is disabled the feature. Because at Developer's requièrent"))
        elif event.sender.id in ban_user:
            await app.send_message(group, MessageChain(At(event.sender.id),
                                                       " Sorry,You have been banned from using this feature. Because at Developer's requièrent"))
        else:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.read()
            await app.send_group_message(group, MessageChain(Image(data_bytes=data)))

    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " The language(en_us) is not available.If you installed it,you can type 'Lang --set-default-lang = xx_xx'"))
