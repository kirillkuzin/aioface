import typing

from dataclasses import dataclass


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
