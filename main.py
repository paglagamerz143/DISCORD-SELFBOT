
# lalala my owned multipurpose selfbot.
# If you want to use this, you need to set your token and prefix in the .env file
# You also need to install the following libraries from the requirements.txt file:
# you can do it with the following command:
# pip install -r requirements.txt
# In this bot you can get many moderation and utility commands.
# Also Have Fun :)

import discord
from discord.ext import commands
import os
import dotenv
import random
import datetime
import string


dotenv.load_dotenv()

# clietn and intents setup
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')
client = commands.Bot(command_prefix=prefix,
    intents=intents,
    self_bot=True,
    )


# checking bot events when the bot is ready
@client.event
async def on_ready():
    print('██████╗  █████╗ ███████╗██╗██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗')
    print('██╔══██╗██╔══██╗██╔════╝██║██╔══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝')
    print('██████╔╝███████║█████╗  ██║██║  ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   ')
    print('██╔══██╗██╔══██║██╔══╝  ██║██║  ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   ')
    print('██║  ██║██║  ██║██║     ██║██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   ')
    print('╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   ')
    print(f'Logged in as {client.user.name}')




#                                 commands for moderation commands in the selfbot
#                                       --------------------------------      
                           
# kick command for kicking a member
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.name} from the server')

# ban command for banning a member
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.name} from the server')

# unban command for unbanning a member
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

    await ctx.send(f'{member.name}#{member_discriminator} is not banned')

# clear command for clearing messages
@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages', delete_after=5)   # delete this massage after 5 seconds

# mass dm command for sending messages to multiple people
@client.command()
async def massdm(ctx, *, message):
    targets = ctx.guild.members  # send the message to all the members in the server

    for target in targets:
        await target.send(message)
    await ctx.send(f'Sent the message to {len(targets)} people')

# mass react command for reacting to messages
@client.command()
async def massreact(ctx, number: int, *, reaction: str):
    reaction = str(reaction)
    if number == None:
        default_number = 100
    else:
        default_number = number
    messages = await ctx.channel.history(limit=number).flatten()
    for message in messages:
        await message.add_reaction(reaction)
    await ctx.send(f'Reacted to {len(messages)} messages')

# banall command for banning all members in the server
@client.command()
async def banall(ctx):
    for member in ctx.guild.members:
        await member.ban()
    await ctx.send(f'Banned all members in the server')

# nuke command for nucking a channel
@client.command()
async def nuke(ctx):
    """ For nuking a channel """
    # create a new channel by duplicating the old channel
    await ctx.channel.clone()
    # delete the old channel
    await ctx.channel.delete()

    # send a message in new channel
    await ctx.channel.send(f'Nuked by {ctx.author.name}')

#nickname command for changing the nickname
@client.command()
async def nickname(ctx, *, member: discord.Member = None, nickname):
    if member is None:
        member = ctx.author  # Defaults to the author if no member is provided
    # change the nickname of the member
    await member.edit(nick=nickname)
    await ctx.send(f'Nickname changed to {nickname}')

#role command for adding a role to a member
@client.command()
async def addrole(ctx, *, member: discord.Member = None, role: discord.Role):
    if member is None:
        member = ctx.author  # Defaults to the author if no member is provided
    # add the role to the member
    await member.add_roles(role)
    await ctx.send(f'Added {role.name} to {member.name}')

#removerole command for removing a role from a member
@client.command()
async def removerole(ctx, *, member: discord.Member = None, role: discord.Role):
    if member is None:
        member = ctx.author  # Defaults to the author if no member is provided
    # remove the role from the member
    await member.remove_roles(role)
    await ctx.send(f'Removed {role.name} from {member.name}')



#                                      Utility commands
#                                      ----------------

# ping command for checking the latency of the selfbot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#spam command for spamming a message
@client.command()
async def spam(ctx, amount: int, *, message):
    for i in range(amount):  # spam the message "amount" times
        await ctx.send(message)

# avatar command for getting the user's avatar
@client.command()
async def avatar(ctx, user: discord.Member):
    await ctx.send(user.avatar_url)

# serverinfo command for getting the server's info
@client.command()
async def serverinfo(ctx):
    server = ctx.guild
    # Get the server details
    name = server.name
    id = server.id
    owner = server.owner
    member_count = server.member_count
    region = server.region
    text_channels = len(server.text_channels)
    voice_channels = len(server.voice_channels)
    categories = len(server.categories)
    roles = len(server.roles)
    created_at = server.created_at.strftime("%B %d, %Y")
    boost_level = server.premium_tier
    boost_count = server.premium_subscription_count

  # Construct the text message with all the server info
    server_info = (
        f"# **SERVER INFO**\n"
        f"**Server Name**: {name}\n"
        f"**Server ID**: {id}\n"
        f"**Owner**: {owner}\n"
        f"**Member Count**: {member_count}\n"
        f"**Region**: {region}\n"
        f"**Text Channels**: {text_channels}\n"
        f"**Voice Channels**: {voice_channels}\n"
        f"**Categories**: {categories}\n"
        f"**Roles**: {roles}\n"
        f"**Created At**: {created_at}\n"
        f"**Boost Level**: {boost_level}\n"
        f"**Boost Count**: {boost_count}\n"  
    )

    # Send the plain text message
    await ctx.send(server_info)

