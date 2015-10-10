# -*- coding: utf-8 -*-
import requests 
import json
import telebot 
from telebot import types
import time 

TOKEN = '112090512:AAFIcT-bEUgl6Bsw1kC20EgqSuDvRbhynR8' 
API_URL = 'http://trenes.mininterior.gov.ar/apps/api_tiempos_temp.php' 

bot = telebot.TeleBot(TOKEN) 
 
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Hola, en que te puedo ayudar?") 
 
@bot.message_handler(commands=['sarmiento'])
def sarmiento(m):
    paramsRequest = {'ramal': '1'}
    data = requests.get(API_URL, params=paramsRequest).json()
    response = "Sale a las: " + data['salidas'][0]['min'] + " Estado: " + data['salidas'][0]['estado'] 
    bot.send_message(m.chat.id, response)

@bot.message_handler(commands=['mitre'])
def mitre(m):
    paramsRequest = {'ramal': '5'}
    data = requests.get(API_URL, params=paramsRequest).json()
    response = "Sale a las: " + data['salidas'][0]['min'] + " Estado: " + data['salidas'][0]['estado'] 
    bot.send_message(m.chat.id, response)

@bot.message_handler(commands=['sanmartin'])
def sanmartin(m):
    paramsRequest = {'ramal': '31'}
    data = requests.get(API_URL, params=paramsRequest).json()
    response = "Sale a las: " + data['salidas'][0]['min'] + " Estado: " + data['salidas'][0]['estado'] 
    bot.send_message(m.chat.id, response)
 
@bot.message_handler(commands=['trendelacosta'])
def trendelacosta(m):
    paramsRequest = {'ramal': '41'}
    data = requests.get(API_URL, params=paramsRequest).json()
    response = "Sale a las: " + data['salidas'][0]['min'] + " Estado: " + data['salidas'][0]['estado'] 
    bot.send_message(m.chat.id, response)

@bot.message_handler(commands=['roca'])
def roca(m):
    response = "Fuera de Servicio por obras de electrificación. Estamos mejorando el servicio para vos :)" 
    bot.send_message(m.chat.id, response) 
    
@bot.message_handler(commands=['tarifaRosario'])
def tarifaRosario(m):
    photo = open('horarios.jpg', 'rb')
    bot.send_message(m.chat.id, "Esta es la tarifa Buenos Aires - Rosario")
    bot.send_photo(m.chat.id, photo)

bot.polling(none_stop=True)