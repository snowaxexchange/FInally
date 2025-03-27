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

from commands.PrefixCommands.SupportTickets import SupportClose


import chat_exporter

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True


class Ticket(discord.ui.View):
    def __init__(self, option_exchange, category, more_options, receive_exchange, receive_exchange_more_options):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange
        self.more_receive_exchange = receive_exchange_more_options


        self.row_big = 0
        self.row_low = 0

        self.price_big = '0'
        self.price_low = '00'


        self.point = None


    @discord.ui.button(label='7', style=discord.ButtonStyle.grey, custom_id='seven', row=0)
    async def seven(self, interaction: discord.Interaction, button: discord.ui.Button):
       
       s = list(self.price_big)



       if self.point == None:
          

          
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1



             s += '7'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

          else:
             

             s[self.row_big] = '7'

             self.price_big = "".join(s)

             self.row_big += 1

          
          
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   



       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '7'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '7'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

    @discord.ui.button(label='8', style=discord.ButtonStyle.grey, custom_id='eight', row=0)
    async def eight(self, interaction: discord.Interaction, button: discord.ui.Button):
       
       s = list(self.price_big)



       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '8'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

          else:
                
                       

             s[self.row_big] = '8'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '8'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '8'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

    @discord.ui.button(label='9', style=discord.ButtonStyle.grey, custom_id='nine', row=0)
    async def nine(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '9'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

          else:
                  
                     

             s[self.row_big] = '9'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '9'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '9'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   



    @discord.ui.button(label='4', style=discord.ButtonStyle.grey, custom_id='four', row=1)
    async def four(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '4'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff) 
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                  
                     
             s[self.row_big] = '4'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '4'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '4'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

    @discord.ui.button(label='5', style=discord.ButtonStyle.grey, custom_id='five', row=1)
    async def five(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '5'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                          

             
             s[self.row_big] = '5'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '5'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '5'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

    @discord.ui.button(label='6', style=discord.ButtonStyle.grey, custom_id='six', row=1)
    async def six(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
          
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '6'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                     
               

             s[self.row_big] = '6'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
              

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break


             await interaction.response.edit_message(embed=embed, view=self)   
             



       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '6'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '6'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   



    @discord.ui.button(label='1', style=discord.ButtonStyle.grey, custom_id='one', row=2)
    async def one(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '1'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                          

             
             s[self.row_big] = '1'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '1'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '1'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   

    @discord.ui.button(label='2', style=discord.ButtonStyle.grey, custom_id='two', row=2)
    async def two(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]
                
             self.row_big += 1

             

             s += '2'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                          

             
             s[self.row_big] = '2'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '2'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '2'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


    @discord.ui.button(label='3', style=discord.ButtonStyle.grey, custom_id='three', row=2)
    async def three(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]

             self.row_big += 1

             

             s += '3'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_big] = '3'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:    
          
          s = list(self.price_low)   
             
          if self.row_low > 1:

             s[-1] = '3'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '3'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             



    @discord.ui.button(label='.', style=discord.ButtonStyle.grey, custom_id='point', row=3)
    async def point(self, interaction: discord.Interaction, button: discord.ui.Button):
       
       if self.point == None:

         s = list(self.price_big)
          

         self.point = 'True'

         if self.price_big == '0':
          
          await interaction.response.edit_message(view=self) 

         else:


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
              
             await interaction.response.edit_message(embed=embed, view=self)   

       else:

          await interaction.response.edit_message(view=self) 
          
    @discord.ui.button(label='0', style=discord.ButtonStyle.grey, custom_id='zero', row=3)
    async def zero(self, interaction: discord.Interaction, button: discord.ui.Button):
              
       s = list(self.price_big)


       
       if self.point == None:
                    
          if self.row_big > 0:
             
             if s[0] == '0':
                del s[0]


             self.row_big += 1

             

             s += '0'


             self.price_big = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_big] = '0'


             self.price_big = "".join(s)

             self.row_big += 1


             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   
             

       else:
          
          s = list(self.price_low)
             
          if self.row_low > 1:

             s[-1] = '0'


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


          else:
                         

             
             s[self.row_low] = '0'


             self.price_low = "".join(s)

             self.row_low += 1

             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big != '0' or self.price_low != '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = False
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


    @discord.ui.button(label='⌫', style=discord.ButtonStyle.grey, custom_id='erase', row=3)
    async def erase(self, interaction: discord.Interaction, button: discord.ui.Button):
              

          
          s = list(self.price_low)
          
                    
          if self.row_low - 1 < 2:
             
             if self.price_low != '00':

               self.row_low -= 1

               s[self.row_low] = '0'

               self.price_low = "".join(s)
             
               embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
               embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                              
               if self.price_big == '0' and self.price_low == '00':
                
                       shiny_button = None

                       for child in self.children:
                        if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = True
                          break
                        
               await interaction.response.edit_message(embed=embed, view=self)   

             else:
                 
                 self.point = None

                 s = list(self.price_big)

                           
                 if self.row_big - 1 < 1:
             
                    if self.price_big != '0':

                      self.row_big -= 1
       
                      s[self.row_big] = '0'

                      self.price_big = "".join(s)
                    
                      embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
                      embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
               
                      if self.price_big == '0' and self.price_low == '00':
                
                       shiny_button = None

                       for child in self.children:
                        if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = True
                          break
                      
                      await interaction.response.edit_message(embed=embed, view=self)   

                    else:

                      await interaction.response.edit_message(view=self)   

                 else:
                    
                    self.row_big -= 1
             

                    del s[-1]
       

                    self.price_big = "".join(s)
             
                    embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
                    embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                                          

                    if self.price_big == '0' and self.price_low == '00':
                
                     shiny_button = None

                     for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = True
                          break
                      
                    await interaction.response.edit_message(embed=embed, view=self)  




          else:
             
             self.row_low -= 1
             

             del s[-1]


             self.price_low = "".join(s)
             
             embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
             embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
                            

             if self.price_big == '0' and self.price_low == '00':
                
                  shiny_button = None

                  for child in self.children:
                      if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = True
                          break
                      
             await interaction.response.edit_message(embed=embed, view=self)   


    @discord.ui.button(label='Clear', style=discord.ButtonStyle.red, custom_id='clear', row=4)
    async def clear(self, interaction: discord.Interaction, button: discord.ui.Button):

       self.row_big = 0
       self.row_low = 0

       self.price_big = '0'
       self.price_low = '00'


       self.point = None
              

                
       shiny_button = None

       for child in self.children:
         if type(child) == discord.ui.Button and child.label == "Submit":
                          shiny_button = child
                          child.disabled = True
                          break
             
       embed = discord.Embed(title=f"Currency Amount Selection", description=f"Click the buttons below to enter an amount.", color=0x6056ff)
       embed.add_field(name="Current Amount", value=f'```{self.price_big}.{self.price_low}€```')
              
       await interaction.response.edit_message(embed=embed, view=self)   


    @discord.ui.button(label='Submit', style=discord.ButtonStyle.green, custom_id='submit', row=4, disabled=True)
    async def submit(self, interaction: discord.Interaction, button: discord.ui.Button):
       
      try:
         with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

         cid = data[f"{interaction.user.id}"]
                  

         channel = discord.utils.get(interaction.guild.channels, id=cid)
         embed = discord.Embed(description=f"**You cannot create two Exchange tickets**!\n⬩ {channel.mention}, close your current ticket and then try again.\n-# ⓘ Used to prevent ticket spam.", color=0x6056ff)
         await interaction.response.edit_message(embed=embed, ephemeral=True)   
         return

      except:
          pass




      embed = discord.Embed(title=f"Only Transact Within Your Ticket!", description="For your own safety **ONLY** transact within your ticket where funds are safety held for both parties. We will **NOT** be responsible if you get scammed due to a transaction outside of your ticket!\n\n**Anyone trying to get you to transact outside of your ticket is most likely trying to scam you!**", color=0x6056ff)

      await interaction.response.edit_message(embed=embed, view=Confirmation_1(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = self.more_receive_exchange, price_low = self.price_low, price_big = self.price_big))





class Confirmation_1(discord.ui.View):
    def __init__(self, option_exchange, category, more_options, receive_exchange, receive_exchange_more_options, price_big, price_low):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange
        self.more_receive_exchange = receive_exchange_more_options

        self.price_big = price_big
        self.price_low = price_low

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green, custom_id='confirm-1')
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
      
      price_send = int(self.price_big) + int(self.price_low) / 100
        
      if price_send < 1:
        await interaction.response.send_message('Your lower than the minimum. **The least you can exchange is 1€**', ephemeral=True)
        return

      price_plus = ''

      ten = ['Revolut', 'Venmo', 'Zelle', 'Skrill', 'Wise', 'Bank Transfer']

      if self.option_exchange == 'CashApp':
        price_receive = price_send - price_send * 10/100 - 3
        
      if self.option_exchange == 'Crypto':
        
        if self.receive_exchange == 'Crypto':

          price_receive = price_send - price_send * 2/100

        elif self.receive_exchange == 'PayPal':
          price_receive = price_send - price_send * 1/100
            
        else:

          price_receive = price_send


      if self.option_exchange in ten:
        price_receive = price_send - price_send * 10/100
          
      if self.option_exchange == 'PayPal':
        
        if self.more_options == 'PayPal Bank/Card':
          price_receive = price_send - price_send * 20/100


        else:
            
          if self.receive_exchange == 'Crypto':
              price_receive = price_send - price_send * 6/100
        
          else:
                
            
            if price_send > 10:
              price_receive = price_send - price_send * 7/100
            
            else:
              price_receive = price_send - price_send * 8/100

      if self.option_exchange == 'Apple Pay':
         price_receive = price_send - price_send * 25/100
            
      if self.option_exchange == 'Amazon':   
         price_receive = price_send - price_send * 25/100  

      if self.option_exchange == 'Paysafe':
         price_receive = price_send - price_send * 20/100
 
      if self.option_exchange == 'Zalando':
         price_receive = price_send - price_send * 25/100
            
      if price_send - price_receive < 0.5:
            price_receive = price_send - 0.5
            
      embed = discord.Embed(title=f"Exch Confirmation", description=f"Make sure everything below is correct before confirming your Exch request!", color=0x6056ff)

    
    
    
      if self.more_options:
        embed.add_field(name="Sending", value=f"{price_send}€ {self.more_options}", inline=True)
        
      else:
        embed.add_field(name="Sending", value=f"{price_send}€ {self.option_exchange}", inline=True)
      
      if self.more_receive_exchange:
        embed.add_field(name="Receiving", value=f"{round(price_receive, 2)}{price_plus}€ {self.more_receive_exchange}", inline=True)

      else:
        embed.add_field(name="Receiving", value=f"{round(price_receive, 2)}{price_plus}€ {self.receive_exchange}", inline=True)

      await interaction.response.edit_message(embed=embed, view=Confirmation_2(option_exchange = self.option_exchange, more_options = self.more_options, category = self.category, receive_exchange = self.receive_exchange, receive_exchange_more_options = self.more_receive_exchange, price_low = self.price_low, price_big = self.price_big))



    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red, custom_id='cancel-1')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):


      embed = discord.Embed(description="<a:blurpleLoad:1327695246037094541> — Your Exch was cancelled.", color=0x6056ff)
      await interaction.response.edit_message(embed=embed, view=None)




