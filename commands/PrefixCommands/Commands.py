import json
import discord
import asyncio
import os
import datetime
from discord.ext.commands import MissingPermissions, BadArgument, has_permissions, CheckFailure
from discord.utils import get
import calendar
from discord.ext import commands, tasks
import random
from discord.ui import Button, Select, View
import chat_exporter

from commands.Ticket.TicketCreation import Ticket, CancelPayment, SentPayment, CloseTicket, DeleteTicket

from commands.PrefixCommands.SupportTickets import SupportClose, SupportDelete

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True




class Sort_lb(discord.ui.View):
    def __init__(self, data, user, u, bot, page, current):
        super().__init__(timeout=None)
        self.data = data
        self.user = user
        self.page = page
        self.u = u
        self.bot = bot
        
        self.current = current
   

    @discord.ui.select(
          placeholder="🔎 Sort by",
          options=[
            discord.SelectOption(label='Highest to lowest', value='05', description='Sort from highest stat to lowest.'),
            discord.SelectOption(label='Lowest to highest', value='06', description='Sort from lowest stat to highest.'),
            discord.SelectOption(label='Next page (if available)', value='07', description=f'Change page to view all users.'),
            discord.SelectOption(label='Weekly Top 10 (Amount)', value='08', description=f'Top 10 highest exchangers of this week.', emoji='⭐'),
            discord.SelectOption(label='Weekly Top 10 (Deals)', value='09', description=f'Top 10 highest exchangers of this week.', emoji='⭐')
    ])
    async def callback(self, interaction: discord.Interaction, select):

            await interaction.response.defer(thinking=True, ephemeral=True)

            if select.values[0] == '05':
                if interaction.user.id == self.user.id:
                   
                   roles = []
                    
                   with open('./private/botdata.json', 'r') as f:
                      data = json.load(f)      
               
                   for i in data["exchangers"]:
                      roles.append(i) 
                        
                   self.current = 'Highest to lowest'
                   self.page = 1
                    
                   data = self.data

                   l = []

                   n_check = 0
                    
                   for user in data:
        
                         for i in interaction.guild.members:
                          if i.id == int(user):
          
                            for op in i.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                                l.append(data[user]["Total-Exchanged"])
                              except:
                                pass 

        

                   n_check = 0
            
                   total = sorted(l, reverse=True)
  
                   lb = []

                   o = 1
              
                   u = []
                   u2 = []
                    
                   for i in data:
        
                         for user in interaction.guild.members:
                          if user.id == int(i):
          
                            for op in user.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                
                               u.append(i)
                               u2.append(i)
                        
                              except:
                                
                                pass 



                   n_check = 0

                   for a in total:
               
                       if len(lb) == 10:
                         break
            
                       for b in u:
                           try:

                             if data[b]["Total-Exchanged"] == a:
            
                              try:

                                g = await interaction.guild.fetch_member(int(b))
                                                
                                for op in g.roles:
                                  if op.id in roles:
                                      n_check = 9
                 
                                if n_check == 9:  
                                 n_check = 0
                        
                                 if self.page == 1:
                                  if o == 1:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                                  elif o == 2:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                
                                  elif o == 3:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                
                                  else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                            
                                 else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')

                                 o += 1

                                 u.remove(b)
                                
                                else:

                                 u.remove(b)



                              except:

                                u.remove(b)
                            
                           except:
                            pass

  
      
                   for k in lb:
                        if str(interaction.user.id) in k or interaction.user.name in k:
                           top = lb.index(k)

                           lb[top] = f'{k} (**YOU**)'



                   t = ''
    
                   for g in lb:
        
                      t += f'{g}\n'
        
                   if t == '':
        
                      embed=discord.Embed(description=f'No data was found related to this server :(', color=0x6056ff)
                      await interaction.followup.send(embed=embed)
                      return

                   embed = discord.Embed(description = f'# FlipX Leaderboard\n-# ⬩ 🔎 Filter: **Highest to lowest**\n{t}', color=0x6056ff)

                   await interaction.followup.edit_message(message_id=interaction.message.id, embed = embed, view=Sort_lb(data = data, user = interaction.user, u = u, bot = self.bot, current = 'Highest to lowest', page = 1))

                   await interaction.followup.send('`✔️` — **Stats were successfully updated**.')

            if select.values[0] == '06':
                if interaction.user.id == self.user.id:
                   
                   roles = []
                    
                   with open('./private/botdata.json', 'r') as f:
                      data = json.load(f)      
               
                   for i in data["exchangers"]:
                      roles.append(i) 
        
                   data = self.data

                   l = []

                   n_check = 0
                    
                   for user in data:
        
                         for i in interaction.guild.members:
                          if i.id == int(user):
          
                            for op in i.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                                l.append(data[user]["Total-Exchanged"])
                              except:
                                pass 
                        


                   n_check = 0
                
                   total = sorted(l)
  
                   lb = []

                   o = 1
              
                   u = []
                   u2 = []

                   for i in data:
        
                         for user in interaction.guild.members:
                          if user.id == int(i):
          
                            for op in user.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                
                               u.append(i)
                               u2.append(i)
                        
                              except:
                                
                                pass 
                    

                    

                    
                   n_check = 0
                    

                   for a in total:
              
                       if len(lb) == 10:
                         break
                        
                       for b in u:
                           try:
                             if a == 0:
                                break
                                
                             if data[b]["Total-Exchanged"] == a:
            
                              try:

                                g = await interaction.guild.fetch_member(int(b))
                        
                                for op in g.roles:
                                  if op.id in roles:
                                      n_check = 9
                 
                                if n_check == 9:  
                                 n_check = 0
                        
                                 if a == total[-1]:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                                
                                 elif a == total[-2]:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                                    
                                 elif a == total[-3]:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                                    
                                 else:
                        
                        
                                  lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')

                                 o += 1

                                 u.remove(b)


                                else:

                                 u.remove(b)


                              except:

                                u.remove(b)
                                
                            
                           except:
                            pass

            
                   for k in lb:
                        if str(interaction.user.id) in k or interaction.user.name in k:
                           top = lb.index(k)

                           lb[top] = f'{k} (**YOU**)'



                   t = ''
    
                   for g in lb:
        
                      t += f'{g}\n'
        
                   if t == '':
        
                      embed=discord.Embed(description=f'No data was found related to this server :(', color=0x6056ff)
                      await interaction.followup.send(embed=embed)
                      return

                   embed = discord.Embed(description = f'# FlipX Leaderboard\n-# ⬩ 🔎 Filter: **Lowest to highest**\n{t}', color=0x6056ff)

                   await interaction.followup.edit_message(message_id=interaction.message.id, embed = embed, view=Sort_lb(data = data, user = interaction.user, u = u, bot = self.bot, current = 'Lowest to highest', page = 1))

                   await interaction.followup.send('`✔️` — **Stats were successfully updated**.')
                 
            if select.values[0] == '07':
                if interaction.user.id == self.user.id:
                    

                   if self.current == 'Week Top 10':
                     await interaction.followup.send('`⌛` — **Currently unavailable**.')
                     return
                    
                    
                   self.page += 1
                   
                   num = 9 + (self.page-1) * 10
                    
                   data = self.data

                   l = []

                   ro = [] 
                    
                   for user in data:
                     for i in interaction.guild.members:
  
                       if i.id == int(user):
        
                            
                        for r in i.roles:
                          ro.append(r.id)
                        
                      
                        if 1281495035182846026 not in ro and 1281495030141554700 not in ro:
                            ro = []
                            pass
                        
                        else:
        
                           try:
                             l.append(data[user]["Total-Exchanged"])
                             ro = []
                        
                           except:
                             ro = []
                             pass
        
                   if self.current == 'Highest to lowest':
                     total = sorted(l, reverse=True)
                   else:
                     total = sorted(l)
  
                   lb = []

                   o = ((self.page - 1) * 10) + 1
              
                   u = self.u
                    
                   j = 9

                   for a in total:

                       for b in u:
                        
                           if len(lb) == 10:
                            break
                            
                           try:
                            
                             if total[num-j] == 0:
                                    break
                            
                             if data[b]["Total-Exchanged"] == total[num-j]:

                                g = await interaction.guild.fetch_member(int(b))
                        
                                if self.current == 'Lowest to highest':
                                  if total[num-j] == total[-1]:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                
                                  elif total[num-j] == total[-2]:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                    
                                  elif total[num-j] == total[-3]:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                    
                                  else:
                        
                        
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                            
                            
                                else:
                                    
                                  if total[num-j] == total[0]:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                
                                  elif total[num-j] == total[1]:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                    
                                  elif total[num-j] == total[2]:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                                    
                                  else:
                        
                        
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(total[num-j], 2)}€`***')
                            

                                o += 1
                                
                                j -= 1

                                u.remove(b)



                           except:
                            pass


            
                   for k in lb:
                        if str(interaction.user.id) in k or interaction.user.name in k:
                           top = lb.index(k)

                           lb[top] = f'{k} (**YOU**)'



                   t = ''
    
                   for g in lb:
        
                      t += f'{g}\n'
        
                   if t == '':
        
                      embed=discord.Embed(description=f'No data was found related to this server :(', color=0x6056ff)
                      await interaction.followup.send(embed=embed)
                      return

                   embed = discord.Embed(description = f'# FlipX Leaderboard\n-# ⬩ 🔎 Filter: **{self.current}** — **Page** ⟶ `{self.page}`\n{t}', color=0x6056ff)

                   await interaction.followup.edit_message(message_id=interaction.message.id, embed = embed, view=Sort_lb(data = data, user = interaction.user, u = u, bot = self.bot, current = self.current, page = self.page))

                   await interaction.followup.send('`✔️` — **Stats were successfully updated**.')


                    
            if select.values[0] == '08':
                if interaction.user.id == self.user.id:
                   
                   roles = []
                    
                   with open('./private/botdata.json', 'r') as f:
                      data = json.load(f)      
               
                   for i in data["exchangers"]:
                      roles.append(i) 
                        
                   self.current = 'Week Top 10'
                   self.page = 1
                    
                   data = self.data

                   l = []

                   n_check = 0
                    
                   for user in data:
                      try:
                            
                         data[user]["Weekly-Exchanged"]   
                            
                         for i in interaction.guild.members:
                          if i.id == int(user):
          
                            for op in i.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                                l.append(data[user]['Weekly-Exchanged']['Total-Exchanged'])
                              except:
                                pass 

                      except:
                        pass
        

                   n_check = 0
            
                   total = sorted(l, reverse=True)
  
                   lb = []

                   o = 1
              
                   u = []
                   u2 = []
                    
                   for i in data:
        
                         for user in interaction.guild.members:
                          if user.id == int(i):
          
                            for op in user.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                
                               u.append(i)
                               u2.append(i)
                        
                              except:
                                
                                pass 



                   n_check = 0

                   for a in total:
               
                       if len(lb) == 10:
                         break
            
                       for b in u:
                           try:

                             if data[b]['Weekly-Exchanged']['Total-Exchanged'] == a:
                
                              if len(lb) == 10:
                                 break
                            
                              try:

                                g = await interaction.guild.fetch_member(int(b))
                                                
                                for op in g.roles:
                                  if op.id in roles:
                                      n_check = 9
                 
                                if n_check == 9:  
                                 n_check = 0
                        
                                 if self.page == 1:
                                  if o == 1:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`*** *—* ***`{data[b]["Weekly-Exchanged"]["Orders"]}` orders***')
                                  elif o == 2:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`*** *—* ***`{data[b]["Weekly-Exchanged"]["Orders"]}` orders***')
                
                                  elif o == 3:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`*** *—* ***`{data[b]["Weekly-Exchanged"]["Orders"]}` orders***')
                
                                  else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`*** *—* ***`{data[b]["Weekly-Exchanged"]["Orders"]}` orders***')
                            
                                 else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`*** *—* ***`{data[b]["Weekly-Exchanged"]["Orders"]}` orders***')

                                 o += 1

                                 u.remove(b)
                                
                                else:

                                 u.remove(b)



                              except:

                                u.remove(b)
                            
                           except:
                            pass

  
      
                   for k in lb:
                        if str(interaction.user.id) in k or interaction.user.name in k:
                           top = lb.index(k)

                           lb[top] = f'{k} (**YOU**)'



                   t = ''
    
                   for g in lb:
        
                      t += f'{g}\n'
        
                   if t == '':
        
                      embed=discord.Embed(description=f'No data was found related to this server :(', color=0x6056ff)
                      await interaction.followup.send(embed=embed)
                      return

                   embed = discord.Embed(description = f'# FlipX Leaderboard ⭐ Weekly Top\n-# ⬩ 🔎 Filter: **Amount**\n{t}', color=0x6056ff)

                   await interaction.followup.edit_message(message_id=interaction.message.id, embed = embed, view=Sort_lb(data = data, user = interaction.user, u = u, bot = self.bot, current = 'Week Top 10', page = 1))

                   await interaction.followup.send('`✔️` — **Stats were successfully updated**.')
                    
                    
                    

                    
            if select.values[0] == '09':
                if interaction.user.id == self.user.id:
                   
                   roles = []
                    
                   with open('./private/botdata.json', 'r') as f:
                      data = json.load(f)      
               
                   for i in data["exchangers"]:
                      roles.append(i) 
                        
                   self.current = 'Week Top 10'
                   self.page = 1
                    
                   data = self.data

                   l = []

                   n_check = 0
                    
                   for user in data:
                      try:
                            
                         data[user]["Weekly-Exchanged"]   
                            
                         for i in interaction.guild.members:
                          if i.id == int(user):
          
                            for op in i.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                                l.append(data[user]['Weekly-Exchanged']['Orders'])
                              except:
                                pass 

                      except:
                        pass
        

                   n_check = 0
            
                   total = sorted(l, reverse=True)
  
                   lb = []

                   o = 1
              
                   u = []
                   u2 = []
                    
                   for i in data:
        
                         for user in interaction.guild.members:
                          if user.id == int(i):
          
                            for op in user.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                
                               u.append(i)
                               u2.append(i)
                        
                              except:
                                
                                pass 



                   n_check = 0

                   for a in total:
               
                       if len(lb) == 10:
                         break
            
                       for b in u:
                           try:

                             if data[b]['Weekly-Exchanged']['Orders'] == a:
               
                              if len(lb) == 10:
                                 break
                        
                              try:

                                g = await interaction.guild.fetch_member(int(b))
                                                
                                for op in g.roles:
                                  if op.id in roles:
                                      n_check = 9
                 
                                if n_check == 9:  
                                 n_check = 0
                        
                                 if self.page == 1:
                                  if o == 1:
                                    lb.append(f'{o}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{a}` orders*** *—* ***`{round(data[b]["Weekly-Exchanged"]["Total-Exchanged"], 2)}€`***')
                                  elif o == 2:
                                    lb.append(f'{o}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{a}` orders*** *—* ***`{round(data[b]["Weekly-Exchanged"]["Total-Exchanged"], 2)}€`***')
                
                                  elif o == 3:
                                    lb.append(f'{o}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{a}` orders*** *—* ***`{round(data[b]["Weekly-Exchanged"]["Total-Exchanged"], 2)}€`***')
                
                                  else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{a}` orders*** *—* ***`{round(data[b]["Weekly-Exchanged"]["Total-Exchanged"], 2)}€`***')
                            
                                 else:
                                    lb.append(f'{o}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{a}` orders*** *—* ***`{round(data[b]["Weekly-Exchanged"]["Total-Exchanged"], 2)}€`***')

                                 o += 1

                                 u.remove(b)
                                
                                else:

                                 u.remove(b)



                              except:

                                u.remove(b)
                            
                           except:
                            pass

  
      
                   for k in lb:
                        if str(interaction.user.id) in k or interaction.user.name in k:
                           top = lb.index(k)

                           lb[top] = f'{k} (**YOU**)'



                   t = ''
    
                   for g in lb:
        
                      t += f'{g}\n'
        
                   if t == '':
        
                      embed=discord.Embed(description=f'No data was found related to this server :(', color=0x6056ff)
                      await interaction.followup.send(embed=embed)
                      return

                   embed = discord.Embed(description = f'# FlipX Leaderboard ⭐ Weekly Top\n-# ⬩ 🔎 Filter: **Orders**\n{t}', color=0x6056ff)

                   await interaction.followup.edit_message(message_id=interaction.message.id, embed = embed, view=Sort_lb(data = data, user = interaction.user, u = u, bot = self.bot, current = 'Week Top 10', page = 1))

                   await interaction.followup.send('`✔️` — **Stats were successfully updated**.') 








