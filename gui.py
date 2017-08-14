
# -*- coding: 850 -*-
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def horarios(id, bot):
	text = 'horarios'
	keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Horarios curso', callback_data='hCurso'),InlineKeyboardButton(text='Horarios clase', callback_data='hClase')]])
	bot.sendMessage(id, "¿Qué horarios quiere ver?:",reply_markup=keyboard)
def fichas(id, bot):
	keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Fichas docentes de curso', callback_data='fCurso'),InlineKeyboardButton(text='Ficha docente de asignatura', callback_data='fAsignatura')]])
	bot.sendMessage(id, "¿Qué Fichas docentes quiere ver?:", reply_markup=keyboard)
def profesores(id,bot):
	bot.sendMessage(id, "¿De qué profesor quieres saber?:")
def clases(id,bot):
	bot.sendMessage(id, "¿Cúal es la clase sobre la que quieres información?:")
		

def seleccionGrado(id, bot):
	keyboard=[[KeyboardButton(text='Informática'),KeyboardButton(text='Software'),KeyboardButton(text='Computadores')],[KeyboardButton(text='Videojuegos'),KeyboardButton(text='Máster'),KeyboardButton(text='Optativas')]]
	bot.sendMessage(id, "Selecciona la titulación:", reply_markup=keyboard)

def seleccionCurso(id,msg, bot, grado):
	if grado == 'Máster': max=1
	elif grado == 'Videojuegos': max=3
	elif grado == 'Optativas': max=1
	else: max=4
	cursos=[[KeyboardButton(text='1', callback_data='1')]]
	for i in range(2,max):
		cursos.append([KeyboardButton(text=str(i), callback_data=str(i))])
	keyboard2 = KeyboardMarkup(keyboard=cursos)

	bot.sendMessage(id, "Selecciona el curso:", reply_markup=keyboard2)

def seleccionGrupo(id,msg, bot):
	keyboard=[[KeyboardButton(text='Informática'),KeyboardButton(text='Software'),KeyboardButton(text='Computadores')],[KeyboardButton(text='Videojuegos'),KeyboardButton(text='Master'),KeyboardButton(text='Optativas')]]
	bot.sendMessage(id, "Selecciona la titulación:", reply_markup=keyboard2)
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	
	"""
	keyboard2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Informática', callback_data='II'),InlineKeyboardButton(text='Software', callback_data='IS'),InlineKeyboardButton(text='Computadores', callback_data='IC')],[InlineKeyboardButton(text='Videojuegos', callback_data='DV'),InlineKeyboardButton(text='Master', callback_data='MII'),InlineKeyboardButton(text='Optativas', callback_data='OP')]])
	bot.sendMessage(id, "Selecciona la titulación:", reply_markup=keyboard2)
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
"""

	
