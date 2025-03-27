#    ____  _       _ __        __   _       __                     __  __  
#   / __ \(_)___ _(_) /_____ _/ /  | |     / /___ __________ ___  / /_/ /_ 
#  / / / / / __ `/ / __/ __ `/ /   | | /| / / __ `/ ___/ __ `__ \/ __/ __ \
# / /_/ / / /_/ / / /_/ /_/ / /    | |/ |/ / /_/ / /  / / / / / / /_/ / / /
#/_____/_/\__, /_/\__/\__,_/_/     |__/|__/\__,_/_/  /_/ /_/ /_/\__/_/ /_/ 
#        /____/                       
#
# The MIT License (MIT)
#
# Copyright (c) 2025 thedvrkwolf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import discord
from discord.ext import commands
import os
from itertools import count
import aiohttp
import time
import random
from discord import app_commands
import datetime
from io import BytesIO
import platform
import calendar
import math
from discord.ext import tasks
import asyncio
from discord.utils import get
from discord.ext.commands import MissingPermissions, BadArgument, CommandOnCooldown
import json
from discord.ui import Button, Select, View, Modal
import logging
import re
import requests

from commands.Ticket.TicketOptions import Exchange_Options
from commands.Ticket.TicketCreation import  AfterClose, TicketOptions, AfterMM, ClaimMM
from commands.PrefixCommands.Application import Application, Delete, Button
from commands.PrefixCommands.SupportTickets import SupportOptions, SupportClose, AfterCloseSupport

#STATUS

with open('./private/botdata.json', 'r') as f:
       data = json.load(f)
            
status = data['bot-status']   

activity = discord.Activity(type=discord.ActivityType.watching, name=status) # <--------


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.members = True
        intents.presences = False

        super().__init__(command_prefix=',', intents=intents, case_insensitive=True, activity=activity, status=discord.Status.online)

    async def setup_hook(self) -> None:
        self.add_view(Exchange_Options())

        self.add_view(AfterClose())
        self.add_view(TicketOptions())
        self.add_view(ClaimMM())
        self.add_view(AfterMM())

        self.add_view(Application())
        self.add_view(Delete())
        self.add_view(Button())

        self.add_view(SupportOptions())
        self.add_view(SupportClose())
        self.add_view(AfterCloseSupport())


        
bot = PersistentViewBot()

#RUN

