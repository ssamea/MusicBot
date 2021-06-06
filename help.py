from lib2to3.pgen2 import driver

import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import help
from main import bot


@bot.command()
async def Help(ctx):
    await ctx.send(embed = discord.Embed(title='도움말',description="""
\n!Help -> 뮤직봇의 모든 명령어를 볼 수 있습니다.
\n!join -> 뮤직봇을 자신이 속한 채널로 부릅니다.
\n!exit -> 뮤직봇을 자신이 속한 채널에서 내보냅니다.
\n!play [노래이름] -> 뮤직봇이 노래를 검색해 틀어줍니다.
\n!stop -> 현재 재생중인 노래를 끕니다.
!pause -> 현재 재생중인 노래를 일시정지시킵니다.
!replay -> 일시정지시킨 노래를 다시 재생합니다.
\n!now -> 지금 재생되고 있는 노래의 제목을 알려줍니다.
\n!chart -> 최신 멜론차트를 재생합니다.
\n!bookmark -> 자신의 즐겨찾기 리스트를 보여줍니다.
!add_bookmark [노래이름] -> 뮤직봇이 노래를 검색해 즐겨찾기에 추가합니다.
!rm_bookmark [숫자] ->자신의 즐겨찾기에서 숫자에 해당하는 노래를 지웁니다.
\n!list -> 이어서 재생할 노래목록을 보여줍니다.
!listplay -> 목록에 추가된 노래를 재생합니다.
!init -> 목록에 추가된 모든 노래를 지웁니다.
\n!add [노래] -> 노래를 대기열에 추가합니다.
!rm [숫자] -> 대기열에서 입력한 숫자에 해당하는 노래를 지웁니다.""", color = 0x00ff00))
