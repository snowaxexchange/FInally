import json
import discord
import asyncio
import os
import datetime
from discord.ext.commands import MissingPermissions, BadArgument, has_permissions, CheckFailure
from discord.utils import get
from discord.ext import commands, tasks
from discord.ui import Button, Select, View, Modal
import traceback
import calendar
import chat_exporter 

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True



    
   
# --------------------------------- SENDING MODAL [BUTTON] ---------------------------------     

class Application(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='📝 Apply', custom_id='application', style=discord.ButtonStyle.blurple)
    async def receive(self, interaction: discord.Interaction, button: discord.ui.Button):
               
                          
        with open('./private/botdata.json', 'r') as f:

            data = json.load(f)      
            
        role = discord.utils.get(interaction.guild.roles, id=data['blacklisted']) 
        
        if role in interaction.user.roles:
          embed = discord.Embed(description=f"**You are blacklisted from our services**! Appeal this in https://discord.com/channels/1315035618048475246/1320348475958755361", color=0x6056ff)
          await interaction.response.send_message(embed=embed, ephemeral=True)
          return

        moderator = None
        exchanger = None

        with open('./private/botdata.json', 'r') as f:
           data = json.load(f)

        try:
             
          role_id = data["moderator"]
          moderator = discord.utils.get(interaction.guild.roles, id=role_id)

        except:
             pass
             

        try:
             
          role_id = data["exchanger"]
          exchanger = discord.utils.get(interaction.guild.roles, id=role_id)

        except:
             pass
        
        list = []
        
        if exchanger in interaction.user.roles and moderator in interaction.user.roles:
                  
                  j = []

                  for i in interaction.user.roles:
                       if i.id == exchanger.id:
                            j.append(exchanger.mention)

                       if i.id == moderator.id:
                            j.append(exchanger.mention)

                  t = ', '.join(j)

            
                  embed = discord.Embed(description=f"⚠️ — **You are already a Staff Member**! You have {t}", color=0x6056ff)
                  await interaction.response.send_message(embed=embed, ephemeral=True) 
                  return
        
        
        try:
                  with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

                  time = prefixes[f"{str(interaction.user.id)}"]['timestamp']
                  sector = prefixes[f"{str(interaction.user.id)}"]['sector'] 

                  with open('./database/Applications/applications.json', 'w') as f:
                      json.dump(prefixes, f, indent=1)
                    
                  embed = discord.Embed(description=f"⚠️ — **You already have a pending application**! Please be patient.\n> Pending — <t:{time}:R> — **{sector}** App.", color=0x6056ff)
                  await interaction.response.send_message(embed=embed, ephemeral=True) 
                    
  
        except:
        
          embed = discord.Embed(description=f'# `📝` —  Where you want to apply?\n> Please select the sector where you want to apply.', color=0x6056ff)
          embed.set_thumbnail(url=interaction.guild.icon)

          await interaction.response.send_message(embed=embed, view=ApplicationSelect(), ephemeral=True)

        
# -------------------------------------------------------------------------------------

    
class ApplicationSelect(View):
        def __init__(self):
          super().__init__(timeout=None)
        
        @discord.ui.select(
          placeholder='📝 - Where you want to apply?',
          custom_id='select-ticket', 
          options=[
              discord.SelectOption(label='Moderator', value='01', emoji=f'🔰', description='Apply for an Moderator.'),
              discord.SelectOption(label='Exchanger', value='03', emoji=f'💱', description='Apply for an Exchanger.')
          ]
        )
        async def callback(self, interaction: discord.Interaction, select):
                

            moderator = None
            exchanger = None

            with open('./private/botdata.json', 'r') as f:
               data = json.load(f)

            try:
             
              role_id = data["moderator"]
              moderator = discord.utils.get(interaction.guild.roles, id=role_id)

            except:
                 pass
             

            try:
             
              role_id = data["exchanger"]
              exchanger = discord.utils.get(interaction.guild.roles, id=role_id)

            except:
                 pass
        
            list = []
        
            if exchanger in interaction.user.roles or moderator in interaction.user.roles:
                  for i in interaction.user.roles:
                    if i.id == exchanger.id:
                        list.append(exchanger.mention)
                        
                    if i.id == moderator.id:
                        list.append(moderator.mention)
                        
                  a = ", ".join(list)
            
                  embed = discord.Embed(description=f"⚠️ — **You are already a Staff Member**! You have {a}", color=0x6056ff)
                  await interaction.response.send_message(embed=embed, ephemeral=True) 
                  return
        
            if select.values[0] == '01':
               await interaction.response.send_modal(StaffApply())
        
        
            if select.values[0] == '03':  
               await interaction.response.send_modal(ExchangerApply())  
                
                
                
