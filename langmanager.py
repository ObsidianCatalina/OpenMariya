from aiohttp import ClientSession
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import  At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import botmanager
from loguru import logger
su = botmanager.bot_config('su')
zh_cn = 1
zh_hk = 0
en_us = 0
fr_fr = 0
ru_ru = 0
es_es = 0
ja_jp = 0
ko_kr = 0 

channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = en_us")],
    )
)
async def us(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if en_us==0:    
    en_us=1
    zh_cn=0
    fr_fr=0
    ru_ru=0
    es_es=0
    ja_jp=0
    ko_kr=0
    zh_hk=0
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

async def cn(app: Ariadne, group: Group,event: GroupMessage):

 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if zh_cn ==0:
    en_us=0
    zh_cn=1
    zh_hk=0
    fr_fr=0
    ru_ru=0
    es_es=0
    ja_jp=0
    ko_kr=0
    zh_hk=0
    await app.send_message(group,MessageChain(At(event.sender.id)," Bot默认语言已更改为简体中文(中国大陆)")) 
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," 默认语言已是简体中文(中国大陆)，无需更改")) 

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = fr_fr")],
    )
)
async def fr(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if fr_fr==0:    
    zh_cn=0
    fr_fr=1
    ru_ru=0
    es_es=0
    ja_jp=0
    ko_kr=0
    zh_hk=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," Maintenant bot par défaut langue est Français(République française)")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," Bot par défaut langue est  Français(République française),Pas besoin changer"))   
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = ru_ru")],
    )
)
async def ru(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if ru_ru==0:    
    zh_cn=0
    fr_fr=0
    ru_ru=1
    es_es=0
    ja_jp=0
    ko_kr=0
    zh_hk=00
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," теперь Язык бота по умолчанию российской(Российская Федерация)")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," Язык бота по умолчанию российской(Российская Федерация) сейчас. Не нужно изменить"))  
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = es_es")],
    )
)
async def es(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if es_es==0:    
    zh_cn=0
    fr_fr=0
    ru_ru=0
    es_es=1
    ja_jp=0
    ko_kr=0
    zh_hk=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," Ahora el idioma predeterminado del bot es Español(Reino de España)")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," El idioma predeterminado del bot es Español(Reino de España),no necesita cambiar")) 
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = ja_jp")],
    )
)
async def jp(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if ja_jp==0:    
    zh_cn=0
    fr_fr=0
    ru_ru=0
    es_es=0
    ja_jp=1
    ko_kr=0
    zh_hk=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," ボットのデフォルト言語が日本語(日本)になりました")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," ボットのデフォルト言語は日本語(日本)になりました,変更する必要はありません")) 
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = ko_kr")],
    )
)
async def kr(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if ko_kr==0:    
    zh_cn=0
    fr_fr=0
    ru_ru=0
    es_es=0
    ja_jp=0
    ko_kr=1
    zh_hk=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," 이제 봇 기본 언어는 한국어(대한민국)입니다.")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," 봇 기본 언어는 이제 한국어(대한민국)이며 변경이 필요하지 않습니다."))
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --set-default-lang = zh_hk")],
    )
)
async def hk(app: Ariadne, group: Group, event: GroupMessage):
 global en_us,zh_cn,fr_fr,ru_ru,es_es,ja_jp,ko_kr,zh_hk
 if ko_kr==0:    
    zh_cn=0
    fr_fr=0
    ru_ru=0
    es_es=0
    ja_jp=0
    ko_kr=1
    zh_hk=0
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," Bot語言已更改為繁體中文（中華人民共和國香港特別行政區）")
     )
 else:
    await app.send_message(group,MessageChain(At(event.sender.id)," 默認語言已是簡體中文（中國大陸），無需更改"))      
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --list-a")],
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage):
   if event.sender.id in su: 
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," Installed language:\nChinese Simplified(China Mainland)\nEnglish(United States)\nFrench(France Republic)\nRussian(Russian Federation)\nSpanish(Spain)\nJapanese(Japan)\nKorean(Republic of Korea/South Korerea)\nChinese Chinese Traditional(PRC SAR HongKong)")
     )
   else:
    await app.send_message(group,MessageChain(At(event.sender.id)," You don't have check privileges")) 