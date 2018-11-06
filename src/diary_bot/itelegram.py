import logging

import const
import telegram
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    update.message.reply_text("Hi, I'm Diary Bot, your personal diary. Nice to meet you. :)")


def unmapped_words(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    handleNotExpectedCase(update)


def handleNotExpectedCase(update):
    update.message.reply_text("Hi.")
    update.message.reply_text("Please tap `/start` to start. ^^")


def setupBot():
    # Create Updater object and attach dispatcher to it
    updater = Updater(const.TOKEN())
    dispatcher = updater.dispatcher
    print("Bot started")

    # Add command handler to dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    unmapped_words_handler = MessageHandler(Filters.text, unmapped_words)
    dispatcher.add_handler(unmapped_words_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


def main():
    setupBot()


if __name__ == '__main__':
    main()
