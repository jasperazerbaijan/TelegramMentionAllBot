from telegram.ext import Updater, CommandHandler

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
    

updater = Updater('KEY')


updater.dispatcher.add_handler(CommandHandler('all', all))

updater.dispatcher.add_handler(CommandHandler('set_members', set_members))

updater.start_polling()
updater.idle()
