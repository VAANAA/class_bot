from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

token = '5076818544:AAHY_0cqgAvD-TunEZO_YQRec7wf-wBy_hQ'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

class state(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()
    state4 = State()
    state5 = State()

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
    button7 = types.KeyboardButton('⬅ Назад')
    markup.add(button1, button2, button3, button4, button5)
    markup.row(button6)
    markup.row(button7)
    return markup

def keyboard2():
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('10А')
    button2 = types.KeyboardButton('10Б')
    button3 = types.KeyboardButton('10В ФИЗМАТ')
    button4 = types.KeyboardButton('10В ТЕХ')
    button5 = types.KeyboardButton('10Д')
    markup.add(button1, button2, button3, button4, button5)
    return markup

def keyboard3():
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('7 класс')
    button2 = types.KeyboardButton('8 класс')
    button3 = types.KeyboardButton('9 класс')
    button4 = types.KeyboardButton('10 класс')
    button5 = types.KeyboardButton('11 класс')
    button6 = types.KeyboardButton('⬅ Назад')
    markup.add(button1, button2, button3, button4, button5)
    markup.row(button6)
    return markup

def keyboard4():
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('7-класс')
    button2 = types.KeyboardButton('8-класс')
    button3 = types.KeyboardButton('9-класс')
    button4 = types.KeyboardButton('10-класс')
    button5 = types.KeyboardButton('11-класс')
    button6 = types.KeyboardButton('⬅ Назад')
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
        await message.answer('Выберите ваш класс: ', reply_markup=keyboard2())
    elif message.text == 'Расписание звонков':

        await message.answer('Выберите класс: ', reply_markup=keyboard3())
    elif message.text == 'Мероприятия':
        # await message.answer('1) Праздник «День Российской Науки» - 8 февраля 🥳\n2) Школьные '
        #                      'спортивные соревновании по волейболу, приуроченные ко Дню защитника Отечества - февраль 🏐\n'
        #                      '3) Общешкольный субботник - 18 апреля 🧹\n4) Сбор макулатуры -  с 20 по 30 апреля ♻️\n'
        #                      '5) Концерт, акции, флэш-мобы, посвящённые Дню Победы - Май 🎭\n'
        #                      '6) Праздник успеха - с 2 по 8 мая 🥳\n7) Последний звонок - с 16 по 22 мая 🔔')
        await message.answer('Выберите класс: ', reply_markup=keyboard4())
    elif message.text == '10В ТЕХ':
        await message.answer('Выберите день недели: ', reply_markup=keyboard1())
        await state.state1.set()
    elif message.text == '10В ФИЗМАТ':
        await message.answer('Выберите день недели: ', reply_markup=keyboard1())
        await state.state2.set()
    elif message.text == '10А':
        await message.answer('Выберите день недели: ', reply_markup=keyboard1())
        await state.state3.set()
    elif message.text == '10Б':
        await message.answer('Выберите день недели: ', reply_markup=keyboard1())
        await state.state4.set()
    elif message.text == '7 класс':
        await message.answer("1 урок: ⏱8:30 - 9:15⏱\n"
                             "2 урок: ⏱9:25 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:35 - 12:20⏱\n"
                             "5 урок: ⏱12:30 - 13:15⏱\n"
                             "6 урок: ⏱13:35 - 14:20⏱\n"
                             "7 урок: ⏱14:40 - 15:25⏱\n")
    elif message.text == '8 класс':
        await message.answer("1 урок: ⏱8:30 - 9:15⏱\n"
                             "2 урок: ⏱9:25 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:35 - 12:20⏱\n"
                             "5 урок: ⏱12:30 - 13:15⏱\n"
                             "6 урок: ⏱13:35 - 14:20⏱\n"
                             "7 урок: ⏱14:40 - 15:25⏱\n")
    elif message.text == '9 класс':
        await message.answer("1 урок: ⏱8:30 - 9:15⏱\n"
                             "2 урок: ⏱9:25 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:35 - 12:20⏱\n"
                             "5 урок: ⏱12:30 - 13:15⏱\n"
                             "6 урок: ⏱13:35 - 14:20⏱\n"
                             "7 урок: ⏱14:40 - 15:25⏱\n")
    elif message.text == '10 класс':
        await message.answer("1 урок: ⏱8:30 - 9:15⏱\n"
                             "2 урок: ⏱9:25 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:35 - 12:20⏱\n"
                             "5 урок: ⏱12:30 - 13:15⏱\n"
                             "6 урок: ⏱13:35 - 14:20⏱\n"
                             "7 урок: ⏱14:40 - 15:25⏱\n"
                             "8 урок: ⏱15:30 - 16:15⏱\n")
    elif message.text == '11 класс':
        await message.answer("1 урок: ⏱8:30 - 9:15⏱\n"
                             "2 урок: ⏱9:25 - 10:10⏱\n"
                             "3 урок: ⏱10:30 - 11:15⏱\n"
                             "4 урок: ⏱11:35 - 12:20⏱\n"
                             "5 урок: ⏱12:30 - 13:15⏱\n"
                             "6 урок: ⏱13:35 - 14:20⏱\n"
                             "7 урок: ⏱14:40 - 15:25⏱\n"
                             "8 урок: ⏱15:30 - 16:15⏱\n")
    elif message.text == '7-класс':
        await message.answer(
                             '1) Праздник "День Российской Науки" 8 февраля\n'
                             '2) Школьные спортивные соревнования по волейболу, приуроченные ко Дню Защитника Отечества - Февраль\n'
                             '3) "Весёлые старты" - Апрель - май\n'
                             '4) Сбор макулатуры - 20-30 впреля')
    elif message.text == '8-класс':
        await message.answer('1) Конкурс "Ученик года" - 7 февраля\n'
                             '2) Праздник "День Российской Науки" 8 февраля\n'
                             '3) Школьные спортивные соревнования по волейболу, приуроченные ко Дню Защитника Отечества - Февраль\n'
                             '4) "Весёлые старты" - Апрель - май\n'
                             '5) Сбор макулатуры - 20-30 впреля')
    elif message.text == '9-класс':
        await message.answer('1) Конкурс "Ученик года" - 7 февраля\n'
                             '2) Праздник "День Российской Науки" 8 февраля\n'
                             '3) Школьные спортивные соревнования по волейболу, приуроченные ко Дню Защитника Отечества - Февраль\n'
                             '4) "Весёлые старты" - Апрель - май\n'
                             '5) Сбор макулатуры - 20-30 впреля')
    elif message.text == '10-класс':
        await message.answer('1) Конкурс "Ученик года" - 7 февраля\n'
                             '2) Праздник "День Российской Науки" 8 февраля\n'
                             '3) Школьные спортивные соревнования по волейболу, приуроченные ко Дню Защитника Отечества - Февраль\n'
                             '4) "Весёлые старты" - Апрель - май\n'
                             '5) Сбор макулатуры - 20-30 впреля\n'
                             '6) Праздник успеха - 2 - 8 мая')
    elif message.text == '11-класс':
        await message.answer('1) Конкурс "Ученик года" - 7 февраля\n'
                             '2) Праздник "День Российской Науки" 8 февраля\n'
                             '3) Школьные спортивные соревнования по волейболу, приуроченные ко Дню Защитника Отечества - Февраль\n'
                             '4) "Весёлые старты" - Апрель - май\n'
                             '5) Сбор макулатуры - 20-30 впреля\n'
                             '6) Праздник успеха - 2 - 8 мая\n'
                             '7) Встреча выпускников\n'
                             '8) Последний звонок 16 - 22 мая')
    elif message.text == '⬅ Назад':
        await message.answer('Выберите повторно: ', reply_markup=keyboard())
    else:
        await message.answer('я тебя не понимать ... ')

@dp.message_handler(state = state.state1)
async def cls_10_v(message: types.Message, state: FSMContext):
    if message.text == 'Понедельник':
        await message.answer(pon)
    elif message.text == 'Вторник':
        await message.answer(ftor)
    elif message.text == 'Среда':
        await message.answer(sreda)
    elif message.text == 'Четверг':
        await message.answer(chetv)
    elif message.text == 'Пятница':
        await message.answer(pyat)

    elif message.text == '⬅ Назад':
        await message.answer('Выберите повторно: ', reply_markup=keyboard())
        return await state.reset_state()

@dp.message_handler(state = state.state2)
async def cls_10_a(message: types.Message, state: FSMContext):
    if message.text == 'Понедельник':
        await message.answer(text = 'ФИЗИКА\nАлгебра\nАнглийский\nБиология\nСтатистика\nИстория')
    elif message.text == 'Вторник':
        await message.answer('Химия\nИнформатика\nГеография\nОБЖ\nАлгебра\nФизика\nФизика')
    elif message.text == 'Среда':
        await message.answer('Алгебра\nРусский язык\nАнглийский\nСтатистика\nОбществознание\nИстория\nФиз-ра')
    elif message.text == 'Четверг':
        await message.answer('Русский\nОбществознание\nФиз-ра\nАстрономия\nФизика\nПроектная деятельность\nАлгебра')
    elif message.text == 'Пятница':
        await message.answer('Геометрия\nРусский язык\nГеография\nЛит-ра\nГеометрия\nАнглийский язык\nОБЖ')
    elif message.text == '⬅ Назад':
        await message.answer('Выберите повторно: ', reply_markup=keyboard())
        return await state.reset_state()
    return await state.reset_state()

@dp.message_handler(state = state.state3)
async def cls_10_v(message: types.Message, state: FSMContext):
    if message.text == 'Понедельник':
        await message.answer('Физ-ра\nАлгебра\nАнглийский язык\nОбществознание\nХимия\nОБЖ')
    elif message.text == 'Вторник':
        await message.answer('Экономика\nАстрономия\nФиз-ра\nИнформатика\nАлгебра\nРусский язык\nИстория')
    elif message.text == 'Среда':
        await message.answer('Алгебра\nРусский язык\nАнглийский язык\nГеография\nОбществознание\nОбществознание\nПроектная деятельность')
    elif message.text == 'Четверг':
        await message.answer('География\nОбществознание\nБиология\nИстория\nРусский язык\nПраво\nАлгебра')
    elif message.text == 'Пятница':
        await message.answer('Геометрия\nЭкономика\nФизика\nОБЖ\nГеометрия\nАнглийский язык\nРусский язык')
    elif message.text == '⬅ Назад':
        await message.answer('Выберите повторно: ', reply_markup=keyboard())
        return await state.reset_state()
    return await state.reset_state()

@dp.message_handler(state = state.state4)
async def cls_10_v(message: types.Message, state: FSMContext):
    if message.text == 'Понедельник':
        await message.answer('Обществознание\nАлгебра\nАнглийский язык\nРусский язык\nЛит-ра\nИстория, Химия')
    elif message.text == 'Вторник':
        await message.answer('Русский язык\nИстория, Химия\nБиология, Химия\nПраво, История\nАлгебра\nОБЖ\nГеография')
    elif message.text == 'Среда':
        await message.answer('Алгебра\nГеография\nАнглийский язык\nОбществознание\nРусский язык\nИстория, Биология\nИнформатика')
    elif message.text == 'Четверг':
        await message.answer('Астрономия\nФиз-ра\nОБЖ\nПроектная деятельность\nИстория, Биология\nАнглийский, Химия\nАлгебра')
    elif message.text == 'Пятница':
        await message.answer('Геометрия\nФизика\nХимия, История\nФиз-ра\nГеометрия\nАнглийский язык\nИстория, Биология\n')
    elif message.text == '⬅ Назад':
        await message.answer('Выберите повторно: ', reply_markup=keyboard())
        return await state.reset_state()
    return await state.reset_state()

executor.start_polling(dp)
