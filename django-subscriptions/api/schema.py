import asyncio

import strawberry
from strawberry.types import Info

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"


@strawberry.type
class Mutation:
    @strawberry.field
    async def send_message(self, info: Info, message: str) -> bool:
        print("sending on_message")
        print(id(info.context.broadcast))
        await info.context.broadcast.publish(channel="chatroom", message=message)

        return True


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def on_message(self, info: Info) -> str:
        print("starting on_message")
        print(id(info.context.broadcast))

        async with info.context.broadcast.subscribe(channel="chatroom") as subscriber:
            print(f"{subscriber=}")
            async for event in subscriber:
                print(f"{event=}")
                yield event.message

    @strawberry.subscription
    async def count(self, target: int = 100) -> int:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
