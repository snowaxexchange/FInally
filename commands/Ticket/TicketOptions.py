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

from commands.Ticket.TicketCreation import Ticket

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True





class OtherCryptoReceive(discord.ui.Modal, title='Write the crypto you want to receive.'):   
    def __init__(self, option_exchange, category, more_options, receive_exchange):
        super().__init__(timeout=None)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange
    
    reason = discord.ui.TextInput(label='Crypto', style=discord.TextStyle.long, required=True)

    async def on_submit(self, interaction: discord.Interaction):
      
      if self.option_exchange == self.receive_exchange and str(self.more_options) == str(self.reason):
              embed = discord.Embed(description=f"`❌` — Please do not select the **same payment twice**.", color=0x6056ff)
              await interaction.response.edit_message(embed=embed, view=None)
         
      else: 
                
         embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
         embed.add_field(name="Current Amount", value=f'```0.00€```')
   
         await interaction.response.edit_message(embed=embed, view=Ticket(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = f"{self.reason} (**Other Crypto**)"))   
                       



class OtherCryptoSend(discord.ui.Modal, title='Write the crypto you want to send.'):   
    def __init__(self, option_exchange, category):
        super().__init__(timeout=None)
        self.option_exchange = option_exchange
        self.category = category

    
    reason = discord.ui.TextInput(label='Crypto', style=discord.TextStyle.long, required=True)

    async def on_submit(self, interaction: discord.Interaction):

                
                
         embed = discord.Embed(title=f"Sending {self.reason}", description=f"You have selected **{self.reason}** as your Sending method. Now please select what you would like to **receive**.", color=0x6056ff)
 
         await interaction.response.edit_message(embed=embed, view=Exchange_Receive_Options(option_exchange = self.option_exchange, more_options = f"{self.reason} (**Other Crypto**)", category = self.category))   
              