@bot.event
async def on_ready():
    
    Total.start()
    Checker.start()
    WeeklyCheckup.start()
    
    print("--------------------")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(
        f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    await asyncio.sleep(2)
    members = [*bot.get_all_members()]
    print("-------------------")
    await asyncio.sleep(0.5)
    print(f'Logged in as: {bot.user} | {bot.user.id}')
    await asyncio.sleep(0.5)
    print(f'Servers Count: {len(bot.guilds)}')
    await asyncio.sleep(0.5)
    print(f'Users Count: {len(members)}')
    await asyncio.sleep(1)
    print('-------------------')
    await asyncio.sleep(0.5)
    print(f'⏳ Ping => [{round(bot.latency*1000)}] ms')
    await asyncio.sleep(1)
    print('-------------------')
    await asyncio.sleep(0.5)
    print('Everything is okay ->')
    await asyncio.sleep(0.5)
    print('Bot is Ready')
   


@bot.event
async def on_command_error(ctx, error):
        
        if isinstance(error, CommandOnCooldown):


            embed=discord.Embed(description=f"`❌` — **You are in cooldown**! Please wait `{error.retry_after:.2f}` more seconds.", color=0xe74c3c)
            await ctx.reply(embed=embed, delete_after=5)


            
            

@tasks.loop(seconds=1) 
async def WeeklyCheckup():
    
   with open('./private/botdata.json', 'r') as f:
       data = json.load(f)
            
   guild_id = data['guild-id']   
   notify_id = data['weekly-notify-channel-id']  

   roles = []
               
   for i in data["exchangers"]:
       roles.append(i) 
                        
   try:

    today = datetime.datetime.now()

    with open("./database/WeeklyCheckup.json") as f:
      data = json.load(f)

    mr = data[f"minutes"]
    hr = data['hours']
    dr = data['days']
    sr = data['seconds']

    yrr = data["cminutes"]
    mrr = data['chours']
    drr = data['cdays']
    hrr = data['cmonth']
    mnrr = data['cyear']
    srr = data['cseconds']   

    timestamp = data['timestamp']

    with open("./database/WeeklyCheckup.json", 'w') as f:
      json.dump(data, f)

    a = int(today.strftime(r"%Y"))*31540000
    b = int(today.strftime(r"%m"))*2628000
    c = int(today.strftime(r"%d"))*86400
    d = int(today.strftime(r"%H"))*3600
    e = int(today.strftime(r"%M"))*60
    f = int(today.strftime(r"%S"))

    

                    

    hours = hr + mrr
    days = dr + drr
    minutes = mr + yrr
    year = mnrr
    months = hrr
                    
    for i in range(20):     
     if minutes>60 or minutes == 60:
       hours += 1
       minutes = 0

       if hours > 24 or hours == 24:
             hours = 0
             days += 1
                                 
    if months == 1:
                            if days > 31:
                             days -= 31
                             months += 1
                            else:
                             pass
                             
    elif months == 2:
                            if days > 29:
                             days -= 29
                             months += 1
                            else:
                             pass
                                                  
    elif months == 3:
                            if days > 31:
                             days -= 31
                             months += 1
                            else:
                             pass
                             
    elif months == 4:
                            if days > 30:
                             days -= 30
                             months += 1
                            else:
                             pass
                             
    elif months == 5:
                            if days > 31:
                             days -= 31
                             months += 1
                            else:
                             pass
                             
    elif months == 6:
                            if days > 30:
                             days -= 30
                             months += 1
                            else:
                             pass
                             
    elif months == 7:
                            if days > 31:
                             days -= 31
                             months += 1
                            else:
                             pass
                             
    elif months == 8:
                            if days > 31:
                             days = 1
                             months += 1
                            else:
                             pass
                             
    elif months == 9:
                            if days > 30:
                             days -= 30
                             months += 1
                            else:
                             pass
                             
    elif months == 10:
                            if days > 31:
                             days -= 31
                             months += 1
                            else:
                             pass
                             
    elif months == 11:
                            if days > 30:
                             days -= 30
                             months += 1
                            else:
                             pass
                             
    elif months == 12:
                            if days > 31:
                             days -= 31
                             months += 1

                             if months > 12:
                                 year += 1
                                 months -= 12
                             else:
                                pass
                            else:
                             pass
    
   
    sum1 = a+b+c+d+e+f

    sum2 = months*2628000 + year*31540000 + minutes*60 + days*86400 + hours*3600 + srr

    
    
    if sum1 == sum2 or sum1 > sum2:
        
        users = []
        
        with open('./database/UserData.json', 'r') as f:
            data = json.load(f)
        
        for i in data:
            
            try:
                
              data[str(i)]['Weekly-Exchanged']
             
              o = data[str(i)]['Weekly-Exchanged']['Orders']
              t = data[str(i)]['Weekly-Exchanged']['Total-Exchanged']
                
              if o < 10:
                
                try:
                
                  guild = bot.get_guild(guild_id)
                  user = await guild.fetch_member(int(i))
                
                  n_check = 0
                
                  for op in user.roles:
                        if op.id in roles:
                            n_check += 1
                 
                  if n_check != 0:  
                    users.append(f'- {user.mention}, {user.name}: **{o}** orders (**{t}**€ Total Exchanged)\n')
                    
                except:
                  pass
            
              with open('./database/UserData.json', 'r') as f:
                    data = json.load(f)
            
              del data[str(i)]['Weekly-Exchanged']     
                
              with open('./database/UserData.json', 'w') as f:
                    json.dump(data, f, indent=1)
        
            except:
                try:
                  guild = bot.get_guild(guild_id)
                  user = await guild.fetch_member(int(i))
                
                  n_check != 0
                
                  for op in user.roles:
                        if op.id in roles:
                            n_check += 1
                 
                  if n_check != 0:  
                    users.append(f'- {user.mention}, {user.name}: **0**! orders (**0**€! Total Exchanged)\n')
                
        
                except:
                  pass


        channel = bot.get_channel(int(notify_id))
            
        await channel.send(f'@everyone\n\nFollowing exchangers did not pass the minimum deals (per week):')
        
        for i in users:
            await channel.send(i)
        
        with open("./database/WeeklyCheckup.json") as f:
          data = json.load(f)

    
        now = datetime.datetime.now()

    
    
    
    
    
    
    
    
        y = today.strftime(r"%Y")
        m = today.strftime(r"%m")
        d = today.strftime(r"%d")
        h = today.hour 
        mn = today.strftime(r"%M")
        s = today.strftime(r"%S")
    
        data[f"minutes"] = 0
        data['hours'] = 0
        data['days'] = 7
        data['seconds'] = 0
    
        data["cminutes"] = int(mn)
        data['chours'] = int(h)
        data['cdays'] = int(d)
        data['cmonth'] = int(m)
        data['cyear'] = int(y)
        data['cseconds'] = int(s)

        
        
        hours = int(h)
        days = int(d) + 7
        minutes = int(mn)
        year = int(y)
                    
                    
        for i in range(20):
                    if minutes>60 or minutes == 60:
                       hours += 1
                       minutes = 0
                       if hours > 24 or hours == 24:
                          hours = 0
                          days += 1
                    
                    
        if int(m) == 1:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 2:
                            if days > 29:
                             days -= 29
                             months = int(m) + 1
                            else:
                             months = int(m)  
                                                  
        elif int(m) == 3:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 4:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 5:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 6:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 7:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 8:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 9:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 10:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 11:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
        elif int(m) == 12:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1

                             if months > 12:
                                 year = int(y) + 1
                                 months -= 12
                             else:
                                pass
                            else:
                             months = int(m)
                             


        d = datetime.datetime(year, months, days, hours, minutes, int(s))

        time_stamp = calendar.timegm(d.timetuple())
        
        
        
        
        
        data['timestamp'] = str(time_stamp)

        with open("./database/WeeklyCheckup.json", 'w') as f:
          json.dump(data, f)
       
      
   except:
    
    with open("./database/WeeklyCheckup.json") as f:
      data = json.load(f)

    
    now = datetime.datetime.now()
    
    y = today.strftime(r"%Y")
    m = today.strftime(r"%m")
    d = today.strftime(r"%d")
    h = today.hour 
    mn = today.strftime(r"%M")
    s = today.strftime(r"%S")
    
    data[f"minutes"] = 0
    data['hours'] = 0
    data['days'] = 7
    data['seconds'] = 0
    
    data["cminutes"] = int(mn)
    data['chours'] = int(h)
    data['cdays'] = int(d)
    data['cmonth'] = int(m)
    data['cyear'] = int(y)
    data['cseconds'] = int(s)

    
    hours = int(h)
    days = int(d) + 7
    minutes = int(mn)
    year = int(y)
                    
                    
    for i in range(20):
                    if minutes>60 or minutes == 60:
                       hours += 1
                       minutes = 0
                       if hours > 24 or hours == 24:
                          hours = 0
                          days += 1
                    
                    
    if int(m) == 1:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 2:
                            if days > 29:
                             days -= 29
                             months = int(m) + 1
                            else:
                             months = int(m)  
                                                  
    elif int(m) == 3:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 4:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 5:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 6:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 7:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 8:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 9:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 10:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 11:
                            if days > 30:
                             days -= 30
                             months = int(m) + 1
                            else:
                             months = int(m)
                             
    elif int(m) == 12:
                            if days > 31:
                             days -= 31
                             months = int(m) + 1

                             if months > 12:
                                 year = int(y) + 1
                                 months -= 12
                             else:
                                pass
                            else:
                             months = int(m)
                             


    d = datetime.datetime(year, months, days, hours, minutes, int(s))

    time_stamp = calendar.timegm(d.timetuple())
        
        
        
        
        
    data['timestamp'] = str(time_stamp)

    with open("./database/WeeklyCheckup.json", 'w') as f:
      json.dump(data, f)
            
            
            
 
            

@tasks.loop(seconds=1)
async def Checker():

    
    with open('./database/UserData.json', 'r') as f:
       data = json.load(f)

    
    for i in data:
      try:
       c = data[str(i)]['Current']
       m = data[str(i)]['max']

       if c < 0:
            data[str(i)]['Current'] = 0
            
            with open('./database/UserData.json', 'w') as f:
                json.dump(data, f, indent=1)
                
                
       if c > m:
            data[str(i)]['Current'] = m
            
            with open('./database/UserData.json', 'w') as f:
                json.dump(data, f, indent=1)
        
    
    
      except:
            pass
    

@tasks.loop(seconds=3600)
async def Total():

 with open('./private/botdata.json', 'r') as f:
    data = json.load(f)
            
 guild_id = data['guild-id']   
 vouch_channel_id = data['vouch-channel-id']
 total = data['total-exchanged-voice-id']
    
 guild = bot.get_guild(guild_id)   
 
 with open("./database/UserData.json") as f:
            data = json.load(f)

 l = 0

 for user in data:
       try:
         l += round(data[user]["Total-Exchanged"], 2)
       except:
         pass
        
 
 with open("data.json") as f:
      data = json.load(f)
    
 last = data['last']

 l = round(l)

 channel = bot.get_channel(total)


 just = channel.name


 j = re.findall('\d+', just)
   
 try:
    j1 = j[1]
    
 except:
    j1 = None
    
 try:
    j2 = j[2]
    
 except:
    j2 = None
  
 try:
    j3 = j[3]
    
 except:
    j3 = None
    
 t = f"{j[0]}{f'{j1}' if j1 != None else ''}{f'{j2}' if j2 != None else ''}{f'{j3}' if j3 != None else ''}" 


 if last != int(float(l)):
        
    s = int(float(l)) - last + int(t)
        
    await channel.edit(name=f'Exchanged: {s:,}€')
    data['last'] = int(float(l))

    with open("data.json", 'w') as f:
      json.dump(data, f)

 channel = bot.get_channel(vouch_channel_id)

 counter = 0
 async for message in channel.history(limit=None):
        counter += 1
        
 s = int(counter)       
 
 with open("vouches.json") as f:
     data = json.load(f) 
        
 number = data['number']

 if s >= number:
    sy = s
    await channel.edit(name=f'vouches-{sy:,}')  
    
    data['number'] = s
    
    with open("vouches.json", 'w') as f:
        json.dump(data, f)





async def load_cogs():
    print('----------------------------------')   
    print('--Prefix Cogs [s!]----------------')             
    print('----------------------------------')    
    for filename in os.listdir('./commands/PrefixCommands'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.PrefixCommands.{filename[:-3]}')
                print(f"Loaded extension '{filename}'")
                print('---- ✔ -----------------------------')
            except Exception as e:
                print('---- :x: -----------------------------')
                print(f"Failed to load extension '{filename}'\n{type(e).__name__}: {e}")
                print('----------------------------------')
    
    print('--Ticket Cogs [/]------------------')             
    print('----------------------------------')             
    for filename in os.listdir('./commands/Ticket'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.Ticket.{filename[:-3]}')
                print(f"Loaded extension '{filename}'")
                print('---- ✔ -----------------------------')
            except Exception as e:
                print('---- :x: -----------------------------')
                print(f"Failed to load extension '{filename}'\n{type(e).__name__}: {e}")
                print('----------------------------------')
  



@bot.remove_command('help')

# HELP -------------------------------------------------------------------

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed1 = discord.Embed(
        title='My Commands',
        description=(
            "— **FlipX Exchanges**:\n\n"
            "`,setamazon | ,setapple | ,setbtc | ,setcashapp | ,seteth | ,setltc | ,setpaypal | ,setpaysafe | ,setrevolut | ,setskrill | ,setusdt | ,setvenmo | ,setwise | ,setzelle` ⟶ Set your payment information.\n"
            "`,max` ⟶ View your max/remaining max.\n"
            "`,limit` ⟶ View your limit/remaining limit.\n"
            "`,profile` ⟶ View your profile.\n"
            "`,tos` ⟶ Shows the Terms of Service\n"
            "`,leaderboard` ⟶ FlipX leaderboard.\n\n"
            "— **Tickets**:\n\n"
            "`,add | ,remove` ⟶ Add someone with no access to a ticket/application | Remove someone from the ticket/application.\n"
            "`,done | ,cancel` ⟶ Complete or cancel the Exchange ticket.\n"
            "`,delete | ,close` ⟶ Delete or close the current ticket/application.\n"
            "`,transcript` ⟶ Generate a transcript of the current ticket/application.\n"
            "`,rename` ⟶ Rename ticket.\n"
            "`,remind` ⟶ Remind user by sending a private message.\n"
            "`,sec` ⟶ Explaining of Security.\n"
            "`,still` ⟶ Checks if the exchange is still needed.\n\n"
            "**Administrators**:\n"
            "`,apply | ,exchangeticket | ,supportticket` ⟶ Send ticket embed.\n"
            "`,addmax` ⟶ Add max to Exchanger.\n"
            "`,removemax` ⟶ Remove max from Exchanger.\n"
            "`,addlimit` ⟶ Add limit to Exchanger.\n"
            "`,removelimit` ⟶ Remove limit from Exchanger.\n"
            "`,blacklist | ,unblacklist` ⟶ Blacklist/unblacklist user from tickets.\n"
            "`,applyltc` ⟶ Send apply ltc embed.\n"
            "`,admin profile` ⟶ View archived profile.\n"
            "`,admin resetactive` ⟶ Reset user's active history."
        ),
        colour=0x6056ff
    )
    embed1.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon)

    msg = await ctx.reply(embed=embed1)

# REMIND -------------------------------------------------------------------------

@bot.command()
async def remind(ctx, user: discord.User, *, text=None):
    color = 0x6056ff
    embed = discord.Embed(description=f"{text if text else ''}", color=color)
    embed.description += f"\n-# **From:** {ctx.channel.jump_url}"
    embed.set_footer(text=f"Time: {ctx.message.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    await ctx.send(f"``✔️`` {user.mention} was notified about:", embed=embed)
    
    dm_embed = discord.Embed(description=f"{text if text else ''}", color=color)
    dm_embed.description += f"\n-# **From:** {ctx.channel.jump_url}"
    dm_embed.set_footer(text=f"Time: {ctx.message.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        await user.send(embed=dm_embed)
    except discord.Forbidden:
        await ctx.send(f"Could not send DM to {user.mention}. Their DMs might be closed.")

# STILL -------------------------------------------------------------------------

@bot.command()
async def still(ctx, user: discord.Member):
    await ctx.message.delete()

    color = 0x6056ff  

    def create_embed(title, description):
        embed = discord.Embed(title=title, description=description, color=color)
        return embed

    initial_embed = create_embed(
        title="Are you still wanna do this Exchange?",
        description="Please click **Yes** if you want to continue this\n deal, otherwise click on **No**.\n-# Ticket will be automatically denied within 5h"
    )

    class ConfirmView(View):
        def __init__(self, timeout=18000):  
            super().__init__(timeout=timeout)
            self.response = None

        async def on_timeout(self):
            await self.message.delete()

            
            ping_msg = await ctx.channel.send(f"{ctx.author.mention}")
            await ping_msg.delete()

            timeout_embed = create_embed(
                title="Not Interested",
                description="Exchange can be closed."
            )
            await ctx.send(f"{user.mention}", embed=timeout_embed)

        @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
        async def yes_button(self, interaction: discord.Interaction, button: Button):
            if interaction.user.id == user.id:
                self.response = "yes"
                await interaction.response.defer()
                await interaction.message.delete()

                
                ping_msg = await interaction.channel.send(f"{ctx.author.mention}")
                await ping_msg.delete()

                yes_embed = create_embed(
                    title="Still Interested",
                    description="Exchange can be continued as normal."
                )
                await interaction.channel.send(f"{user.mention}", embed=yes_embed)
                self.stop()
            else:
                await interaction.response.send_message("You are not allowed to respond to this.", ephemeral=True)

        @discord.ui.button(label="No", style=discord.ButtonStyle.red)
        async def no_button(self, interaction: discord.Interaction, button: Button):
            if interaction.user.id == user.id:
                self.response = "no"
                await interaction.response.defer()
                await interaction.message.delete()

                
                ping_msg = await interaction.channel.send(f"{ctx.author.mention}")
                await ping_msg.delete()

                no_embed = create_embed(
                    title="Not Interested",
                    description="Exchange can be closed."
                )
                await interaction.channel.send(f"{user.mention}", embed=no_embed)
                self.stop()
            else:
                await interaction.response.send_message("You are not allowed to respond to this.", ephemeral=True)

    view = ConfirmView()
    view.message = await ctx.send(f"{user.mention}", embed=initial_embed, view=view)

    try:
        await view.wait()
    except asyncio.TimeoutError:
        pass

#  Verify Embed [ Vaultcord ] ------------

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def verify(ctx):
        EmbedVerify = discord.Embed(
            title="Verification Required!",
            description="Click **\"Verify Now\"** to become an official Member of the **FlipX Community**",
            color=0x6056ff
        )
        EmbedVerify.set_image(url="https://cdn.discordapp.com/attachments/1322300070170726520/1329951840518803536/banner.jpg?ex=678c35ac&is=678ae42c&hm=6fedbed72bc398d9ede63c77a2ca9fd6e0816e9b90cf54a4429072d4c6437e56&")

        # Erstelle den Button mit dem Label direkt im Konstruktor
        button = Button(label="Verify Now", style=discord.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=1324511060958646372&redirect_uri=https://vaultcord.win/auth&response_type=code&scope=identify%20guilds.join%20email%20guilds&state=27385")

        view = View()
        view.add_item(button)

        await ctx.send(embed=EmbedVerify, view=view)

# AUTO REACTION -----------
@bot.event
async def on_ready():
    channel = bot.get_channel(1326690826444607585)
    async for message in channel.history(limit=None):
        if not message.author.bot:
            try:
                await message.add_reaction("<a:flareon_hearts:1329587161560780882>")
            except:
                pass
    print("Reactions added to existing messages.")

@bot.event
async def on_message(message):
    if message.channel.id == 1326690826444607585 and not message.author.bot:
        try:
            await message.add_reaction("<a:flareon_hearts:1329587161560780882>")
        except:
            pass

# TOS ------------------
@bot.command(name="tos")
async def tos(ctx):
    
    embed_color = 0x6056ff

    embed = discord.Embed(
        description=(
            "__**Exchanger Rules for FlipX**__\n\n"
            "__**Rules:**__\n"
            "- Don't talk any shit in tickets.\n"
            "- Always be respectful in tickets or in staff chat.\n"
            "- Don't talk bad about someone's religion.\n"
            "- Exchanging in staff chat is not allowed.\n"
            "- Taking lower fees or higher fees is not allowed.\n"
            "- No spam or advertising anywhere.\n"
            "- No illegal or prohibited items.\n"
            "- Always provide a screenshot as proof.\n"
            "- **No private deals outside the server**.\n"
            "  This means only to clients who are from these servers.\n"
            "\n**-> If you break any of these small rules, instant warn.**\n\n"
            "__**About Handling Warns:**__\n"
            "- We don't warn without a reason.\n"
            "- For every warn you get, you can open any time a [support](https://canary.discord.com/channels/1315035618048475246/1320348475958755361) ticket.\n"
            "- If you get 3 Warns, you will get a Team Kick Without Security Back.\n"
            "- Doing DM deals with any client of this server is an instant Team kick without Security Back.\n"
            "- We clear every month all warns.\n"
            "- If you don't respect any higher one, it is automatically a restriction of 12 hours.\n\n"
            "__**About Retirement:**__\n"
            "- If you want to retire, you need to show your apply ticket once.\n"
            "- We only accept HTML.\n"
            "- Apply tickets are getting instant-sent in your DMs.\n"
            "- You can retire after 14 days = 2 weeks.\n"
            "- Retirement process needs 5 days for safety.\n"
            "- Also, if you get termed, follow all the rules as retirement.\n\n"
            "__**What Happens if You Get Marked from Scammer Alert?**__\n"
            "- If you get marked from scammer alert as a scammer, it is an instant removal of roles.\n"
            "- Also means that your security is lost.\n"
            "- We don't care if you get unmarked (one time marked is enough).\n"
            "- If you have a report open against you, it is a role removal till you finish it.\n\n"
            "__**Monthly Donations:**__\n"
            "- We take every month 1€ to pay the host and the devs.\n"
            "- Payments are open on the first day of the month.\n"
            "- You have 24 hours to pay it.\n"
            "- If you don't pay, we will take the 1€ of your security.\n"
            "- Retire before it is not accepted; you would still need to pay the monthly amount.\n\n"
            "__**Final Note:**__\n"
            "You agree to all these rules when doing your first exchange. "
            "Also, after 24 hours, you get the roles."
        ),
        color=embed_color
    )
    await ctx.send(embed=embed)
# sec ------------------------------------------------------------------------------------------------------
@bot.command()
async def sec(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="What are security fees?",
        description=(
            "- Securities help us to refund the victims if they got scammed.\n"
            "- You have to pay securities fees.\n"
            "- You get your securities back once you retire."
        ),
        color=0x6056ff
    )
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
      
      with open('./private/botdata.json', 'r') as f:
          data = json.load(f)
            
      guild_id = data['guild-id']   
      vouch_channel_id = data['vouch-channel-id']
      categories = data['whitelisted-channels']
      
      try:
        if message.guild.id != guild_id:
            return
      except:
        return
      
      await bot.process_commands(message)
      
      if message.author.id == bot.user.id:
             return

    
      try:    
        if message.channel.id == vouch_channel_id:
          await message.add_reaction("<a:flareon_hearts:1329587161560780882>")
          
      except:
        pass  
        
    
      try:
        if message.author.guild_permissions.manage_messages:
             return
        if message.author.guild_permissions.administrator:
             return
        if message.author.id == message.guild.owner.id:
             return
            
      except:
        pass


      with open('./private/botdata.json', 'r') as f:
                data = json.load(f)
        
      r1 = discord.utils.get(message.guild.roles, id=data['trial-moderator'])
      r2 = discord.utils.get(message.guild.roles, id=data['moderator'])
        
      try:
                  
              
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        userid = data[f"{str(message.channel.id)}"]["Exchange-Request-User"]["ID"]  
        msgid = data[f"{str(message.channel.id)}"]["Message"] 

        try:
          data[f"{str(message.channel.id)}"]['Exchange-Complete-User']
          return
        
        except:
            
            try:
                count = data[f"{str(message.channel.id)}"]["Message-Count"]
                
                if count > 10:
                
                  embed=discord.Embed(title='Remember!', description=f"> Only deal in claimed tickets. If a scam occurs and the ticket isn’t claimed, you won’t get a refund.", color=0x73b2df)
                  await message.channel.send(f"<@{userid}>", embed=embed)
                
                
                  data[f"{str(message.channel.id)}"]["Message-Count"] = 1
                    
                else:
                  data[f"{str(message.channel.id)}"]["Message-Count"] += 1
                
                
            except:
                
                data[f"{str(message.channel.id)}"]["Message-Count"] = 1
           
        

        
            if r1 in message.author.roles or r2 in message.author.roles and not message.author.guild_permissions.administrator:
              try:
                  count = data[f"{str(message.channel.id)}"]["Message-Count-Mod"]

                    
                  if count > 4:
                    
                
                    embed=discord.Embed(title='Remember!', description=f"> Don’t deal with Moderators, otherwise you will not get any refund.", color=0x73b2df)
                    await message.channel.send(f"<@{userid}>", embed=embed)
                
                
                    data[f"{str(message.channel.id)}"]["Message-Count-Mod"] = 1
                    
                    
                  else:
                    data[f"{str(message.channel.id)}"]["Message-Count-Mod"] += 1
                
                
              except:
                
                embed=discord.Embed(title='Remember!', description=f"> Don’t deal with Moderators, otherwise you will not get any refund.", color=0x73b2df)
                await message.channel.send(f"<@{userid}>", embed=embed)
                
                data[f"{str(message.channel.id)}"]["Message-Count-Mod"] = 1
        
            
            with open('./database/TicketData.json', 'w') as f:
              json.dump(data, f, indent=1)
        
        
        
        
        
        
      except:
        pass
















# ------------------------------------------------------------------------- RUN ---------------------------------------------------------------------------------

# GETTING TOKEN
with open('./private/botdata.json') as f:
    prefixes = json.load(f)
token = prefixes["token"]

# RUNNING
async def main():
    await load_cogs()
    discord.utils.setup_logging(level=logging.INFO, root=False)
    await bot.start(token)

asyncio.run(main())