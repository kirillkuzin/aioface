import typing


class BaseStorage:

    async def get_data(self, user_id: str) -> typing.Dict:
        raise NotImplementedError

    async def set_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    async def update_data(self, user_id: str, data: typing.Dict):
        raise NotImplementedError

    async def reset_data(self, user_id: str):
        await self.set_data(user_id=user_id, data=dict())
