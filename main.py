import discord
from discord.ext import commands


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

bot.run('ODQzMDM3MDEzNjE4OTgyOTMy.YJ-BZg.2HAzNjVvFU0Ctzxxm0r14r9iGQo')