import asyncio
import os
import random

import discord
import fastapi

import gen

USER_ID = int(os.getenv("USER_ID"))
last_msg: str
on_last_msg = asyncio.Event()
background_tasks = set()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        global last_msg
        if message.author.id == USER_ID:
            print(f"< {message.content}")
            last_msg = message.content
            on_last_msg.set()


app = fastapi.FastAPI()
client = MyClient(chunks_guilds_on_startup=False)


@app.on_event("startup")
async def start_discord_client():
    await client.login(os.getenv("TOKEN"))
    task = asyncio.create_task(client.connect(reconnect=True))
    background_tasks.add(task)


@app.get("/random")
async def get_random():
    user = client.get_user(USER_ID)

    async with user.dm_channel.typing():
        await asyncio.sleep(random.randint(10, 30) / 10)
        content = gen.gen()
        print(f"> {content}")

        await user.dm_channel.send(content=content)

    on_last_msg.clear()
    await on_last_msg.wait()

    return last_msg