# --------------------------------- MODAL APPLICATION ---------------------------------      
        
class ExchangerApply(discord.ui.Modal, title='Exchanger Application.'):   
    def __init__(self):
        super().__init__(timeout=None)
        
    question1 = discord.ui.TextInput(label='Question 1', style=discord.TextStyle.long, placeholder='Which exchanges could you do?', required=True, max_length=2000)
    
    question2 = discord.ui.TextInput(label='Question 2', placeholder='How much experience do you have?', style=discord.TextStyle.long, required=True, max_length=2000)
    
    question3 = discord.ui.TextInput(label='Question 3', placeholder='How much securities are you ready to pay?', style=discord.TextStyle.short, required=True, max_length=100)
    
    question4 = discord.ui.TextInput(label='Question 4', placeholder='Are you exchanging by yourself?', style=discord.TextStyle.short, required=True, max_length=1000)

    question5 = discord.ui.TextInput(label='Question 5 (Optional)', placeholder='Any more informations about you?', style=discord.TextStyle.long, required=False, max_length=2000)

    
    async def on_submit(self, interaction: discord.Interaction):


        with open('./private/botdata.json', 'r') as f:
               data = json.load(f)

             

        try:
             
              role_id = data["exchanger"]
              exchanger = discord.utils.get(interaction.guild.roles, id=role_id)

        except:
                 pass
            
        user = interaction.user
 

             

        
      
 
        overwrites = { # DEFAULT PERMISSIONS FOR @EVERYONE AND USER, CURRENTLY ONLY ADMINS CAN SEE TICKET.
                     interaction.guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False),
                     interaction.user: discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        }             
 
        with open('./private/botdata.json', 'r') as f:
          data = json.load(f)
 
        for i in data['ids-to-have-full-access-in-exchanger-applications']:
           r = discord.utils.get(interaction.guild.roles, id=i)

           overwrites[r] = discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
          
                  

        category = discord.utils.get(interaction.guild.channels, id=data["category-for-exchanger-applications"])

         
        if len(category.channels) > 49:
                
              if discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1') != None:
                     category = discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1')
                     ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)    
                
              else:
                
                category = await interaction.guild.create_category('Support Overflow 1', position=category.position+1)
                ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)    
                
        else:     
            ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)      

        
        now = datetime.datetime.now()

        d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time_stamp = calendar.timegm(d.timetuple())
        
    
        embed = discord.Embed(description=f'# Exchanger Application\n> Status: **Pending**', color=0x6056ff)
        embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
        embed.add_field(name = f'— Which exchanges could you do?', value=f'```yaml\n- {self.question1}```', inline = False)
        embed.add_field(name = f'— How much experience do you have?', value=f'```yaml\n- {self.question2}```', inline = False)
        embed.add_field(name = f'— How much securities are you ready to pay?', value=f'```yaml\n- {self.question3}```', inline = False)
        embed.add_field(name = f'— Are you exchanging by yourself?', value=f'```yaml\n- {self.question4}```', inline = False)

        if self.question5:
          embed.add_field(name = f'— Any more informations about you?', value=f'```yaml\n- {self.question5}```', inline = False)

        msg = await ticket_channel.send(interaction.user.mention, embed=embed, view=Button())
        await msg.pin()
      

        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                
        prefixes[f"{str(interaction.user.id)}"] = {}
        prefixes[f"{str(interaction.user.id)}"]['message'] = msg.id
        prefixes[f"{str(interaction.user.id)}"]['sector'] = 'Exchanger'
        prefixes[f"{str(interaction.user.id)}"]['timestamp'] = str(time_stamp)
        
        prefixes[f"{str(msg.id)}"] = {}
        prefixes[f"{str(msg.id)}"]['user'] = interaction.user.id
        prefixes[f"{str(msg.id)}"]['sector'] = 'Exchanger'
        prefixes[f"{str(msg.id)}"]['timestamp'] = str(time_stamp)
        
        prefixes[f"{str(msg.id)}"]['question1'] = str(self.question1)
        prefixes[f"{str(msg.id)}"]['question2'] = str(self.question2)
        prefixes[f"{str(msg.id)}"]['question3'] = str(self.question3)
        prefixes[f"{str(msg.id)}"]['question4'] = str(self.question4) 

        if self.question5:
          prefixes[f"{str(msg.id)}"]['question5'] = str(self.question5) 

        
        prefixes[f"{str(msg.id)}"]['Role'] = role_id
        
        prefixes[f"{str(msg.id)}"]['Status'] = 'Pending' 

        prefixes[f"{str(ticket_channel.id)}"] = interaction.user.id

        with open('./database/Applications/applications.json', 'w') as f:
                      json.dump(prefixes, f, indent=1)


        embed = discord.Embed(description = f'`✔️` — **Application created** <t:{time_stamp}:R>, {ticket_channel.mention}', color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   
        

class StaffApply(discord.ui.Modal, title='Moderator Application.'):
    def __init__(self):
        super().__init__(timeout=None)
        
    question1 = discord.ui.TextInput(label='Question 1', style=discord.TextStyle.long, placeholder='Why do you want to be a moderator?', required=True, max_length=2000)
    
    question2 = discord.ui.TextInput(label='Question 2', placeholder='What is your timezone?', style=discord.TextStyle.long, required=True, max_length=2000)
    
    question3 = discord.ui.TextInput(label='Question 3', placeholder='Do you have any expierence?', style=discord.TextStyle.short, required=True, max_length=2000)


    async def on_submit(self, interaction: discord.Interaction):

        
        if 'indian' in str(self.question2).lower() or 'india' in str(self.question2).lower() or 'gmt+5:30' in str(self.question2).lower():
            embed = discord.Embed(title=f'Mentioned timezone/region is banned', description=f'⬩ Mentioned region (**India** - **GMT**+**5**:**30**) has been banned from creating application tickets due to its timezone. **Please accept it and do not create a different application with __fake timezone__**.', color=0x6056ff)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        with open('./private/botdata.json', 'r') as f:
               data = json.load(f)

             

        try:
             
              role_id = data["moderator"]
              moderator = discord.utils.get(interaction.guild.roles, id=role_id)

        except:
                 pass
            
        user = interaction.user
 

        
        

 
        overwrites = { # DEFAULT PERMISSIONS FOR @EVERYONE AND USER, CURRENTLY ONLY ADMINS CAN SEE TICKET.
                     interaction.guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False),
                     interaction.user: discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        }             
 
        with open('./private/botdata.json', 'r') as f:
          data = json.load(f)
 
        for i in data['ids-to-have-full-access-in-moderator-applications']:
           r = discord.utils.get(interaction.guild.roles, id=i)

           overwrites[r] = discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
          
                    
        category = discord.utils.get(interaction.guild.channels, id=data["category-for-moderator-applications"])

         
                             
        if len(category.channels) > 49:
                
              if discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1') != None:
                     category = discord.utils.get(interaction.guild.categories, name=f'Support Overflow 1')
                     ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)    
                
              else:
                
                category = await interaction.guild.create_category('Support Overflow 1', position=category.position+1)
                ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)    
                
        else:     
            ticket_channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-app", category=category, overwrites=overwrites)   
 

        
        
        now = datetime.datetime.now()

        d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time_stamp = calendar.timegm(d.timetuple())
        
    
        embed = discord.Embed(description=f'# Moderator Application\n> Status: **Pending**', color=0x6056ff)
        embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
        embed.add_field(name = f'— Why do you want to be a moderator?', value=f'```yaml\n- {self.question1}```', inline = False)
        embed.add_field(name = f'— What is your timezone?', value=f'```yaml\n- {self.question2}```', inline = False)
        embed.add_field(name = f'— Do you have any expierence?', value=f'```yaml\n- {self.question3}```', inline = False)

             
      

        msg = await ticket_channel.send(interaction.user.mention, embed=embed, view=Button())
        await msg.pin()



        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                
        prefixes[f"{str(interaction.user.id)}"] = {}
        prefixes[f"{str(interaction.user.id)}"]['message'] = msg.id
        prefixes[f"{str(interaction.user.id)}"]['sector'] = 'Moderator'
        prefixes[f"{str(interaction.user.id)}"]['timestamp'] = str(time_stamp)
        
        prefixes[f"{str(msg.id)}"] = {}
        prefixes[f"{str(msg.id)}"]['user'] = interaction.user.id
        prefixes[f"{str(msg.id)}"]['sector'] = 'Moderator'
        prefixes[f"{str(msg.id)}"]['timestamp'] = str(time_stamp)
        
        prefixes[f"{str(msg.id)}"]['question1'] = str(self.question1)
        prefixes[f"{str(msg.id)}"]['question2'] = str(self.question2)
        prefixes[f"{str(msg.id)}"]['question3'] = str(self.question3)
        
        prefixes[f"{str(msg.id)}"]['Role'] = role_id
        
        prefixes[f"{str(msg.id)}"]['Status'] = 'Pending' 
        
        prefixes[f"{str(ticket_channel.id)}"] = interaction.user.id


        with open('./database/Applications/applications.json', 'w') as f:
                      json.dump(prefixes, f, indent=1)

        embed = discord.Embed(description = f'`✔️` — **Application created** <t:{time_stamp}:R>, {ticket_channel.mention}', color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   
        
        
        
# --------------------------------- ACCEPT/DECLINE APPLICATION ---------------------------------    

class Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='✔️ Accept', custom_id='Accept',style=discord.ButtonStyle.green)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
       
       with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
       
       s = prefixes[f"{str(interaction.message.id)}"]['sector']

       with open('./private/botdata.json', 'r') as f:
          data = json.load(f)

       n = 0

       for i in interaction.user.roles:
            
         if s == "Exchanger":
            if i.id in data["ids-to-have-full-access-in-exchanger-applications"]: 
                 n += 1
                 break

         else:
            if i.id in data["ids-to-have-full-access-in-moderator-applications"]: 
                 n += 1
                 break

       if n < 1 and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message('You cannot do that.', ephemeral=True)
            return

       try:
        
        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

        user = prefixes[f"{str(interaction.message.id)}"]['user']
        s = prefixes[f"{str(interaction.message.id)}"]['sector']
        time_stamp = prefixes[f"{str(interaction.message.id)}"]['timestamp']
        
        
        roleid = prefixes[f"{str(interaction.message.id)}"]['Role']
        
        
        prefixes[f"{str(interaction.message.id)}"]['Status']
        
        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                
        del prefixes[f"{str(user)}"]
        
        prefixes[f"{str(interaction.message.id)}"]['Status'] = 'Accepted'
        
        with open('./database/Applications/applications.json', 'w') as f:
                      json.dump(prefixes, f, indent=1)  
                
        if s == 'Exchanger':
             

            question1 = prefixes[f"{str(interaction.message.id)}"]['question1']
            question2 = prefixes[f"{str(interaction.message.id)}"]['question2']
            question3 = prefixes[f"{str(interaction.message.id)}"]['question3']
            question4 = prefixes[f"{str(interaction.message.id)}"]['question4']
            question5 = prefixes[f"{str(interaction.message.id)}"]['question5']
      
             
            

            
        
            try:
                u = await interaction.guild.fetch_member(user)
    
                role = discord.utils.get(interaction.guild.roles, id=roleid)
                                           
                with open('./private/botdata.json', 'r') as f:
                  data = json.load(f)      
        
                role2 = discord.utils.get(interaction.guild.roles, id=data['------[ Staff ]------'])
        
        
                await u.add_roles(role)
                await u.add_roles(role2)
    
    

    
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Accepted** by {interaction.user.mention}', color=0x6056ff)
    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Which exchanges could you do?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— How much experience do you have?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— How much securities are you ready to pay?', value=f'```yaml\n- {question3}```', inline = False)
                embed.add_field(name = f'— Are you exchanging by yourself?', value=f'```yaml\n- {question4}```', inline = False)

                if question5:
                  embed.add_field(name = f'— Any more informations about you?', value=f'```yaml\n- {question5}```', inline = False)
        
                await interaction.message.edit(embed=embed, view=Accepted())
    
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was accepted by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())

            
            except:
                
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined** — **User left**!', color=0x6056ff)    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Which exchanges could you do?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— How much experience do you have?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— How much securities are you ready to pay?', value=f'```yaml\n- {question3}```', inline = False)
                embed.add_field(name = f'— Are you exchanging by yourself?', value=f'```yaml\n- {question4}```', inline = False)

                if question5:
                  embed.add_field(name = f'— Any more informations about you?', value=f'```yaml\n- {question5}```', inline = False)
                
                await interaction.message.edit(embed=embed, view=Accepted())

                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())

        else:
            
            question1 = prefixes[f"{str(interaction.message.id)}"]['question1'] 
            question2 = prefixes[f"{str(interaction.message.id)}"]['question2']
            question3 = prefixes[f"{str(interaction.message.id)}"]['question3']
      
             
            

            
        
            try:

                u = await interaction.guild.fetch_member(user)
        
        
                role = discord.utils.get(interaction.guild.roles, id=roleid)     
            
                with open('./private/botdata.json', 'r') as f:
                  data = json.load(f)      
        
                role2 = discord.utils.get(interaction.guild.roles, id=data['------[ Staff ]------'])
        
        
                await u.add_roles(role)
                await u.add_roles(role2)
    
    

    
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Accepted** by {interaction.user.mention}***', color=0x6056ff)
    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Why do you want to be a moderator?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— What is your timezone?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— Do you have any expierence?', value=f'```yaml\n- {question3}```', inline = False)
        
                await interaction.message.edit(embed=embed, view=Accepted())
    
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was accepted by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())
        
            except:
                
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined** — **User left**!', color=0x6056ff) 
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Why do you want to be a moderator?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— What is your timezone?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— Do you have any expierence?', value=f'```yaml\n- {question3}```', inline = False)
                
                await interaction.message.edit(embed=embed, view=Accepted())
        
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())
                    
        try:
                  user = await interaction.guild.fetch_member(int(user))

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Application Ticket Has been Deleted.", description=f'- Application was deleted by {interaction.user.mention}\n> Name: `{interaction.channel.name}`', color=0x6056ff)

                  await user.send(embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))

                  
                  os.remove(f"Tickets/{interaction.channel.name}.htm")        

        except:
                    pass   
            

            
            
            
       except:
         pass
                
                
                
    @discord.ui.button(label='❌ Reject', custom_id='Reject',style=discord.ButtonStyle.red)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
       

       
       with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
       
       s = prefixes[f"{str(interaction.message.id)}"]['sector']

       with open('./private/botdata.json', 'r') as f:
          data = json.load(f)

       n = 0

       for i in interaction.user.roles:
            
         if s == "Exchanger":
            if i.id in data["ids-to-have-full-access-in-exchanger-applications"]: 
                 n += 1
                 break

         else:
            if i.id in data["ids-to-have-full-access-in-moderator-applications"]: 
                 n += 1
                 break

       if n < 1 and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message('You cannot do that.', ephemeral=True)
            return



       try:
        
        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)

        user = prefixes[f"{str(interaction.message.id)}"]['user']
        s = prefixes[f"{str(interaction.message.id)}"]['sector']
        time_stamp = prefixes[f"{str(interaction.message.id)}"]['timestamp']
        
        
        roleid = prefixes[f"{str(interaction.message.id)}"]['Role']
        
        
        prefixes[f"{str(interaction.message.id)}"]['Status']

        
        
        with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                
        del prefixes[f"{str(user)}"]
        
        prefixes[f"{str(interaction.message.id)}"]['Status'] = 'Declined'
        
        with open('./database/Applications/applications.json', 'w') as f:
                      json.dump(prefixes, f, indent=1)  
        
        if s == 'Exchanger':
             

            question1 = prefixes[f"{str(interaction.message.id)}"]['question1']
            question2 = prefixes[f"{str(interaction.message.id)}"]['question2']
            question3 = prefixes[f"{str(interaction.message.id)}"]['question3']
            question4 = prefixes[f"{str(interaction.message.id)}"]['question4']
            question5 = prefixes[f"{str(interaction.message.id)}"]['question5']
      
             
            

            
        
            try:
                u = await interaction.guild.fetch_member(user)
    
    

    
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined** by {interaction.user.mention}***', color=0x6056ff)
    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Which exchanges could you do?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— How much experience do you have?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— How much securities are you ready to pay?', value=f'```yaml\n- {question3}```', inline = False)
                embed.add_field(name = f'— Are you exchanging by yourself?', value=f'```yaml\n- {question4}```', inline = False)

                if question5:
                  embed.add_field(name = f'— Any more informations about you?', value=f'```yaml\n- {question5}```', inline = False)
        
                await interaction.message.edit(embed=embed, view=Accepted())
    
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())

            
            except:
                
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined** — **User left**!', color=0x6056ff)    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Which exchanges could you do?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— How much experience do you have?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— How much securities are you ready to pay?', value=f'```yaml\n- {question3}```', inline = False)
                embed.add_field(name = f'— Are you exchanging by yourself?', value=f'```yaml\n- {question4}```', inline = False)

                if question5:
                  embed.add_field(name = f'— Any more informations about you?', value=f'```yaml\n- {question5}```', inline = False)
                
                await interaction.message.edit(embed=embed, view=Accepted())

                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x2ecc71)
                await interaction.response.send_message(embed=embed3, view=Delete())

        else:
            
            question1 = prefixes[f"{str(interaction.message.id)}"]['question1'] 
            question2 = prefixes[f"{str(interaction.message.id)}"]['question2']
            question3 = prefixes[f"{str(interaction.message.id)}"]['question3']
      
             
            

            
        
            try:

                u = await interaction.guild.fetch_member(user)
    
    

    
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined** by {interaction.user.mention}***', color=0x6056ff)
    
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Why do you want to be a moderator?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— What is your timezone?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— Do you have any expierence?', value=f'```yaml\n- {question3}```', inline = False)
        
                await interaction.message.edit(embed=embed, view=Accepted())
    
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())
        
            except:
                
                now = datetime.datetime.now()

                da = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp2 = calendar.timegm(da.timetuple())
    
                embed = discord.Embed(description=f'# {s} Application\n> Status: **Declined**  — **User left**!', color=0x6056ff) 
                embed.set_author(name = f'{interaction.user.name}', icon_url = interaction.user.avatar)
                embed.add_field(name = f'— Why do you want to be a moderator?', value=f'```yaml\n- {question1}```', inline = False)
                embed.add_field(name = f'— What is your timezone?', value=f'```yaml\n- {question2}```', inline = False)
                embed.add_field(name = f'— Do you have any expierence?', value=f'```yaml\n- {question3}```', inline = False)
                
                await interaction.message.edit(embed=embed, view=Accepted())
        
                embed3 = discord.Embed(description=f'# {s} Application\n> Submitted: <t:{time_stamp}:R> — Was declined by: {interaction.user.mention}', color=0x6056ff)
                await interaction.response.send_message(embed=embed3, view=Delete())
           
        
        try:
                  user = await interaction.guild.fetch_member(int(user))

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Application Ticket Has been Deleted.", description=f'- Application was deleted by {interaction.user.mention}\n> Name: `{interaction.channel.name}`', color=0x6056ff)

                  await user.send(embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))

                  
                  os.remove(f"Tickets/{interaction.channel.name}.htm")        

        except:
                    pass   

            
            
            
       except:
         pass
        
        

