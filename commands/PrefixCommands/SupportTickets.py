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
import chat_exporter
from discord.ui import Button, Select, View

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True








class SupportOptions(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)

        
    @discord.ui.select(
            custom_id="select-ticket-1",
            placeholder='Select ticket category',
            options=[
                discord.SelectOption(label='General Support', emoji="<:pngerssupport:1281582306515091561>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='Blacklist Appeal', emoji="<:cross:1281495021488570449>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):

       await interaction.message.edit(view=self)

        
       interaction.message.author = interaction.user
       bucket = self.cooldown.get_bucket(interaction.message)
       retry = bucket.update_rate_limit()
    






       if retry:
          
          embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
          await interaction.response.send_message(embed=embed, ephemeral=True)   
            
       else:



       
            try:
               with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

               cid = data[f"{interaction.user.id}"]
                  

               channel = discord.utils.get(interaction.guild.channels, id=cid)
               embed = discord.Embed(description=f"**You cannot create two exchange tickets**!\n⬩ {channel.mention}, close your current ticket and then try again.\n-# ⓘ Used to prevent ticket spam.", color=0x6056ff)
               await interaction.response.send_message(embed=embed, ephemeral=True)   
               return

            except:
                pass





            await interaction.response.defer(thinking=True, ephemeral=True) 




            overwrites = { # DEFAULT PERMISSIONS FOR @EVERYONE AND USER, CURRENTLY ONLY ADMINS CAN SEE TICKET.
                    interaction.guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False),
                    interaction.user: discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
            }             


            with open('./private/botdata.json', 'r') as f:
               data = json.load(f)
 

            category = discord.utils.get(interaction.guild.channels, id=data["support-category"])


            for i in data['ids-to-have-full-access-in-support-tickets']:
                r = discord.utils.get(interaction.guild.roles, id=i)

                overwrites[r] = discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

            
                
            if len(category.channels) > 49:
                
              if discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1') != None:
                    category = discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1')
                    ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-support", category=category, overwrites=overwrites)
                
              else:
                
                category = await interaction.guild.create_category('Support Overflow 1', position=category.position+1)
                ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-support", category=category, overwrites=overwrites)
                
            else:
              ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-support", category=category, overwrites=overwrites)

               
                



            created = interaction.user.created_at
              
            d = datetime.datetime(created.year, created.month, created.day, created.hour, created.minute, created.second)
            time_stamp = calendar.timegm(d.timetuple())
        
        
        
            joinedat = interaction.user.joined_at
                  
    
            da = datetime.datetime(joinedat.year, joinedat.month, joinedat.day, joinedat.hour, joinedat.minute, joinedat.second)
            time_stamp2 = calendar.timegm(da.timetuple())
            
            now = datetime.datetime.now()
    
            d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
            time_stamp_c = calendar.timegm(d.timetuple())

            
            em = discord.Embed(description= f"# {select.values[0]} Request\n> Describe your Issue, be patient and wait for some staff to handle your case.\n- {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*), <t:{time_stamp_c}:R>\n- Account created <t:{time_stamp}:R>, joined <t:{time_stamp2}:R>\n-# User ID: {interaction.user.id}", color=0x6056ff)
            em.set_author(name=f'{interaction.user.name}', icon_url=interaction.user.avatar)
            em.set_thumbnail(url=interaction.guild.icon)
                
            msg=await ticket_channel.send(interaction.user.mention, embed=em, view=SupportClose())
            await msg.pin()



            with open('./database/SupportTickets/TicketData.json', 'r') as f:
               data = json.load(f)

            data[f"{str(ticket_channel.id)}"] = {}

            data[f"{str(ticket_channel.id)}"]['Support-Request-User'] = {}
            data[f"{str(ticket_channel.id)}"]['Support-Request-User']['ID'] = interaction.user.id
            data[f"{str(ticket_channel.id)}"]['Support-Request-User']['Name'] = interaction.user.name

            data[f"{str(ticket_channel.id)}"]['Users'] = []
            data[f"{str(ticket_channel.id)}"]['Users'].append(interaction.user.id)
            
            
            data[f"{str(ticket_channel.id)}"]['Message'] = msg.id


            data[int(interaction.user.id)] = ticket_channel.id
                
            with open('./database/SupportTickets/TicketData.json', 'w') as f:
               json.dump(data, f, indent=1)


            
            now = datetime.datetime.now()
    
            d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
            time_stamp_c = calendar.timegm(d.timetuple())

            embed = discord.Embed(description = f'`✔️` — **Ticket created** <t:{time_stamp_c}:R>, {ticket_channel.mention}', color=0x6056ff)
            await interaction.edit_original_response(embed=embed)   





class AfterCloseSupport(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)

    @discord.ui.button(label='Delete', style=discord.ButtonStyle.gray, custom_id='deletesupport-3')
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()
     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0xf1c40f)
        await interaction.response.send_message(embed=embed, ephemeral=True)   
     else:

                
                embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0xe74c3c)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                embed = discord.Embed(description='`❓` — **Are you sure you want to delete this application**?\n-# Select an option down below.', color=0x6056ff)
                msg = await interaction.channel.send(interaction.user.mention, embed=embed)
                await msg.edit(view=SupportDelete(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))