class Confirmation_2(discord.ui.View):
    def __init__(self, option_exchange, category, more_options, receive_exchange, receive_exchange_more_options, price_big, price_low):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.user)
        self.option_exchange = option_exchange
        self.category = category
        self.more_options = more_options
        self.receive_exchange = receive_exchange
        self.more_receive_exchange = receive_exchange_more_options

        self.price_big = price_big
        self.price_low = price_low

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green, custom_id='confirm-2')
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
      
      price_send = int(self.price_big) + int(self.price_low) / 100

      price_plus = ''

      ten = ['Revolut', 'Venmo', 'Zelle', 'Skrill', 'Wise', 'Bank Transfer']

      if self.option_exchange == 'CashApp':
        price_receive = price_send - price_send * 10/100 - 3
        
      if self.option_exchange == 'Crypto':
        
        if self.receive_exchange == 'Crypto':

          price_receive = price_send - price_send * 2/100

        elif self.receive_exchange == 'PayPal':
          price_receive = price_send - price_send * 1/100
            
        else:

          price_receive = price_send


      if self.option_exchange in ten:
        price_receive = price_send - price_send * 10/100
          
      if self.option_exchange == 'PayPal':
        
        if self.more_options == 'PayPal Bank/Card':
          price_receive = price_send - price_send * 20/100


        else:
            
          if self.receive_exchange == 'Crypto':
              price_receive = price_send - price_send * 6/100
        
          else:
                
            
            if price_send > 10:
              price_receive = price_send - price_send * 7/100
            
            else:
              price_receive = price_send - price_send * 8/100

      if self.option_exchange == 'Apple Pay':
         price_receive = price_send - price_send * 25/100
            
      if self.option_exchange == 'Amazon':   
         price_receive = price_send - price_send * 25/100  

      if self.option_exchange == 'Paysafe':
         price_receive = price_send - price_send * 20/100
 
      if self.option_exchange == 'Zalando':
         price_receive = price_send - price_send * 25/100
            
      if price_send - price_receive < 0.5:
            price_receive = price_send - 0.5
    
      embed=discord.Embed(description=f'<a:blurpleLoad:1327695246037094541>  —  Creating Exchange ticket...', color=0x6056ff)
      await interaction.response.edit_message(embed=embed, view=None)

       
      try:
         with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

         cid = data[f"{interaction.user.id}"]
                  

         channel = discord.utils.get(interaction.guild.channels, id=cid)
         embed = discord.Embed(description=f"**You cannot create two Exch tickets**!\n⬩ {channel.mention}, close your current ticket and then try again.\n-# ⓘ Used to prevent ticket spam.", color=0x6056ff)
         await interaction.edit_original_response(embed=embed)   
         return

      except:
          pass




      category = discord.utils.get(interaction.guild.categories, id=self.category)
    
      with open('./private/botdata.json', 'r') as f:
            data = json.load(f)
    
      category2 = discord.utils.get(interaction.guild.categories, id=data['ticket-overflow-1'])
        
      if price_send >= 100:
        category = discord.utils.get(interaction.guild.categories, id=data['100+category'])

      #mod = discord.utils.get(interaction.guild.roles, id=ID)  <- moderator   
      #exchanger = discord.utils.get(interaction.guild.roles, id=ID)  <- exchanger            

      with open('./database/Stats.json', 'r') as f:
         data = json.load(f)

      n = data["count"]
      data["count"] += 1

      with open('./database/Stats.json', 'w') as f:
         json.dump(data, f, indent=1)

      overwrites = { # DEFAULT PERMISSIONS FOR @EVERYONE AND USER, CURRENTLY ONLY ADMINS CAN SEE TICKET.
                    interaction.guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False),
                    interaction.user: discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
      }             

      with open('./private/botdata.json', 'r') as f:
         data = json.load(f)
 
      for i in data['ids-to-have-full-access-in-tickets']:
          r = discord.utils.get(interaction.guild.roles, id=i)

          overwrites[r] = discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
          

      for i in data['ids-to-have-access-before-claim-in-tickets']:
          r = discord.utils.get(interaction.guild.roles, id=i)

          overwrites[r] = discord.PermissionOverwrite(send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
          
      for i in data['exchangers']:
          r = discord.utils.get(interaction.guild.roles, id=i)

          overwrites[r] = discord.PermissionOverwrite(send_messages=False, read_messages=True, add_reactions=False, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
         
      try:             
        ticket_channel = await interaction.guild.create_text_channel(f"{self.option_exchange[0].lower()}2{self.receive_exchange[0].lower()}・{interaction.user.name}", category=category, overwrites=overwrites)
      except:
        ticket_channel = await interaction.guild.create_text_channel(f"{self.option_exchange[0].lower()}2{self.receive_exchange[0].lower()}・{interaction.user.name}", category=category2, overwrites=overwrites)
        


      with open('./database/TicketData.json', 'r') as f:
         data = json.load(f)

      data[f"{str(ticket_channel.id)}"] = {}

      data[f"{str(ticket_channel.id)}"]['Position'] = n

      data[f"{str(ticket_channel.id)}"]['Exchange'] = {}
      data[f"{str(ticket_channel.id)}"]['Exchange']['Type'] = str(self.option_exchange)
      data[f"{str(ticket_channel.id)}"]['Exchange']['More-Options'] = str(self.more_options)

      data[f"{str(ticket_channel.id)}"]['Receive-Exchange'] = {}
      data[f"{str(ticket_channel.id)}"]['Receive-Exchange']['Type'] = str(self.receive_exchange)
      data[f"{str(ticket_channel.id)}"]['Receive-Exchange']['More-Options'] = str(self.more_receive_exchange)

      data[f"{str(ticket_channel.id)}"]['Price-Send'] = round(price_send, 2)
      data[f"{str(ticket_channel.id)}"]['Price-Receive'] = f"{round(price_receive, 2)}{price_plus}"

      data[f"{str(ticket_channel.id)}"]['Exchange-Request-User'] = {}
      data[f"{str(ticket_channel.id)}"]['Exchange-Request-User']['ID'] = interaction.user.id
      data[f"{str(ticket_channel.id)}"]['Exchange-Request-User']['Name'] = interaction.user.name

      data[f"{str(ticket_channel.id)}"]['Users'] = []
      data[f"{str(ticket_channel.id)}"]['Users'].append(interaction.user.id)

      data[f"{str(ticket_channel.id)}"]["Status"] = 'Pending'


      data[int(interaction.user.id)] = ticket_channel.id
                
      with open('./database/TicketData.json', 'w') as f:
         json.dump(data, f, indent=1)


          

      now = datetime.datetime.now()

      d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
      time_stamp = calendar.timegm(d.timetuple())

      embed = discord.Embed(title=f"{self.option_exchange} Balance Exch", description=f"Please be patient and wait for a reply as we are not always available.\n-# Created by **{interaction.user.name}** ({interaction.user.id}), **<t:{time_stamp}:R>**", color=0x6056ff)

      if self.more_options:
        embed.add_field(name="Sending", value=f"{round(price_send, 2)}€ {self.more_options}", inline=True)
        
      else:
        embed.add_field(name="Sending", value=f"{round(price_send, 2)}€ {self.option_exchange}", inline=True)
      
      if self.more_receive_exchange:
        embed.add_field(name="Receiving", value=f"{round(price_receive, 2)}{price_plus}€ {self.more_receive_exchange}", inline=True)

      else:
        embed.add_field(name="Receiving", value=f"{round(price_receive, 2)}{price_plus}€ {self.receive_exchange}", inline=True)
        
        
      msg = await ticket_channel.send(interaction.user.mention, embed=embed, view=TicketOptions())
      
        
      if self.option_exchange == 'Apple Pay' or self.option_exchange == 'Amazon' or self.option_exchange == 'Paysafe':
          embed2 = discord.Embed(title="Giftcard Region", description="- Please mention your giftcard's region. **Your ticket won't be claimed if you don't do so**.", color=0x6056ff)
          await ticket_channel.send(embed=embed2)

      with open('./private/botdata.json', 'r') as f:
         data = json.load(f)

          
      if price_send >= 100:
        
          role = discord.utils.get(interaction.guild.roles, id=data[f"100+Ping"])

          m = await ticket_channel.send(role.mention)
          await m.delete()   
      
      else:
            
        if discord.utils.get(interaction.guild.roles, id=data[f"{self.option_exchange}-Ping"]):
          role = discord.utils.get(interaction.guild.roles, id=data[f"{self.option_exchange}-Ping"])

          m = await ticket_channel.send(role.mention)
          await m.delete()



      with open('./database/TicketData.json', 'r') as f:
         data = json.load(f)

      data[str(ticket_channel.id)]['Message'] = msg.id
                
      with open('./database/TicketData.json', 'w') as f:
         json.dump(data, f, indent=1)


      embed = discord.Embed(description = f'<a:BlueCheck:1327693608115245056>  — **Ticket created** {ticket_channel.mention}', color=0x6056ff)
      await interaction.edit_original_response(embed=embed)   



    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red, custom_id='cancel-2')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        
      embed = discord.Embed(description="<a:snowy_redx:1329584889825333299> — Your Exch was cancelled.", color=0x6056ff)
      await interaction.response.edit_message(embed=embed, view=None)

        
class AfterMM(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)

    @discord.ui.button(label='Close', style=discord.ButtonStyle.red, custom_id='close-3')
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):

     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:


          
        with open('./private/botdata.json', 'r') as f:

            data = json.load(f)      

        c = 0


        for i in data['ids-to-have-full-access-in-tickets']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    if r in interaction.user.roles:
                        c += 1


        try:

             
          if interaction.user.guild_permissions.administrator or c > 0:
            pass 
          
          else:

            try:

                  with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)

                  d = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']
                  status = data[f"{interaction.channel.id}"]["Status"]
                    
                  if status == 'Completed' or status == 'Cancelled':
                    pass
                
                  else:
                    
                    if interaction.user.id != d:
                      await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
                      return

            except:
                       
              await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
              return
                    

        except:
                    
            await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
            return


        embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        embed = discord.Embed(description='`❓` — **Are you sure you want to close this ticket**?\n-# Select an option down below.', color=0x6056ff)
        msg = await interaction.channel.send(interaction.user.mention, embed=embed)
        await msg.edit(view=CloseTicket(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))



    @discord.ui.button(label='Claim', style=discord.ButtonStyle.green, custom_id='claim-disabled', disabled=True)
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
        
        
        
        
        
        
        

