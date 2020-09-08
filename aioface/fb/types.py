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
class FacebookAddress:
    street_1: str = None
    street_2: str = None
    city: str = None
    postal_code: str = None
    state: str = None
    country: str = None


@dataclass
class FacebookSummary:
    subtotal: float = None
    shipping_cost: float = None
    total_tax: float = None
    total_cost: float = None


@dataclass
class FacebookAdjustment:
    name: str = None
    amount: float = None


@dataclass
class FacebookTemplate:
    title: str
    subtitle: str = None
    image_url: str = None
    default_action: FacebookButton = None
    buttons: typing.List[FacebookButton] = None
    quantity: float = None
    price: float = None
    currency: str = None


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
    elements: typing.List[FacebookTemplate] = None
    buttons: typing.List[FacebookButton] = None
    url: str = None
    is_reusable: bool = None
    recipient_name: str = None
    merchant_name: str = None
    order_number: str = None
    currency: str = None
    payment_method: str = None
    order_url: str = None
    timestamp: str = None
    summary: FacebookSummary = None
    adjustments: typing.List[FacebookAdjustment] = None
    address: FacebookAddress = None


@dataclass
class FacebookAttachment:
    type: str
    payload: FacebookAttachmentPayload
