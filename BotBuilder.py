import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "UserProject.settings"
django.setup()

from NewBotHandler import ConfigureBot
from botmanager.views import SaveNewBot, SaveNewBotManager

from tokens import bnb
import logging
from telegram.update import Update
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, InvalidCallbackData
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ParseMode
from urllib.parse import quote_plus
import telegram
import requests
import threading as th
import json
import subprocess

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
bot = telegram.Bot(bnb)


def start(update: Update, context: CallbackContext) -> None:
    username = update['message']['chat']['first_name']

    reply_markup = InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton('Accept', callback_data='accept')]
    )
    update.message.reply_text(
        f""" Hi, {username}.
Please accept our Terms of Service and Privacy Policy before using Beyond Native

Terms of Service Link - https://demo_link/TermsOfService
Privacy policy Link - https://demo_link/PrivacyPolicy
        """,
        reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def create_bot(update: Update, context: CallbackContext) -> None:
    msg = """Please Follow the @BotFather instructions to  create a newbot provide us the <b>API key</b> ! <u>Don't Share with anyone else </u>
Please paste the API Token here to create a bot.
    """
    url = "https://t.me/TalentNativeBot"
    reply_markup = InlineKeyboardMarkup.from_column(
        [
            InlineKeyboardButton('Create Bussiness Bot',
                                 callback_data='create_bot'),
            InlineKeyboardButton('Talent Labs', url=url)
        ]
    )
    update.message.reply_text(
        msg, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


def runNewBot(script_name):
    subprocess.Popen(['python3', script_name])


def prepareBot(update: Update, context: CallbackContext):
    owner = update['message']['chat']['first_name']
    text = update.message.text
    msg = ""
    if text.lower() == 'allow':
        msg = "Thanks for accepting our Terms Of Service & Privacy Policy."
        bot.sendMessage(chat_id=update.effective_chat.id, text=msg)
        msg = "Please Follow the @BotFather instructions to  create a newbot provide us the <b>API key</b> ! <u> Don't Share with anyone else </u>  "
    elif ':' in text:
        token = text
        crr_token = text
        text = text.split(':')

        if len(text[0]) == 10:
            print("Inside Bot Creation\n")
            botURL = f'https://api.telegram.org/bot{crr_token}/getMe'

            botObj = requests.get(botURL).json()
            botObjStatus = botObj['ok']
            botObjResult = botObj['result']

            first_name = botObjResult['first_name']
            username = botObjResult['username']
            print(first_name, username)

            SaveNewBot(username, owner)
            SaveNewBotManager(owner, username)

            get_new_bot_script = ConfigureBot(token, username)
            # print(get_new_bot_script)
            script_name = f'auto_generated_bot_{token[:5]}.py'
            file = open(script_name, "w")
            file.write(get_new_bot_script)
            file.close()

            CrrnewBot = th.Thread(target=runNewBot, args=(script_name,))
            CrrnewBot.start()

            msg = f"""The Beyond Native Powered Business Chatbot is now Live

Here is your Bot Link :
@{username} (within telegram) or 
https://t.me/{username} (for External Usage)
Here is your digital identitiy link:
http://localhost:8000/botmanager/{owner}
            """
            talentlab_url = "https://t.me/TalentNativeBot"
            workspace_url = "http://127.0.0.1:8000/"
            profile_url = f"http://127.0.0.1:8000/"
            reply_markup = InlineKeyboardMarkup.from_column(
                [
                    InlineKeyboardButton(
                        'Create Bussiness Bot', callback_data='create_bot'),
                    InlineKeyboardButton('Talent Labs', url=talentlab_url),
                    InlineKeyboardButton('Your Workspace', url=workspace_url),
                    InlineKeyboardButton('Your Profile', url=profile_url),
                ]
            )

            update.message.reply_text(
                msg, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
            return
        else:
            print("\n\n\nIn else\n\n\n")
            msg = f"The API token was provided <b>is not valid</b> anymore please check any typo or try create another bot"

    elif text.lower() == 'deny':
        msg = f"Okay ! Thanks for your time! bye, bye :-"

    else:
        print("\n\n\nUnknown\n\n\n")
        msg = f"Sorry! The API token format is not a recognized! "

    update.message.reply_text(msg, parse_mode=ParseMode.HTML)


def list_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data

    reply_markup = ''

    if (data == "accept"):
        msg = "Thanks for accepting our Terms Of Service & Privacy Policy."
        url = "https://t.me/TalentNativeBot"
        reply_markup = InlineKeyboardMarkup.from_column(
            [
                InlineKeyboardButton('Create Bussiness Bot',
                                     callback_data='create_bot'),
                InlineKeyboardButton('Talent Labs', url=url)
            ]
        )
        query.edit_message_text(
            text=msg,
            reply_markup=reply_markup
        )
    if (data == "create_bot"):
        msg = """Please Follow the @BotFather instructions to  create a newbot provide us the <b>API key</b> ! <u>Don't Share with anyone else </u>

Please paste the API Token here to create a bot.
    """
        url = "https://t.me/TalentNativeBot"
        query.edit_message_text(msg, parse_mode=ParseMode.HTML)


def handle_invalid_button(update: Update, context: CallbackContext) -> None:
    """Informs the user that the button is no longer available."""
    update.callback_query.answer()
    update.effective_message.edit_text(
        'Sorry, I could not process this button click 😕 Please send /start to get a new keyboard.'
    )


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(bnb)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('create_bot', create_bot))

    updater.dispatcher.add_handler(
        CallbackQueryHandler(handle_invalid_button,
                             pattern=InvalidCallbackData)
    )
    updater.dispatcher.add_handler(CallbackQueryHandler(list_button))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, prepareBot))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


"""
http://BeyondNative/dashboard/bot_id/YourWork
https://BeyondNative/dashboard/user/{owner}
newlyCreatedBot = telegram.Bot(token)
botD = json.loads(botObj)
botObj = newlyCreatedBot.get_me()
print(botD, type(botD))
print(bot_json_object)
requests.post()
print(botObj)
print(botURL)
chat_id = bot.get_updates()[-1].update_id
bot.send_message(chat_id=update.effective_chat.id, text='API key collected ... ')
bot.send_message(chat_id=update.effective_chat.id, text='Initilizing Bot ... ')
bot.send_message(chat_id=update.effective_chat.id, text=f'Bot Name is <b>{first_name}</b>', parse_mode=ParseMode.HTML)
bot.send_message(chat_id=update.effective_chat.id, text=botObj)
myinsm = "To create a bot please follow the tutorial...(wait a miniute uploading a video)"
vid='https://www.youtube.com/shorts/3povjMEya8Y'
bot.sendMessage(chat_id=update.effective_chat.id, text=myinsm)
bot.sendVideo(update.effective_chat.id, open('BotFatherNewBotlow.mp4', 'rb'), supports_streaming=True)
"""
