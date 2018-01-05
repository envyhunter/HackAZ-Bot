"""
IF a discord user says a bad word, a bot deletes it and shouts at them.
"""
badwords = ""
with open('./black_listed_words.txt') as file:
    badwords = [line.strip() for line in file]

whitelisted = ["ass", "asses", "assess", "arse"]


async def profanity_Filter(message, bot):
    if message.author.id != bot.user.id:
        message_list = message.content.lower().split(" ")
        print("Here: " + message_list[0])
    if "#report" not in message_list[0]:
        for word in badwords:
            if (word in message_list or ((word not in whitelisted) and word in
                message.content.lower())):
                try:
                    await bot.send_message(message.author,
                                           "Greetings " + message.author.name
                                           + " on " + message.channel.name +
                                           " you said \"" + message.content +
                                           "\".\nPlease refrain from such " +
                                           "harsh language.\nIf you think " +
                                           "that your message was deleted " +
                                           "though error.\nPlease message " +
                                           "@envyhunter with your message." +
                                           "\nFlagged word: " + word +
                                           "\n\n\n ")
                    await bot.delete_message(message)
                except Exception:
                    print('send_message error')
                return
    return