class Accepted(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='✔️ Accept', custom_id='Accept',style=discord.ButtonStyle.grey, disabled=True)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
      pass
                
                
                
    @discord.ui.button(label='❌ Reject', custom_id='Reject',style=discord.ButtonStyle.grey, disabled=True)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
      pass
        



class Delete(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)


    @discord.ui.button(label='Delete application', style=discord.ButtonStyle.grey, custom_id='deletenotdisabled-button-5', disabled=False)
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        
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
                await msg.edit(view=DeleteTicket(interaction_msg = msg, interaction_user = interaction.user))





               
class DeleteTicket(View):
    def __init__(self, interaction_msg, interaction_user):
        super().__init__(timeout=15)
        self.interaction_msg = interaction_msg
        self.interaction_user = interaction_user

    @discord.ui.select(options=[
            discord.SelectOption(label='Action', value='05', emoji='✔️', description='Delete the application.'),
            discord.SelectOption(label='Return', value='06', emoji='❌', description='Return without deleting the application.')
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
              embed = discord.Embed(description=f"# `🗑️` Deleting Application\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)", color=0x2ecc71)
              embed.set_author(name=f'[{interaction.user.name}]: Deleting application', icon_url=interaction.user.avatar)
              m = await interaction.response.edit_message(content='', embed=embed, view=self)

                
              embed2 = discord.Embed(description=f'`🗑️` {interaction.channel.mention} will be deleted in 5 seconds.\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)', color=0x2ecc71)
              await interaction.channel.send(embed=embed2)
              await asyncio.sleep(5)
         



              try:

                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(interaction.guild.channels, id=data["applications-logs-channel-id"])

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)

                  with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                    
                  uid = prefixes[f"{str(interaction.channel.id)}"]
                
                
                  try:
                        
                        user = interaction.client.get_user(uid)
                        
                        uid_send = f'{user.mention}, {user.name} ({user.id})'
                        
                  except:
                        uid_send = uid

                  embed=discord.Embed(title="Application Ticket Has been Deleted.", description=f'- Application was deleted by {interaction.user.mention}\n- Application Creator: {uid_send}', color=0x73b2df)

                  await channel.send(uid_send, embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm'))

                  
                  os.remove(f"Tickets/{interaction.channel.name}.htm")        

              except:
                    pass   


              await interaction.channel.delete()  



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







        
# --------------------------------- COG ---------------------------------    

class ApplicationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        commands = self.get_commands()
        print(f"COG: Application.py ENABLED [{len(commands)}] commands LOADED")

  
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def apply(self, ctx):
        embed = discord.Embed(description=f'Create an application to become an **Exchanger** or **Moderator.**\n- If you apply as an exchanger, securities are mandatory and will be released on retirement.', color=0x6056ff)

        await ctx.send(embed=embed, view=Application())
        await ctx.message.delete()
        
        
        
        
        
        
            
    # ------------------------------------------------------------------------------THE END---


async def setup(bot):
    await bot.add_cog(ApplicationCog(bot))