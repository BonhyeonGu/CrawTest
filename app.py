import random
import asyncio

import discord
from discord.ext import tasks, commands

from private import BOT_TOKEN
from craw00 import Craw00

intents = discord.Intents.default()  # 기본 intents 활성화
intents.messages = True  # 메시지 관련 이벤트 수신을 위해 활성화
intents.guilds = True  # 서버(길드) 관련 이벤트 수신을 위해 활성화
intents.message_content = True #v2
bot = commands.Bot(command_prefix='!', intents=intents)

craw00 = Craw00(bot)
tasks = {"craw00": craw00}


@bot.command()
async def start(ctx, task_name):
    task = tasks.get(task_name)
    if task and not task.is_running:
        task.is_running = True
        await ctx.send(f"{task_name} 크롤링을 시작합니다.")
        bot.loop.create_task(task.run(ctx.channel.id))  # bot 객체를 전달합니다.
    elif not task:
        await ctx.send("잘못된 명령입니다.")
    else:
        await ctx.send(f"{task_name} 크롤링이 이미 실행 중입니다.")


@bot.command()
async def stop(ctx, task_name):
    task = tasks.get(task_name)
    if task and task.is_running:
        task.is_running = False
        await ctx.send(f"{task_name} 크롤링을 중지합니다.")
    elif not task:
        await ctx.send("잘못된 명령입니다.")
    else:
        await ctx.send(f"{task_name} 크롤링이 이미 중지되었습니다.")


bot.run(BOT_TOKEN)