class TicketOptions(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)

    @discord.ui.button(label='Close', style=discord.ButtonStyle.red, custom_id='close')
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):

     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:


          
        with open('./private/botdata.json', 'r') as f:

            data = json.load(f)      

        c = 0


        for i in data['ids-to-have-full-access-in-tickets']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    if r in interaction.user.roles:
                        c += 1


        try:

             
          if interaction.user.guild_permissions.administrator or c > 0:
            pass 
          
          else:

            try:

                  with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)

                  d = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']
                  status = data[f"{interaction.channel.id}"]["Status"]
                    
                  if status == 'Completed' or status == 'Cancelled':
                    pass
                
                  else:
                    
                    if interaction.user.id != d:
                      await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
                      return

            except:
                       
              await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
              return
                    

        except:
                    
            await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
            return


        embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        embed = discord.Embed(description='`❓` — **Are you sure you want to close this ticket**?\n-# Select an option down below.', color=0x6056ff)
        msg = await interaction.channel.send(interaction.user.mention, embed=embed)
        await msg.edit(view=CloseTicket(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))



    @discord.ui.button(label='Claim', style=discord.ButtonStyle.green, custom_id='claim')
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
            
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:
        
                await interaction.response.defer(thinking=True, ephemeral=True) 


                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                uid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]

                try:
                    
                    user = await interaction.guild.fetch_member(uid)

                except:
                  
                  name = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["Name"]

                  embed = discord.Embed(description=f'`❌` — {name}, {uid} left, Exchange cannot be continued. Talk with an administrator.', color=0x6056ff)
                  await interaction.followup.send(f"{interaction.user.mention}", embed=embed)  
                  return

                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                price = data[str(interaction.channel.id)]['Price-Send']
 
                    

                


                try:

                     try:

                       with open('./database/UserData.json', 'r') as f:
                         data = json.load(f)

                       m = data[str(interaction.user.id)]['limit']

                       try:
                          
                          current = data[str(interaction.user.id)]['Current-Limit']

                          if current + price > m:
                               
                              await interaction.followup.send(f"Out of your limit! `{current + price} > {m}`.", ephemeral=True)
                              return
                           
                          else:
                              pass

                             
                       except:
                           

                          if price > m:
                               
                              await interaction.followup.send(f"Out of your limit! `{price} > {m}`.", ephemeral=True)
                              return


                     except:
                       await interaction.followup.send("You don't have limit! Please talk with an administrator.", ephemeral=True)
                       return
                    

                except:
                    
                    await interaction.followup.send("You don't have limit! Please talk with an administrator.", ephemeral=True)
                    return
                    

               


                try:

                     try:

                       with open('./database/UserData.json', 'r') as f:
                         data = json.load(f)

                       m = data[str(interaction.user.id)]['max']

                       try:
                          
                          current = data[str(interaction.user.id)]['Current']

                          if current + price > m:
                               
                              await interaction.followup.send(f"Out of your max! `{current + price} > {m}`.", ephemeral=True)
                              return
                           
                          else:
                              pass

                             
                       except:
                           

                          if price > m:
                               
                              await interaction.followup.send(f"Out of your max! `{price} > {m}`.", ephemeral=True)
                              return


                     except:
                       await interaction.followup.send("You don't have max! Please talk with an administrator.", ephemeral=True)
                       return
                    

                except:
                    
                    await interaction.followup.send("Your not an Exchanger. You cannot claim this exchange!", ephemeral=True)
                    return
                    
                
                
                
                try:    
                       
                          with open('./database/UserData.json', 'r') as f:
                             data = json.load(f)
                    
                          data[str(interaction.user.id)]['Current-Limit'] += round(price, 2)
                       
                          with open('./database/UserData.json', 'w') as f:
                             json.dump(data, f, indent=1)
 
                        
                except:  
                            with open('./database/UserData.json', 'r') as f:
                               data = json.load(f)
                            
                            data[str(interaction.user.id)]['Current-Limit'] = round(price, 2)

                            with open('./database/UserData.json', 'w') as f:
                               json.dump(data, f, indent=1)
                
                    
                    
                try:      
                       
                          with open('./database/UserData.json', 'r') as f:
                             data = json.load(f)
                    
                          data[str(interaction.user.id)]['Current'] += round(price, 2)
                       
                          with open('./database/UserData.json', 'w') as f:
                             json.dump(data, f, indent=1)

                        
                except:  
                    
                            with open('./database/UserData.json', 'r') as f:
                               data = json.load(f)
                            
                            data[str(interaction.user.id)]['Current'] = round(price, 2)

                            with open('./database/UserData.json', 'w') as f:
                               json.dump(data, f, indent=1)
                    
                    
                    
                    
                with open('./private/botdata.json', 'r') as f:

                     data = json.load(f)

                c = 0


                for i in data['exchangers']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    if r in interaction.user.roles:
                        c += 1

                if interaction.user.guild_permissions.administrator or c > 0:
                    pass

                else:
                    await interaction.followup.send("Your not an Exchanger. You cannot claim this exchange!", ephemeral=True)
                    return

                await interaction.message.edit(view=AfterMM())



                for i in data['ids-to-have-access-before-claim-in-tickets']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    
                    await interaction.channel.set_permissions(r, send_messages=True, read_messages=False)
          
                for i in data['exchangers']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    
                    await interaction.channel.set_permissions(r, send_messages=True, read_messages=False)
          

                await interaction.channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=True)




                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"] = {}
                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["Name"] = interaction.user.name
                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"] = interaction.user.id
                data[f"{str(interaction.channel.id)}"]["Status"] = 'Claimed'
                
                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)




        

                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                n = data[str(interaction.channel.id)]['Position']


                option_exchange = data[str(interaction.channel.id)]['Exchange']['Type']
                more_options = data[str(interaction.channel.id)]['Exchange']['More-Options']

                receive_exchange = data[str(interaction.channel.id)]['Receive-Exchange']['Type']
                more_receive_options = data[str(interaction.channel.id)]['Receive-Exchange']['More-Options']
    
                with open('./private/botdata.json', 'r') as f:
                    data = json.load(f)
    
                category = discord.utils.get(interaction.guild.categories, id=data['claimed-exchanges-category-id'])

                
                await interaction.channel.edit(name=f'{option_exchange[0].lower()}2{receive_exchange[0].lower()}・{interaction.user.name}', category=category)

                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
                        
                id = data[str(interaction.channel.id)]['Message']

                msg = await interaction.channel.fetch_message(id)

                embed = msg.embeds[0]
                embed.add_field(name=f"Exchanger", value=f"{interaction.user.mention}", inline=True)
                await msg.edit(embed=embed)

                now = datetime.datetime.now()

                price_send = data[str(interaction.channel.id)]['Price-Send']
                price_receive = data[str(interaction.channel.id)]['Price-Receive']

                    
                with open('./database/UserData.json', 'r') as f:
                    data = json.load(f)


                now = datetime.datetime.now()

                d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp = calendar.timegm(d.timetuple())
                    
                    
                try:
                        
                    data[str(interaction.user.id)]['Active']
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                except:
                                              
                    data[str(interaction.user.id)]['Active'] = []
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")

                with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)


                       


                payment = ''
                p2 = ''

                try:

                    with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                    data[str(interaction.user.id)]

                    if more_options:

                      if option_exchange == 'Crypto':

                        if more_options == 'Litecoin':
                           payment = data[str(interaction.user.id)]['ltc'] 
                           p2 = payment
                            
                           payment = f"{more_options}: **`{payment}`**"
                          
                        if more_options == 'Bitcoin':
                           payment = data[str(interaction.user.id)]['btc']
                           p2 = payment
                            
                           payment = f"{more_options}: **`{payment}`**"
                          
                        if more_options == 'Ethereum':
                           payment = data[str(interaction.user.id)]['eth'] 
                           p2 = payment
                            
                           payment = f"{more_options}: **`{payment}`**"


                        if payment == '':
                          
                          payment = 'No payment details were found.'

                      else:
                          
                           payment = data[str(interaction.user.id)][f'{option_exchange}'] 
                        
                           p2 = payment
                            
                           payment = f"{option_exchange}: **`{payment}`**"


                            
                      
                          
                      

                    else:

                    

                      payment = data[str(interaction.user.id)][f'{option_exchange}']
                        
                      p2 = payment
                    
                      payment = f"{option_exchange}: **`{payment}`**"
                    






                except:
             
                    p2 = ''
                    payment = 'No payment details were found.'

                with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)  
                        
                role = discord.utils.get(interaction.guild.roles, id=data['on-break-role-id'])
                
                if role in interaction.user.roles:
                  channel = discord.utils.get(interaction.guild.channels, id=data["admin-notify-channel-id"])
                
                  await channel.send(f'@everyone\n\n{interaction.user.mention}, {interaction.user.name} ({interaction.user.id}) claimed exchange ticket while being **ON BREAK**.')

                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)


                user = data[str(interaction.channel.id)][f'Exchange-Request-User']['ID']
                usersend = await interaction.guild.fetch_member(int(user))

                embed2 = None
                
                if option_exchange == 'PayPal':
                  embed2 = discord.Embed(title="Terms of Service", description="Failing to follow any TOS below will result in no refund or exchange.\n- Send as Friends and Family only!\n- Don't add any notes\n- Send from PayPal Balance\n- Only send in Euro Currency\n- If the PayPal account is getting locked, you won't get any refund.\n- If the account is grabbed, you will not get any refund.", color=0x6056ff)

 
                
                embed = discord.Embed(title=f'Ticket Claimed', description=f"- Ticket has been claimed by {interaction.user.mention}\n- If the amount shouldn’t be correct, let the Exchanger know.\n- Sending too much money which is not the stated deal amount will result in no refund in case of a scam.", color=0x6056ff)
                
                if embed2:
                  msg = await interaction.channel.send(f"{usersend.mention}, {interaction.user.mention}", embeds=[embed, embed2])
                else:
                  msg = await interaction.channel.send(f"{usersend.mention}, {interaction.user.mention}", embed=embed)

                embed3 = discord.Embed(title=f'Ticket Claimed', description=f"- Ticket has been claimed by {interaction.user.mention}, check it out {interaction.channel.mention}", color=0x6056ff)
                
                try: 
                  await usersend.send(embed=embed3)
                except:
                   pass


                embed=discord.Embed(title=f"{interaction.user.name} payment details", description=f"{payment}", color=0x6056ff)
                await interaction.channel.send(f"{p2}", embed=embed)
            


                await interaction.followup.send("You successfully claimed this exchange.", ephemeral=True)

    @discord.ui.button(label='Request MM', style=discord.ButtonStyle.green, custom_id='claim-as-mm-1')
    async def mm(self, interaction: discord.Interaction, button: discord.ui.Button):
            
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:
            
        
        await interaction.response.defer(thinking=True, ephemeral=True)     
            
        with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

        uid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]

        try:
                    
                    user = await interaction.guild.fetch_member(uid)

        except:
                  
                  name = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["Name"]

                  embed = discord.Embed(description=f'`❌` — {name}, {uid} left, Exchange cannot be continued. Talk with an administrator.', color=0x6056ff)
                  await interaction.followup.send(f"{interaction.user.mention}", embed=embed)  
                  return

        with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

        price = data[str(interaction.channel.id)]['Price-Send']
                


        try:

                     try:

                       with open('./database/UserData.json', 'r') as f:
                         data = json.load(f)

                       m = data[str(interaction.user.id)]['max']

                     except:
                       await interaction.followup.send("You don't have max! Please talk with an administrator.")
                       return
                    

        except:
                    
                    await interaction.followup.send("Your not an Exchanger. You cannot claim this exchange!")
                    return
                    
            
        with open('./private/botdata.json', 'r') as f:
            data = json.load(f)  
      
        for i in data['exchangers']:
                  if i != data['middleman-role-id']:
                    r = discord.utils.get(interaction.guild.roles, id=i)
                    await interaction.channel.set_permissions(r, send_messages=False, read_messages=False)
    
        await interaction.channel.set_permissions(interaction.user, send_messages=False, read_messages=True, add_reactions=False)
          
           
        button.disabled = True
        await interaction.message.edit(view=AfterMM()) 
                 
      
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)  
            
        option_exchange = data[str(interaction.channel.id)]['Exchange']['Type']
        more_options = data[str(interaction.channel.id)]['Exchange']['More-Options']

        receive_exchange = data[str(interaction.channel.id)]['Receive-Exchange']['Type']
        more_receive_options = data[str(interaction.channel.id)]['Receive-Exchange']['More-Options']
        
        price_receive = data[str(interaction.channel.id)]['Price-Receive']

            
        with open('./database/UserData.json', 'r') as f:
                    data = json.load(f)


        now = datetime.datetime.now()

        d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time_stamp = calendar.timegm(d.timetuple())
                    
                    
        try:
                        
                    data[str(interaction.user.id)]['Active']
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
        except:
                                              
                    data[str(interaction.user.id)]['Active'] = []
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")

        with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)
            
            
        with open('./private/botdata.json', 'r') as f:
                    data = json.load(f)
        
        middleman = discord.utils.get(interaction.guild.roles, id=data['middleman-role-id'])
                
        category = discord.utils.get(interaction.guild.categories, id=data['mm-request-category-id'])

        await interaction.channel.edit(category=category)
            
        embed = discord.Embed(description=f"A Middleman got requested by {interaction.user.mention}.", color=0x6056ff)
        msg = await interaction.channel.send(middleman.mention, embed=embed, view=ClaimMM())
        
      
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)  

        data[str(msg.id)] = interaction.user.id        

        data[f"{str(interaction.channel.id)}"]["MM-Request-User"] = {}
        data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["Name"] = interaction.user.name
        data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"] = interaction.user.id
                
        with open('./database/TicketData.json', 'w') as f:
            json.dump(data, f, indent=1)


        with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)  
                        
        role = discord.utils.get(interaction.guild.roles, id=data['on-break-role-id'])
                
        if role in interaction.user.roles:
                  channel = discord.utils.get(interaction.guild.channels, id=data["admin-notify-channel-id"])
                
                  await channel.send(f'@everyone\n\n{interaction.user.mention}, {interaction.user.name} ({interaction.user.id}) requested MM while being **ON BREAK**.')
            
        await interaction.followup.send(f'Wait for a {middleman.mention} to claim this ticket.')
        
        
        
        

