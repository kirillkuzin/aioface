import typing
from dataclasses import dataclass, asdict

from aioface.fb.utils import fb_dict_factory

import aiohttp


@dataclass
class FacebookButton:
    title: str
    type: str
    payload: str = None
    url: str = None


@dataclass
class FacebookTemplate:
    title: str
    subtitle: str = None
    image_url: str = None
    buttons: typing.List[FacebookButton] = None


@dataclass
class FacebookQuickReply:
    content_type: str
    payload: typing.Union[str, int] = None
    title: str = None
    image_url: str = None


@dataclass
class FacebookAttachmentPayload:
    template_type: str = None
    elements: typing.List[FacebookTemplate] = None
    url: str = None
    is_reusable: bool = False


@dataclass
class FacebookAttachment:
    type: str
    payload: FacebookAttachmentPayload


class FacebookResponse:
    def __init__(self,
                 recipient_id: str,
                 page_token: str = None,
                 text: str = None,
                 attachment: FacebookAttachment = None,
                 quick_replies: typing.List[FacebookQuickReply] = None,
                 sender_action: str = None):
        if text is None and attachment is None:
            if sender_action is None:
                raise ValueError
        elif text is not None and attachment is not None:
            raise ValueError
        elif sender_action is not None:
            raise ValueError
        self.page_token = page_token
        self.recipient_id = recipient_id
        self.text = text
        self.attachment = attachment
        self.quick_replies = quick_replies
        self.sender_action = sender_action

    async def send(self):
        data = self._build()
        async with aiohttp.ClientSession() as session:
            await session.post(
                url='https://graph.facebook.com/v2.6/me/messages',
                params={'access_token': self.page_token},
                json=data
            )

    def _build(self):
        body = {'recipient': {'id': self.recipient_id},
                'message': dict()}
        if self.text is not None:
            body['message']['text'] = self.text
        elif self.attachment is not None:
            body['message']['attachment'] = asdict(
                obj=self.attachment,
                dict_factory=fb_dict_factory
            )
        elif
        if self.quick_replies is not None:
            body['message']['quick_replies'] = [
                asdict(obj=reply, dict_factory=fb_dict_factory)
                for reply in self.quick_replies
            ]
        print(body)
        return body


class FacebookRequest:
    def __init__(self,
                 page_token: str,
                 sender_psid: int,
                 message_text: str,
                 contains=None):
        self.page_token = page_token
        self.sender_psid = sender_psid
        self.message_text = message_text
        self.contains = contains

    async def response(self, text: str):
        request_body = {'recipient': {'id': self.sender_psid},
                        'message': {'text': text}}
        print(request_body)
        async with aiohttp.ClientSession() as session:
            await session.post(
                url=f'https://graph.facebook.com/v2.6/me/messages',
                params={'access_token': self.page_token},
                json=request_body
            )
