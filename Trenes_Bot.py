# -*- coding: utf-8 -*-
import requests #Libreria para hacer request a API
import json
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from wand.image import Image

TOKEN = '112090512:AAFIcT-bEUgl6Bsw1kC20EgqSuDvRbhynR8' # Nuestro tokken del bot (el que @BotFather nos dió).
API_URL = 'http://trenes.mininterior.gov.ar/apps/api_tiempos_temp.php' # URL del web service, de donde obtenemos los datos

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
 
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

    
# def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
#     for m in messages: # Por cada dato 'm' en el dato 'messages'
#         cid = m.chat.id # Almacenaremos el ID de la conversación.
#         print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
     
        
#         if m.text == "/tarifaRosario":
            
            
#         if m.text != "/trendelacosta" and  m.text != "/tarifaRosario" and m.text != "/sanmartin" and  m.text != "/roca" and  m.text != "/mitre" and  m.text != "/sarmiento" and  m.text != "/start" and m.text != "/about" and m.text != "/help":
#             bot.send_message(cid, "El comando no es valido :( . Podes ingresar /trendelacosta, /sanmartin, /roca, /mitre, /sarmiento, /buenosairesrosarioTarifa")
 
# bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
 
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.