# calculate command for calculating the equation
@client.command()
async def calc(ctx, equation):
    try:
        result = eval(equation)
        await ctx.send(f"The result is {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")


# A dictionary to store user's AFK status
afk_users = {}

#afk command for making the selfbot afk
@client.command()
async def afk(ctx, *, reason=None):
    # Check if the user is already AFK
    if ctx.author.id not in afk_users:
        # If not, set the user as AFK with a reason and timestamp
        afk_users[ctx.author.id] = {
            'reason': reason or "No reason provided",
            'time': datetime.now()
        }
        await ctx.send(f"{ctx.author.mention} is now AFK! Reason: {reason or 'No reason provided'}")
    else:
        await ctx.send(f"{ctx.author.mention}, you're already AFK.")


# unafk command for making the selfbot not afk
@client.command()
async def unafk(ctx):
    # If the user is AFK, remove them from the AFK list
    if ctx.author.id in afk_users:
        del afk_users[ctx.author.id]
        await ctx.send(f"Welcome back {ctx.author.mention}!")
    else:
        await ctx.send(f"{ctx.author.mention}, you're not marked as AFK.")


# join voice channel command for joining a voice channel
@client.command()
async def joinvc(ctx, channel: discord.VoiceChannel = None):
    try:
        if channel is None:
            await ctx.send("Invalid voice channel.")
            return

        await channel.connect()
        await ctx.send(f'Joined the voice channel: {channel.name}')
    except Exception as e:
        await ctx.send(f'An error occurred: {e}')


# leave voice channel command for leaving a voice channel
@client.command()
async def leavevc(ctx):
    channel = ctx.voice_client
    if channel:
        await channel.disconnect()
        await ctx.send("Successfully left the voice channel.")
    else:
        await ctx.send("I'm not connected to any voice channel.")

# bkash number command for sending the bkash number
@client.command()
async def bkash(ctx):
    await ctx.send('**Bkash Marchent : 01768950155**')

#nagad number command for sending the nagad number
@client.command()
async def nagad(ctx):
    await ctx.send('**Nagad Personal : 01768950155**')

#rocket number command for sending the rocket number
@client.command()
async def rocket(ctx):
    await ctx.send('**Rocket Number : Nai ;-;**')

#vouch command for sending the vouch channel
@client.command()
async def vouch(ctx):
    await ctx.send('Vouch Channel : <#1275440346641469490>')

# server link command for sending the server link
@client.command()
async def serverlink(ctx):
    await ctx.send('Server Link : https://discord.gg/PYwM9pycTg')

#guild bannner command for sending the guild banner
@client.command()
async def guildbanner(ctx):
    guild = ctx.guild
    await ctx.send(f'{guild.banner_url}')

# guild icon command for sending the guild icon
@client.command()
async def guildicon(ctx):
    guild = ctx.guild
    await ctx.send(f'{guild.icon_url}')

# user banner command for sending the user banner
@client.command()
async def banner(ctx, *, user: discord.Member):
    await ctx.send(f'{user.banner_url}')



#                                      Just for fun commands
#                                        ----------------
#                                  this is only for fun commands
#                            DO NOT USE THIS COMMAND FOR ANY PURPOSE


# user id command for sending the user id
@client.command()
async def userid(ctx, member: discord.Member = None):
    
    if member is None:
        member = ctx.author  # Defaults to the author if no member is provided
    
    # Send the user ID of the member
    await ctx.send(f"{member.name}'s User ID is: `{member.id}`")

# user info command for getting the user's info
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author  # Defaults to the author if no member is provided

    # Get the user's info
    name = member.name
    discriminator = member.discriminator
    id = member.id
    created_at = member.created_at.strftime("%B %d, %Y")
    joined_at = member.joined_at.strftime("%B %d, %Y")
    roles = ', '.join([role.name for role in member.roles])
    avatar_url = member.avatar_url
    platform = member.platform

    user_info = (
        f"# **User Info**\n"
        f"**Username**: {name}\n"
        f"**Discriminator**: {discriminator}\n"
        f"**User ID**: {id}\n"
        f"**Created At**: {created_at}\n"
        f"**Joined At**: {joined_at}\n"
        f"**Roles**: {roles}\n"
        f"**Avatar URL**: {avatar_url}\n"
        f"**Platform**: {platform}\n"
    )
    await ctx.send(user_info)

