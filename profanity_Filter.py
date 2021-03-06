"""
IF a discord user says a bad word, a bot deletes it and shouts at them.
"""
badwords = ""
with open('./black_listed_words.txt') as file:
    badwords = [line.strip() for line in file]

whitelisted = ["ass", "asses", "assess", "arse", "shitake"]


async def profanity_Filter(message, bot):
    message_list = message.content.lower().split(" ")
    if not message.content.startswith('!report'):
        for word in badwords:
            if (word in message_list or ((word not in whitelisted) and word in
                message.content.lower())):
                
                author = message.author.name
                channel = message.channel.name
                msg = message.content
                await bot.delete_message(message)
                await bot.send_message(message.author,
                                           "Greetings " + author
                                           + " on " + channel +
                                           " you said \"" + msg +
                                           "\".\nPlease refrain from such " +
                                           "harsh language.\nIf you think " +
                                           "that your message was deleted " +
                                           "though error.\nPlease message " +
                                           "@envyhunter with your message." +
                                           "\nFlagged word: " + word +
                                           "\n\n\n ")
                
                return
    return