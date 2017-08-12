
# -*- coding: 850 -*-
import sys
import time
import telepot
from gui import *
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
profesorRequest = False 
profesorNombre = 'Fulanito'
class BotMentorStarter(telepot.helper.ChatHandler):
	def __init__(self, *args, **kwargs):
		super(BotMentorStarter, self).__init__(*args, **kwargs)
		
	def on_chat_message(self, msg):
		if msg['text'] == '/start':
			content_type, chat_type, chat_id = telepot.glance(msg)
			self.sender.sendMessage('Hola!!\nEste bot te sirve para consultar información sobre Tutorias, horarios, profesores y mucho más.\nPulsa "Consultar" para comenzar a utilizar el BotMentor de la Facultad de informática de la UCM',
			reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                    InlineKeyboardButton(text='Consultar', callback_data='menu'),]]
			)
		)
		elif profesorRequest:
			global profesorNombre
			profesorNombre = msg['text']
			print(profesorNombre)
			self.sender.sendMessage('Espera mientras busco a ' + profesorNombre + ' en mi base de datos')

class Alumno:
	def __init__(self):
		curso = 1
		grado = 'II'
		grupo = 'A'
	def parseGrado(g):
		if g == 'Informática': grado = 'II'
		elif g == 'Software': grado = 'IS'
		elif g == 'Máster': grado = 'MI'
		elif g == 'Computadores': grado = 'IC'
		elif g == 'Videojuegos': grado = 'DV'

	def parseGrupo(g):
		grupo = g.upper()

class BotMentor(telepot.helper.ChatHandler):

	def __init__(self,*args, **kwargs):
		super(BotMentor, self).__init__(*args, **kwargs)
		self.al = Alumno()

	def on_chat_message(msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		texto = msg['text']
		if texto == '/menu':
			global seleccionC, seleccionG, seleccionGr
			seleccionC = False
			seleccionG = False
			seleccionGr = False
			bot.sendMessage(chat_id, 'Menú principal:\n ¿Qué quieres saber?',
			reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Horarios"), KeyboardButton(text="Tutorías")],
				[KeyboardButton(text="Profesores"), KeyboardButton(text="Clases")],
				[KeyboardButton(text="Fichas docentes")]]))
		


	def on_callback_query(self, msg):
		query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
			
		if query_data == 'menu':
			keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Horarios', callback_data='horarios'),	InlineKeyboardButton(text='Tutorias', callback_data='tutorias')],	[InlineKeyboardButton(text='Profesores', callback_data='profesores'),InlineKeyboardButton(text='Clases', callback_data='clases')],	[InlineKeyboardButton(text='Fichas docentes', callback_data='fichas')],
			])
			bot.sendMessage(from_id, "Seleccione la opción deseada:", reply_markup=keyboard)
		elif query_data == 'horarios':
			horarios(from_id, bot)
		elif query_data == 'fichas':
			fichas(from_id, bot)
		elif query_data == 'profesores':
			global profesorRequest
			profesorRequest = True
			profesores(from_id, bot)
		elif query_data == 'clases':
			clases(from_id, bot)			
	def on_idle(self, event):
		self.editor.editMessageText(text + '\n\nThis message will disappear in 5 seconds to test deleteMessage',reply_markup=None)
		time.sleep(5)
		self.editor.deleteMessage()
		self.close()
	"""
		casos = {'hClase':hClase, 'hCurso':hCurso,'profesores':profesores, 'clases':clases, 'fichas':fichas}
		query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
		casos[query_data](int(from_id),msg)
		text = str(casos[query_data])
		bot.answerCallbackQuery(query_id, text)
"""

TOKEN = "423194965:AAFJtn4HcgYQmR0oN6WoSAEHZljARFlBSeI"

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, BotMentorStarter, timeout=60),
    pave_event_space()(
        per_callback_query_origin(), create_open, BotMentor, timeout=300),
])

MessageLoop(bot).run_as_thread()
print('Listening ...')


# Keep the program running.
while 1:
	time.sleep(10)