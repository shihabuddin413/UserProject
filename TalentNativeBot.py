import telegram
from urllib.parse import quote_plus
from telegram import ParseMode
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, InvalidCallbackData
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.update import Update
import logging
from tokens import tlb
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "UserProject.settings"
django.setup()


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
bot = telegram.Bot(tlb)


def start(update: Update, context: CallbackContext) -> None:
    username = update['message']['chat']['first_name']

    payment_url = 'https://shihabuddin413.github.io/talentnative/'
    create_add_url = f'https:/domain/username/new'

    reply_markup = InlineKeyboardMarkup.from_column(
        [
            InlineKeyboardButton('See Pricing and plans',
                                 web_app=telegram.WebAppInfo(payment_url)),
            InlineKeyboardButton('Create New Add',
                                 web_app=telegram.WebAppInfo(create_add_url))
        ]
    )

    update.message.reply_text(
        f""" Hi! {username}, Here you can add different types of Job ads for your users.""", reply_markup=reply_markup)


def otherText(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I don't understand what you are talking about")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(tlb)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, otherText))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
