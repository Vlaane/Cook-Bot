from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

manual_b = KeyboardButton('Manual')
kbm_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kbm_1.add(manual_b)


borsh_b = KeyboardButton('Борщ с курицей')
borsh_kb = InlineKeyboardMarkup(row_width=2)
borsh_rec = InlineKeyboardButton('Рецепт', url='https://eda.ru/recepty/supy/borsch-s-kuricej-28797')
borsh_time = InlineKeyboardButton('Начать', callback_data="borsh")
borsh_kb.add(borsh_rec, borsh_time)


zavtrak_b = KeyboardButton('Ленивый завтрак')
zavtrak_kb = InlineKeyboardMarkup(row_width=2)
zavtrak_rec = InlineKeyboardButton('Рецепт', url='https://eda.ru/recepty/zavtraki/zavtrak-dlja-lenivih-21975')
zavtrak_time = InlineKeyboardButton('Начать', callback_data="zavtrak")
zavtrak_kb.add(zavtrak_rec, zavtrak_time)


sup_b = KeyboardButton('Куриный суп')
sup_kb = InlineKeyboardMarkup(row_width=2)
sup_rec = InlineKeyboardButton('Рецепт', url='https://eda.ru/recepty/supy/kurinij-sup-po-domashnemu-16144')
sup_time = InlineKeyboardButton('Начать', callback_data="sup")
sup_kb.add(sup_rec, sup_time)


kasha_b = KeyboardButton('Рисовая каша')
kasha_kb = InlineKeyboardMarkup(row_width=2)
kasha_rec = InlineKeyboardButton('Рецепт', url='https://eda.ru/recepty/zavtraki/risovaya-kasha-126246')
kasha_time = InlineKeyboardButton('Начать', callback_data="kasha")
kasha_kb.add(kasha_rec, kasha_time)






kbluda = ReplyKeyboardMarkup(resize_keyboard=True)
kbluda.add(borsh_b, zavtrak_b, sup_b, kasha_b)