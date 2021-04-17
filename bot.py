from telegram.ext import Updater, CommandHandler
def start(update, context):

    update.message.reply_text('Hola humano')

def help(update, context):

    update.message.reply_text('Help to play')

if __name__ == '__main__':

    updater = Updater(token='1784474668:AAG6DffL1G2VBkzzMH1X74ZEBQGsii9i8-Y', use_context=True)

    dp = updater.dispatcher

    #add handler
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', help))

    updater.start_polling()
    updater.idle()