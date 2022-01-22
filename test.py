from aiogram import Bot, Dispatcher, executor, types

token = '5076818544:AAHY_0cqgAvD-TunEZO_YQRec7wf-wBy_hQ'
bot = Bot(token)
dp = Dispatcher(bot)

def keyboard():
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Узнать расписание')
    button2 = types.KeyboardButton('Расписание звонков')
    button3 = types.KeyboardButton('Мероприятия')
    markup.add(button1, button2, button3)
    return markup

def keyboard1():
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Понедельник')
    button2 = types.KeyboardButton('Вторник')
    button3 = types.KeyboardButton('Среда')
    button4 = types.KeyboardButton('Четверг')
    button5 = types.KeyboardButton('Пятница')
    button6 = types.KeyboardButton('Расписание звонков')
    markup.add(button1, button2, button3, button4, button5)
    markup.row(button6)
    return markup

pon = "1) Физика\n2) Алгебра\n3) Английский\n4) Биология\n5) Информатика\n6) Обществознание"
ftor = '1) Химия\n2) Информатка\n3) География\n4) ОБЖ\n5) Алгебра\n6) Информатика\n7) Информатика\n8) Алгебра'
sreda = "1) Геометрия\n2) Литература\n3) Английский\n4) Информатика\n5) История\n6) Обществознание\n7) Физ-ра\n8) Информатика"
chetv = "1) Русский язык\n2) История\n3) Физ-ра\n4) Астрономия\n5) Физика\n6) Информатика\n7) Алгебра"
pyat = '1) Алгебра\n2) Руссикй язык\n3) География\n4) Литература\n5) Геометрия\n6) Английский\n7) ОБЖ'

@dp.message_handler(commands=['start', 'начать'])
async def answer(message):
    await message.answer('Добро пожаловать к нам в бот!!', reply_markup = keyboard())

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    if message.text == 'Узнать расписание':
        await message.answer('Выберите день недели: ', reply_markup=keyboard1())
    elif message.text == 'Расписание звонков':
        await message.answer("1 урок: ⏱8:35 - 9:15⏱\n"
                             "2 урок: ⏱9:30 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:30 - 12:15⏱\n"
                             "5 урок: ⏱12:25 - 13:10⏱\n"
                             "6 урок: ⏱13:25 - 14:05⏱\n"
                             "7 урок: ⏱14:25 - 15:10⏱\n"
                             "8 урок: ⏱15:25 - 16:10⏱")
    elif message.text == 'Понедельник':
        await message.answer(pon)
    elif message.text == 'Вторник':
        await message.answer(ftor)
    elif message.text == 'Среда':
        await message.answer(sreda)
    elif message.text == 'Четверг':
        await message.answer(chetv)
    elif message.text == 'Пятница':
        await message.answer(pyat)
    elif message.text == 'Мероприятия':
        await message.answer('1) Праздник «День Российской Науки» - 8 февраля 🥳\n2) Школьные '
                             'спортивные соревновании по волейболу, приуроченные ко Дню защитника Отечества - февраль 🏐\n'
                             '3) Общешкольный субботник - 18 апреля 🧹\n4) Сбор макулатуры -  с 20 по 30 апреля ♻️\n'
                             '5) Концерт, акции, флэш-мобы, посвящённые Дню Победы - Май 🎭\n'
                             '6) Праздник успеха - с 2 по 8 мая 🥳\n7) Последний звонок - с 16 по 22 мая 🔔')
    else:
        await message.answer('я тебя не понимать ... ')

executor.start_polling(dp)