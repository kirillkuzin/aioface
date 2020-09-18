import typing
from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    def get_data(self, user_id: str) -> typing.Dict:
        raise NotImplementedError

    @abstractmethod
    def set_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    @abstractmethod
    def update_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    def reset_data(self, user_id: str):
        self.set_data(user_id=user_id, data=dict())
