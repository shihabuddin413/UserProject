import glob

import subprocess


def ConfigureBot(token, botname):
    return f"""
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "UserProject.settings"
django.setup()

from allusers.views import SaveUser
from botmanager.views import AdModel, BotModel

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
import json


token = '{token}'

thisBot = '{botname}'
mybot = telegram.Bot(token)

def strToArray(string):
    if (string == '[]' or string == 'None' or string.strip() == ''):
        return []
    str_array = string
    str_array = str_array.replace('[', '')
    str_array = str_array.replace(']', '')
    str_array = str_array.strip()
    num_str_list = str_array.split(',')
    num_int_list = []
    for i in num_str_list:
        num_int_list.append(int(i))
    return num_int_list

def job_search():
	crrBot = BotModel.objects.filter(botName=thisBot)
	crrBotManagerName = crrBot[0].botManagerName
	crrManager = BotManager.objects.filter(name=crrBotManagerName)
	ads = strToArray(crrManager[0].ManagerAdsIds)
	data = []
	job_sum = ''
	for job_id in ads:
		crrAd = AdModel.objects.filter(job_id=job_id)
		this_job = crrAd[0]
		job_sum ='''
			job matched
			title: %s
			location: %s
			salary: %s
			work time: %s
			link: https://bnb/job/%s/%s
		''' % ( this_job.job_title, this_job.job_location, this_job.max_salary, this_job.working_hours, crrBotManagerName, job_id )
		data.append(job_sum)
		
	return data




print ('Another Bot Started ... {botname}:{token}')
updater = Updater(token, use_context=True)
def start(update: Update, context: CallbackContext):
	username = update['message']['chat']['first_name']
    SaveUser(username)
	job_url = "https://google.com"
	profile_url = ""
	reply_markup = InlineKeyboardMarkup.from_column( [
		InlineKeyboardButton('Apply Now', url=job_url),
		InlineKeyboardButton('View Details', url=job_url),
		InlineKeyboardButton('Your profile', url=profile_url),
		InlineKeyboardButton('Job Search', callback_data='search')
	])
	
	data = job_search()
	for job in data :
		mybot.send_message(chat_id=update.effective_chat.id, text=job)

	update.message.reply_text("%s" % (data), reply_markup=reply_markup)

def btnCommand (update: Update, context: CallbackContext):
	query = update.callback_query
    query.answer()
    data = query.data
	job_matched = ''                       
	if (data == 'search'):
		data = job_search()
		for job in data :
			mybot.send_message(chat_id=update.effective_chat.id, text=job)

	reply_markup = InlineKeyboardMarkup.from_column( [
		InlineKeyboardButton('Apply Now', url=job_url),
		InlineKeyboardButton('View Details', url=job_url),
		InlineKeyboardButton('Your profile', url=profile_url),
		InlineKeyboardButton('Job Search', callback_data='search')
	])
	
	update.message.reply_text("%s" % (job_matched), reply_markup=reply_markup)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(btnCommand))
print("Starting polling...")
updater.start_polling()
"""


def activateAllBots(new_bot_name):
    bots = glob.glob("./bots/*.py")
    for i in bots:
        if (i == "main.py"):
            print("This bot is not intend for schedule...")
        else:
            subprocess.Popen(['python', i])


def activateNewBot(new_bot_name):
    print(f"Starting bot --> {new_bot_name}")
    subprocess.Popen(['python', new_bot_name])


# def bot_thread(token, command_plus_replies={"test": "This is a test command", "done": "fine then bye", "take care": "Thanks ! have a nice day", "baby": "Oh! so adorable"}):
# 	botName = "Beyond Native Bot"
# 	token = '{token}'
# 	print ('Another Bot Started ... {token}')
# 	updater = Updater(token, use_context=True)

# 	def handleReplies (update: Update, context: CallbackContext):
# 		for cmd, reply in command_plus_replies.items():
# 			if (update.message.text == '{cmd}' ):
# 				msg='{reply}'
# 				update.message.reply_text(msg)

# 	def start(update: Update, context: CallbackContext):
# 		update.message.reply_text('Hi, welcome to our service !')

# 	updater.dispatcher.add_handler(CommandHandler('start', start))
# 	updater.dispatcher.add_handler(MessageHandler(Filters.text, handleReplies))
# 	print("Starting polling...")
# 	updater.start_polling()\


# #search for job
# job_matched ='''
# Job Matched Waiter/waitress
# $10 per hour
# 165 tanjing road
# # 22 october 5.00pm-11:00 pm'''
