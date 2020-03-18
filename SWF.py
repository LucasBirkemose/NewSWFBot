import discord
import asyncio
from discord.ext import commands
import random
import discord.utils
from discord.utils import get
from discord.utils import find
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='//')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(bot.user.name + " Is ready")
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='//help'))

@bot.command()
async def help(ctx):
    help = discord.Embed(
        colour=discord.Colour.blue(),
        title="Help options",
        description="This is where all the help is going to be."
    )

    help.add_field(name='Staff commands', value='These are all the staff commands to use them do //staff', inline=False)
    help.add_field(name="Fun commands", value="Please use //fun to get some funny things to look at.", inline=False)
    help.add_field(name='Coding help command', value='If you need help with any code do //code_help to get help with the thing that you need help with.')

    await ctx.send(embed=help)

@bot.command()
async def code_help(ctx):
    helpers=['@jfries#4063', '@SWF#7079', '@big c h u n g#4436', '@IggyMations#4121', '@ɘꙅomɘʞɿiᙠꙅɒɔu⅃#5922']
    await ctx.send('This guy needs some help ' + random.choice(helpers))

@bot.command()
@commands.has_permissions(kick_members=True)
async def staff(ctx):
    staff=discord.Embed(
        colour=discord.Colour.blue(),
        title='These are the staff commands',
        description='These are the s=commands for the staff on the server'
    )

    staff.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJxydhPevX1EuMuwc5GThEFYTwVR0LsU38yvqw=s288-c-k-c0xffffffff-no-rj-mo')
    staff.add_field(name='createText', value='If you are a Mod you can use //createText Name if you are too lazy to create a text channel manualy', inline=False)

    await ctx.send(embed=staff)

@bot.command()
async def fun(ctx):

    fun = discord.Embed(
        colour=discord.Colour.blue(),
        title="Funny things.",
        description="No sadnes allowed here."
    )

    fun.add_field(name="Coinflip command", value="Use //coinflip to either get heads or tails and maybe SIDE?", inline=False)
    fun.add_field(name="magicBall command", value="Use //magicBall to get an answer to your question.", inline=False)

    await ctx.send(embed=fun)

@bot.command()
async def coinflip(ctx):
    coin=['Heads!', 'Tails', 'Heads!', 'Tails', 'Heads!', 'Tails', 'Heads!', 'Tails', 'Wow Side!']
    await ctx.send(random.choice(coin))

@bot.command(aliases=['commandInfo fun'])
async def Info(ctx):
    IN=discord.Embed(
        colour=discord.Colour.blue(),
        title='The fun command is a command that shows you all the fun commands you can do'
    )

    await ctx.send(embed=IN)

@bot.command()
async def VeryLongCommandToType(ctx, amount=1):

    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)

    mod = discord.Embed(
        colour=discord.Colour.green(),
        title="command",
        description='Owner only yes'
    )

    mod.add_field(name='Annoy command', value='This is a trolling command only for the owner role')

    await ctx.send(embed=mod)

@bot.command()
@commands.has_role('Owner')
async def annoy(ctx, member, amount=1):

    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)

    await ctx.send(member)
    await ctx.send(member)
    await ctx.send(member)
    await ctx.send(member)
    await ctx.send(member)

@bot.command()
async def createText(ctx, name):
    guild = ctx.message.guild
    await guild.create_text_channel(name)

@bot.command()
async def createVoice(ctx, name):
    guild = ctx.message.guild
    await guild.create_voice_channel(name)

@bot.command()
async def magicBall(ctx, question):

    ball=["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never", "Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]
    ba = discord.Embed(
        colour=discord.Colour.blue()
    )

    ba.add_field(name='This is a ball', value=random.choice(ball))

    await ctx.send(embed=ba)

@bot.command()
async def botInfo(ctx):
    botin = discord.Embed(
        colour=discord.Colour.orange(),
        title='Bot info!',
        description='This is a bot made for SWF and his discord server Coding Central'
    )

    botin.set_author(name="Author", icon_url="https://imgur.com/zOe457n")
    botin.set_thumbnail(url='https://cdn.discordapp.com/attachments/661888062468521984/676164069660688385/image0.png')
    botin.set_image(url='https://cdn.discordapp.com/attachments/661888062468521984/676164070302285874/image1.png')
    botin.set_footer(text='SWF bot not for sale!')
    botin.add_field(name='Info about the bot', value='The bot is a bot that is for the person named SWF in discord. The bot is a bot both for fun and other stuff', inline=False)
    botin.add_field(name='SWF', value='SWF is a nice person that likes to talk about coding and C#. I do not know if he codes in anything else than C#.', inline=True)
    botin.add_field(name='SWF channel', value='SWF has a channel named SWF and with a box with lighting things on the side', inline=True)

    await ctx.send(embed=botin)

@bot.command(pass_context=True, aliases=['kickuser'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=""):
    await member.kick(reason=reason)
    await ctx.send('The member has been kicked from the server')

@bot.command(pass_context=True, aliases=['banuser'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=""):
    await member.ban(reason=reason)
    await ctx.send('The member has been kicked from the server')

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send('Messaged deleted.')


































bot.run('NjY5NTQwMzI2NDI3NDU5NTg1.XmvnHA.ibAmD_22gY1GMAzpMpqHljkq2tQ')
