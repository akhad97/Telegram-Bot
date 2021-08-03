import telebot
from django.http import HttpResponse
from .models import *
# from telebot import types
import telebot


bot = telebot.TeleBot("1687659313:AAER6qBD__aw9LPMQJolvSp_4WNzPZVhzn0")
HOST = ""
bot.set_webhook(url="https://uzvacancybot.herokuapp.com/")



# ===========================WEBHOOK=======================

def webhook(request):
    if request.method == 'POST':
        json_string = request.body.decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return HttpResponse(status=200)
    return HttpResponse("BOT IS LIVE HERE")

    
@bot.message_handler(commands=['start'])
def start(message):
    user = get_user(message)
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # item_1 = types.KeyboardButton('Python')
    # item_2 = types.KeyboardButton('PHP')
    # item_4 = types.KeyboardButton('C#')
    # item_5 = types.KeyboardButton('JavaScript')
    items = ['Python', 'PHP', 'C#', 'JavaScript']

    markup_inline.add(*[types.KeyboardButton(item) for item in items])
    bot.send_message(message.chat.id, 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced'
    'below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are'
    'also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham. /start\n\n'
        'Are you a developer ?', reply_markup=markup_inline)
        

@bot.message_handler(content_types=['text'])
def answer(message):
    print('answer')
    user = TelegramUser.objects.get(user_id=message.chat.id)
    vacancy = Vacancy.objects.get(name__icontains=message.text)
    if vacancy:
        post = Post.objects.create(user=user, vacancy=vacancy)
        if  message.text == 'Python':
            markup  = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, 'Full Name:', reply_markup=markup)
        elif message.text == 'PHP':
            markup  = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, 'Full Name:', reply_markup=markup)
        elif message.text == 'C#':
            markup  = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, 'Full Name:', reply_markup=markup)
        elif message.text == 'JavaScript':
            markup  = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, 'Full Name:', reply_markup=markup)
        bot.register_next_step_handler(message, get_info)
        

@bot.message_handler(content_types=['text'])
def get_info(message):
    user = TelegramUser.objects.get(user_id=message.chat.id)
    try:
        chat_id = message.chat.id
        full_name = message.text
        if full_name.isdigit():
            bot.reply_to(message, 'wrong!!!')
            bot.register_next_step_handler(message, get_info)
            return
        user.full_name = full_name
        user.save()
    except Exception as e:
        pass

    bot.send_message(message.chat.id, 'Phone number:')
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_number = types.KeyboardButton('Share my number', request_contact=True)
    markup_inline.add(contact_number)
    bot.send_message(message.chat.id, 'Type your number or share your contact', reply_markup=markup_inline)
    bot.register_next_step_handler(message,  user_resume)
    

@bot.message_handler(content_types=['text'])
def user_resume(message):
    user = TelegramUser.objects.get(user_id=message.chat.id)
   
    if message.text is None:
        phone = message.contact.phone_number
        user.phone_number = phone
        user.save()
    else:
        phone_number = message.text
        user.phone_number = phone_number
        user.save()
    try:
        chat_id = message.chat.id
        phone_number = message.text
        if not phone_number.isdigit():
            bot.reply_to(message, 'phone number should be numeric \n example:  972558899')
            bot.register_next_step_handler(message, user_resume)
            return
        user.phone_number = phone_number
        user.save()
    except Exception as e:
        pass
    

    markup  = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Please send your resume!', reply_markup=markup)
    bot.register_next_step_handler(message,  info_end)
   


@bot.message_handler(content_types=['document'])
def info_end(message):
    try:
        if message.content_type == 'document':
            user = TelegramUser.objects.get(user_id=message.chat.id)
            
            user.resume = message.document.file_id
            user.save()
            bot.send_message(message.chat.id, 'Thank you, soon we will contact you') 
        else:
            bot.send_message(message.chat.id, 'send only file pls!')
            bot.register_next_step_handler(message, info_end) 
    except Exception as e:
        pass    
   

def get_user(message):
    user = TelegramUser.objects.filter(user_id=message.chat.id).first()
    if not user:
        user = TelegramUser.objects.create(user_id=message.chat.id)
    return user