class ltc(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Copy Addy', emoji='<:ltc:1256681739493838990>', style=discord.ButtonStyle.grey, custom_id='ltc-2')
    async def ltc(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('ltc1qy0357z4dw7lvu5mgcjfukva6kwcmj9y6jl0tep', ephemeral=True)



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        commands = self.get_commands()
        print(f"COG: Commands.py ENABLED [{len(commands)}] commands LOADED")


    @commands.command()
    async def client(self, ctx, member: discord.Member):
        
        with open('./private/botdata.json', 'r') as f:
          data = json.load(f)      
        
        role = discord.utils.get(ctx.guild.roles, id=data['client-role-id'])
        
        if not ctx.author.guild_permissions.administrator and role not in ctx.author.roles:
            return
        
        else:
            role = discord.utils.get(ctx.guild.roles, id=data['client-role-id'])
            await member.add_roles(role)
            
            
            embed = discord.Embed(description=f'{role.mention} was added to {member.mention} by {ctx.author.mention}.', color=0x6056ff)
            await ctx.reply(embed=embed)
            
            

    @commands.command()
    async def sigma(self, ctx):
        
        with open('./private/botdata.json', 'r') as f:
          data = json.load(f)      


        role = discord.utils.get(ctx.guild.roles, id=data['100+ping'])
        await ctx.author.add_roles(role)
            
            
        embed = discord.Embed(description=f'{role.mention} was added to {ctx.author.mention}.', color=0x6056ff)
        await ctx.reply(embed=embed)
        
        
        
        
    
        
        
        
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def save(self, ctx, user: discord.Member, txid: str, amount: int):

        o = []
        
        for g in txid:
           if g not in o:
              o.append(g)
                    
        if len(o) < 5:
            await ctx.reply(f'`⚠️` Try again by using a valid TXID. **Only 5 different letters/numbers**!?')
            return
            
        elif len(txid) < 20:
            await ctx.reply(f'`⚠️` Try again by using a valid TXID. **Text too small**!')
            return
            
        elif len(txid) > 100:
            await ctx.reply('`⚠️` Try again by using a valid TXID. **Text too big**!')
            return
            
        else:
            pass
        
        if len(ctx.message.attachments) == 0:
            await ctx.reply('`⚠️` You forgot the image.')
            return
        
        
        guild_i = self.bot.get_guild(1260521615289090089)
        
        overwrites = { # DEFAULT PERMISSIONS FOR @EVERYONE AND USER, CURRENTLY ONLY ADMINS CAN SEE TICKET.
                    guild_i.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False)
        }      
            
        category = self.bot.get_channel(1274683613283094560)
        
        ticket_channel = await category.create_text_channel(f'{user.name}-securities', overwrites=overwrites)
         
        urls = self.bot.get_channel(1274675447447420939)
         
        file = await ctx.message.attachments[0].to_file()

        raa = await urls.send(f'{user.id}', file = file) 
        
        embed=discord.Embed(title=f'{user.name} securities', color=0x6056ff)
        embed.add_field(name=f'Securities amount:', value=f'{amount}€', inline=False)
        embed.add_field(name=f'TXID:', value=f'```{txid}```', inline=False)
        embed.add_field(name=f'User information:', value=f'```yaml\n- ID: {user.id}\n- Name: {user.name}```', inline=False)
        embed.set_image(url=raa.attachments[0].url)
        await ticket_channel.send(f'Created by: {ctx.author.mention}', embed=embed)
        
        await ctx.message.delete()
        await ctx.send(f'`💾` **Information saved**. {ticket_channel.jump_url}')
           
        
        
    @commands.command(aliases=['lb', 'top'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def leaderboard(self, ctx):
     roles = []  
                                               
     with open('./private/botdata.json', 'r') as f:
        data = json.load(f)      
               
     for i in data["exchangers"]:
        roles.append(i) 
        
     with open("./database/UserData.json") as f:
            data = json.load(f)

     l = []

     n_check = 0
    
     for user in data:
            
            
        
       for i in ctx.guild.members:
        if i.id == int(user):
          
          for op in i.roles:
                if op.id in roles:
                    n_check += 1
                 
          if n_check != 0:  
        
            try:
              l.append(data[user]["Total-Exchanged"])
            except:
              pass



     n_check = 0

     total = sorted(l, reverse=True)
  
     lb = []

     o = 1

     u = []

     n = 1

     for i in data:
        
                         for user in ctx.guild.members:
                          if user.id == int(i):
          
                            for op in user.roles:
                                  if op.id in roles:
                                      n_check += 1
                 
                            if n_check != 0:  
        
                              try:
                
                               u.append(i)
                        
                              except:
                                
                                pass 

     
     n_check = 0

     for a in total:

        if len(lb) == 10:
            break
        
        if a == 0:
          break
              
        for b in u:
         try:
          if data[b]["Total-Exchanged"] == a:
            
           try:
            g = await ctx.guild.fetch_member(int(b))
            
            for op in g.roles:
               if op.id in roles:
                   n_check = 9
                 
            if n_check == 9:  
             n_check = 0
            
             if n == 1:
              lb.append(f'{n}. 🥇 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
             elif n == 2:
              lb.append(f'{n}. 🥈 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                
             elif n == 3:
              lb.append(f'{n}. 🥉 **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')
                
             else:
              lb.append(f'{n}. **{discord.utils.escape_markdown(g.name)}**, {g.mention}: ***`{round(a, 2)}€`***')

             o += 1

             u.remove(b)

             n += 1
           
            else:

             u.remove(b)

           except:

             u.remove(b)
                
         except:
            pass
      

     for k in lb:
          if str(ctx.author.id) in k or ctx.author.name in k:
             top = lb.index(k)

             lb[top] = f'{k} (**YOU**)'



     t = ''
    
     for g in lb:
        
        t += f'{g}\n'
             
      

     if t == '':
        
        embed=discord.Embed(description=f'`❌` — No data was found :(', color=0x6056ff)
        await ctx.reply(embed=embed)
        return

     embed = discord.Embed(description = f'# FlipX Leaderboard\n-# ⬩ 🔎 Filter: **Highest to lowest**\n{t}', color=0x6056ff)
     await ctx.reply(embed = embed, mention_author=False, view=Sort_lb(data = data, u = u, bot = self.bot, user = ctx.author, current = "Highest to lowest", page = 1))  
        
        
          
    @commands.command()
    async def rename(self, ctx, *, name: str):
         
            
       c = ''   
            
       try:
            
            with open('./database/SupportTickets/TicketData.json', 'r') as f:
               data = json.load(f)

            data[f"{str(ctx.channel.id)}"]
            
            c = 'support'
        
       except:
            
            try:
                
              with open('./database/TicketData.json', 'r') as f:
                 data = json.load(f)

              data[f"{str(ctx.channel.id)}"]
                            
              c = 'exchange'
                
            except:
                    
                try:
                    
                  with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

                  prefixes[f"{str(ctx.channel.id)}"]  
                
                  c = 'exchange'
                   
                except:
                  c = ''

                
                
                
       if c == '':
            await ctx.reply('This is not a ticket.', delete_after=5)
            return
                                  
       with open('./private/botdata.json', 'r') as f:
            data = json.load(f)      
               
       senior = discord.utils.get(ctx.guild.roles, id=data["senior-moderator"])
        
       if ctx.author.guild_permissions.administrator or senior in ctx.author.roles:     
          await ctx.message.delete()
          await ctx.channel.edit(name=name)
        
        
        
    @commands.command()
    async def blacklist(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        senior = discord.utils.get(ctx.guild.roles, id=data["senior-moderator"])
        log_channel_id = data.get("log-channel", None)

        if ctx.author.guild_permissions.administrator or senior in ctx.author.roles:
            if member != ctx.author:
                role = discord.utils.get(ctx.guild.roles, id=data["blacklisted"])
                await member.add_roles(role)

                await ctx.reply(f'{member.mention} has been successfully blacklisted for: {reason}')

                if log_channel_id:
                    log_channel = self.bot.get_channel(log_channel_id)
                    if log_channel:
                        await log_channel.send(
                            f":no_entry: **Blacklist Action** :no_entry:\n\n**User:** {member.mention}\n**By:** {ctx.author.mention}\n**Reason:** {reason}"
                        )
            else:
                await ctx.reply("You cannot blacklist yourself.")
        else:
            await ctx.reply("You do not have the required permissions to use this command.")
        
        
    @commands.command()
    async def unblacklist(self, ctx, member: discord.Member):
                          
       with open('./private/botdata.json', 'r') as f:
            data = json.load(f)      
               
       senior = discord.utils.get(ctx.guild.roles, id=data["senior-moderator"])
        
       if ctx.author.guild_permissions.administrator or senior in ctx.author.roles:
        if member != ctx.author:
          
          role = discord.utils.get(ctx.guild.roles, id=data["blacklisted"])
          await member.remove_roles(role)
        
          await ctx.reply(f'{member.mention} has been successfully unblacklisted.')
        
        
    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.channel)
    async def transcript(self, ctx, member: discord.Member = None):
 
            
         c = ''   
            
         try:
            
            with open('./database/SupportTickets/TicketData.json', 'r') as f:
               data = json.load(f)

            data[f"{str(ctx.channel.id)}"]
            
            c = 'support'
        
         except:
            
            try:
                
              with open('./database/TicketData.json', 'r') as f:
                 data = json.load(f)

              data[f"{str(ctx.channel.id)}"]
                            
              c = 'exchange'
                
            except:
                 
                    
              try:
                
                with open('./database/Applications/applications.json', 'r') as f:
                   data = json.load(f)

                data[f"{str(ctx.author.id)}"]
                            
                c = 'exchange'
              
              except:
                    
                try:
                    
                  with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

                  prefixes[f"{str(ctx.channel.id)}"]  
                
                  c = 'exchange'
                   
                except:
                  c = ''
                
                
                
         if c == '':
            await ctx.reply('This is not a ticket/application.', delete_after=5)
            
            
         else:

              try:

                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)


                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{ctx.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)
                    
                    
                  embed=discord.Embed(title="FlipX Ticket Transcript.", description=f'- Requested by {ctx.author.mention}', color=0x6056ff)

                  if member:
                        
                    await member.send(embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))
                    
                  else:
                    await ctx.reply(embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))
                    

                  
                  os.remove(f"Tickets/{ctx.channel.name}.htm")        

              except:
                await ctx.reply("Couldn't do that.", delete_after=5)
                

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def remove(self, ctx, Member: discord.Member|int):
        
                  
        with open('./private/botdata.json', 'r') as f:

            data = json.load(f)      

        c = 0

                        
        r = discord.utils.get(ctx.guild.roles, id=data["senior-moderator"])
        
        if r in ctx.author.roles:
            pass
        
        else:
             
          if ctx.author.guild_permissions.administrator or c > 0:
            pass 
         
          else:
            return
        
        
        
        user = Member
        
        if type(user) == int:
            
            try:
              user = await ctx.guild.fetch_member(user)
            
            except:
                
              em = discord.Embed(description = f"Unable to find a user with `{user}` id.", colour=0x6056ff)
              await ctx.reply(embed=em)   
              return
            
            
        else:
            pass


        try:
          

          with open('./database/TicketData.json') as f:
            data = json.load(f)
        
          data[str(ctx.channel.id)]
          s = data[f"{str(ctx.channel.id)}"]["Status"]  
        
          if s != 'Completed' or s != 'Cancelled':

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == False and overwrite.read_messages == False:

              em = discord.Embed(description = f"{user.mention} already doesn't have access to this exchange ticket.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:

  
              with open("./database/TicketData.json") as f:
                 data = json.load(f)

              data[f"{ctx.channel.id}"]["Users"].append(user.id)

              with open("./database/TicketData.json", 'w') as f:
                json.dump(data, f, indent=1)

              await ctx.channel.set_permissions(user, send_messages=False, read_messages=False)

              embed = discord.Embed(description=f"{user.mention} was successfully removed from this exchange ticket.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

          else:
            await ctx.reply(f'The ticket is already {s}.', delete_after=5)
    
        except:
            pass  

        

        try:
          

            with open('./database/SupportTickets/TicketData.json') as f:
              data = json.load(f)
        
            data[str(ctx.channel.id)]
        

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == False and overwrite.read_messages == False:

              em = discord.Embed(description = f"{user.mention} already doesn't have access to this support ticket.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:

  
              with open("./database/SupportTickets/TicketData.json") as f:
                 data = json.load(f)

              data[f"{ctx.channel.id}"]["Users"].append(user.id)

              with open("./database/SupportTickets/TicketData.json", 'w') as f:
                json.dump(data, f, indent=1)

              await ctx.channel.set_permissions(user, send_messages=False, read_messages=False)

              embed = discord.Embed(description=f"{user.mention} was successfully removed from this support ticket.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

    
        except:
            pass         
                
         
        

        try:
          

            with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

            prefixes[f"{str(ctx.channel.id)}"]
        

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == False and overwrite.read_messages == False:

              em = discord.Embed(description = f"{user.mention} already doesn't have access to this application.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:

              await ctx.channel.set_permissions(user, send_messages=False, read_messages=False)

              embed = discord.Embed(description=f"{user.mention} was successfully removed from this application.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

    
        except:
            pass        
        
        
        
        
        
                
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def add(self, ctx, Member: discord.Member|int):
        
                  
        with open('./private/botdata.json', 'r') as f:
            data_2 = json.load(f)      

        c = 0

                        
        r = discord.utils.get(ctx.guild.roles, id=data_2["senior-moderator"])
        
        if r in ctx.author.roles:
            pass
        
        else:
             
          if ctx.author.guild_permissions.administrator or c > 0:
            pass 
         
          else:
            return
        
        
        
        user = Member
        
        if type(user) == int:
            
            try:
              user = await ctx.guild.fetch_member(user)
            
            except:
                
              em = discord.Embed(description = f"Unable to find a user with `{user}` id.", colour=0x6056ff)
              await ctx.reply(embed=em)   
              return
            
            
        else:
            pass


        try:
          

          with open('./database/TicketData.json') as f:
            data = json.load(f)
        
          data[str(ctx.channel.id)]
          s = data[f"{str(ctx.channel.id)}"]["Status"]  
        
          if s != 'Completed' or s != 'Cancelled':

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == True and overwrite.read_messages == True:

              em = discord.Embed(description = f"{user.mention} already has access to this exchange ticket.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:

  
              with open("./database/TicketData.json") as f:
                 data = json.load(f)

              data[f"{ctx.channel.id}"]["Users"].append(user.id)

              with open("./database/TicketData.json", 'w') as f:
                json.dump(data, f, indent=1)

              await ctx.channel.set_permissions(user, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

              embed = discord.Embed(description=f"{user.mention} successfully received access to this exchange ticket.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

          else:
            await ctx.reply(f'The ticket is already {s}.', delete_after=5)
    
        except:
            pass  

        

        try:
          

            with open('./database/SupportTickets/TicketData.json') as f:
              data = json.load(f)
        
            data[str(ctx.channel.id)]
        

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == True and overwrite.read_messages == True:

              em = discord.Embed(description = f"{user.mention} already has access to this support ticket.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:

  
              with open("./database/SupportTickets/TicketData.json") as f:
                 data = json.load(f)

              data[f"{ctx.channel.id}"]["Users"].append(user.id)

              with open("./database/SupportTickets/TicketData.json", 'w') as f:
                json.dump(data, f, indent=1)

              await ctx.channel.set_permissions(user, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

              embed = discord.Embed(description=f"{user.mention} successfully granted access to this support ticket.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

    
        except:
            pass  
        
         
        

        try:
          

            with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

            prefixes[f"{str(ctx.channel.id)}"]
        

            overwrite = ctx.channel.overwrites_for(user)
            ov = ctx.channel.overwrites_for(user.top_role)

            if overwrite.send_messages == True and overwrite.read_messages == True:

              em = discord.Embed(description = f"{user.mention} already has access to this application.", colour=0x6056ff)
              await ctx.reply(embed=em)   
      

            else:
            
              await ctx.channel.set_permissions(user, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

              embed = discord.Embed(description=f"{user.mention} successfully granted access to this application.", color=0x6056ff)
  
              await ctx.reply(Member.mention, embed=embed, mention_author=False)

    
        except:
            pass        
        





        
        
        

    @commands.command()
    async def applyltc(self, ctx):

      embed = discord.Embed(description="# FlipX - Security\n## What are security fees?\n- Securities help us to refund the victims if they got scammed.\n- You have to pay securities fees.\n- You get your securities back once you retire.\n\n## What Are Limit Fees?\nFlipx charges a 1% fee on all transactions made through our service.\nFor example, if you want to exchange €1000, a 1% limit fee will be applied based on your total exchange amount.\n\n(Note: Once Flipx verifies you as a stable exchanger, your limit fee will gradually decrease.)\n\n## Note\n- You can retire after 2 weeks.\n- You will receive your funds in LTC\n- If you have any ongoing report on [ScammerAlert](https://discord.gg/scammeralert) you will be roled as Quarantined, in this time you can't do any exchanges.\n- If you are getting marked as a Scammer on [ScammerAlert](https://discord.gg/scammeralert) you will not get your securities back.\n- In order to retire or get your roles back you need to provide the Application Transcript as a HTML-File\n\n**By paying your securities you are accepting the terms and conditions writting above and that the adress which sent the money belongs to you. If you disaagree with any part of these, you can close the ticket.**\n\n **ltc1qy0357z4dw7lvu5mgcjfukva6kwcmj9y6jl0tep**\n- The limit deposit is non-refundable.\nOnce you sent the securities, make sure to send the Transaction Link and a Screenshot of the payment.\nWe are not Responsible if Litecoin goes down.", color=0x6056ff)
      await ctx.reply(embed=embed, view=ltc())









    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.channel)
    async def done(self, ctx):
                
         c = ''   
            

            
         try:
                
              with open('./database/TicketData.json', 'r') as f:
                 data = json.load(f)

              data[f"{str(ctx.channel.id)}"]
              uid = data[f"{str(ctx.channel.id)}"]["Exchange-Request-User"]["ID"]
                            
              c = 'exchange'
                
         except:
                
              c = ''
                
                
                
         if c == '':
            await ctx.reply('This is not a ticket.', delete_after=5)
          
         else:
          embed = discord.Embed(title="Confirm Exchange", description=f"> Only press the button when you received the payment.", color=0x6056ff)
          await ctx.reply(f"<@{uid}>", embed=embed, view=SentPayment())



    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.channel)
    async def cancel(self, ctx):
                
         c = ''   
            

            
         try:
                
              with open('./database/TicketData.json', 'r') as f:
                 data = json.load(f)

              data[f"{str(ctx.channel.id)}"]
              uid = data[f"{str(ctx.channel.id)}"]["Exchange-Request-User"]["ID"]
                            
              c = 'exchange'
                
         except:
                
              c = ''
                
                
                
         if c == '':
            await ctx.reply('This is not a ticket.', delete_after=5)
            
         else:
          embed = discord.Embed(title="Cancel Exchange", description=f"> Only press the button if your sure about cancelling the Exchange.", color=0x6056ff)
          await ctx.reply(f"<@{uid}>", embed=embed, view=CancelPayment())










    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addlimit(self, ctx, exchanger: discord.Member, max: int):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**{exchanger.mention} is not an exchanger**!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return



        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            data[str(exchanger.id)]['limit'] = max

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)] = {}

            data[str(exchanger.id)]['limit'] = max

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

              
        embed=discord.Embed(description=f"{exchanger.mention} limit was changed to `{max}`", color=0x6056ff)
        await ctx.reply(embed=embed)
         

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removelimit(self, ctx, exchanger: discord.Member):

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            max = data[str(exchanger.id)]['limit']
            del data[str(exchanger.id)]['limit']
            
            try:
                
              del data[str(exchanger.id)]['Current-Limit']
                
            except:
                pass
                

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:
            max = None


        if max:
          embed=discord.Embed(description=f"{exchanger.mention} limit was successfully removed. They had a limit of `{max}`.", color=0x6056ff)

        else: 
          embed=discord.Embed(description=f"{exchanger.mention} doesn't have limit.", color=0x6056ff)
             

        await ctx.reply(embed=embed)
    
    
    
    
    
    

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addmax(self, ctx, exchanger: discord.Member, max: int):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**{exchanger.mention} is not an exchanger**!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return



        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            data[str(exchanger.id)]['max'] = max

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)] = {}

            data[str(exchanger.id)]['max'] = max

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

              
        embed=discord.Embed(description=f"{exchanger.mention} max was changed to `{max}`", color=0x6056ff)
        await ctx.reply(embed=embed)
         

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removemax(self, ctx, exchanger: discord.Member):

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            max = data[str(exchanger.id)]['max']
            del data[str(exchanger.id)]['max']
            
            try:
                
              del data[str(exchanger.id)]['Current']
                
            except:
                pass
                

            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:
            max = None


        if max:
          embed=discord.Embed(description=f"{exchanger.mention} max was successfully removed. They had a max of `{max}`.", color=0x6056ff)

        else: 
          embed=discord.Embed(description=f"{exchanger.mention} doesn't have max.", color=0x6056ff)
             

        await ctx.reply(embed=embed)

        

    @commands.command()
    async def limit(self, ctx):
        
        exchanger = ctx.author




        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in exchanger.roles:
                c += 1

        if exchanger.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**{exchanger.mention} is not an exchanger**!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        n = 1 
        
        
        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            
        
            try:
                
              
              m2 = data[str(exchanger.id)]['limit']
              m = f'{m2}€'

            except:
              
              m = '❌'

            try:
              
              current = data[str(exchanger.id)]['Current-Limit']

              current = round(m2 - current)
              current = f'{current}€'

            except:

              if m != '❌':
                  current = m
              
              else:
                  current = '❌'
    
        except:
             
              usdt = ''

              eth = ''

              btc = ''

              ltc = ''

              paypal = ''

              m = '0'

              total = '❌'

              current = '0'

              active = '❌'
            
              history = '❌'
                
                
        await ctx.reply(f'You have ***`{m}`*** limit with ***`{current}`*** remaining.')       
        

    # COMMANDS


    @commands.command()
    async def max(self, ctx):
        
        exchanger = ctx.author




        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in exchanger.roles:
                c += 1

        if exchanger.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**{exchanger.mention} is not an exchanger**!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        n = 1 
        
        
        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]
            
        
            try:
                
              
              m2 = data[str(exchanger.id)]['max']
              m = f'{m2}€'

            except:
              
              m = '❌'

            try:
              
              current = data[str(exchanger.id)]['Current']

              current = round(m2 - current)
              current = f'{current}€'

            except:

              if m != '❌':
                  current = m
              
              else:
                  current = '❌'
    
        except:
             
              usdt = ''

              eth = ''

              btc = ''

              ltc = ''

              paypal = ''

              m = '0'

              total = '❌'

              current = '0'

              active = '❌'
            
              history = '❌'
                
                
        await ctx.reply(f'You have ***`{m}`*** max with ***`{current}`*** remaining.')        
    
    
    
    @commands.group(name='admin', invoke_without_command=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def admin(self, ctx): 
      pass
    
    @admin.command(name='resetactive')
    @commands.has_permissions(administrator=True)
    async def resetactive(self, ctx, exchanger: int):

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger)]
            
            try:
              
              g = data[str(exchanger)]['Active']
              g.reverse()

              active = ''
              n = 1

              for i in g:
                   active += f'{n}. {i}\n'
                   n += 1

              active += f'-# Total: {len(g)}'
       

              del data[str(exchanger)]['Active']
   
              with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)
            

            except:
              
              active = '`❌`'
                
                
            embed = discord.Embed(title='Active History Purged', description=f'<@{exchanger}> (**{exchanger}**) active history was purged.', color=0x6056ff)   
            embed.add_field(name=f"`🔄` Purged data:", value=f"{active}", inline=False)
            await ctx.reply(f"<@{exchanger}>", embed=embed)
                


        except:
            await ctx.reply('Exchanger not found.')
        
    
    @admin.command(name='profile')
    @commands.has_permissions(administrator=True)
    async def adminprofile(self, ctx, exchanger: int):
        n = 1


        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger)]



            try:
              
              g = data[str(exchanger)]['Active']
              g.reverse()

              active = ''
              n = 1

              for i,z in zip(g, range(0,5)):
                   active += f'{n}. {i}\n'
                   n += 1

              if n > 4:
                active += f'-# Total: {len(g)}'
                   


            except:
              
              active = '`❌`'


            try:
              
              g = data[str(exchanger)]['History']
              g.reverse()

              history = ''
              n = 1

              for i,z in zip(g, range(0,5)):
                   history += f'{n}. {i}\n'
                   n += 1

              if n > 4:
                
                ns = 0
                ys = 0
                
                for i in g:
                    
                    if '❌' in i:
                        ns += 1
                    
                    else:
                        ys += 1
                
                history += f'-# **Total**: {len(g)} — **Successfull**: **`{ys}✔️`**, **cancelled**: **`{ns}❌`**'
                   


            except:
              
              history = '`❌`'

            try:
              
              total = data[str(exchanger)]['Total-Exchanged']
              total = f'{round(total)}€'

            except:
              
              total = '`0€`'
              
            
            try:
              
              paypal = data[str(exchanger)]['PayPal']
              paypal = f'\n- PayPal: `{paypal}`'
              n += 1

            except:
              
              paypal = ''

            try:
              
              ltc = data[str(exchanger)]['ltc']
              ltc = f'\n- Litecoin (ltc): `{ltc}`'
              n += 1

            except:
              
              ltc = ''

            try:
              
              btc = data[str(exchanger)]['btc']
              btc = f'\n- Bitcoin (btc): `{btc}`'
              n += 1

            except:
              
              btc = ''

            try:
              
              eth = data[str(exchanger)]['eth']
              eth = f'\n- Ethereum (eth): `{eth}`'

            except:
              
              eth = ''

            try:
              
              usdt = data[str(exchanger)]['usdt']
              usdt = f'\n- Tether (usdt): `{usdt}`'
              n += 1

            except:
              
              usdt = ''

            try:
              
              m2 = data[str(exchanger)]['max']
              m = f'{m2}€'

            except:
              
              m = '❌'

            try:
              
              current = data[str(exchanger)]['Current']

              current = round(m2 - current)
              current = f'{current}€'

            except:

              if m != '❌':
                  current = m
              
              else:
                  current = '❌'



            try:
              
              m2 = data[str(exchanger.id)]['limit']
              limit_max = f'{m2}€'

            except:
              
              limit_max = '❌'

            try:
              
              limit_current = data[str(exchanger.id)]['Current-Limit']

              limit_current = round(m2 - limit_current)
              limit_current = f'{limit_current}€'

            except:

              if limit_max != '❌':
                  limit_current = limit_max
              
              else:
                  limit_current = '❌'
                
                
                
                
        except:
             
              limit_current = '❌'
            
              limit_max = '❌'
             
              usdt = ''

              eth = ''

              btc = ''

              ltc = ''

              paypal = ''

              m = '❌'

              total = '❌'

              current = '❌'

              active = '❌'
            
              history = '❌'

        if history == '':
            history = '`❌`'

        if active == '':
            active = '`❌`'

        p = ''    
            
        if n != 1:
            p = 'Payment details'
            
        embed=discord.Embed(title=f"FlipX Archive", description=f"-# User id: **{exchanger}**, **MAIN PROFILE**\n- **Total exchanged**: `{total}`\n- **Max** (Security): `{m}`, remaining: `{current}`\n- **Limit** (Security): `{limit_max}`, remaining: `{limit_current}`", color=0x6056ff)
        
        if p != '':
          embed.add_field(name=f"`💳` {p}:", value=f"{paypal}{ltc}{btc}{usdt}{eth}", inline=False)
            
        
        embed.add_field(name=f"`📜` Exchange History (last 5):", value=f"{history}", inline=False)
        embed.add_field(name=f"`🕒` Currently Active Exchanges (5 more recent):", value=f"{active}", inline=False)
        await ctx.reply(embed=embed)
    
    
    
    
    @commands.command(aliases=['p'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def profile(self, ctx, exchanger: discord.Member = None):


        if exchanger == None:
               exchanger = ctx.author




        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in exchanger.roles:
                c += 1

        if exchanger.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**{exchanger.mention} is not an exchanger**!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        n = 1


        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(exchanger.id)]


            try:

                orders = data[str(exchanger.id)]['Weekly-Exchanged']['Orders']
                exchanged = data[str(exchanger.id)]['Weekly-Exchanged']['Total-Exchanged']   

                weekly = f"**{orders}** {'orders' if orders != 1 else 'order'} (**{round(exchanged, 2)}**€ Total Exchanged)"
                
            except:
                  

                orders = 0
                exchanged = 0  
            
                weekly = f'**0** orders (**0**€ Total Exchanged)'

            try:
              
              g = data[str(exchanger.id)]['Active']
              g.reverse()

              active = ''
              n = 1

              total_active = 0
            
              for i,z in zip(g, range(0,5)):
                    
                   check = 0 
                    
                   for p in i.split():
                    
                      if check == 1:
                            pass
                        
                      else:
                    
                        if '€' in p:

                            
                          check = 1
                          p = p.replace('€', '')
                        
                                         
                          if '-' in p:
                            p = p.split('-', 1)[1]
                            
                          total_active += int(float(p))
                    
                   active += f'{n}. {i}\n'
                   n += 1

              if n > 4:
                active += f'-# [...] Total: **`{len(g)}💱`** — **{total_active}**€ total amount'
              
              else:
                active += f'-# **{total_active}**€ total amount'
                   


            except:

              total_active = 0
            
              active = '`❌`'


            jh = 0
            jt = ''
                
            try:
              
              g = data[str(exchanger.id)]['History']
                
              for i in g:
                
                check = ''
                
                for p in i.split():

                    if '❌' in p:
                        check = '1'
                    
                    if check != '1':

                    
                      if '€' in p:
                        
                        
                        
                        p = p.replace('€', '')
                        
                        if '-' in p:
                            p = p.split('-', 1)[1]
                        
                        p_int = int(float(p))
                        
                        jtt = ''
                        
                        if p_int > jh:
                            jh = p_int
                            
                            
                            for u in i.split():

                              if '<t:' in u:  
                                
                                if ':R>' in u:
                                  jtt += u
                                    
                                if ':d>' in u:
                                  jtt += f' {u} '
                                 
                                if ':t>' in u:
                                  jtt += f'{u}'
                                
                              else:
                                                                
                                if '/' in u:
                                 jtt += u
                            
                                if ':' in u:
                                  jtt += f' {u}'
                            
                            jt = jtt
                    
                
            except:
              
              jt = ''
                
                
            try:
              
              g = data[str(exchanger.id)]['History']

            
              g.reverse()


            
              first = g[-1]
                
              for p in g[-1].split():

                    
                      if '€' in p:
                        
                        
                        
                        p = p.replace('€', '')
                        
                        if '-' in p:
                            p = p.split('-', 1)[1]
                        
                        p_int = int(float(p))
                        
                        jtt = ''
                        
                            
                            
                        for u in g[-1].split():

                              if '<t:' in u:  
                                
                                if ':R>' in u:
                                  jtt += u
                                    
                                if ':d>' in u:
                                  jtt += f' {u} '
                                 
                                if ':t>' in u:
                                  jtt += f'{u}'
                                
                              else:
                                                                
                                if '/' in u:
                                 jtt += u
                            
                                if ':' in u:
                                  jtt += f' {u}'
                            
                        first = f"{jtt} — **{p_int}**€"
                    
                    

            except:
              
              first = '`❌`' 
                
                
                
            try:
              
              g = data[str(exchanger.id)]['History']

              history = ''
              n = 1

              for i,z in zip(g, range(0,5)):
                   history += f'{n}. {i}\n'
                   n += 1

              if n > 4:
                
                ns = 0
                ys = 0
                
                for i in g:
                    
                    if '❌' in i:
                        ns += 1
                    
                    else:
                        ys += 1
                
                history += f'-# [...] Total: **`{len(g)}💱`** — **`{ys}✔️`**, **`{ns}❌`** — **{round(ys / (ys + ns) * 100, 1)}**% success'
                   


            except:
              
              history = '`❌`'

            try:
              
              total = data[str(exchanger.id)]['Total-Exchanged']
              total = f'{round(total)}€'

            except:
              
              total = '`0€`'
              
            
            try:
              
              paypal = data[str(exchanger.id)]['PayPal']
              paypal = f'\n- PayPal: `{paypal}`'
              n += 1

            except:
              
              paypal = ''

            try:
              
              ltc = data[str(exchanger.id)]['ltc']
              ltc = f'\n- Litecoin (ltc): `{ltc}`'
              n += 1

            except:
              
              ltc = ''

            try:
              
              btc = data[str(exchanger.id)]['btc']
              btc = f'\n- Bitcoin (btc): `{btc}`'
              n += 1

            except:
              
              btc = ''

            try:
              
              eth = data[str(exchanger.id)]['eth']
              eth = f'\n- Ethereum (eth): `{eth}`'

            except:
              
              eth = ''

            try:
              
              usdt = data[str(exchanger.id)]['usdt']
              usdt = f'\n- Tether (usdt): `{usdt}`'
              n += 1

            except:
              
              usdt = ''

            try:
              
              m2 = data[str(exchanger.id)]['max']
              m = f'{m2}€'

            except:
              
              m = '❌'

            try:
              
              current = data[str(exchanger.id)]['Current']

              current = round(m2 - current)
              current = f'{current}€'

            except:

              if m != '❌':
                  current = m
              
              else:
                  current = '❌'


            try:
              
              m2 = data[str(exchanger.id)]['limit']
              limit_max = f'{m2}€'

            except:
              
              limit_max = '❌'

            try:
              
              limit_current = data[str(exchanger.id)]['Current-Limit']

              limit_current = round(m2 - limit_current)
              limit_current = f'{limit_current}€'

            except:

              if limit_max != '❌':
                  limit_current = limit_max
              
              else:
                  limit_current = '❌'
                
                
                
                
        except:
             
              limit_current = '❌'
            
              limit_max = '❌'
            
              usdt = ''

              eth = ''

              btc = ''

              ltc = ''

              paypal = ''

              m = '❌'

              total = '❌'

              current = '❌'

              active = '❌'
            
              history = '❌'
            
              first = '❌'
                
              jh = 0
            
              jt = ''
            
              weekly = f'**0** orders (**0**€ Total Exchanged)'
               
              orders = 0
                
              exchanged = 0  
                
              total_active = 0
            
        if history == '':
            history = '`❌`'

        if active == '':
            active = '`❌`'

        p = ''    
            
        if n != 1:
            p = 'Payment details'
            
        with open("./database/WeeklyCheckup.json") as f:
          data = json.load(f)
         
        timestamp = data['timestamp']    
        
        embed=discord.Embed(title=f"{exchanger.name} profile", description=f"- **Total exchanged**: `{total}`\n- **Max** (Security): `{m}`, remaining: `{current}`\n- **Limit** (Security): `{limit_max}`, remaining: `{limit_current}`\n- **First deal**: {first}\n\n`🎯` **Weekly Goal**: **{f'{orders}' if orders < 10 else '10'}**/10\n{weekly}, **to be resetted <t:{timestamp}:R>**", color=0x6056ff)
        
            
        if jt != '':
          embed.add_field(name=f"`⭐` Highest Deal:", value=f"{jt} — **{jh}**€", inline=False)
        
        if p != '':
          embed.add_field(name=f"`💳` {p}:", value=f"{paypal}{ltc}{btc}{usdt}{eth}", inline=False)

        
        embed.add_field(name=f"`📜` Exchange History (last 5):", value=f"{history}", inline=False)
        embed.add_field(name=f"`🕒` Currently Active Exchanges (5 more recent):", value=f"{active}", inline=False)
        embed.set_thumbnail(url=exchanger.avatar)
        await ctx.reply(embed=embed)
        


    @commands.command()
    async def setwise(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Wise']

              if mail:
                data[str(ctx.author.id)]['Wise'] = mail

              else:
                del data[str(ctx.author.id)]['Wise']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Wise'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Wise mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Wise'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Wise mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
        
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
    
    @commands.command()
    async def setapple(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Apple Pay']

              if mail:
                data[str(ctx.author.id)]['Apple Pay'] = mail

              else:
                del data[str(ctx.author.id)]['Apple Pay']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Apple Pay'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Apple Pay mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Apple Pay'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Apple Pay mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
    
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setamazon(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Amazon']

              if mail:
                data[str(ctx.author.id)]['Amazon'] = mail

              else:
                del data[str(ctx.author.id)]['Amazon']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Amazon'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Amazon mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Amazon'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Amazon mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
     
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setpaysafe(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Paysafe']

              if mail:
                data[str(ctx.author.id)]['Paysafe'] = mail

              else:
                del data[str(ctx.author.id)]['Paysafe']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Paysafe'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Paysafe mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Paysafe'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Paysafe mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        

    @commands.command()
    async def setskrill(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Skrill']

              if mail:
                data[str(ctx.author.id)]['Skrill'] = mail

              else:
                del data[str(ctx.author.id)]['Skrill']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Skrill'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Skrill mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Skrill'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Skrill mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setzelle(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Zelle']

              if mail:
                data[str(ctx.author.id)]['Zelle'] = mail

              else:
                del data[str(ctx.author.id)]['Zelle']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Zelle'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Zelle mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Zelle'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Zelle mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
     
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setvenmo(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Venmo']

              if mail:
                data[str(ctx.author.id)]['Venmo'] = mail

              else:
                del data[str(ctx.author.id)]['Venmo']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Venmo'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Venmo mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Venmo'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Venmo mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        

    @commands.command()
    async def setrevolut(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['Revolut']

              if mail:
                data[str(ctx.author.id)]['Revolut'] = mail

              else:
                del data[str(ctx.author.id)]['Revolut']

            except:
  
              if mail:
                data[str(ctx.author.id)]['Revolut'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your Revolut mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['Revolut'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your Revolut mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        

    @commands.command()
    async def setcashapp(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['CashApp']

              if mail:
                data[str(ctx.author.id)]['CashApp'] = mail

              else:
                del data[str(ctx.author.id)]['CashApp']

            except:
  
              if mail:
                data[str(ctx.author.id)]['CashApp'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your CashApp mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['CashApp'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your CashApp mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        


    @commands.command()
    async def setpaypal(self, ctx, mail = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)]

            try:
              current = data[str(ctx.author.id)]['PayPal']

              if mail:
                data[str(ctx.author.id)]['PayPal'] = mail

              else:
                del data[str(ctx.author.id)]['PayPal']

            except:
  
              if mail:
                data[str(ctx.author.id)]['PayPal'] = mail

              else:
              
                embed=discord.Embed(description=f"**Please write your paypal mail after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return


            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if mail:
              data[str(ctx.author.id)]['PayPal'] = mail

            else:
              
              embed=discord.Embed(description=f"**Please write your paypal mail after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your mail was successfully changed**.\n```yaml\n- {current} ⟶ {mail}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        

    @commands.command()
    async def setltc(self, ctx, addy = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            try:
              current = data[str(ctx.author.id)]['ltc']

              if addy:
                data[str(ctx.author.id)]['ltc'] = addy

              else:
                del data[str(ctx.author.id)]['ltc']

            except:
  
              if addy:
                data[str(ctx.author.id)]['ltc'] = addy

              else:
              
                embed=discord.Embed(description=f"**Please write your ltc addy after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if addy:
              data[str(ctx.author.id)]['ltc'] = addy

            else:
              
              embed=discord.Embed(description=f"**Please write your ltc addy after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your addy was successfully changed**.\n```yaml\n- {current} ⟶ {addy}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setbtc(self, ctx, addy = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            try:
              current = data[str(ctx.author.id)]['btc']

              if addy:
                data[str(ctx.author.id)]['btc'] = addy

              else:
                del data[str(ctx.author.id)]['btc']

            except:
  
              if addy:
                data[str(ctx.author.id)]['btc'] = addy

              else:
              
                embed=discord.Embed(description=f"**Please write your btc addy after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if addy:
              data[str(ctx.author.id)]['btc'] = addy

            else:
              
              embed=discord.Embed(description=f"**Please write your btc addy after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your addy was successfully changed**.\n```yaml\n- {current} ⟶ {addy}```", color=0x6056ff)
        await ctx.reply(embed=embed)
     
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def seteth(self, ctx, addy = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            try:
              current = data[str(ctx.author.id)]['eth']

              if addy:
                data[str(ctx.author.id)]['eth'] = addy

              else:
                del data[str(ctx.author.id)]['eth']

            except:
  
              if addy:
                data[str(ctx.author.id)]['eth'] = addy

              else:
              
                embed=discord.Embed(description=f"**Please write your eth addy after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if addy:
              data[str(ctx.author.id)]['eth'] = addy

            else:
              
              embed=discord.Embed(description=f"**Please write your eth addy after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your addy was successfully changed**.\n```yaml\n- {current} ⟶ {addy}```", color=0x6056ff)
        await ctx.reply(embed=embed)
     
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        
    @commands.command()
    async def setusdt(self, ctx, addy = None):


        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)

        c = 0


        for i in data['exchangers']:
                    
            r = discord.utils.get(ctx.guild.roles, id=i)

            if r in ctx.author.roles:
                c += 1

        if ctx.author.guild_permissions.administrator or c > 0:
            pass

        else:

            embed=discord.Embed(description=f"**Your not an Exchanger**. You cannot use this command!", color=0x6056ff)
            await ctx.reply(embed=embed)
            return

        current = '❌'

        try:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            try:
              current = data[str(ctx.author.id)]['usdt']

              if addy:
                data[str(ctx.author.id)]['usdt'] = addy

              else:
                del data[str(ctx.author.id)]['usdt']

            except:
  
              if addy:
                data[str(ctx.author.id)]['usdt'] = addy

              else:
              
                embed=discord.Embed(description=f"**Please write your usdt addy after the command**. Try again!", color=0x6056ff)
                await ctx.reply(embed=embed)
                return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        except:

            with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

            data[str(ctx.author.id)] = {}

            if addy:
              data[str(ctx.author.id)]['usdt'] = addy

            else:
              
              embed=discord.Embed(description=f"**Please write your usdt addy after the command**. Try again!", color=0x6056ff)
              await ctx.reply(embed=embed)
              return



            with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

        
        embed=discord.Embed(description=f"**Your addy was successfully changed**.\n```yaml\n- {current} ⟶ {addy}```", color=0x6056ff)
        await ctx.reply(embed=embed)
 
        channel = self.bot.get_channel(1262385612187500657)
        await channel.send(f"{ctx.author.name}, {ctx.author.id}", embed=embed)
        
        


async def setup(bot):
    await bot.add_cog(Commands(bot))