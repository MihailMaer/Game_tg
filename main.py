import telebot
from telebot import types # для указание типов
import sqlite3
import random
import time

bot = telebot.TeleBot('7044598513:AAEveGXsJfYPk6RuGc6Iuzax2g2iD2x2Bqg')







def locations_command(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i = types.InlineKeyboardButton('Корчма', callback_data='saloon')
    i2 = types.InlineKeyboardButton('Город', callback_data='city')
    markup.add(i, i2)
    bot.send_message(message.chat.id, 'Выберете начальную локацию: ', reply_markup=markup)

    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("yep")
    button2 = types.KeyboardButton("nope")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! готов".format(message.from_user), reply_markup=markup)


#Функция для возврата к описанию героев
def back(message):
    back = types.ReplyKeyboardMarkup(resize_keyboard=True)
    backbtn = types.KeyboardButton("🧙‍♂️Маг🧙‍♂️")
    backbtn1 = types.KeyboardButton("⚔️Воин⚔️")
    back.add(backbtn, backbtn1)
    bot.send_message(message.chat.id, text="Вернуться к описнию?".format(message.from_user), reply_markup=back)
#Выбор героя
def choise(message):
    character = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton("🧙‍♂️Маг🧙‍♂️")
    #btn4 = types.KeyboardButton("⚔️Воин⚔️")
    character.add(btn3) #btn4)
    bot.send_message(message.chat.id, text="{0.first_name}! Выбери класс персонажа".format(message.from_user), reply_markup=character)

#Описание мага
def magic_Super(message): 
    bot.send_message(message.chat.id, text="Ваш персонаж 🧙‍♂️Маг🧙‍♂️")
    magic = types.ReplyKeyboardMarkup(resize_keyboard=True)
    magbtn1 = types.KeyboardButton("История 🧙‍♂️Мага🧙‍♂️")     
    magbtn2 = types.KeyboardButton("Характеристики\n 🧙‍♂️Мага🧙‍♂️")
    back = types.KeyboardButton("Выбрать другого персонажа")   
    magic.add(magbtn1, magbtn2, back)
    bot.send_message(message.chat.id, text="Узнайте своего персонажа по ближе".format(message.from_user), reply_markup=magic)
#Описание война
def voin_Super(message):
    bot.send_message(message.chat.id, text="Ваш персонаж ⚔️Воин⚔️")
    voin = types.ReplyKeyboardMarkup(resize_keyboard=True)
    voinbtn1 = types.KeyboardButton("История ⚔️Воина⚔️")     
    voinbtn2 = types.KeyboardButton("Характеристики\n ⚔️Воина⚔️")
    back = types.KeyboardButton("Выбрать другого персонажа")   
    voin.add(voinbtn1, voinbtn2, back)
    bot.send_message(message.chat.id, text="Узнайте своего персонажа по ближе".format(message.from_user), reply_markup=voin)


#Характеристики мага
def Mag_haracteristic(message):
    bot.send_message(message.chat.id, text="Характеристики: \n ❤️хп: 3 \n 💀урон: \n 🔥огнем: 5 \n ⚡️молнией: 2 \n Шанс крита: 20%".format(message.from_user))    
#Характеристики война
def Voin_haracteristic(message):
    bot.send_message(message.chat.id, text="Характеристики: \n ❤️хп 5 \n 💀урон: \n 🗡кинжал 2 \n Шанс крита: 50% ".format(message.from_user))

#Справочник
def enemy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    en1 = types.KeyboardButton("Животные")
    en2 = types.KeyboardButton("Люди")
    en3 = types.KeyboardButton("Огры")
    en4 = types.KeyboardButton("Мертвецы")
    markup.add(en1, en2, en3, en4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Тут находится справочник с врагами".format(message.from_user), reply_markup=markup)
    
#Локации
def locations_command(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i = types.InlineKeyboardButton('🍻Трактир🍻', callback_data='saloon')
    i2 = types.InlineKeyboardButton('Город', callback_data='city')
    markup.add(i, i2)
    bot.send_message(message.chat.id, 'Выберете начальную локацию: ', reply_markup=markup)

def location(message):
    location = types.ReplyKeyboardMarkup(resize_keyboard=True)
    locbtn1 = types.KeyboardButton('🍻Трактир🍻')
    locbtn2 = types.KeyboardButton('🌲Лес🌲')
    location.add(locbtn1, locbtn2)
    bot.send_message(message.chat.id, text="Куда направитесь?".format(message.from_user), reply_markup=location)

#Вызов карты
def map(message):       
        if(message.text == "Открыть карту"):
            location(message)

#Локация трактир
def tractir(message):
        if(message.text == "🍻Трактир🍻"):
            tractirbtn = types.ReplyKeyboardMarkup(resize_keyboard=True)
            TractirBookBtn = types.KeyboardButton("Открыть справочник")
            TractirFightBtn = types.KeyboardButton("Устройте тренировочный бой с 🧛Вампиром🧛" )
            trakt1 = types.KeyboardButton('Подойти к барной стойке')
            trakt2 = types.KeyboardButton('Подойти к столу')
            map_tractir = types.KeyboardButton('Открыть карту')
            tractirbtn.add(trakt1, trakt2, TractirBookBtn, TractirFightBtn, map_tractir)
            bot.send_message(message.chat.id, text='Куда хочешь подойти?'.format(message.from_user), reply_markup=tractirbtn)

    
def back_en(message):
    back_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_en1 = types.KeyboardButton('Животные')
    back_en2 = types.KeyboardButton('Люди')
    back_en3 = types.KeyboardButton('Огры')
    back_en4 = types.KeyboardButton('Мертвецы')
    locbtn1 = types.KeyboardButton('🍻Трактир🍻')   
    back_en.add(back_en1, back_en2, back_en3, back_en4, locbtn1)
    bot.send_message(message.chat.id, text='Кто тебя интересует теперь?'.format(message.from_user),reply_markup=back_en)


#🌲Лес🌲
def forest(message):
    forest = types.ReplyKeyboardMarkup(resize_keyboard=True)
    forestbtn1 = types.KeyboardButton('🌼Луг🌼')
    forestbtn2 = types.KeyboardButton('⛺Лагерь⛺')
    forestbtn3 = types.KeyboardButton('Берлога')
    map_forest = types.KeyboardButton('Открыть карту')   
    forest.add(forestbtn1, forestbtn2, forestbtn3, map_forest)
    bot.send_message(message.chat.id, text='Вы вошли в лес'.format(message.from_user),reply_markup=forest)


@bot.message_handler(commands=['start']) #Дикоратар с функцией для начала игры
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("😎Конечно😎")
    btn2 = types.KeyboardButton("😢Пока нет😢")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Ты готов к приключениям?".format(message.from_user), reply_markup=markup)


    
    
@bot.message_handler(content_types=['text'])
def otvet(message): 
    if(message.text == "😎Конечно😎"):
       choise(message)
       
    elif(message.text == "🧙‍♂️Маг🧙‍♂️"):
        magic_Super(message)
    elif(message.text == "Характеристики\n 🧙‍♂️Мага🧙‍♂️"):
        Mag_haracteristic(message)
        travel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locationbtn1 = types.KeyboardButton("Открыть карту")
        back_map = types.KeyboardButton("Выбрать другого персонажа")
        travel.add(locationbtn1, back_map)
        bot.send_message(message.chat.id, text="Вы готовы отправиться в путишествие? ".format(message.from_user), reply_markup=travel)
    elif(message.text == "История 🧙‍♂️Мага🧙‍♂️"):
        bot.send_message(message.chat.id, text="Маг - Давным-давно один ученик был изгнан из коллегии волшебства. Но он не собирался сдаваться, ведь упорства у него было не занимать. За пару лет юноша смог многого достичь в школе магии. И теперь решил начать исследовать мир.".format(message.from_user))
        back(message)
    elif(message.text == "⚔️Воин⚔️"):
        voin_Super(message)
    elif(message.text == "Выбрать другого персонажа"):
        choise(message)
    elif(message.text == "История ⚔️Воина⚔️"):
        bot.send_message(message.chat.id, text="Воин – Он был обычным сыном кузнеца, не знавшим проблем. Как вдруг бандиты убили всю его семью. Много лет он сражался, чтобы найти их и отомстить. За то время, что парень искал главаря банды, его разум помутнел. Смерть главаря не стала концом в его истории, и он захотел славы.".format(message.from_user))
        back(message)
    elif(message.text == "Характеристики\n ⚔️Воина⚔️"):
        Voin_haracteristic(message)
        travel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locationbtn1 = types.KeyboardButton("Открыть карту")
        back_map = types.KeyboardButton("Выбрать другого персонажа")
        travel.add(locationbtn1, back_map)
        bot.send_message(message.chat.id, text="Вы готовы отправиться в путишествие? ".format(message.from_user), reply_markup=travel)
    elif(message.text == "Открыть карту"):
        map(message)
    elif(message.text == "😢Пока нет😢"):
        backk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("/start")
        backk.add(btn5)
        bot.send_message(message.chat.id, text="Возвращайся как будешь готов".format(message.from_user), reply_markup=backk)






    #Трактир
    elif(message.text == "🍻Трактир🍻"):
        tractir(message)
    elif(message.text == "Устройте тренировочный бой с 🧛Вампиром🧛"):
        bot.send_message(message.chat.id, text="Тренер: Чтож я не против сразиться с тобой".format(message.from_user))
        time.sleep(1)   
        fighting = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start_boy = types.KeyboardButton("бой")
        fighting.add(start_boy)
        bot.send_message(message.chat.id, text="Вы готовы?".format(message.from_user), reply_markup=fighting)
        
    elif(message.text == 'Подойти к барной стойке'):
        dialog = types.ReplyKeyboardMarkup(resize_keyboard=True)
        trakt1_1 = types.KeyboardButton('Трактирщик')
        trakt1_2 = types.KeyboardButton('Официантка')
        dialog.add(trakt1_1, trakt1_2)
        bot.send_message(message.chat.id, text='Ты подошел к барной стойке'.format(message.from_user), reply_markup=dialog)
    elif (message.text == 'Подойти к столу'):
        dialog = types.ReplyKeyboardMarkup(resize_keyboard=True)
        trakt2_1 = types.KeyboardButton('Заказать еду')
        trakt2_2 = types.KeyboardButton('Заказать выпивку')
        dialog.add(trakt2_1, trakt2_2)
        bot.send_message(message.chat.id, text='Ты подошел к столу'.format(message.from_user), reply_markup=dialog)
    elif(message.text == "Открыть справочник"):
        back_en(message)
    elif (message.text == 'Животные'):
        character_enemy = types.ReplyKeyboardMarkup(resize_keyboard=True)
        en1_1 = types.KeyboardButton('Волк')
        en1_2 = types.KeyboardButton('Собака')
        en1_3 = types.KeyboardButton('Медведь')
        en1_4 = types.KeyboardButton('Гиена')
        en1_5 = types.KeyboardButton('Вепрь')
        character_enemy.add(en1_1, en1_2, en1_3, en1_4, en1_5)
        bot.send_message(message.chat.id, text="Это все виды животных".format(message.from_user), reply_markup=character_enemy)
    elif (message.text == 'Люди'):
        character_enemy = types.ReplyKeyboardMarkup(resize_keyboard=True)
        en2_1 = types.KeyboardButton('Вампир')
        en2_2 = types.KeyboardButton('Высший вампир')
        en2_3 = types.KeyboardButton('Сектант')
        en2_4 = types.KeyboardButton('Бандит')
        en2_5 = types.KeyboardButton('Главарь бандитов')
        character_enemy.add(en2_1, en2_2, en2_3, en2_4, en2_5)
        bot.send_message(message.chat.id, text="Это все виды людей".format(message.from_user), reply_markup=character_enemy)
    elif (message.text == 'Огры'):
        character_enemy = types.ReplyKeyboardMarkup(resize_keyboard=True)
        en3_1 = types.KeyboardButton('Накер')
        en3_2 = types.KeyboardButton('Циклоп')
        en3_3 = types.KeyboardButton('Великан')
        en3_4 = types.KeyboardButton('Троль')
        en3_5 = types.KeyboardButton('Орк')
        character_enemy.add(en3_1, en3_2, en3_3, en3_4, en3_5)
        bot.send_message(message.chat.id, text="Это все виды огров".format(message.from_user), reply_markup=character_enemy)
    elif (message.text == 'Мертвецы'):
        character_enemy = types.ReplyKeyboardMarkup(resize_keyboard=True)
        en4_1 = types.KeyboardButton('Гуль')
        en4_2 = types.KeyboardButton('Утопец')
        en4_3 = types.KeyboardButton('Вурдалак')
        en4_4 = types.KeyboardButton('Скелет')
        en4_5 = types.KeyboardButton('Поганище')
        character_enemy.add(en4_1, en4_2, en4_3, en4_4, en4_5)
        bot.send_message(message.chat.id, text="Это все виды мертвецов".format(message.from_user), reply_markup=character_enemy)

    elif (message.text == 'Волк'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 3 \n 💀урон: 2 \n 💢Шанс крита: 15%')
        back_en(message)
    elif (message.text == 'Собака'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 2 \n 💀урон: 2 \n 💢Шанс крита: 10%')
        back_en(message)
    elif (message.text == 'Медведь'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 6 \n 💀урон: 2 \n 💢Шанс крита: 20%')
        back_en(message)
    elif (message.text == 'Гиена'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 4 \n 💀урон: 2 \n 💢Шанс крита: 25%')
        back_en(message)
    elif (message.text == 'Вепрь'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 4 \n 💀урон: 1 \n 💢Шанс крита: 35%')
        back_en(message)

    elif (message.text == 'Вампир'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 6 \n 💀урон: 2 \n 💢Шанс крита: 25%')  
        back_en(message)  
    elif (message.text == 'Высший вампир'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 7 \n 💀урон: 3 \n 💢Шанс крита: 30%')
        back_en(message)
    elif (message.text == 'Сектант'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 4 \n 💀урон: 2 \n 💢Шанс крита: 40%')
        back_en(message)
    elif (message.text == 'Бандит'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 5 \n 💀урон: 3 \n 💢Шанс крита: 30%')
        back_en(message)
    elif (message.text == 'Главарь бандитов'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 9 \n 💀урон: 3 \n 💢Шанс крита: 35%')
        back_en(message)    

    elif (message.text == 'Накер'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 5 \n 💀урон: 2 \n 💢Шанс крита: 10%')
        back_en(message)
    elif (message.text == 'Циклоп'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 11 \n 💀урон: 4 \n 💢Шанс крита: 30%')
        back_en(message)
    elif (message.text == 'Великан'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 13 \n 💀урон: 5 \n 💢Шанс крита: 35%')
        back_en(message)
    elif (message.text == 'Троль'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 8 \n 💀урон: 4 \n 💢Шанс крита: 30%')
        back_en(message)
    elif (message.text == 'Орк'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 9 \n 💀урон: 3 \n 💢Шанс крита: 25%')
        back_en(message)   

    elif (message.text == 'Гуль'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 8 \n 💀урон: 1 \n 💢Шанс крита: 45%')
        back_en(message)
    elif (message.text == 'Утопец'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 8 \n 💀урон: 3 \n 💢Шанс крита: 30%')
        back_en(message)
    elif (message.text == 'Вурдалак'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 9 \n 💀урон: 2 \n 💢Шанс крита: 25%')
        back_en(message)
    elif (message.text == 'Скелет'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 6 \n 💀урон: 4 \n 💢Шанс крита: 40%')
        back_en(message)
    elif (message.text == 'Поганище'):
        bot.send_message(message.chat.id, text = 'Характеристики: \n ❤️хп: 14 \n 💀урон: 3 \n 💢Шанс крита: 40%')
        back_en(message)   
    
    
    elif (message.text == 'бой'):
        fight(message)
    elif message.text == '⚡Молния⚡':
        attack(message)
    elif message.text == '🔥Огонь🔥':
        fire(message)
    
    #Лес
    elif (message.text == '🌲Лес🌲'):
        forest(message)


user_health = 100
enemy_health = 100


@bot.message_handler(commands=['бой'])
def fight(message):
    global sent
    ydar = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('⚡Молния⚡')
    item2 = types.KeyboardButton('🔥Огонь🔥')
    ydar.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите удар", reply_markup=ydar)
    
    
@bot.message_handler(commands=['⚡Молния⚡'])
def attack(message):
    time.sleep(2)
    global user_health, enemy_health
    user = random.randint(1, 10)
    enem = random.randint(5, 5)
    if enem <= 5:
        enemy_damage = 5
        test = random.randint(1, 1)
        if test == 1:
            bot.send_message(message.chat.id, text="fsdgdg".format(message.from_user))
        enem = enemy_damage
        user_health -= enemy_damage
        bot.reply_to(message, text="Тренер нанес обычный удар")
        time.sleep(1)
    elif enem == 6:
        enemy_health
        enemy_damage = 2 
        enem = enemy_damage
        heal_amount = random.randint(10, 20)
        enemy_health += heal_amount
        user_health -= enemy_damage
        bot.send_message(message.chat.id, text=f"Тренер восстоновил {heal_amount} здоровья. У Тренера {enemy_health} здоровья.".format(message.from_user))
        time.sleep(1)
    elif enem == 7:
        user_health, enemy_health
        blood = random.randint(15, 20)
        enemy_damage = blood
        user_health -= blood
        enemy_health += blood
        bot.send_message(message.chat.id, text=f"Тренер забрал у вас {blood} здоровья. У Тренера {enemy_health} здоровья.".format(message.from_user))
        time.sleep(1)
    else:
        enemy_damage = 7
        enem = enemy_damage
        user_health -= enemy_damage
        bot.reply_to(message, text="Тренер нанес критический удар")
        time.sleep(1)

    if user <= 5:
        user_damage = 10
        bot.reply_to(message, text="Вы наносите критический удар".format(message.from_user))
        time.sleep(1)
        enemy_damage = random.randint(5,8)

        enemy_health -= user_damage
        user_health -= enemy_damage
        bot.reply_to(message, f" Вы нанесли 💥 {user_damage} 💥 урона. \n У вас осталось ❤️ {user_health} ❤️здоровья. \n "
                        f" Противник нанес 💥 {enemy_damage} 💥 урона. \n У него осталось ❤️ {enemy_health} ❤️ здоровья. ")
    elif user > 6:
        user_damage = 5
        bot.reply_to(message, text="Вы наносите обычный удар".format(message.from_user))
        time.sleep(1)
        enemy_damage = random.randint(5,8)

        enemy_health -= user_damage
        user_health -= enemy_damage


        bot.reply_to(message, f" Вы нанесли 💥 {user_damage} 💥 урона. \n У вас осталось ❤️ {user_health} ❤️здоровья. \n "
                        f" Противник нанес 💥 {enemy_damage} 💥 урона. \n У него осталось ❤️ {enemy_health} ❤️ здоровья. ")
    

    if user_health <= 0:
        bot.reply_to(message, "Вы проиграли!")
        user_health = 100
        enemy_health = 100
        location = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locbtn1 = types.KeyboardButton('🍻Трактир🍻')
        location.add(locbtn1)
        bot.send_message(message.chat.id, text="Куда направитесь?".format(message.from_user), reply_markup=location)
        
    elif enemy_health <= 0:
        bot.reply_to(message, "Вы победили! \n ")
        user_health = 100
        enemy_health = 100
        location = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locbtn1 = types.KeyboardButton('🍻Трактир🍻')
        location.add(locbtn1)
        bot.send_message(message.chat.id, text="Куда направитесь?".format(message.from_user), reply_markup=location)
        
@bot.message_handler(commands=['🔥Огонь🔥'])
def fire(message):
    time.sleep(1)
    global user_health, enemy_health
    user = random.randint(1, 10)
    enem = random.randint (1, 10)
    if enem <= 5:
        enemy_damage = 5
        enem = enemy_damage
        user_health -= enemy_damage
        bot.reply_to(message, text="Тренер нанес обычный удар")
        time.sleep(1)
    elif enem == 6:
        enemy_health
        enemy_damage = 2 
        enem = enemy_damage
        heal_amount = random.randint(10, 20)
        enemy_health += heal_amount
        user_health -= enemy_damage
        bot.send_message(message.chat.id, text=f"Тренер восстоновил {heal_amount} здоровья. У Тренера {enemy_health} здоровья.".format(message.from_user))
        time.sleep(1)
    elif enem == 7:
        user_health, enemy_health
        blood = random.randint(15, 20)
        enemy_damage = blood
        user_health -= blood
        enemy_health += blood
        bot.send_message(message.chat.id, text=f"Тренер забрал у вас {blood} здоровья. У Тренера {enemy_health} здоровья.".format(message.from_user))
        time.sleep(1)
    else:
        enemy_damage = 7
        enem = enemy_damage
        user_health -= enemy_damage
        bot.reply_to(message, text="Тренер нанес критический удар")
        time.sleep(1)


    if user <= 2:
        user_damage = 20 
        bot.reply_to(message, text="Вы наносите критический удар".format(message.from_user))
        time.sleep(1)
        bot.reply_to(message, text="Враг горит".format(message.from_user))
        user_damage += random.randint(1, 20)
        enemy_health -= user_damage    
        time.sleep(1)
        bot.reply_to(message, text="Враг получил дополнительный урон огнем".format(message.from_user))
        time.sleep(1)
        bot.reply_to(message, f" Вы нанесли 💥 {user_damage} 💥 урона. \n У вас осталось ❤️ {user_health} ❤️здоровья. \n"
                        f" Противник нанес 💥 {enemy_damage} 💥 урона. \n У него осталось ❤️ {enemy_health} ❤️ здоровья.")
        
        
    elif user > 2:
        user_damage = 6
        bot.reply_to(message, text="Вы наносите обычный удар".format(message.from_user))
        time.sleep(1)
        enemy_health -= user_damage    
        bot.reply_to(message, f" Вы нанесли 💥 {user_damage} 💥 урона. \n У вас осталось ❤️ {user_health} ❤️здоровья. \n"
                        f" Противник нанес 💥 {enemy_damage} 💥 урона. \n У него осталось ❤️ {enemy_health} ❤️ здоровья.")

        


   
    
   
    if user_health <= 0:
        bot.reply_to(message, "Вы проиграли! \nТренер: Приходи когда будешь сильнее")
        user_health = 100
        enemy_health = 100
        location = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locbtn1 = types.KeyboardButton('🍻Трактир🍻')
        location.add(locbtn1)
        bot.send_message(message.chat.id, text="Куда направитесь?".format(message.from_user), reply_markup=location)
    
    elif enemy_health <= 0:
        bot.reply_to(message, "Вы победили! \n Тренер: Ты достойный соперник. ")
        time.sleep(1)
        user_health = 100
        enemy_health = 100
        location = types.ReplyKeyboardMarkup(resize_keyboard=True)
        locbtn1 = types.KeyboardButton('🍻Трактир🍻')
        location.add(locbtn1)
        bot.send_message(message.chat.id, text="Куда направитесь?".format(message.from_user), reply_markup=location)
        
    










@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'saloon':
            bot.send_message(call.message.chat.id, 'Вы выбрали трактир, как начальную локацию')

        elif call.data == 'city':
            bot.send_message(call.message.chat.id, 'Вы выбрали город как начальную локацию')
    
    
    #Справочник
   
    

   
bot.polling(none_stop=True)