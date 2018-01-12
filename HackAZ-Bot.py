"""
Instantiates a discord bot with some basic commands and activates it for the
Hack-AZ discord channel.
"""

import login_Credentials
import discord
from profanity_Filter import profanity_Filter
from discord.ext.commands import Bot

# ____SET-UP____#
bot = Bot(command_prefix="!")
apps = [profanity_Filter]


# ____EVENTS____#
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.event
async def on_message_edit(before, after):
    if before.author.id != bot.user.id:
        await bot.send_message(discord.Object(id='398952807107002370'), str(before.author) + " : Edit :" + 
                                                                        "\n\tBefore: " + before.content + 
                                                                        "\n\tAfter: " + after.content)
        for app in apps:
            await app(message, bot)
        await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author.id != bot.user.id:
        await bot.send_message(discord.Object(id='398952807107002370'), str(message.author) + " : Delete :" + 
                                                                        "\n\t " + message.content)

@bot.event
async def on_message(message):
    try:
        if message.author.id != bot.user.id:
            await bot.send_message(discord.Object(id='398952807107002370'), "Channel: " + message.channel.name +" Author: "+ str(message.author) + " Message: " + message.content)
            for app in apps:
                await app(message, bot)
    except Exception:
        print("line 42 DM Error most likely")
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(emoji, user):
    print("reaction")



# ____COMMANDS____#
@bot.command(pass_context=True)
async def report(ctx, user, *message):
    """!report <username/user id> <description>"""
    try:
        discord.Object(id=user[3:-1]).created_at #This is checking if user exists and throwing an error DON'T Erase
        author = ctx.message.author
        print(author)
        await bot.send_message(discord.Object(id='397562402033369088'),
                               "Report: \n\tFrom: " + 
                               str(ctx.message.author) + "\n\tAgainst: " +
                               str(user) + "\n\tDescription: \n\t\t\"" +
                               ' '.join(message) + "\"")
    except Exception:
        await bot.send_message(ctx.message.author,
                               "There was an error with the command!\n " +
                               "(Format: !report @username description)\n " +
                               "You can try again in a dm to HackAZ Bot. " +
                               "If you are still having trouble please " +
                               "message @envyhunter. You wrote: " +
                               str(ctx.message.content))
    try:
        await bot.delete_message(ctx.message)
    except Exception:
        print("Report Command: Delete try/catch")

# ____RUN____#
bot.run(login_Credentials.BOT_TOKEN)