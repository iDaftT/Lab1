import telebot
from telebot import types
import random
import datetime
now = datetime.datetime.now()

# Создаем экземпляр бота
bot = telebot.TeleBot('5106108075:AAHTg8xDHFuQCh43My-A_I3u4QbZEkHUKAc')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
# Обработка клавиатуры
    keyboard.row("/unv", "/time", "/rnd")
# Стартовое сообщение
    bot.send_message(message.chat.id, 'Добро пожаловать в IDPY! Выберите команду (для описания команд, воспользуйтесь командой /help):', reply_markup=keyboard)
# Обработка команд
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Список команд: \n 1. /unv - подробности о МТУСИ \n 2. /time - Показать время, когда был запущен бот  \n 3. /rnd - Случайное число от 1 до 6')
@bot.message_handler(commands=['unv'])
def start_message(message):
    bot.send_message(message.chat.id, 'Подробности можно узнать здесь – https://mtuci.ru/')
@bot.message_handler(commands=['time'])
def start_message(message):
    bot.send_message(message.chat.id, now.strftime("%d-%m-%Y %H:%M"))
@bot.message_handler(commands=['rnd'])
def start_message(message):
    bot.send_message(message.chat.id, random.randint(1, 6))
# Обработка текста
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет, пользователь!')
    if message.text.lower() == "как дела":
        bot.send_message(message.chat.id, 'Лучше не бывает!')
    if message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'Уже уходите?')
# Цикл для постоянной работы
bot.polling(none_stop=True, interval=0)