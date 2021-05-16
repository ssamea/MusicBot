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

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def greet(ctx,*,text):
    await ctx.send(embed=discord.Embed(title='따라쟁이', description= text,color=0x00ff00))

@bot.command()
async def join(ctx):
    try:
        global vc
        vc= await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)

        except:
            await ctx.send("채널에 플레이어가 없네요...")

@bot.command()
async def exit(ctx):
    try:
        await vc.disconnect()

    except:
        await ctx.send("이미 그 채널에서 나왔어요!")


#@bot.command()
#async def play(ctx, *, url):
#    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
#    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

#    if not vc.is_playing():
 #       with YoutubeDL(YDL_OPTIONS) as ydl:
  #          info = ydl.extract_info(url, download=False)
   #     URL = info['formats'][0]['url']
    #    vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)) #FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)
     #   await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    #else:
     #   await ctx.send("노래가 이미 재생되고 있습니다!")


@bot.command()
async def play(ctx, *, msg):
    if not vc.is_playing():
        global entireText
        # ffmpeg 와 youtube_dl의 기본 설정
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}

        # 크롬 드라이버랑 셀레니움을 활용하여 유튜브에서 영상 제목과 링크등을 가져오는 곳.
        chromedriver_dir = r"C:\Users\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get("https://www.youtube.com/results?search_query=" + msg + "+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com' + musicurl

        # url 재생과 마찬가지로 음악을 재생하는 부분
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(
            embed=discord.Embed(title="노래 재생", description="현재 " + entireText + "을(를) 재생하고 있습니다.", color=0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

bot.run('본인의 토큰을 여기에 붙여주세용')