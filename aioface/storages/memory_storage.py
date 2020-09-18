import typing

from .base_storage import BaseStorage


class MemoryStorage(BaseStorage):
    def __init__(self):
        self.data = {}

    def get_data(self, user_id: str) -> typing.Dict:
        if user_id not in self.data:
            self.data[user_id] = {}
        return self.data[user_id]

    def set_data(self, user_id: str, data: typing.Dict):
        self.data[user_id] = data

    def update_data(self, user_id: str, data: typing.Dict):
        self.data[user_id].update(data)