class AfterClose(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.channel)


    @discord.ui.button(label='Close', style=discord.ButtonStyle.red, custom_id='close-2', disabled=True)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):

     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:


          
        with open('./private/botdata.json', 'r') as f:

            data = json.load(f)      

        c = 0


        for i in data['ids-to-have-full-access-in-tickets']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    if r in interaction.user.roles:
                        c += 1


        try:

             
          if interaction.user.guild_permissions.administrator or c > 0:
            pass 
          
          else:

            try:

                  with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)

                  d = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']                  
                  status = data[f"{interaction.channel.id}"]["Status"]
                    
                  if status == 'Completed' or status == 'Cancelled':
                    pass
                
                  else:
                    
                    if interaction.user.id != d:
                      await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
                      return

            except:
                       
              await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
              return
                    

        except:
                    
            await interaction.response.send_message("You don't have enough permissions to use this.", ephemeral=True)
            return


        embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        embed = discord.Embed(description='`❓` — **Are you sure you want to close this ticket**?\n-# Select an option down below.', color=0x6056ff)
        msg = await interaction.channel.send(interaction.user.mention, embed=embed)
        await msg.edit(view=CloseTicket(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))
                

    @discord.ui.button(label='Delete', style=discord.ButtonStyle.gray, custom_id='delete-2')
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):

     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:



                embed=discord.Embed(description='⬩ You have 15 seconds to interact.', color=0x6056ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                embed = discord.Embed(description='`❓` — **Are you sure you want to delete this ticket**?\n-# Select an option down below.', color=0x6056ff)
                msg = await interaction.channel.send(interaction.user.mention, embed=embed)
                await msg.edit(view=DeleteTicket(interaction_msg = msg, interaction_user = interaction.user, message_for_edit = interaction.message))



              
            
            
            
class DeleteTicket(View):
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
 
                
              if interaction.user.id is not self.interaction_user.id:
                  return

              now = datetime.datetime.now()
              limit = datetime.timedelta(seconds=6)

              o = now+limit

              d = datetime.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second)
              time_stamp = calendar.timegm(d.timetuple())
            
              to = time_stamp
            
              select.disabled = True
              embed = discord.Embed(description=f"# `🗑️` Deleting Ticket\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)", color=0x6056ff)
              embed.set_author(name=f'[{interaction.user.name}]: Deleting ticket', icon_url=interaction.user.avatar)
              m = await interaction.response.edit_message(content='', embed=embed, view=self)

                
              embed2 = discord.Embed(description=f'`🗑️` {interaction.channel.mention} will be deleted <t:{to}:R>.\n — **Responsible Moderator**: {interaction.user.mention} (*{discord.utils.escape_markdown(interaction.user.name)}*)', color=0x6056ff)
              await interaction.channel.send(embed=embed2)
              await asyncio.sleep(5)
            

              try:
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                user = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']
            
                del data[str(user)]

                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                        
              except:
                pass

              
              chid = interaction.channel.id


              try:


                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  user = data[f"{chid}"]['Exchange-Request-User']['ID']
                  userid = data[f"{chid}"]['Exchange-Request-User']['ID']
                  username = data[f"{chid}"]['Exchange-Request-User']['Name']
                  price_send = data[f"{chid}"]['Price-Send']

                  price_receive = data[f"{chid}"]['Price-Receive']

                  
                
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(interaction.guild.channels, id=data["exchange-logs-channel-id"])

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{interaction.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)

                  with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)

                  urn = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["Name"]
                  urid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]
                    
                  try:
                    u1n = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["Name"]
                    u1id = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"] 
                  except:
                    u1n = None
                    
                  try:  
                    with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)

                    u2n = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["Name"]
                    u2id = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"]
                    
                  except:
                    
                    u2n = None
                    
                    
                  if u2n:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {interaction.user.mention}\n> Name: `{interaction.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    embed.add_field(name=f'MM request user:', value=f'{u2n} ({u2id})', inline=False)
                    embed.add_field(name=f'Exchanger (MM):', value=f'{u1n} ({u1id})', inline=False)
                    
                  elif u1n:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {interaction.user.mention}\n> Name: `{interaction.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    embed.add_field(name=f'Exchanger:', value=f'{u1n} ({u1id})', inline=False)
                    
                  else:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {interaction.user.mention}\n> Name: `{interaction.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    

                  await channel.send(f"Exchange Request: {urn} ({urid}) - <@{urid}>{f' | Exchanger: {u1n} ({u1id}) - <@{u1id}>' if u1n != None else ''}{f' | MM Request: {u2n} ({u2id}) - <@{u2id}>' if u2n != None else ''}", embed=embed, file=discord.File(f'Tickets/{interaction.channel.name}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))

                      

              except:
                    pass   

                
              try:
                 try:
                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  transcript = data[f"{chid}"]['Exchange-Request-User']['Trascript']
                
                 except:
                  transcript = None
                
                 if transcript == 'Received':
                        pass
                    
                 else:
                
                  user = data[f"{chid}"]['Exchange-Request-User']['ID']
                  username = data[f"{chid}"]['Exchange-Request-User']['Name']
                  price_send = data[f"{chid}"]['Price-Send']

                  price_receive = data[f"{chid}"]['Price-Receive']

                  
                
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{chid}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {interaction.user.mention}', color=0x6056ff)

                
                  usersend = await interaction.guild.fetch_member(int(user))
                  await usersend.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    
              except:
                    pass   

              try:

                 try:
                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  transcript = data[f"{chid}"]['Exchange-Complete-User']['Trascript']
                
                 except:
                  transcript = None
                
                 if transcript == 'Received':
                        pass
                    
                 else:
                    
                    with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)

                    
                    exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                    username = data[f"{chid}"]['Exchange-Request-User']['Name']
                    price_send = data[f"{chid}"]['Price-Send']
                    userid = data[f"{chid}"]['Exchange-Request-User']['ID']
                
                    price_receive = data[f"{chid}"]['Price-Receive']
              
                    option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                    receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']


                    embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {interaction.user.mention}', color=0x6056ff)
                    exchanger = await interaction.guild.fetch_member(int(exchangerid))
                    await exchanger.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    


                    try:

                       try:
                        with open('./database/TicketData.json', 'r') as f:
                             data = json.load(f)
                              
                        transcript = data[f"{chid}"]['MM-Request-User']['Trascript']
                
                       except:
                        transcript = None
                
                       if transcript == 'Received':
                              pass
                    
                       else:
                        
                            with open('./database/TicketData.json', 'r') as f:
                               data = json.load(f)
                        
                            k = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"]


                            k2 = await interaction.guild.fetch_member(int(k))
                            await k2.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    
                    except:
                       pass
                    
              except:
                    pass
                
              try:
                os.remove(f"Tickets/{interaction.channel.name}.htm")   
              except:
                pass
 
              try:
        
                with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                user = data[f"{chid}"]['Exchange-Request-User']['ID']
        
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                del data[str(interaction.channel.id)]

                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                 
                try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                  del data[str(user)]

                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                    
                except:
                    pass
                
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


               
class CloseTicket(View):
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
                
                await interaction.response.defer(thinking=True) 

                select.disabled = True
                await interaction.message.edit(view=self)

                if self.msg:
                  await self.msg.edit(view=AfterClose())


                now = datetime.datetime.now()




                try:

                  with open('./database/TicketData.json', 'r') as f:

                     data = json.load(f)

                  user2 = data[f"{str(interaction.channel.id)}"]['Users']
                
                   
                  for i in user2:

                     try:
                       
                       user = await interaction.guild.fetch_member(i)
                       await interaction.channel.set_permissions(user, send_messages=False, read_messages=False)

                     except:
                       pass

                except:
                  pass

                now = datetime.datetime.now()

                d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp = calendar.timegm(d.timetuple())
            
            
                chid = interaction.channel.id

                try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  exchanger = data[f"{chid}"]["Exchange-Complete-User"]["Name"]
                  exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                  status = data[f"{chid}"]["Status"]


                  price_send = data[f"{chid}"]['Price-Send']
                  price_receive = data[f"{chid}"]['Price-Receive']
   
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
                  more_options = data[f"{chid}"]['Exchange']['More-Options']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']
                  more_receive_options = data[f"{chid}"]['Receive-Exchange']['More-Options']

                  username = data[f"{chid}"]['Exchange-Request-User']['Name']


                  with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

                  if status == 'Claimed':
                    data[str(exchangerid)]['Current'] -= price_send
                    
                    data[str(exchangerid)]['Current-Limit'] -= price_send
                    
                  ex = None

                  for i in data[str(exchangerid)][f"Active"]:
                      if f"{interaction.channel.mention}" in i:
                          ex = i
                          break 


                  if ex:

                      index = data[str(exchangerid)][f"Active"].index(ex)
                      del data[str(exchangerid)][f"Active"][index]

                  with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)




                  if status == 'Completed':

                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                    emoj = '✔️'
                    data[f"{chid}"]["Status"] = 'Completed'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                    
                    
                    
                  elif status == 'Cancelled':  

                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                    emoj = '❌'
                    data[f"{chid}"]["Status"] = 'Cancelled'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                    
                  else:

                   with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                   data[f"{chid}"]["Status"] = 'Cancelled' 
                    
                   with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)


                   with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                   data[str(exchangerid)]


        
                   try:

                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] += 1

                   except:
                  
                       data[str(exchangerid)]['Weekly-Exchanged'] = {}    
                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] = 1
                       data[str(exchangerid)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
                
                
                   try:
                        
                        data[str(exchangerid)]['History']
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                   except:
                                              
                        data[str(exchangerid)]['History'] = []
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

                   with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

  
                except:

                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  data[f"{chid}"]["Status"] = 'Closed' 
                    
                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                  exchanger = None

                
                
                
                try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  exchangerid = data[f"{chid}"]["MM-Request-User"]["ID"]



                  with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)
                    
                  ex = None

                  for i in data[str(exchangerid)][f"Active"]:
                      if f"{interaction.channel.mention}" in i:
                          ex = i
                          break 


                  if ex:

                      index = data[str(exchangerid)][f"Active"].index(ex)
                      del data[str(exchangerid)][f"Active"][index]

                  with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)



                  if status == 'Completed':
                    pass

                    
                  elif status == 'Cancelled':  
                    pass
                    
                  else:


                   with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                   data[str(exchangerid)]


        
                   try:

                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] += 1

                   except:
                  
                       data[str(exchangerid)]['Weekly-Exchanged'] = {}    
                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] = 1
                       data[str(exchangerid)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
                
                
                   try:
                        
                        data[str(exchangerid)]['History']
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                   except:
                                              
                        data[str(exchangerid)]['History'] = []
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

                   with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

  
                except:

                  pass
                
                
                

                try:

                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)

                  user = data[f"{chid}"]['Exchange-Request-User']['ID']
                  username = data[f"{chid}"]['Exchange-Request-User']['Name']
                  price_send = data[f"{chid}"]['Price-Send']
                
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                  price_receive = data[f"{chid}"]['Price-Receive']
                  userid = data[f"{chid}"]['Exchange-Request-User']['ID']

                  export = await chat_exporter.export(channel=interaction.channel)
                  file_name=f"Tickets/{chid}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {interaction.user.mention}', color=0x6056ff)

                
                  usersend = await interaction.guild.fetch_member(int(user))
                  await usersend.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                  data[f"{chid}"]['Exchange-Request-User']['Trascript'] = 'Received'

                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                    
                except:
                    pass   

                try:


                    with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)

                    username = data[f"{chid}"]['Exchange-Request-User']['Name']
                    price_send = data[f"{chid}"]['Price-Send']
                
                    option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                    receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                    price_receive = data[f"{chid}"]['Price-Receive']
                    userid = data[f"{chid}"]['Exchange-Request-User']['ID']

                    embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {interaction.user.mention}', color=0x6056ff)
                    exchanger = await interaction.guild.fetch_member(int(exchangerid))
                    await exchanger.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    
                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                    data[f"{chid}"]['Exchange-Complete-User']['Trascript'] = 'Received'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                    try:

                      with open('./database/TicketData.json', 'r') as f:
                         data = json.load(f)
                        
                      k = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"]
                    
                    
                      with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)
            
                      data[f"{chid}"]['MM-Request-User']['Trascript'] = 'Received'

                      with open('./database/TicketData.json', 'w') as f:
                         json.dump(data, f, indent=1)
                    
                      k2 = await interaction.guild.fetch_member(int(k))
                      await k2.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))


                    except:
                        pass
                    
                except:
                    pass
                
                try:
                  os.remove(f"Tickets/{chid}.htm")  
                
                except:
                    pass
                
                try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  del data[str(user)]

                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                
                except:
                   pass
                
                embed = discord.Embed(title=f'Ticket Closed', description=f"- The ticket has been closed by {interaction.user.mention}\n`❓` — To delete ticket, use the `delete` button [here]({self.msg.jump_url}).", color=0x6056ff)
                await interaction.followup.send(embed=embed)



                
                
                
            if select.values[0] == '06':
                
                if interaction.user.id is not self.interaction_user.id:
                  return

                select.disabled = True
                embed = discord.Embed(description=f'`❌` — Action cancelled', color=0x6056ff)
                await interaction.response.edit_message(embed=embed, view=self)     

    async def on_timeout(self):
     try:
      await self.interaction_msg.delete()
      return
     except:
      return




class SentPayment_0(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=5)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment', style=discord.ButtonStyle.green, custom_id='sent-payment-0', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_1(msg = self.msg))



class SentPayment_1(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (10)', style=discord.ButtonStyle.green, custom_id='sent-payment1', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_2(msg = self.msg))


class SentPayment_2(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (9)', style=discord.ButtonStyle.green, custom_id='sent-payment2', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_3(msg = self.msg))


class SentPayment_3(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (8)', style=discord.ButtonStyle.green, custom_id='sent-payment3', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_4(msg = self.msg))


class SentPayment_4(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (7)', style=discord.ButtonStyle.green, custom_id='sent-payment4', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_5(msg = self.msg))


class SentPayment_5(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (6)', style=discord.ButtonStyle.green, custom_id='sent-payment5', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_6(msg = self.msg))


class SentPayment_6(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (5)', style=discord.ButtonStyle.green, custom_id='sent-payment6', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_7(msg = self.msg))


class SentPayment_7(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (4)', style=discord.ButtonStyle.green, custom_id='sent-payment7', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_8(msg = self.msg))


class SentPayment_8(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (3)', style=discord.ButtonStyle.green, custom_id='sent-payment8', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_9(msg = self.msg))


class SentPayment_9(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (2)', style=discord.ButtonStyle.green, custom_id='sent-payment9', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment_10(msg = self.msg))


class SentPayment_10(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=1)
        self.msg = msg
        self.seconds = 15


    @discord.ui.button(label=f'Sent Payment (1)', style=discord.ButtonStyle.green, custom_id='sent-payment0', disabled=True)
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    async def on_timeout(self):
        await self.msg.edit(view=SentPayment(msg = self.msg))





class SentPayment(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.channel)
        
    @discord.ui.button(label=f'Confirm Payment', style=discord.ButtonStyle.green, custom_id='sent-payment-last')
    async def sent(self, interaction: discord.Interaction, button: discord.ui.Button):
            
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:


      await interaction.response.defer(thinking=True, ephemeral=True)  

      with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

      s = data[f"{str(interaction.channel.id)}"]["Status"]


      if s != 'Claimed':
          await interaction.followup.send(f"You cannot do that. The ticket is already {s.lower()}.")
          return



      with open('./database/TicketData.json', 'r') as f:
          data = json.load(f)

      client = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]

      with open('./private/botdata.json', 'r') as f:
         data = json.load(f)
 
      c = 0

      for i in data['ids-to-have-full-perms-in-tickets']:
          r = discord.utils.get(interaction.guild.roles, id=i)
            
          if r in interaction.user.roles:
            c += 1
            break
        
      if interaction.user.id != client and not interaction.user.guild_permissions.administrator:
          await interaction.followup.send("Your not the Exchanger of this ticket! You cannot use that.")
          return
      
      else:

        button.disabled = True
        await interaction.message.edit(view=self)
          
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        data[f"{str(interaction.channel.id)}"]["Status"] = 'Completed'

        with open('./database/TicketData.json', 'w') as f:
            json.dump(data, f, indent=1)

              
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        exchanger = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"] 
        userid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]  
        msgid = data[f"{str(interaction.channel.id)}"]["Message"] 

        price_send = data[str(interaction.channel.id)]['Price-Send']
        price_receive = data[str(interaction.channel.id)]['Price-Receive']

        option_exchange = data[str(interaction.channel.id)]['Exchange']['Type']
        more_options = data[str(interaction.channel.id)]['Exchange']['More-Options']

        receive_exchange = data[str(interaction.channel.id)]['Receive-Exchange']['Type']
        more_receive_options = data[str(interaction.channel.id)]['Receive-Exchange']['More-Options']

        username = data[str(interaction.channel.id)]['Exchange-Request-User']['Name']


        msg = await interaction.channel.fetch_message(msgid)


        now = datetime.datetime.now()

        d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time_stamp = calendar.timegm(d.timetuple())

                    
        with open('./database/UserData.json', 'r') as f:
            data = json.load(f)

        data[str(exchanger)]['Current'] -= price_send
                    
        ex = None

        for i in data[str(exchanger)][f"Active"]:
            if f"{interaction.channel.mention}" in i:
                ex = i
                break 


        if ex:
            index = data[str(exchanger)][f"Active"].index(ex)
            del data[str(exchanger)][f"Active"][index]
        
        try:

            data[str(exchanger)]['Total-Exchanged'] += price_send

        except:
                        
            data[str(exchanger)]['Total-Exchanged'] = price_send

        
        try:

            data[str(exchanger)]['Weekly-Exchanged']['Orders'] += 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] += price_send

        except:
                  
            data[str(exchanger)]['Weekly-Exchanged'] = {}    
            data[str(exchanger)]['Weekly-Exchanged']['Orders'] = 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] = price_send
            
            
        try:
                        
            data[str(exchanger)]['History']
            data[str(exchanger)]['History'].append(f"`✔️` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
        except:
                                              
            data[str(exchanger)]['History'] = []
            data[str(exchanger)]['History'].append(f"`✔️` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

        with open('./database/UserData.json', 'w') as f:
            json.dump(data, f, indent=1)

        try:

          with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)
            
          exchanger = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"]  
            
            
          with open('./database/UserData.json', 'r') as f:
            data = json.load(f)
                    
          ex = None

          for i in data[str(exchanger)][f"Active"]:
            if f"{interaction.channel.mention}" in i:
                ex = i
                break 


          if ex:
            index = data[str(exchanger)][f"Active"].index(ex)
            del data[str(exchanger)][f"Active"][index]
        
          try:

            data[str(exchanger)]['Total-Exchanged'] += price_send

          except:
                        
            data[str(exchanger)]['Total-Exchanged'] = price_send

        
          try:

            data[str(exchanger)]['Weekly-Exchanged']['Orders'] += 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] += price_send

          except:
                  
            data[str(exchanger)]['Weekly-Exchanged'] = {}    
            data[str(exchanger)]['Weekly-Exchanged']['Orders'] = 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] = price_send
            
            
          try:
                        
            data[str(exchanger)]['History']
            data[str(exchanger)]['History'].append(f"`✔️` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
          except:
                                              
            data[str(exchanger)]['History'] = []
            data[str(exchanger)]['History'].append(f"`✔️` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

          with open('./database/UserData.json', 'w') as f:
            json.dump(data, f, indent=1)
            
    
        except:
          pass        





        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)
            
        user = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']
        n = data[str(interaction.channel.id)]['Position']
        
        exchangername = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["Name"] 
            
        with open('./private/botdata.json', 'r') as f:
               data = json.load(f)
                
        vouch_channel_id = data["vouch-channel-id"]
        category = discord.utils.get(interaction.guild.categories, id=data['completed-exchanges-category-id'])

        await interaction.channel.edit(name=f'✔️{option_exchange[0].lower()}2{receive_exchange[0].lower()}・{exchangername}', category=category)
        
        
        e = await interaction.guild.fetch_member(int(exchanger))

        try:
            more_options = more_options.replace(f' (**Other Crypto**)', '')
            
        except:
            pass
        

        try:
            more_receive_options = more_receive_options.replace(f' (**Other Crypto**)', '')
            
        except:
            pass
        
        embed = discord.Embed(title=f'Ticket Payment Confirmed', description=f"- Exch has been completed by {interaction.user.mention}\n`❓` — To close ticket, use the `close` button [here]({msg.jump_url}).\n- Vouch channel: <#{vouch_channel_id}>", color=0x6056ff)
        await interaction.message.edit(content=f"+vouch {e.name} Exchange | {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} to {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'} | {price_send}€", embed=embed)

    
        
        
        embed = discord.Embed(title=f'Ticket Payment Confirmed', description=f"- You confirmed your Exch: {interaction.channel.mention}, `{interaction.channel.name}`", color=0x6056ff)
        
        try: 

          usersend = await interaction.guild.fetch_member(int(user))
        
          with open('./private/botdata.json', 'r') as f:
               data = json.load(f)

          client = discord.utils.get(interaction.guild.roles, id=data["client-role-id"])
          await usersend.add_roles(client)
            
          await usersend.send(embed=embed)
        except:
            pass
        
        
        await interaction.followup.send("The Exch has been successfully completed.")


class CancelPayment(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.channel)


    @discord.ui.button(label=f'Cancel Payment', style=discord.ButtonStyle.red, custom_id='cancel-payment0')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
            
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:

      await interaction.response.defer(thinking=True, ephemeral=True)  
        
      with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

      s = data[f"{str(interaction.channel.id)}"]["Status"]


      if s != 'Claimed':
          await interaction.followup.send(f"You cannot do that. The ticket is already {s.lower()}.")
          return


      with open('./database/TicketData.json', 'r') as f:
          data = json.load(f)

      exchangerid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]

      with open('./private/botdata.json', 'r') as f:
         data = json.load(f)
 
      c = 0

      for i in data['ids-to-have-full-perms-in-tickets']:
          r = discord.utils.get(interaction.guild.roles, id=i)
            
          if r in interaction.user.roles:
            c += 1
            break
        
      if interaction.user.id != exchangerid and not interaction.user.guild_permissions.administrator:
          await interaction.followup.send("Your not the Exchanger of this ticket! You cannot use that.")
          return
      
      else:
          
        button.disabled = True
        await interaction.message.edit(view=self)
              


        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        data[f"{str(interaction.channel.id)}"]["Status"] = 'Cancelled'

        with open('./database/TicketData.json', 'w') as f:
            json.dump(data, f, indent=1)

            
        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        userid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]  
        exchanger = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"]
        msgid = data[f"{str(interaction.channel.id)}"]["Message"] 

        price_send = data[str(interaction.channel.id)]['Price-Send']
        price_receive = data[str(interaction.channel.id)]['Price-Receive']

        option_exchange = data[str(interaction.channel.id)]['Exchange']['Type']
        more_options = data[str(interaction.channel.id)]['Exchange']['More-Options']

        receive_exchange = data[str(interaction.channel.id)]['Receive-Exchange']['Type']
        more_receive_options = data[str(interaction.channel.id)]['Receive-Exchange']['More-Options']

        username = data[str(interaction.channel.id)]['Exchange-Request-User']['Name']

        msg = await interaction.channel.fetch_message(msgid)


        
        now = datetime.datetime.now()

        d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time_stamp = calendar.timegm(d.timetuple())


        with open('./database/UserData.json', 'r') as f:
            data = json.load(f)

            
        
        try:

            data[str(exchanger)]['Weekly-Exchanged']['Orders'] += 1

        except:
                  
            data[str(exchanger)]['Weekly-Exchanged'] = {}    
            data[str(exchanger)]['Weekly-Exchanged']['Orders'] = 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
            
        data[str(exchanger)]['Current'] -= price_send
                    
        data[str(exchanger)]['Current-Limit'] -= price_send
        
        ex = None

        for i in data[str(exchanger)][f"Active"]:
            if f"{interaction.channel.mention}" in i:
                ex = i
                break 


        if ex:
            index = data[str(exchanger)][f"Active"].index(ex)
            del data[str(exchanger)][f"Active"][index]

        try:
                        
            data[str(exchanger)]['History']
            data[str(exchanger)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
        except:
                                              
            data[str(exchanger)]['History'] = []
            data[str(exchanger)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€, {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

        with open('./database/UserData.json', 'w') as f:
            json.dump(data, f, indent=1)

                       

        try:

          with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)
            
          exchanger = data[f"{str(interaction.channel.id)}"]["MM-Request-User"]["ID"]  
            
            
          with open('./database/UserData.json', 'r') as f:
            data = json.load(f)
                    
          ex = None

          for i in data[str(exchanger)][f"Active"]:
            if f"{interaction.channel.mention}" in i:
                ex = i
                break 


          if ex:
            index = data[str(exchanger)][f"Active"].index(ex)
            del data[str(exchanger)][f"Active"][index]
        
          try:

            data[str(exchanger)]['Weekly-Exchanged']['Orders'] += 1

          except:
                  
            data[str(exchanger)]['Weekly-Exchanged'] = {}    
            data[str(exchanger)]['Weekly-Exchanged']['Orders'] = 1
            data[str(exchanger)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
            
            
            
          try:
                         
            data[str(exchanger)]['History']
            data[str(exchanger)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
          except:
                                              
            data[str(exchanger)]['History'] = []
            data[str(exchanger)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€, {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

          with open('./database/UserData.json', 'w') as f:
            json.dump(data, f, indent=1)
            
    
        except:
          pass           
                
                
                

        with open('./database/TicketData.json', 'r') as f:
            data = json.load(f)

        exchanger = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"]
        user = data[str(interaction.channel.id)]['Exchange-Request-User']['ID']
        n = data[str(interaction.channel.id)]['Position']






        exchangername = data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["Name"]
        
        
        with open('./private/botdata.json', 'r') as f:
               data = json.load(f)
    
        category = discord.utils.get(interaction.guild.categories, id=data['cancelled-exchanges-category-id'])


        await interaction.channel.edit(name=f'❌{option_exchange[0].lower()}2{receive_exchange[0].lower()}・{exchangername}', category=category)



        
        embed = discord.Embed(title=f'Ticket Payment Cancelled', description=f"- Exch has been cancelled by {interaction.user.mention}\n`❓` — To close ticket, use the `close` button [here]({msg.jump_url}).", color=0x6056ff)
        await interaction.message.edit(embed=embed)

        with open('./database/TicketData.json', 'r') as f:
          data = json.load(f)
                      
        user = data[str(interaction.channel.id)][f'Exchange-Request-User']['ID']
        usersend = await interaction.guild.fetch_member(int(user))


        embed = discord.Embed(title=f'Ticket Payment Cancelled', description=f"- You cancelled your Exch: {interaction.channel.mention}, `{interaction.channel.name}`", color=0x6056ff)
        
        try: 
          await usersend.send(embed=embed)
        except:
            pass

        await interaction.followup.send("The Exch has been successfully cancelled.")




class ClaimMM(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.channel)

    @discord.ui.button(label='Claim as MM', style=discord.ButtonStyle.green, custom_id='claim-mm')
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
            
     interaction.message.author = interaction.user
     bucket = self.cooldown.get_bucket(interaction.message)
     retry = bucket.update_rate_limit()

     if retry:
        embed = discord.Embed(description=f"**Your in cooldown**! Please wait `{round(retry, 1)}` more seconds.", color=0x6056ff)
        await interaction.response.send_message(embed=embed, ephemeral=True)   

     else:
        
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                status = data[f"{str(interaction.channel.id)}"]["Status"]
                
                if status != 'Pending':
                     await interaction.response.send_message(f"You cannot do that. The ticket is already {status.lower()}.", ephemeral=True)
                     return
        
        
                with open('./private/botdata.json', 'r') as f:
                    data = json.load(f)
        
                role = discord.utils.get(interaction.guild.roles, id=data['middleman-role-id'])
                if role not in interaction.user.roles:
                    
                    await interaction.response.send_message(f"You cannot do that your not an MM.", ephemeral=True)
                    return

                with open('./database/TicketData.json', 'r') as f:
                     data = json.load(f)  
         
                user = data[str(interaction.message.id)]
            
                if interaction.user.id == user:
                    
                    await interaction.response.send_message(f"You're the one who requested MM. You cannot claim it.", ephemeral=True)
                    return
                

                await interaction.response.defer(thinking=True, ephemeral=True) 


                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                uid = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["ID"]

                try:
                    
                    user = await interaction.guild.fetch_member(uid)

                except:
                  
                  name = data[f"{str(interaction.channel.id)}"]["Exchange-Request-User"]["Name"]

                  embed = discord.Embed(description=f'`❌` — {name}, {uid} left, Exchange cannot be continued. Talk with an administrator.', color=0x6056ff)
                  await interaction.followup.send(f"{interaction.user.mention}", embed=embed)  
                  return

                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                price = data[str(interaction.channel.id)]['Price-Send']
                


                try:


                     try:

                       with open('./database/UserData.json', 'r') as f:
                         data = json.load(f)

                       m = data[str(interaction.user.id)]['max']

                       try:
                          
                          current = data[str(interaction.user.id)]['Current']

                          if current + price > m:
                               
                              await interaction.followup.send(f"Out of your max! `{current + price} > {m}`.", ephemeral=True)
                              return
                           
                          else:
                              pass


                             
                       except:

                          if price > m:
                               
                              await interaction.followup.send(f"Out of your max! `{price} > {m}`.", ephemeral=True)
                              return




                     except:
                       await interaction.followup.send("You don't have max! Please talk with an administrator.", ephemeral=True)
                       return
                    

                except:
                    
                    await interaction.followup.send("Your not an Exchanger. You cannot claim this exchange!", ephemeral=True)
                    return
                    

                try:


                     try:

                       with open('./database/UserData.json', 'r') as f:
                         data = json.load(f)

                       m = data[str(interaction.user.id)]['limit']

                       try:
                          
                          current = data[str(interaction.user.id)]['Current-Limit']

                          if current + price > m:
                               
                              await interaction.followup.send(f"Out of your limit! `{current + price} > {m}`.", ephemeral=True)
                              return
                           
                          else:
                              pass

                             
                       except:

                          if price > m:
                               
                              await interaction.followup.send(f"Out of your limit! `{price} > {m}`.", ephemeral=True)
                              return



                     except:
                       await interaction.followup.send("You don't have limit! Please talk with an administrator.", ephemeral=True)
                       return
                    

                except:
                    
                    await interaction.followup.send("You don't have limit! Please talk with an administrator.", ephemeral=True)
                    return

                
                
                
                
                try:    
                       
                          with open('./database/UserData.json', 'r') as f:
                             data = json.load(f)
                    
                          data[str(interaction.user.id)]['Current-Limit'] += round(price, 2)
                       
                          with open('./database/UserData.json', 'w') as f:
                             json.dump(data, f, indent=1)
 
                        
                except:  
                            with open('./database/UserData.json', 'r') as f:
                               data = json.load(f)
                            
                            data[str(interaction.user.id)]['Current-Limit'] = round(price, 2)

                            with open('./database/UserData.json', 'w') as f:
                               json.dump(data, f, indent=1)
                
                    
                    
                try:      
                       
                          with open('./database/UserData.json', 'r') as f:
                             data = json.load(f)
                    
                          data[str(interaction.user.id)]['Current'] += round(price, 2)
                       
                          with open('./database/UserData.json', 'w') as f:
                             json.dump(data, f, indent=1)

                        
                except:  
                    
                            with open('./database/UserData.json', 'r') as f:
                               data = json.load(f)
                            
                            data[str(interaction.user.id)]['Current'] = round(price, 2)

                            with open('./database/UserData.json', 'w') as f:
                               json.dump(data, f, indent=1)
                
                
                
                
                
                now = datetime.datetime.now()

                d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                time_stamp = calendar.timegm(d.timetuple())
                    
                    
                with open('./private/botdata.json', 'r') as f:

                     data = json.load(f)

                c = 0


                for i in data['exchangers']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    if r in interaction.user.roles:
                        c += 1

                if interaction.user.guild_permissions.administrator or c > 0:
                    pass

                else:
                    await interaction.followup.send("Your not an Exchanger. You cannot claim this exchange!", ephemeral=True)
                    return

                button.disabled = True
                await interaction.message.edit(view=self)



                for i in data['ids-to-have-access-before-claim-in-tickets']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    
                    await interaction.channel.set_permissions(r, send_messages=False, read_messages=False)
          
                for i in data['exchangers']:
                    r = discord.utils.get(interaction.guild.roles, id=i)

                    
                    await interaction.channel.set_permissions(r, send_messages=False, read_messages=False)
   
        
        
        
                await interaction.channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=True)

   
                with open('./database/TicketData.json', 'r') as f:
                     data = json.load(f)  

                mmask = data[str(interaction.message.id)]  
                ask = await interaction.guild.fetch_member(int(mmask))

                await interaction.channel.set_permissions(ask, send_messages=True, read_messages=True, add_reactions=True)




                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"] = {}
                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["Name"] = interaction.user.name
                data[f"{str(interaction.channel.id)}"]["Exchange-Complete-User"]["ID"] = interaction.user.id

                data[f"{str(interaction.channel.id)}"]["Status"] = 'Claimed'
                
                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)




        


                n = data[str(interaction.channel.id)]['Position']


                option_exchange = data[str(interaction.channel.id)]['Exchange']['Type']
                more_options = data[str(interaction.channel.id)]['Exchange']['More-Options']

                receive_exchange = data[str(interaction.channel.id)]['Receive-Exchange']['Type']
                more_receive_options = data[str(interaction.channel.id)]['Receive-Exchange']['More-Options']

                with open('./private/botdata.json', 'r') as f:
                    data = json.load(f)
                
                category = discord.utils.get(interaction.guild.categories, id=data["claimed-exchanges-category-id"])
                
                await interaction.channel.edit(name=f'{option_exchange[0].lower()}2{receive_exchange[0].lower()}・{interaction.user.name}', category=category)
                
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
                    
                id = data[str(interaction.channel.id)]['Message']

                msg = await interaction.channel.fetch_message(id)

                embed = msg.embeds[0]
                embed.add_field(name=f"Exchanger", value=f"{interaction.user.mention}", inline=True)
                await msg.edit(embed=embed)

                now = datetime.datetime.now()

                price_send = data[str(interaction.channel.id)]['Price-Send']
                price_receive = data[str(interaction.channel.id)]['Price-Receive']

                    
                with open('./database/UserData.json', 'r') as f:
                    data = json.load(f)

                try:
                        
                    data[str(interaction.user.id)]['Active']
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                except:
                                              
                    data[str(interaction.user.id)]['Active'] = []
                    data[str(interaction.user.id)]['Active'].append(f"`⌛` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {interaction.channel.mention}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")

                with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)


                       


                payment = ''
                p2 = ''

                try:

                    with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                    data[str(interaction.user.id)]

                    if more_options:

                      if receive_exchange == 'Crypto':

                        if more_options == 'Litecoin':
                           payment = data[str(interaction.user.id)]['ltc'] 
                           p2 = payment
                            
                           payment = f"{more_receive_options}: **`{payment}`**"
                          
                        if more_options == 'Bitcoin':
                           payment = data[str(interaction.user.id)]['btc']
                           p2 = payment
                            
                           payment = f"{more_receive_options}: **`{payment}`**"
                          
                        if more_options == 'Ethereum':
                           payment = data[str(interaction.user.id)]['eth'] 
                           p2 = payment
                            
                           payment = f"{more_receive_options}: **`{payment}`**"


                        if payment == '':
                          
                          payment = 'No payment details were found.'

                      else:
                          
                           payment = data[str(interaction.user.id)][f'{receive_exchange}'] 
                        
                           p2 = payment
                            
                           payment = f"{receive_exchange}: **`{payment}`**"


                            
                      
                          
                      

                    else:

                    

                      payment = data[str(interaction.user.id)][f'{receive_exchange}']
                        
                      p2 = payment
                    
                      payment = f"{receive_exchange}: **`{payment}`**"
                    






                except:
             
                    p2 = ''
                    payment = 'No payment details were found.'


                with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)  
                        
                role = discord.utils.get(interaction.guild.roles, id=data['on-break-role-id'])
                
                if role in interaction.user.roles:
                  channel = discord.utils.get(interaction.guild.channels, id=data["admin-notify-channel-id"])
                
                  await channel.send(f'@everyone\n\n{interaction.user.mention}, {interaction.user.name} ({interaction.user.id}) claimed an MM request while being **ON BREAK**.')
                    
                    
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)


                user = data[str(interaction.channel.id)][f'Exchange-Request-User']['ID']
                usersend = await interaction.guild.fetch_member(int(user))

                embed2 = None
                
                if option_exchange == 'PayPal':
                  embed2 = discord.Embed(title="Terms of Service", description="Failing to follow any TOS below will result in no refund or exchange.\n- Send as Friends and Family only!\n- Don't add any notes\n- Send from PayPal Balance\n- Only send in Euro Currency\n- If the PayPal account is getting locked, you won't get any refund.\n- If the account is grabbed, you will not get any refund.", color=0x6056ff)

 
                
                embed = discord.Embed(title=f'Ticket Claimed', description=f"- Ticket has been claimed by {interaction.user.mention} (**MM**)\n- If the amount shouldn’t be correct, let the Exchanger know.\n- Sending too much money which is not the stated deal amount will result in no refund in case of a scam.\n-# **MM request by {ask.mention}**", color=0x6056ff)
                
                if embed2:
                  msg = await interaction.channel.send(f"{usersend.mention}, {interaction.user.mention}", embeds=[embed, embed2])
                else:
                  msg = await interaction.channel.send(f"{usersend.mention}, {interaction.user.mention}", embed=embed)

                embed3 = discord.Embed(title=f'Ticket Claimed', description=f"- Ticket has been claimed by {interaction.user.mention}, check it out {interaction.channel.mention}", color=0x6056ff)
                
                try: 
                  await usersend.send(embed=embed3)
                except:
                   pass

            
        
                try:
                  with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)

                  msg_id = data[str(interaction.channel.id)]['Message']
        
                  msg = await interaction.channel.fetch_message(msg_id)

                  await msg.edit(view=AfterMM())
                
        
                except:
                    pass

                embed=discord.Embed(title=f"{interaction.user.name} payment details", description=f"{payment}", color=0x6056ff)
                await interaction.channel.send(f"{p2}", embed=embed)
            


                await interaction.followup.send("You successfully claimed this exchange.", ephemeral=True)



class TicketCreation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        commands = self.get_commands()
        print(f"COG: TicketCreation.py ENABLED [{len(commands)}] commands LOADED")

       
        
    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.channel)
    async def delete(self, ctx):
                
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
                
                  c = 'application'
                   
                except:
                  c = '' 

                
                
                
         if c == '':
            await ctx.reply('This is not a ticket.', delete_after=5)
         
         elif c == 'exchange':


          
            with open('./private/botdata.json', 'r') as f:

                data = json.load(f)      

            c = 0

    
            for i in data['ids-to-have-full-access-in-tickets']:
                    r = discord.utils.get(ctx.guild.roles, id=i)

                    if r in ctx.author.roles:
                        c += 1


            try:

             
              if ctx.author.guild_permissions.administrator or c > 0:
                pass 
          
              else:
    
                try:
    
                  with open('./database/UserData.json', 'r') as f:
                    data = json.load(f)

                  data[str(ctx.author.id)]

                  with open('./database/UserData.json', 'w') as f:
                    json.dump(data, f, indent=1)

                except:
                       
                  await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                  return
                    

            except:
                    
                await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                return

            with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)
                    
            id = data[str(ctx.channel.id)]['Message']
            status = data[f"{ctx.channel.id}"]["Status"]
            
            if status != 'Completed' and status != 'Closed' and status != 'Cancelled':
              await ctx.reply(f'You have to close the ticket first before deleting.')
              return


            now = datetime.datetime.now()
            limit = datetime.timedelta(seconds=5)

            o = now+limit

            d = datetime.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second)
            time_stamp = calendar.timegm(d.timetuple())
            
            to = time_stamp
                
            embed2 = discord.Embed(description=f'`🗑️` {ctx.channel.mention} will be deleted <t:{to}:R>.\n — **Responsible Moderator**: {ctx.author.mention} (*{discord.utils.escape_markdown(ctx.author.name)}*)', color=0x6056ff)
            await ctx.reply(embed=embed2)
            await asyncio.sleep(5)
            

            try:
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                user = data[str(ctx.channel.id)]['Exchange-Request-User']['ID']
            
                del data[str(user)]

                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                        
            except:
                pass
            
            chid = ctx.channel.id
            
            try:


                 try:
                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  transcript = data[f"{chid}"]['Exchange-Request-User']['Trascript']
                
                 except:
                  transcript = None
                
                 if transcript == 'Received':
                        pass
                    
                 else:
                
                
                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  data[f"{chid}"]['Exchange-Request-User']['Trascript']
                  user = data[f"{chid}"]['Exchange-Request-User']['ID']
                  username = data[f"{chid}"]['Exchange-Request-User']['Name']
                  price_send = data[f"{chid}"]['Price-Send']

                  price_receive = data[f"{chid}"]['Price-Receive']

                  
                
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{chid}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {ctx.author.mention}', color=0x6056ff)

                
                  usersend = await ctx.guild.fetch_member(int(user))
                  await usersend.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    
            except:
                    pass   

            try:

                 try:
                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                        
                  transcript = data[f"{chid}"]['Exchange-Complete-User']['Trascript']
                
                 except:
                  transcript = None
                
                 if transcript == 'Received':
                        pass
                    
                 else:
                    

                    with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)
                    
                    exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                    username = data[f"{chid}"]['Exchange-Request-User']['Name']
                    price_send = data[f"{chid}"]['Price-Send']
                    userid = data[f"{chid}"]['Exchange-Request-User']['ID']
                
                    price_receive = data[f"{chid}"]['Price-Receive']
              
                    option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                    receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']


                    embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {ctx.author.mention}', color=0x6056ff)
                    exchanger = await ctx.guild.fetch_member(int(exchangerid))
                    await exchanger.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    


                    try:


                       try:
                        with open('./database/TicketData.json', 'r') as f:
                             data = json.load(f)
                        
                        transcript = data[f"{chid}"]['MM-Request-User']['Trascript']
                
                       except:
                        transcript = None
                
                       if transcript == 'Received':
                              pass
                    
                       else:
                        
                            with open('./database/TicketData.json', 'r') as f:
                               data = json.load(f)
                        
                            k = data[f"{str(ctx.channel.id)}"]["MM-Request-User"]["ID"]


                            k2 = await ctx.guild.fetch_member(int(k))
                            await k2.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))
                    
                    except:
                       pass
                    
            except:
                    pass

            try:
                  os.remove(f"Tickets/{ctx.channel.name}.htm")      
                
            except:
                pass
                
            try:

                   
                  chid = ctx.channel.id

                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  exchanger = data[f"{chid}"]["Exchange-Complete-User"]["Name"]
                  exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                  status = data[f"{chid}"]["Status"]
                  userid = data[f"{chid}"]['Exchange-Request-User']['ID']


                  price_send = data[f"{chid}"]['Price-Send']
                  price_receive = data[f"{chid}"]['Price-Receive']
   
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
                  more_options = data[f"{chid}"]['Exchange']['More-Options']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']
                  more_receive_options = data[f"{chid}"]['Receive-Exchange']['More-Options']

                  username = data[f"{chid}"]['Exchange-Request-User']['Name']


                
                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(ctx.guild.channels, id=data["exchange-logs-channel-id"])

                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{ctx.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)

                  with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)

                  urn = data[f"{str(ctx.channel.id)}"]["Exchange-Request-User"]["Name"]
                  urid = data[f"{str(ctx.channel.id)}"]["Exchange-Request-User"]["ID"]
                    
                  try:
                    u1n = data[f"{str(ctx.channel.id)}"]["Exchange-Complete-User"]["Name"]
                    u1id = data[f"{str(ctx.channel.id)}"]["Exchange-Complete-User"]["ID"] 
                  except:
                    u1n = None
                    
                  try:  
                    with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)

                    u2n = data[f"{str(ctx.channel.id)}"]["MM-Request-User"]["Name"]
                    u2id = data[f"{str(ctx.channel.id)}"]["MM-Request-User"]["ID"]
                    
                  except:
                    
                    u2n = None
                    
                    
                  if u2n:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {ctx.author.mention}\n> Name: `{ctx.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    embed.add_field(name=f'MM request user:', value=f'{u2n} ({u2id})', inline=False)
                    embed.add_field(name=f'Exchanger (MM):', value=f'{u1n} ({u1id})', inline=False)
                    
                  elif u1n:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {ctx.author.mention}\n> Name: `{ctx.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    embed.add_field(name=f'Exchanger:', value=f'{u1n} ({u1id})', inline=False)
                    
                  else:
                    embed=discord.Embed(title="Exchange Ticket Has been Deleted.", description=f'- Ticket was deleted by {ctx.author.mention}\n> Name: `{ctx.channel.name}`', color=0x6056ff)
                    embed.add_field(name=f'Exchange request user:', value=f'{urn} ({urid})', inline=False)
                    

                  await channel.send(f"Exchange Request: {urn} ({urid}) - <@{urid}>{f' | Exchanger: {u1n} ({u1id}) - <@{u1id}>' if u1n != None else ''}{f' | MM Request: {u2n} ({u2id}) - <@{u2id}>' if u2n != None else ''}", embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))

        
                  os.remove(f"Tickets/{ctx.channel.name}.htm")        

            except:
                    pass   

 
            try:
                with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                del data[str(ctx.channel.id)]

                with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                        
            except:
                pass
            
            await ctx.channel.delete()  
        
        
         elif c == 'support':

                             
            with open('./private/botdata.json', 'r') as f:
    
                data = json.load(f)      

            c = 0


            for i in data['ids-to-have-full-access-in-support-tickets']:
                        r = discord.utils.get(ctx.guild.roles, id=i)

                        if r in ctx.author.roles:
                            c += 1


             
            if ctx.author.guild_permissions.administrator or c > 0:
                pass 
               
            else:
                await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                return

            now = datetime.datetime.now()
            limit = datetime.timedelta(seconds=5)

            o = now+limit

            d = datetime.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second)
            time_stamp = calendar.timegm(d.timetuple())
            
            to = time_stamp
                
            embed2 = discord.Embed(description=f'`🗑️` {ctx.channel.mention} will be deleted <t:{to}:R>.\n — **Responsible Moderator**: {ctx.author.mention} (*{discord.utils.escape_markdown(ctx.author.name)}*)', color=0x6056ff)
            await ctx.reply(embed=embed2)
            await asyncio.sleep(5)
            

 



            try:

                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(ctx.guild.channels, id=data["support-tickets-logs-channel-id"])

                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{ctx.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)
                    
                  with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

                  user = data[str(ctx.channel.id)]['Support-Request-User']['ID']

                  try:
                    
                    user_get = await ctx.guild.fetch_member(user)
                    hy = f'{user_get.mention} ({user})'
                    

                    embed=discord.Embed(title="Your Support Ticket was deleted.", description=f'- Ticket was deleted by {ctx.author.mention}', color=0x6056ff)
  
                    await user_get.send(embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))
    
                    
                  except:
                    
                    hy = f'{user}'

                  embed=discord.Embed(title="Support Ticket Has been Deleted.", description=f'- Ticket was deleted by {ctx.author.mention}\n- Ticket Creator: {hy}', color=0x6056ff)

                  await channel.send(hy, embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))

                  channel = self.bot.get_channel(1260523935657754685)
                  await channel.send(hy, embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))
                  
                  os.remove(f"Tickets/{ctx.channel.name}.htm")        

            except:
                    pass   
                
                
              


            await ctx.channel.delete()  

            try:
              with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

              user = data[str(ctx.channel.id)]['Support-Request-User']['ID']
            
              del data[str(user)]

              with open('./database/SupportTickets/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

            except:
                pass
                    

            try:
              with open('./database/SupportTickets/TicketData.json', 'r') as f:
                      data = json.load(f)

              del data[str(ctx.channel.id)]

              with open('./database/SupportTickets/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

            except:
                pass


         else:


              now = datetime.datetime.now()
              limit = datetime.timedelta(seconds=5)

              o = now+limit

              d = datetime.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second)
              time_stamp = calendar.timegm(d.timetuple())
            
              to = time_stamp
 
              embed2 = discord.Embed(description=f'`🗑️` {ctx.channel.mention} will be deleted <t:{to}:R>.\n — **Responsible Moderator**: {ctx.author.mention} (*{discord.utils.escape_markdown(ctx.author.name)}*)', color=0x6056ff)
              await ctx.reply(embed=embed2)
              await asyncio.sleep(5)
         



              try:


                  with open('./private/botdata.json', 'r') as f:
                     data = json.load(f)

                  channel = discord.utils.get(ctx.guild.channels, id=data["applications-logs-channel-id"])

                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{ctx.channel.name}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)

                  with open('./database/Applications/applications.json', 'r') as f:
                      prefixes = json.load(f)
                    
                  uid = prefixes[f"{str(ctx.channel.id)}"]
                
                
                  try:
                        
                        user = self.bot.get_user(uid)
                        
                        uid_send = f'{user.mention}, {user.name} ({user.id})'
                        
                  except:
                        uid_send = uid

                  embed=discord.Embed(title="Application Ticket Has been Deleted.", description=f'- Application was deleted by {ctx.author.mention}\n- Application Creator: {uid_send}', color=0x6056ff)

                  await channel.send(uid_send, embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))

                  channel = self.bot.get_channel(1262511784712208435)

                  await channel.send(uid_send, embed=embed, file=discord.File(f'Tickets/{ctx.channel.name}.htm'))
                  
                  os.remove(f"Tickets/{ctx.channel.name}.htm")        

              except:
                    pass   


              await ctx.channel.delete()  

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.channel)
    async def close(self, ctx):
                
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
                
              c = ''
                
                
                
         if c == '':
            await ctx.reply('This is not a ticket.', delete_after=5)
         
         elif c == 'exchange':


          
            with open('./private/botdata.json', 'r') as f:

                data = json.load(f)      

            c = 0

    
            for i in data['ids-to-have-full-access-in-tickets']:
                    r = discord.utils.get(ctx.guild.roles, id=i)

                    if r in ctx.author.roles:
                        c += 1


            try:

             
              if ctx.author.guild_permissions.administrator or c > 0:
                pass 
          
              else:
    
                try:
    
                  with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)

                  d = data[str(ctx.channel.id)]['Exchange-Request-User']['ID']
                  status = data[f"{ctx.channel.id}"]["Status"]
                    
                  if status == 'Completed' or status == 'Cancelled':
                    pass
                
                  else:
                        
                    if ctx.author.id != d:
                      await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                      return


                except:
                       
                  await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                  return
                    

            except:
                    
                await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                return

            with open('./database/TicketData.json', 'r') as f:
                    data = json.load(f)
                    
            id = data[str(ctx.channel.id)]['Message']
            status = data[f"{ctx.channel.id}"]["Status"]
            
            if status == 'Closed':
              await ctx.reply(f'The ticket is already closed.')
              return

            msg = await ctx.channel.fetch_message(id)
            

        
        
            await msg.edit(view=AfterClose())


            now = datetime.datetime.now()




            try:

                  with open('./database/TicketData.json', 'r') as f:

                     data = json.load(f)

                  user2 = data[f"{str(ctx.channel.id)}"]['Users']
                
                   
                  for i in user2:

                     try:
                       
                       user = await ctx.guild.fetch_member(i)
                       await ctx.channel.set_permissions(user, send_messages=False, read_messages=False)

                     except:
                       pass

            except:
                  pass

            chid = ctx.channel.id


            now = datetime.datetime.now()

            d = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
            time_stamp = calendar.timegm(d.timetuple())

            try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  exchanger = data[f"{chid}"]["Exchange-Complete-User"]["Name"]
                  exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                  status = data[f"{chid}"]["Status"]


                  price_send = data[f"{chid}"]['Price-Send']
                  price_receive = data[f"{chid}"]['Price-Receive']
   
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
                  more_options = data[f"{chid}"]['Exchange']['More-Options']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']
                  more_receive_options = data[f"{chid}"]['Receive-Exchange']['More-Options']

                  username = data[f"{chid}"]['Exchange-Request-User']['Name']


                  with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)

                  if status == 'Claimed':
                    data[str(exchangerid)]['Current'] -= price_send
                    
                    data[str(exchangerid)]['Current-Limit'] -= price_send
                    
                  ex = None

                  for i in data[str(exchangerid)][f"Active"]:
                      if f"{ctx.channel.mention}" in i:
                          ex = i
                          break 


                  if ex:

                      index = data[str(exchangerid)][f"Active"].index(ex)
                      del data[str(exchangerid)][f"Active"][index]

                  with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)




                  if status == 'Completed':

                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                    emoj = '✔️'
                    data[f"{chid}"]["Status"] = 'Completed'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                    
                    
                    
                  elif status == 'Cancelled':  

                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                    emoj = '❌'
                    data[f"{chid}"]["Status"] = 'Cancelled'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                    
                  else:

                   with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                   data[f"{chid}"]["Status"] = 'Cancelled' 
                    
                   with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)


                   with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                   data[str(exchangerid)]


        
                   try:

                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] += 1

                   except:
                  
                       data[str(exchangerid)]['Weekly-Exchanged'] = {}    
                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] = 1
                       data[str(exchangerid)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
                
                
                   try:
                        
                        data[str(exchangerid)]['History']
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                   except:
                                              
                        data[str(exchangerid)]['History'] = []
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

                   with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

  
            except:

                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  data[f"{chid}"]["Status"] = 'Closed' 
                    
                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                  exchanger = None

                
                
                
            try:
                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

                  exchangerid = data[f"{chid}"]["MM-Request-User"]["ID"]



                  with open('./database/UserData.json', 'r') as f:
                      data = json.load(f)
                    
                  ex = None

                  for i in data[str(exchangerid)][f"Active"]:
                      if f"{ctx.channel.mention}" in i:
                          ex = i
                          break 


                  if ex:

                      index = data[str(exchangerid)][f"Active"].index(ex)
                      del data[str(exchangerid)][f"Active"][index]

                  with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)



                  if status == 'Completed':
                    pass

                    
                  elif status == 'Cancelled':  
                    pass
                    
                  else:


                   with open('./database/UserData.json', 'r') as f:
                              data = json.load(f)

                   data[str(exchangerid)]


        
                   try:

                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] += 1

                   except:
                  
                       data[str(exchangerid)]['Weekly-Exchanged'] = {}    
                       data[str(exchangerid)]['Weekly-Exchanged']['Orders'] = 1
                       data[str(exchangerid)]['Weekly-Exchanged']['Total-Exchanged'] = 0 
                
                
                   try:
                        
                        data[str(exchangerid)]['History']
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                      
                   except:
                                              
                        data[str(exchangerid)]['History'] = []
                        data[str(exchangerid)]['History'].append(f"`❌` <t:{time_stamp}:R> (<t:{time_stamp}:d>, <t:{time_stamp}:t>) {username}, {price_send}€ {f'{option_exchange}' if more_options == 'None' else f'{more_options}'} ⟶ {price_receive}€ {f'{receive_exchange}' if more_receive_options == 'None' else f'{more_receive_options}'}")
                        

                    

                   with open('./database/UserData.json', 'w') as f:
                      json.dump(data, f, indent=1)

  
            except:

                  pass


            now = datetime.datetime.now()

            try:

                  with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)

                  user = data[f"{chid}"]['Exchange-Request-User']['ID']
                  username = data[f"{chid}"]['Exchange-Request-User']['Name']
                  price_send = data[f"{chid}"]['Price-Send']
                  userid = data[f"{chid}"]['Exchange-Request-User']['ID']
                
                  option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                  receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']
                
                  price_receive = data[f"{chid}"]['Price-Receive']

                  export = await chat_exporter.export(channel=ctx.channel)
                  file_name=f"Tickets/{chid}.htm"
                  with open(file_name, "w", encoding="utf-8") as f:
                    f.write(export)


                  embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {ctx.author.mention}', color=0x6056ff)

                
                  usersend = await ctx.guild.fetch_member(int(user))
                  await usersend.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))

                  with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                  data[f"{chid}"]['Exchange-Request-User']['Trascript'] = 'Received'

                  with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)
                
            except:
                    pass   

            try:


                    with open('./database/TicketData.json', 'r') as f:
                       data = json.load(f)

                    exchangerid = data[f"{chid}"]["Exchange-Complete-User"]["ID"]
                    username = data[f"{chid}"]['Exchange-Request-User']['Name']
                    userid = data[f"{chid}"]['Exchange-Request-User']['ID']
                    price_send = data[f"{chid}"]['Price-Send']
                
                    option_exchange = data[f"{chid}"]['Exchange']['Type']
    
                    receive_exchange = data[f"{chid}"]['Receive-Exchange']['Type']

                    price_receive = data[f"{chid}"]['Price-Receive']
                    

                    embed=discord.Embed(title="Your Exch Ticket was closed.", description=f'- Ticket was closed by {ctx.author.mention}', color=0x6056ff)
                    exchanger = await ctx.guild.fetch_member(int(exchangerid))
                    await exchanger.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))

                    with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)
            
                    data[f"{chid}"]['Exchange-Request-User']['Trascript'] = 'Received'

                    with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)

                    try:
                      k = data[f"{str(ctx.channel.id)}"]["MM-Request-User"]["ID"]
                    
                      with open('./database/TicketData.json', 'r') as f:
                        data = json.load(f)
            
                      data[f"{chid}"]['MM-Request-User']['Trascript'] = 'Received'

                      with open('./database/TicketData.json', 'w') as f:
                        json.dump(data, f, indent=1)
                    
                    
                      k2 = await ctx.guild.fetch_member(int(k))
                      await k2.send(f"{username} ({userid}) - <@{userid}>", embed=embed, file=discord.File(f'Tickets/{chid}.htm', filename=f"{username} ({userid}) - {price_send} ⟶ {price_receive} ({option_exchange[0].lower()}2{receive_exchange[0].lower()}).htm"))


                    except:
                        pass
                    
            except:
                    pass
                
            os.remove(f"Tickets/{chid}.htm") 

                
            with open('./database/TicketData.json', 'r') as f:
                      data = json.load(f)

            del data[str(user)]

            with open('./database/TicketData.json', 'w') as f:
                      json.dump(data, f, indent=1)  
                
                
            embed = discord.Embed(title=f'Ticket Closed', description=f"- The ticket has been closed by {ctx.author.mention}\n`❓` — To delete ticket, use the `delete` button [here]({msg.jump_url}).", color=0x6056ff)
            await ctx.reply(embed=embed)
                
                

        
        
        
        
         else:

                             
            with open('./private/botdata.json', 'r') as f:
    
                data = json.load(f)      

            c = 0


            for i in data['ids-to-have-full-access-in-support-tickets']:
                        r = discord.utils.get(ctx.guild.roles, id=i)

                        if r in ctx.author.roles:
                            c += 1


             
            if ctx.author.guild_permissions.administrator or c > 0:
                pass 
               
            else:
                await ctx.reply("You don't have enough permissions to use this.", delete_after=5)
                return


            with open('./database/SupportTickets/TicketData.json', 'r') as f:
                    data = json.load(f)
                    
            id = data[str(ctx.channel.id)]['Message']

            msg = await ctx.channel.fetch_message(id)

            embed = discord.Embed(description='`❓` — **Are you sure you want to close this ticket**?\n-# Select an option down below.', color=0x6056ff)
            msg = await ctx.reply(embed=embed)
            await msg.edit(view=SupportClose(interaction_msg = msg, interaction_user = ctx.author, message_for_edit = msg))
        
        


async def setup(bot):
    await bot.add_cog(TicketCreation(bot))