from telegram.ext import Updater, CommandHandler
from utilities import utilities

import asyncio

async def run(message, matches, chat_id, step, crons=None):

    response = []

    chat = message.chat_id

    users = await utilities.client.get_participants(chat)

    uwu = ""

    bots = ""

    inde = [1, 1]

    for user in users:

        if user.username != None and user.bot == False:

            uwu = uwu + "@" + user.username + "-"

            inde[0] = inde[0] + 1

        elif user.username == None and user.first_name != None:

            continue

        elif user.bot == True:

            bots = bots + "@" + user.username + "-"

            inde[1] = inde[1] + 1

    uwu = uwu + bots

    x = 4080

    length = len(uwu)

    some_string = uwu.split("-")

    index = 0

    me_sg = ""

    while index < len(some_string):

        if some_string[index] == "  ":

            continue

        if len(me_sg) < x:

            if me_sg != "" and (

                index + 1 == len(some_string) or (me_sg != "" and index % 500 == 0)

            ):

                response.append(utilities.client.send_message(chat, me_sg[:-2]))

                response.append(asyncio.sleep(2))

                me_sg = ""

                continue

            me_sg = me_sg + some_string[index] + " - "

        else:

            if me_sg != "":

                response.append(message.reply(me_sg[:-2]))

                response.append(asyncio.sleep(2))

                me_sg = some_string[index] + " - "

        index = index + 1

    return response

plugin = {

    "name": "tag all",

    "desc": "tag all memebers in chat you in.",

    "usage": ["`[!/#]mention`"],

    "run": run,

    "sudo": False,

    "patterns": ["^[!/#]mention$",],

}


members = {}



def all(bot, update):
    update.message.reply_text(
        'HEY {}'.format(members[str(update.message.chat.id)]))

def set_members(bot, update):
    global members 
    members[str(update.message.chat.id)]=update.message.text.replace("/set_members"," ")
    update.message.reply_text(
        'The members have been saved, you can use the all command to mention them.')
    print ("Setted members: "+update.message.text)
    

updater = Updater('1696209895:AAFfW2S65QsqFU_-YAj6Fl_Ll94_WKMyWxQ')


updater.dispatcher.add_handler(CommandHandler('all', all))

updater.dispatcher.add_handler(CommandHandler('set_members', set_members))

updater.start_polling()
updater.idle()
