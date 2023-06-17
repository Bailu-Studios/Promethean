from abc import ABC

from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_member import ABCMember
from promethean.api.vila.abc_message import ABCMessage, ABCTextMessage, ABCImageMessage


class Message(ABCMessage, ABC):
    _msg_id: str
    _send_time: int
    _bot: ABCBot
    _sender: int
    _room_id: int
    _villa_id: int
    _quote: ABCMessage

    def __init__(self, bot: ABCBot, sender: int, msg_id: str = '-1', room_id: int = -1, villa_id: int = -1,
                 send_time: int = -1, quote: ABCMessage = None):
        self._msg_id = msg_id
        self._send_time = send_time
        self._bot = bot
        self._sender = sender if sender != '-1' else bot.get_bot_uid()
        self._room_id = room_id
        self._villa_id = villa_id
        self._quote = quote

    async def reply(self, msg: ABCMessage):
        """
        回复消息
        """
        msg.set_quote(self)
        await self._bot.send_msg(self._room_id, msg)

    async def get_sender(self) -> ABCMember:
        """
        :return: 消息发送者
        """
        return await self._bot.get_member(self._sender)

    def get_id(self) -> str:
        """
        :return: 消息 ID
        """
        return self._msg_id

    def get_send_time(self) -> int:
        """
        :return: 消息发送时间
        """
        return self._send_time

    def get_quote(self) -> ABCMessage:
        """
        :return: 引用的消息
        """
        return self._quote

    def set_quote(self, msg: ABCMessage):
        """
        引用消息
        """
        self._quote = msg

    def get_room_id(self) -> int:
        """
        :return: 房间 ID
        """
        return self._room_id

    def get_villa_id(self) -> int:
        """
        :return: 别野 ID
        """
        return self._villa_id


class TextMessage(Message, ABCTextMessage):
    _text: str

    def __init__(self, bot: ABCBot, text: str = '', msg_id: str = '-1', send_time: int = -1, room_id: int = -1,
                 villa_id: int = -1, sender: int = -1, quote: ABCMessage = None):
        super().__init__(bot=bot, msg_id=msg_id, send_time=send_time, sender=sender,
                         room_id=room_id, villa_id=villa_id, quote=quote)
        self._text = text

    def get_text(self) -> str:
        """
        :return: 消息文本
        """
        return self._text

    def __str__(self):
        return f'[{self._room_id}] [{self._sender}] {self._text}'

    async def serialize(self) -> dict:
        """
        :return: 序列化的消息
        """
        text = ''
        texts = self._text.split('(met)')
        offset = 0
        entities = []
        user_id_list = []
        for i in range(len(texts)):
            if (i % 2) - 1 == 0 and i != len(texts) - 1:
                member = await self._bot.get_member(int(texts[i]))
                texts[i] = f'@{member.get_name()}'
                user_id_list.append(member.get_uid())
                entities.append({
                    'entity': {
                        'type': 'mentioned_user',
                        'user_id': f'{member.get_uid()}'
                    },
                    "length": len(texts[i]),
                    "offset": offset
                })
            offset += len(texts[i])
            text += texts[i]
        if len(texts) % 2 == 0:
            texts.append('(met)')
        out = {
            'content': {
                'text': text,
                'entities': entities
            },
            'mentionedInfo': {
                "type": 2,
                "userIdList": user_id_list
            }
        }
        if self.get_quote() is not None:
            out['quote'] = {
                "original_message_id": self.get_quote().get_id(),
                "original_message_send_time": self.get_quote().get_send_time(),
                "quoted_message_id": self.get_quote().get_id(),
                "quoted_message_send_time": self.get_quote().get_send_time()
            }
        return out

    @classmethod
    def get_type(cls) -> str:
        """
        :return: 消息类型
        """
        return 'MHY:Text'


class ImageMessage(Message, ABCImageMessage):
    _url: str

    def __init__(self, bot: ABCBot, url: str = '', msg_id: str = '-1', send_time: int = -1, room_id: int = -1,
                 villa_id: int = -1, sender: int = -1, quote: ABCMessage = None):
        super().__init__(bot=bot, msg_id=msg_id, send_time=send_time, sender=sender,
                         room_id=room_id, villa_id=villa_id, quote=quote)
        self._url = url

    def __str__(self):
        return f'[{self._room_id}] [{self._sender}] :img[{self._url}]'

    def get_url(self) -> str:
        """
        :return: 图片链接
        """
        return self._url

    async def serialize(self) -> dict:
        """
        :return: 序列化的消息
        """
        out = {
            'content': {
                'url': self._url
            }
        }
        if self.get_quote() is not None:
            out['quote'] = {
                "original_message_id": self.get_quote().get_id(),
                "original_message_send_time": self.get_quote().get_send_time(),
                "quoted_message_id": self.get_quote().get_id(),
                "quoted_message_send_time": self.get_quote().get_send_time()
            }
        return out

    @classmethod
    def get_type(cls) -> str:
        """
        :return: 消息类型
        """
        return 'MHY:Image'
