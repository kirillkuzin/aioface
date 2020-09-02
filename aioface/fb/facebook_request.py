import typing
from dataclasses import dataclass, asdict

from aioface import config
from aioface.fb.utils import fb_dict_factory

import aiohttp


@dataclass
class FacebookButton:
    type: str
    title: str = None
    payload: str = None
    url: str = None
    messenger_extensions: bool = None
    webview_height_ratio: str = None
    fallback_url: str = None


@dataclass
class FacebookTemplate:
    title: str
    subtitle: str = None
    image_url: str = None
    default_action: FacebookButton = None
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
    text: str = None
    top_element_style: str = None
    elements: typing.List[FacebookTemplate] = None
    buttons: typing.List[FacebookButton] = None
    url: str = None
    is_reusable: bool = None


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
                url=config.GRAPH_API_URL,
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
                 message_text: str):
        self.page_token = page_token
        self.sender_psid = sender_psid
        self.message_text = message_text
        self.contains = None
