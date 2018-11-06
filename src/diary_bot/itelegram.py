import logging
from functools import wraps

import const
from telegram import ChatAction
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(*args, **kwargs):
            bot, update = args
            bot.send_chat_action(chat_id=update.message.chat_id, action=action)
            func(bot, update, **kwargs)
        return command_func
    return decorator


send_typing_action = send_action(ChatAction.TYPING)
send_upload_video_action = send_action(ChatAction.UPLOAD_VIDEO)
send_upload_photo_action = send_action(ChatAction.UPLOAD_PHOTO)


@send_typing_action
def start(bot, update):
    handle_intent(bot, update, const.INTENT_START())


@send_typing_action
def unmapped_words(bot, update):
    handle_not_expected_case(bot, update)


@send_typing_action
def handle_not_expected_case(bot, update):
    update.message.reply_text("Please tap `/start` to start. ^^")


def handle_intent(bot, update, intentReplies):
    for intentReply in intentReplies:
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        update.message.reply_text(intentReply)


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
