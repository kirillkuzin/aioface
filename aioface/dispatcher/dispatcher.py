import typing
from dataclasses import dataclass

from aioface.storages.base_storage import BaseStorage
from aioface.fb.facebook_request import FacebookResponse
import aioface.dispatcher.utils as utils


@dataclass
class Filter:
    full_text: typing.Union[str, typing.List[str]]
    contains: typing.Union[str, typing.Set[str]]


@dataclass
class Handler:
    callback: typing.Callable
    filter: Filter


class Dispatcher:
    def __init__(self, storage: BaseStorage):
        self.storage = storage
        self.handlers: typing.List[Handler] = list()

    @staticmethod
    def create_filter_object(
            full_text: typing.Union[str, typing.List[str]] = None,
            contains: typing.Union[str, typing.List[str]] = None
    ) -> Filter:
        return Filter(full_text=full_text,
                      contains=set(contains) if contains else None)

    def register_message_handler(
            self,
            callback: typing.Callable,
            full_text: typing.Union[str, typing.List[str]] = None,
            contains: typing.Union[str, typing.List[str]] = None
    ):
        filter_obj = self.create_filter_object(full_text=full_text,
                                               contains=contains)
        handler_obj = Handler(callback=callback, filter=filter_obj)
        self.handlers.append(handler_obj)

    def message_handler(
            self,
            full_text: typing.Union[str, typing.List[str]] = None,
            contains: typing.Union[str, typing.List[str]] = None
    ):
        def decorator(callback):
            self.register_message_handler(callback=callback,
                                          full_text=full_text,
                                          contains=contains)
            return callback
        return decorator

    async def notify_handler(self, fb_request):
        fb_response = FacebookResponse(recipient_id=fb_request.sender_psid,
                                       text='Server error')
        for handler_obj in self.handlers:
            filter_obj = handler_obj.filter
            if not utils.check_full_text(
                    fb_full_text=fb_request.message_text,
                    filter_full_text=filter_obj.full_text):
                continue
            if not utils.check_contains(fb_contains=fb_request.contains,
                                        filter_contains=filter_obj.contains):
                continue
            fb_response = await handler_obj.callback(fb_request)
            break
        await fb_response.send()
