import login_Credentials
import discord
from profanity_Filter import profanity_Filter
from discord.ext.commands import Bot
from discord.user import User
#____SET-UP____#
bot = Bot(command_prefix="#")
apps = [profanity_Filter]


#____EVENTS____#
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.event
async def on_message_edit(before, after):
   print( bot.get_message(id = after.id))

@bot.event
async def on_message(message):
    for app in apps:
        await app(message,bot)
    await bot.process_commands(message)

@bot.event
async def on_command(command, ctx):
    print("test")


#____COMMANDS____#
@bot.command(pass_context=True)
async def report(ctx, user, *message):
    try:
        discord.Object(id=user[3:-1]).created_at
        author = ctx.message.author
        print(author)
        await bot.send_message(discord.Object(id='397562402033369088'), "Report: \n\tFrom: " + str(ctx.message.author) + "\n\tAgainst: " + str(user) + "\n\tDescription: \n\t\t\"" + str(message) + "\"")
    except Exception:
        await bot.send_message(ctx.message.author, "There was an error with the command!\n (Format: #report username description)\n You can try again in a dm to HackAZ Bot. If you are still having trouble please message @envyhunter. You wrote: " + ctx.message)
    await bot.delete_message(ctx.message)  


#____RUN____#
bot.run(login_Credentials.BOT_TOKEN)