# nitro link gen command for generating the nitro link
@client.command()
async def nitro(ctx):
    
    # Generate a fake Nitro giveaway link
    link = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    promo_link = f"https://discord.gift/{link}"
    # Send the fake Nitro promo link with a fun message
    await ctx.send(f"**Nitro Giveaway!**\nGet your Nitro Boost here: {promo_link}\n*Disclaimer: This is just for fun. No actual Nitro is being given away!*")

# nine eleven command for sending the tribute message
@client.command()
async def nine_eleven(ctx):
    
    tribute_message = (
        "**In Memory of 9/11** \n"
        "On September 11, 2001, a series of terrorist attacks shook the world. Thousands of innocent lives were lost, "
        "and many others were affected by this tragic event. We remember those who lost their lives, their families, "
        "and all the heroes who responded to the crisis.\n\n"
        "Let us all take a moment of silence to honor their memory and reflect on the importance of peace and unity. "
        "We will never forget. "
    )
    
    await ctx.send(tribute_message)

# hack command for generating a fake hacking profile
@client.command()
async def hack(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author  # Use the command author's details if no member is mentioned
    # Sample fake bio data
    fake_bio_data = {
        "username": member.name,
        "hacker_name": f"H4ck3r_{''.join(random.choices(string.ascii_uppercase + string.digits, k=5))}",
        "ip_address": f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "location": random.choice(["California", "New York", "London", "Moscow", "Tokyo", "Berlin"]),
        "device": random.choice(["Linux", "Windows", "MacOS", "Android", "iOS"]),
        "status": random.choice(["Online", "Offline", "Infiltrating Systems", "Decrypting Files"]),
        "level": random.randint(1, 100),
        "hacked_accounts": random.randint(0, 50),
        "encryption_strength": f"{random.randint(256, 512)}-bit",
        "last_login": f"{random.randint(1, 12)} hours ago",
        "skills": random.choice(["Social Engineering", "Malware Analysis", "Cryptography", "Phishing", "Ethical Hacking"]),
    }

    # Constructing the hack bio
    hack_bio = (
        f"**{fake_bio_data['username']}**'s Hacking Profile:\n"
        f"**Hacker Alias**: {fake_bio_data['hacker_name']}\n"
        f"**IP Address**: {fake_bio_data['ip_address']}\n"
        f"**Location**: {fake_bio_data['location']}\n"
        f"**Device**: {fake_bio_data['device']}\n"
        f"**Status**: {fake_bio_data['status']}\n"
        f"**Level**: {fake_bio_data['level']}\n"
        f"**Hacked Accounts**: {fake_bio_data['hacked_accounts']}\n"
        f"**Encryption Strength**: {fake_bio_data['encryption_strength']}\n"
        f"**Last Login**: {fake_bio_data['last_login']}\n"
        f"**Skills**: {fake_bio_data['skills']}\n"
    )
    # Send the generated bio to the chat
    await ctx.send(f"{member.mention}, here's your **hacker profile**:\n\n{hack_bio}")

# joke command for sending a funny joke
@client.command()
async def joke(ctx):
    jokes = [
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
        "What's the object-oriented way to become a butterfly? Inheritance.",
        "Why do some people only see a shared experience as a trip? Because it leaves you wonderingly alone.",
        "What's the best thing about being a vegetarian? You get to eat all the food on the planet!"
    ]
    await ctx.send(random.choice(jokes))

# channel info command for getting the channel's info
@client.command()
async def channelinfo(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel  # Defaults to the current channel if no channel is provided
    # Get the channel details
    name = channel.name
    id = channel.id
    topic = channel.topic
    created_at = channel.created_at.strftime("%B %d, %Y")
    category = channel.category
    # Construct the text message with all the channel info
    channel_info = (
        f"# **CHANNEL INFO**\n"
        f"**Channel Name**: {name}\n"
        f"**Channel ID**: {id}\n"
        f"**Topic**: {topic}\n"
        f"**Created At**: {created_at}\n"
        f"**Category**: {category}\n"
    )
    await ctx.send(channel_info)

# cum command for sending a cum picture
@client.command()
async def cum(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1339252123388350576/1339252227704881213/FwiX29KWwAIgeB2.jpg")

# dick command for sending a dick picture
@client.command()
async def dick(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1339252123388350576/1339252532219744256/images_2.jpeg")


#running the selfbot
client.run(os.getenv('TOKEN'), bot=False)