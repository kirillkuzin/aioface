import typing
from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    async def get_data(self, user_id: str) -> typing.Dict:
        raise NotImplementedError

    @abstractmethod
    async def set_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    @abstractmethod
    async def update_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    @abstractmethod
    async def reset_data(self, user_id: str):
        await self.set_data(user_id=user_id, data=dict())