class SupportClose(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)

    @discord.ui.button(label='Delete', style=discord.ButtonStyle.gray, custom_id='deletesupport-2')
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()
     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   
     else:

                
                embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0xe74c3c)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                embed = discord.Embed(description='`❓` — **Are you sure you want to delete this application**?\n-# Select an option down below.', color=0x6056ff)
                msg = await interaction.channel.send(interaction.user.mention, embed=embed)
                await msg.edit(view=SupportDelete(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))




class SupportDelete(View):
    def __init__(self, interaction_msg, interaction_user, message_for_edit):
        super().__init__(timeout=15)
        self.interaction_msg = interaction_msg
        self.interaction_user = interaction_user
        self.msg = message_for_edit

    @discord.ui.select(options=[
            discord.SelectOption(label='Action', value='05', emoji='✔️', description='Delete the ticket.'),
            discord.SelectOption(label='Return', value='06', emoji='❌', description='Return without deleting the ticket.')
    ])
    async def callback(self, interaction: discord.Interaction, select):
        
            if select.values[0] == '05':


              now = datetime.datetime.now()
              limit = datetime.timedelta(seconds=7)

              o = now+limit

              d = datetime.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second)
              time_stamp = calendar.timegm(d.timetuple())
            
              to = time_stamp
 
                
              if interaction.user.id is not self.interaction_user.id:
                  return

              select.disabled = True
              embed = discord.Embed(description=f"# `🗑️` Deleting Ticket\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)", color=0x2ecc71)
              embed.set_author(name=f'[{interaction.user.name}]: Deleting ticket', icon_url=interaction.user.avatar)
              m = await interaction.response.edit_message(content='', embed=embed, view=self)

                
              embed2 = discord.Embed(description=f'`🗑️` {interaction.channel.mention} will be deleted in 5 seconds.\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)', color=0x2ecc71)
              await interaction.channel.send(embed=embed2)
              await asyncio.sleep(5)
            

 



              try:

                  with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

                  user = data[str(interaction.channel.id)]['Support-Request-User']['ID']
        
                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(interaction.guild.channels, id=data["support-tickets-logs-channel-id"])

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)

                  try:
                    
                    user_get = await interaction.guild.fetch_member(user)
                    hy = f'{user_get.mention} ({user})'
                    

                    embed=discord.Embed(title="Your Support Ticket was deleted.", description=f'- Ticket was deleted by {interaction.user.mention}', color=0x73b2df)
  
                    await user_get.send(embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))
    
                    
                  except:
                    
                    hy = f'{user}'

                  embed=discord.Embed(title="Support Ticket Has been Deleted.", description=f'- Ticket was deleted by {interaction.user.mention}\n- Ticket Creator: {hy}', color=0x73b2df)

                  await channel.send(hy, embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))

                
                  os.remove(f"Tickets/{interaction.channel.name}.htm")        

              except:
                    pass   
                
                
              


              await interaction.channel.delete()  

              try:
                with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

                user = data[str(interaction.channel.id)]['Support-Request-User']['ID']
            
                del data[str(user)]

                with open('./database/SupportTickets/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

              except:
                pass
                    

              try:
                with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

                del data[str(interaction.channel.id)]

                with open('./database/SupportTickets/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                   
              except:
                pass
            
            if select.values[0] == '06':
                if interaction.user.id is not self.interaction_user.id:
                  return


                select.disabled = True
                embed = discord.Embed(description='`❌` — Action cancelled', color=0x6056ff)
                await interaction.response.edit_message(embed=embed, view=self)   

    async def on_timeout(self):
     try:
      await self.interaction_msg.delete()
      return
     except:
      return


               
class SupportCloseTicket(View):
    def __init__(self, interaction_msg, interaction_user, message_for_edit):
        super().__init__(timeout=15)
        self.interaction_msg = interaction_msg
        self.interaction_user = interaction_user
        self.msg = message_for_edit

    @discord.ui.select(options=[
            discord.SelectOption(label='Action', value='05', emoji='✔️', description='Close the ticket.'),
            discord.SelectOption(label='Return', value='06', emoji='❌', description='Return without closing the ticket.')
    ])
    async def callback(self, interaction: discord.Interaction, select):

            if select.values[0] == '05':
                
                if interaction.user.id is not self.interaction_user.id:
                  return
                
                
                await interaction.response.defer(thinking=True, ephemeral=True) 

                select.disabled = True
                await interaction.message.edit(view=self)

                      
                await self.msg.edit(view=AfterCloseSupport())


                try:

                  with open('./database/SupportTickets/TicketData.json', 'r') as f:

                     data = json.load(f)

                  user2 = data[f"{str(interaction.channel.id)}"]['Users']
                  
                  for user in interaction.guild.members:
                   
                   if user.id in user2:

                     try:
                       await interaction.channel.set_permissions(user, send_messages=False, read_messages=False)
                     except:
                       pass

                except:
                  pass


        


                with open('./database/SupportTickets/TicketData.json', 'r') as f:
                     data = json.load(f)


                username = data[str(interaction.channel.id)]['Support-Request-User']['Name']
                user = data[str(interaction.channel.id)]['Support-Request-User']['ID']



                await interaction.channel.edit(name=f'{username}-support')


                now = datetime.datetime.now()

                d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp = calendar.timegm(d.timetuple())

                embed = discord.Embed(title=f'Ticket Closed', description=f"- The ticket has been closed by {interaction.user.mention}, <t:{time_stamp}:R>\n`❓` — To delete ticket, use the `delete` button [here]({self.msg.jump_url}).", color=0x6056ff)
                await interaction.channel.send(f"{interaction.user.mention}", embed=embed)
                



                try:


                  usersend = await interaction.guild.fetch_member(int(user))

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Your Support Ticket was closed.", description=f'- Ticket was closed by {interaction.user.mention}', color=0x6056ff)

                  await usersend.send(embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))

                  
                  os.remove(f"Tickets/{interaction.channel.name}.htm")        

                except:
                    pass   

                

                
                try:
                  with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

                  del data[str(user)]

                  with open('./database/SupportTickets/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                except:
                   pass
        

                await interaction.followup.send('The ticket was successfully closed.', ephemeral = True)

                
                
                
            if select.values[0] == '06':
                
                if interaction.user.id is not self.interaction_user.id:
                  return

                select.disabled = True
                embed = discord.Embed(description=f'`❌` — Action cancelled', color=0xe74c3c)
                await interaction.response.edit_message(embed=embed, view=self)     

    async def on_timeout(self):
     try:
      await self.interaction_msg.delete()
      return
     except:
      return




class SupportTickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        commands = self.get_commands()
        print(f"COG: SupportTickets.py ENABLED [{len(commands)}] commands LOADED")



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def supportticket(self, ctx):
       embed=discord.Embed(description=f"## Click the button below to ask questions, get support or purchase something.", color=0x6056ff)
       embed.set_author(name="➤ FlipX Support")
       embed.set_image(url="https://cdn.discordapp.com/attachments/1322300070170726520/1330292340367036486/WhatsApp_Bild_2025-01-16_um_20.32.59_4e3dac93.jpg?ex=678d72c9&is=678c2149&hm=2e2b2e88d1a3bf68141f6a29c35bf4b87401d44af49e7b32f48ff64c8bd29980&")
       await ctx.send(embed=embed, view=SupportOptions())
       await ctx.message.delete()






async def setup(bot):
    await bot.add_cog(SupportTickets(bot))