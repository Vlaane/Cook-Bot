import time
from aiogram import Bot, Dispatcher, types, executor
from config import Token
from keyboards import kbm_1, kbluda, borsh_kb, zavtrak_kb, sup_kb, kasha_kb
bot = Bot(token=Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.answer(text='Привет! Это бот с готовыми рецептами разных блюд. Нажми кнопку "Manual"'
                          ' для просмотра инструкции перед дальнейшим использованием', reply_markup=kbm_1)


@dp.message_handler(text='Manual')
async def manual_msg(msg: types.Message):
    await msg.answer(text='В боте представлены рецепты самых популярных блюд. Нажимая на кнопку с названием одного из них, '
                          'вы получаете полный рецепт. По кнопке "Начать", вы запускаете поэтапный таймер готовки, который не '
                          'даст вам ошибиться. Все блюда рассчитаны на +- 4 порции.'
                          ' Приятного пользования и аппетита!', reply_markup=kbluda)


@dp.message_handler(text='Борщ с курицей')
async def borsh_msg(msg: types.Message):
    await msg.answer(text='Ознакомьтесь с рецептом и давайте начнём!', reply_markup=borsh_kb)

@dp.callback_query_handler(text='borsh')
async def timer_borsh(call: types.CallbackQuery):
    await call.message.answer(text='Начнём, поставьте курицу закипать на плиту, время закипания 20 минут.')
    time.sleep(1200)
    await call.message.answer(text='Время добавить картошку и начинать обжаривать заправку, 5 минут.')
    time.sleep(300)
    await call.message.answer(text='Картошка уже должна была размякнуть, добавьте заправку и продолжайте варить.')
    time.sleep(300)
    await call.message.answer(text='Борщ готов, приятного аппетита!')
    await call.answer()


@dp.message_handler(text='Ленивый завтрак')
async def zavtrak_msg(msg: types.Message):
    await msg.answer(text='Ознакомьтесь с рецептом и давайте начнём!', reply_markup=zavtrak_kb)


@dp.callback_query_handler(text='zavtrak')
async def timer_zavtrak(call: types.CallbackQuery):
    await call.message.answer(text='Начнём, поставьте воду закипать на плиту, время закипания 20 минут.')
    time.sleep(1200)
    await call.message.answer(text='Время добавить вареники, 3 минуты.')
    time.sleep(200)
    await call.message.answer(text='Ваш завтрак готов, приятного аппетита!')
    await call.answer()


@dp.message_handler(text='Куриный суп')
async def sup_msg(msg: types.Message):
    await msg.answer(text='Ознакомьтесь с рецептом и давайте начнём!', reply_markup=sup_kb)


@dp.callback_query_handler(text='sup')
async def timer_sup(call: types.CallbackQuery):
    await call.message.answer(text='Начнём, поставьте курицу закипать на плиту, время закипания 20 минут.')
    time.sleep(12)
    await call.message.answer(text='Убавьте огонь до минимума, посолите по вкусу и положите луковицу,\n'
                                   'накройте крышкой, 30 минут.')
    time.sleep(18)
    await call.message.answer(text='Время достать луковицу и добавить морковь, 5 минут.')
    time.sleep(3)
    await call.message.answer(text='Добавьте картофель и попробуйте на соль, 15 минут.')
    time.sleep(9)
    await call.message.answer(text='Добавьте вермишель, 15 минут.')
    time.sleep(9)
    await call.message.answer(text='Положите специи, 5 минут.')
    time.sleep(3)
    await call.message.answer(text='Выключите газ и дайте супу постоять, 10 минут.')
    time.sleep(6)
    await call.message.answer(text='Ваш суп готов, приятного аппетита!')
    await call.answer()


@dp.message_handler(text='Рисовая каша')
async def kasha_msg(msg: types.Message):
    await msg.answer(text='Ознакомьтесь с рецептом и давайте начнём!', reply_markup=kasha_kb)


@dp.callback_query_handler(text='kasha')
async def timer_kasha(call: types.CallbackQuery):
    await call.message.answer(text='Начнём, положите рис в кастрюлю и залейте водой,\n'
                                   'поставьте на огонь, время закипания 20 минут.')
    time.sleep(1200)
    await call.message.answer(text='Продолжайте варить 15 минут периодически помешивая,\n'
                                   'Параллельно в отдельной кастрюле подогрейте молоко, не доводя до кипения.')
    time.sleep(900)
    await call.message.answer(text='Влейте молоко к полуготовому рису, добавьте сахар и соль.\n'
                                   ' Варите еще 15 минут, помешивая, пока рис не станет полностью мягким.')
    time.sleep(900)
    await call.message.answer(text='Не забудьте добавить сливочное масло, приятного аппетита!')
    await call.answer()






@dp.message_handler()
async def echo(msg: types.Message):
    await msg.answer(text='Кажется вы ошиблись, нажмите кнопку или по команде /start начните заново.')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)