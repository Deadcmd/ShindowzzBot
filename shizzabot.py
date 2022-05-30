from http import client
from sys import prefix
from tkinter import BOTTOM
from urllib import response
import discord
import requests
import os
import io
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
clent = commands.Bot(command_prefix = 's!')
clent.remove_command('help')

#bot start
@clent.event
async def on_ready():  
    print('bot started!')
    
    await clent.change_presence(status = discord.Status.idle, activity = discord.Game('s!help'))
    
@clent.event 
async def on_member_join(member):
    guild = clent.get_guild(964241360184033300)
    channel = guild.get_channel(968479980868735026)
    emb = discord.Embed(title = 'Привет!', description = 'Приветствую {member.mention} на сервере!', colour = discord.Color.green())
    await ctx.send(embed = emb)

@clent.event 
async def on_command_error( ctx, error ):
    pass

#clear messages
@clent.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount : int ):
    await ctx.channel.purge(limit = amount )

#about
@clent.command(pass_context = True)
async def about(ctx):
    await ctx.send("Привет! Я ШиндовззБот! Список моих команд по команде s!help. Ах, да вот сервер моего создателя: https://discord.gg/uMSJqkb26S")

#kick
@clent.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed(title = 'Кик', colour = discord.Color.red())
   
    emb.set_author(name = member.name, icon_url = member.avatar_url)
    emb.add_field(name = 'Кик участника', value = 'Кикнут : {}' .format(member.mention))
    await ctx.send(embed = emb)
   
    await member.kick(reason = reason)
    #await ctx.send(f'kick user {member.mention}')

#ban
@clent.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed(title = 'Бан', colour = discord.Color.red())
    await ctx.channel.purge(limit = 1)

    await member.ban(reason = reason)

    emb.set_author(name = member.name, icon_url = member.avatar_url)
    emb.add_field(name = 'Бан участника', value = 'Забанен : {}' .format(member.mention))
    await ctx.send(embed = emb)

    #await ctx.send(f'Участник {member.mention} забанен!')

#mute
@clent.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member):
    emb = discord.Embed(title = 'Мьют', colour = discord.Color.red())
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

    await member.add_roles(mute_role)

    emb.set_author(name = member.name, icon_url = member.avatar_url)
    emb.add_field(name = 'Мьют участника', value = 'Замьючен : {}' .format(member.mention))
    await ctx.send(embed = emb)

    #await ctx.send(f'Учасник {member.mention}, замьчен за нарушение правил!')
    
#help
@clent.command(pass_context = True)

async def help(ctx):
    emb = discord.Embed(title = '**_Навигация по командам_**', colour = discord.Color.blue())

    emb.add_field(name ='s!about', value='Немного о боте')
    emb.add_field(name ='s!clear', value='Очистка чата')
    emb.add_field(name ='s!ban', value='Бан участника')
    emb.add_field(name ='s!kick', value='Кик участника')
    emb.add_field(name ='s!mute', value='Мьют участника')
    emb.add_field(name ='s!warn', value='Дать пред участнику(скоро)')
    emb.add_field(name ='s!user', value='Инфо об учаснике')

    await ctx.send(embed = emb)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, укажи сколько сообщений надо удалить!')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, у тебя недостаточно прав!')
      
@mute.error
async def mute_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, у тебя недостаточно прав!')

@ban.error
async def ban_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, у тебя недостаточно прав!')

@kick.error
async def kick_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, у тебя недостаточно прав!')

token = OTY3NzU2MjUxMDY2OTMzMjc4.YmU7Pg.eLJ_rdijAF2MTPniOsHVJHSwqiQ

clent.run( token )