class Exchange_Options(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)

        
    @discord.ui.select(
            custom_id="select-exchange-1",
            placeholder='What will you be sending?',
            options=[
                discord.SelectOption(label='PayPal', description="6% Service Fee", emoji="<:PaypalFlipX:1330282353360371733>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>' READ IT AGAIN BRO INSIDE THE "" NOT WITHOUT ""can u fix LIKE THAT change them all and it will work MARK IT "AWDJIA" AND THEN CLICH THE ""
                discord.SelectOption(label='Crypto', description="0-2% Service Fee", emoji="<:crypto:1330282465834569748>"),
                discord.SelectOption(label='Bank Transfer', description="10% Service Fee", emoji="<:bank:1330282779975618580>"),
                discord.SelectOption(label='Revolut', description="10% Service Fee", emoji="<:revolut:1330283065540345899>"),
                discord.SelectOption(label='Paysafe', description="20% Service Fee", emoji="<:psc:1330282965317455933>"),
                discord.SelectOption(label='Amazon', description="25% Service Fee", emoji="<:amazon:1330283035681357915>"),
                discord.SelectOption(label='Zalando', description= "25% Service Fee", emoji= "<:emoji_1:1330282865161928735>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):

       await interaction.message.edit(view=self)
        
       
       role = discord.utils.get(interaction.guild.roles, id=1281495051427516468) 
        
       if role in interaction.user.roles:
          embed = discord.Embed(description=f"**You are blacklisted from our services**! Appeal this in https://discord.com/channels/1281493293435326474/1281495087054065708", color=0x6056ff)
          await interaction.response.send_message(embed=embed, ephemeral=True)
          return
        
       
       interaction.message.author = interaction.user
       bucket = self.cooldown.get_bucket(interaction.message)
       retry = bucket.update_rate_limit()
    
       if retry:
          
          embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
          await interaction.response.send_message(embed=embed, ephemeral=True)   
            
       else:

            
            with open('./private/botdata.json', 'r') as f:
                      categories_id = json.load(f)
                    

            more_options = ['PayPal', 'Crypto', 'Bank Transfer']

            await interaction.response.defer(thinking=True, ephemeral=True) 

            if select.values[0] in more_options:

              embed = discord.Embed(title=f"Sending {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select which **{select.values[0]}** you will be Sending.", color=0x6056ff)
 




              if select.values[0] == 'PayPal':
                  
                await interaction.followup.send(embed=embed, view=PayPal(option_exchange = select.values[0], category = categories_id[str(select.values[0]) + "-Category"]), ephemeral=True)  

              elif select.values[0] == 'Crypto':
         
                await interaction.followup.send(embed=embed, view=Crypto(option_exchange = select.values[0], category = categories_id[str(select.values[0]) + "-Category"]), ephemeral=True)  

              else:

                await interaction.followup.send(embed=embed, view=Bank_Transfer(option_exchange = select.values[0], category = categories_id[str(select.values[0]) + "-Category"]), ephemeral=True)   

            else:
                
              embed = discord.Embed(title=f"Sending {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select what you would like to **receive**.", color=0x6056ff)
 
              await interaction.followup.send(embed=embed, view=Exchange_Receive_Options(option_exchange = select.values[0], more_options = None, category = categories_id[str(select.values[0]) + "-Category"]), ephemeral=True)   
             
# MORE OPTIONS


# PAYPAL MORE OPTIONS

class PayPal(View):
    def __init__(self, option_exchange, category):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category

        
    @discord.ui.select(
            custom_id="select-paypal-1",
            placeholder='Which PayPal you will be sending?',
            options=[
                discord.SelectOption(label='PayPal Balance', description="6% Service Fee", emoji="<:PaypalFlipX:1330282353360371733>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='PayPal Bank/Card', description="20% Service Fee", emoji="<:PaypalFlipX:1330282353360371733>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):
       

                
       embed = discord.Embed(title=f"Sending {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select what you would like to **receive**.", color=0x6056ff)
 
       await interaction.response.edit_message(embed=embed, view=Exchange_Receive_Options(option_exchange = self.option_exchange, more_options = select.values[0], category = self.category))   
             


          
# CRYPTO MORE OPTIONS 

class Crypto(View):
    def __init__(self, option_exchange, category):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category

        
    @discord.ui.select(
            custom_id="select-crypto-1",
            placeholder='Which Crypto you will be sending?',
            options=[
                discord.SelectOption(label='Bitcoin', description="0-2% Service Fee", emoji="<:btc:1281494990542868542>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='Ethereum', description="0-2% Service Fee", emoji="<:pingers_eth:1281494982225690748>"),
                discord.SelectOption(label='Litecoin', description="0-2% Service Fee", emoji="<:ltc:1281494988269682698>"),
                discord.SelectOption(label='Other', description="0-2% Service Fee", emoji="<:bitz_crypto:1281494969781194792>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):


      if select.values[0] == 'Other':
          
         await interaction.response.send_modal(OtherCryptoSend(option_exchange = self.option_exchange, category = self.category))

      else:
                
       embed = discord.Embed(title=f"Sending {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select what you would like to **receive**.", color=0x6056ff)
 
       await interaction.response.edit_message(embed=embed, view=Exchange_Receive_Options(option_exchange = self.option_exchange, more_options = select.values[0], category = self.category))   
             

# BANK MORE OPTIONS

class Bank_Transfer(View):
    def __init__(self, option_exchange, category):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category

        
    @discord.ui.select(
            custom_id="select-bank-1",
            placeholder='Which Bank Transfer you will be sending?',
            options=[
                discord.SelectOption(label='IBAN Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='UK Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>"),
                discord.SelectOption(label='ACH Bank Transfer', description="10% Service Fee", emoji="<:bank:1279742058147348521>"),
                discord.SelectOption(label='Other Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):
       
                
         embed = discord.Embed(title=f"Sending {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select what you would like to **receive**.", color=0x6056ff)
 
         await interaction.response.edit_message(embed=embed, view=Exchange_Receive_Options(option_exchange = self.option_exchange, more_options = select.values[0], category = self.category))   
             






# NEXT OPTIONS RECEIVING

class Exchange_Receive_Options(View):
    def __init__(self, option_exchange, more_options, category):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.more_options = more_options
        self.category = category

        
    @discord.ui.select(
      custom_id="select-exchange-2",
      placeholder='What you will be receiving?',
      options=[
                discord.SelectOption(label='PayPal', emoji="<:PaypalFlipX:1330282353360371733>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>' READ IT AGAIN BRO INSIDE THE "" NOT WITHOUT ""can u fix LIKE THAT change them all and it will work MARK IT "AWDJIA" AND THEN CLICH THE ""
                discord.SelectOption(label='Crypto',emoji="<:crypto:1330282465834569748>"),
                discord.SelectOption(label='Bank Transfer', emoji="<:bank:1330282779975618580>"),
                discord.SelectOption(label='Revolut', emoji="<:revolut:1330283065540345899>"),
                discord.SelectOption(label='Paysafe', emoji="<:psc:1330282965317455933>"),
                discord.SelectOption(label='Amazon', emoji="<:amazon:1330283035681357915>"),
                discord.SelectOption(label='Zalando', emoji= "<:emoji_1:1330282865161928735>")
      ]
    )
    async def callback(self, interaction: discord.Interaction, select):

         if select.values[0] == self.option_exchange and self.more_options == None:
              embed = discord.Embed(description=f"`❌` — Please do not select the **same payment twice**.", color=0x6056ff)
              await interaction.response.send_message(embed=embed, ephemeral=True)
         
         else:

            more_options = ['PayPal', 'Crypto', 'Bank Transfer']


            if select.values[0] in more_options:
                

              embed = discord.Embed(title=f"Receiving {select.values[0]}", description=f"You have selected **{select.values[0]}** as your Sending method. Now please select which **{select.values[0]}** you will be receiving.", color=0x6056ff)
 




              if select.values[0] == 'PayPal':
                  
                await interaction.response.edit_message(embed=embed, view=PayPal_Receiving(option_exchange = self.option_exchange, category = self.category, more_options = self.more_options, receive_exchange = select.values[0]))  

              elif select.values[0] == 'Crypto':
         
                await interaction.response.edit_message(embed=embed, view=Crypto_Receiving(option_exchange = self.option_exchange, category = self.category, more_options = self.more_options, receive_exchange = select.values[0]))  

              else:

                await interaction.response.edit_message(embed=embed, view=Bank_Transfer_Receiving(option_exchange = self.option_exchange, category = self.category, more_options = self.more_options, receive_exchange = select.values[0]))   

            else:
                
                
              embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
              embed.add_field(name="Current Amount", value=f'```0.00€```')
              
              await interaction.response.edit_message(embed=embed, view=Ticket(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = select.values[0], receive_exchange_more_options = None))   
             


# MORE RECEIVING OPTIONS

# PAYPAL MORE OPTIONS

class PayPal_Receiving(View):
    def __init__(self, option_exchange, category, more_options, receive_exchange):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange

        
    @discord.ui.select(
            custom_id="select-paypal-2",
            placeholder='Which PayPal you will be receiving?',
            options=[
                discord.SelectOption(label='PayPal Balance', emoji="<:PaypalFlipX:1330282353360371733>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='PayPal Bank/Card', emoji="<:PaypalFlipX:1330282353360371733>")
            ]
    )
    async def callback(self, interaction: discord.Interaction, select):
      
      if self.option_exchange == self.receive_exchange and self.more_options == select.values[0]:
              embed = discord.Embed(description=f"`❌` — Please do not select the **same payment twice**.", color=0x6056ff)
              await interaction.response.send_message(embed=embed, ephemeral=True)
         
      else: 

                
       embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
       embed.add_field(name="Current Amount", value=f'```0.00€```')
 
       await interaction.response.edit_message(embed=embed, view=Ticket(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = select.values[0]))   
             


          
# CRYPTO MORE OPTIONS 

class Crypto_Receiving(View):
    def __init__(self, option_exchange, category, more_options, receive_exchange):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange

        
    @discord.ui.select(
            custom_id="select-crypto-2",
            placeholder='Which Crypto you will be receiving?',
            options=[
                discord.SelectOption(label='Bitcoin', description="0-2% Service Fee", emoji="<:btc:1281494990542868542>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='Ethereum', description="0-2% Service Fee", emoji="<:eth:1281494991679524948>"),
                discord.SelectOption(label='Litecoin', description="0-2% Service Fee", emoji="<:ltc:1281494988269682698>"),
                discord.SelectOption(label='Other', description="0-2% Service Fee", emoji="<:bitz_crypto:1281494969781194792>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):

       
       if select.values[0] == 'Other':
          
         await interaction.response.send_modal(OtherCryptoReceive(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange))

       else:

      
        if self.option_exchange == self.receive_exchange and self.more_options == select.values[0]:
              embed = discord.Embed(description=f"`❌` — Please do not select the **same payment twice**.", color=0x6056ff)
              await interaction.response.send_message(embed=embed, ephemeral=True)
         
        else: 

         embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
         embed.add_field(name="Current Amount", value=f'```0.00€```')
   
         await interaction.response.edit_message(embed=embed, view=Ticket(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = select.values[0]))   
                       

# BANK MORE OPTIONS

class Bank_Transfer_Receiving(View):
    def __init__(self, option_exchange, category, more_options, receive_exchange):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 40, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange

        
    @discord.ui.select(
            custom_id="select-bank-2",
            placeholder='Which Bank Transfer you will be receiving?',
            options=[
                discord.SelectOption(label='IBAN Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>"),       # CHANGE emoji=None to emoji='' AND PUT THE EMOJI INSIDE THE '', '<- ->' e.g. emoji='<:seliniapproved:1198374002650001498>'
                discord.SelectOption(label='UK Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>"),
                discord.SelectOption(label='ACH Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>"),
                discord.SelectOption(label='Other Bank Transfer', description="10% Service Fee", emoji="<:bank:1281495004426145824>")
            ]
    )

    async def callback(self, interaction: discord.Interaction, select):

                  
      if self.option_exchange == self.receive_exchange and self.more_options == select.values[0]:
              embed = discord.Embed(description=f"`❌` — Please do not select the **same payment twice**.", color=0x6056ff)
              await interaction.response.send_message(embed=embed, ephemeral=True)
         
      else: 
           
       embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
       embed.add_field(name="Current Amount", value=f'```0.00€```')
 
       await interaction.response.edit_message(embed=embed, view=Ticket(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = select.values[0]))   
             






class TicketOptions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        commands = self.get_commands()
        print(f"COG: TicketOptions.py ENABLED [{len(commands)}] commands LOADED")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def exchangeticket(self, ctx):
       embed = discord.Embed(description=f"# FlipX Exchanges\n> With creating a Ticket, you are accepting the https://discord.com/channels/1315035618048475246/1316860655030239375.\n## -  Reminder\nPlease read our https://discord.com/channels/1315035618048475246/1316860655030239375 before creating a ticket.\n## - Minimum Amount\nOur minimum service amount is 0.50€ and is applicable on every deal and is non-negotiable.", color=0x6056ff)
       embed.set_footer(text="FlipX Exchanges - Transform your money cheap, fast and easily!")
       embed.set_image(url="https://cdn.discordapp.com/attachments/1322300070170726520/1329951840518803536/banner.jpg?ex=678c35ac&is=678ae42c&hm=6fedbed72bc398d9ede63c77a2ca9fd6e0816e9b90cf54a4429072d4c6437e56&")
       await ctx.send(embed=embed, view=Exchange_Options())
       await ctx.message.delete()



async def setup(bot):
    await bot.add_cog(TicketOptions(bot))