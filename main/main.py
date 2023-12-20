from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, MediaGroup
from aiogram.types import InputMediaDocument
from aiogram.types import InputFile
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Command
import os
import pygsheets
import asyncio

bot = Bot(token='6501950453:AAHAEmpf3Iix2TLUyp-DGdFBXn-IKqBQbKA')#test   6508551273:AAFAUNHu2Jb2Ip69TYFBtUDOhCHvLvlnJ3Y     original 6501950453:AAHAEmpf3Iix2TLUyp-DGdFBXn-IKqBQbKA
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

CONSTANT_USER_ID = 6416219442

current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory, 'studious-rhythm-390907-df0cd6e3852a.json')
gc = pygsheets.authorize(service_account_file=path)
print(gc.spreadsheet_titles())
sh = gc.open('b2b')
wks_person = sh[0]
sh1 = gc.open('b2c')
wks_person= sh1[0]


def find_last_row_with_id(sheet, user_id):
    matching_cells = sheet.find(str(user_id), searchByRegex=False, matchEntireCell=True, includeFormulas=False, matchCase=True, forceFetch=True)
    if not matching_cells:
        return None
    return max(cell.row for cell in matching_cells)

def split_list(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]


keyboard1 = InlineKeyboardMarkup(row_width=1)
button_company = InlineKeyboardButton("Узбекистан", callback_data='Узбекистан')
button_self = InlineKeyboardButton("Казахстан", callback_data='Казахстан')
keyboard1.add(button_company, button_self)

keyboard_4 = InlineKeyboardMarkup(row_width=1)
button_zakaz = InlineKeyboardButton("Хочу заказать", callback_data='zakaz')
button_eche = InlineKeyboardButton("Посмотреть ещё", callback_data='eche')
keyboard_4.add(button_zakaz, button_eche)

keyboard = InlineKeyboardMarkup(row_width=3)
button_5000 = InlineKeyboardButton("<5000", callback_data="budget_<5000")
button_500010000 = InlineKeyboardButton("5000-10000", callback_data="budget_5000-10000")
button_10000 = InlineKeyboardButton(">10000", callback_data="budget_>10000")
keyboard.add(button_5000,button_500010000,button_10000)



######клавы товаров
keyboard_genre = InlineKeyboardMarkup(row_width=3)
button_selfimporve = InlineKeyboardButton("Саморазвитие", callback_data="Саморазвитие")
keyboard_genre.add(button_selfimporve)

keyboard_aromat = InlineKeyboardMarkup(row_width=3)
button_aromatcitrus = InlineKeyboardButton("Цитрус", callback_data="Цитрус")
button_aromatflower = InlineKeyboardButton("Цветочный", callback_data="Цветочный")
button_aromatcoconut = InlineKeyboardButton("Кокос", callback_data="Кокос")
button_aromatcofe = InlineKeyboardButton("Кофейный", callback_data="Кофейный")
keyboard_aromat.add(button_aromatcitrus,button_aromatflower,button_aromatcoconut,button_aromatcofe)

keyboard_chocolate = InlineKeyboardMarkup(row_width=3)
button_chocolategorki = InlineKeyboardButton("Горький", callback_data="Горький")
button_chocolateblack = InlineKeyboardButton("Тёмный", callback_data="Тёмный")
button_chocolatemilk = InlineKeyboardButton("Молочный", callback_data="Молочный")
button_chocolatewhite = InlineKeyboardButton("Белый", callback_data="Белый")
keyboard_chocolate.add(button_chocolategorki,button_chocolateblack,button_chocolatemilk,button_chocolatewhite)

keyboard_colorpizhama = InlineKeyboardMarkup(row_width=3)
button_colorpink = InlineKeyboardButton("Розовый", callback_data="Белый")
button_colorblue = InlineKeyboardButton("Синий", callback_data="Синий")
button_colorblack = InlineKeyboardButton("Чёрный", callback_data="Чёрный")
button_colorfuks = InlineKeyboardButton("Фуксия", callback_data="Фуксия")
keyboard_colorpizhama.add(button_colorpink,button_colorblue,button_colorblack,button_colorfuks)

keyboard_sizepizhama = InlineKeyboardMarkup(row_width=3)
button_sizeS = InlineKeyboardButton("S", callback_data="S")
button_sizeM = InlineKeyboardButton("M", callback_data="M")
button_sizeL = InlineKeyboardButton("L", callback_data="L")
button_sizeXL = InlineKeyboardButton("XL", callback_data="XL")
keyboard_sizepizhama.add(button_sizeS,button_sizeM,button_sizeL,button_sizeXL)


keyboard3 = InlineKeyboardMarkup(row_width=3)
button_skidki = InlineKeyboardButton("Книги", callback_data='Книги')
button_soap = InlineKeyboardButton("Мыло", callback_data='Мыло')
button_bele = InlineKeyboardButton("Пижамы", callback_data='Белье')
button_chocolate = InlineKeyboardButton("Шоколад", callback_data='Шоколад')
button_beauty = InlineKeyboardButton("Украшения", callback_data='Украшения')
button_flower = InlineKeyboardButton("Цветы", callback_data='Цветы')
keyboard3.add(button_skidki, button_soap, button_bele,button_chocolate,button_beauty,button_flower)
######клавы товаров



class Form(StatesGroup):
    company_name = State()
    company_name_1 = State()
    company_name_2 = State()
    self_name = State()
    inline1 = State()
    inline = State()
    inline2 = State()
    book_company = State()
    soap_company = State()
    belbe_company = State()
    belbe1_company = State()
    jewelery_company = State()
    flowers_company = State()
    chocolate_company = State()
    zakaz = State()
    zakaz1 = State()
    sam_podarok = State()
    sam_podarok1 = State()
    asd = State()
    number = State()

product_photos = {
    'Книги': {
        'budget_<5000': ['11.png', '13.png', '14.png', '15.png', '16.png', '18.png', '19.png', '21.png', '22.png','23.png','24.png','27.png','28.png','29.png','31.png','32.png','33.png','35.png','36.png'],
        'budget_5000-10000': ['12.png', '17.png', '20.png','25.png','26.png','30.png','34.png',],
        'budget_>10000': 'нету',
    },
    'Мыло': {
        'budget_<5000': 'нету',
        'budget_5000-10000': ['2.png','3.png','1.png'],
        'budget_>10000': 'нету',
    },
    'Пижамы': {
        'budget_<5000': 'нету',
        'budget_5000-10000': 'нету',
        'budget_>10000': ['37.png','38.png'],
    },
    'Шоколад': {
        'budget_<5000': ['7.png','8.png','9.png'],
        'budget_5000-10000': 'нету',
        'budget_>10000': 'нету',
    },
    'Украшения': {
        'budget_<5000': ['10.png'],
        'budget_5000-10000': ['10.png'],
        'budget_>10000': ['10.png'],
    },
    'Цветы': {
        'budget_<5000': 'нету',
        'budget_5000-10000': ['6.png'],
        'budget_>10000': ['4.png','5.png'],
    }
    
}

product_photos_company = {
    'Книги': ['11.png', '13.png', '14.png', '15.png', '16.png', '18.png', '19.png', '21.png', '22.png','23.png','24.png','27.png','28.png','29.png','31.png','32.png','33.png','35.png','36.png','12.png', '17.png', '20.png','25.png','26.png','30.png','34.png'],
    'Мыло': ['2.png','3.png','1.png'],
    'Пижамы': ['37.png','38.png'],
    'Шоколад': ['7.png','8.png','9.png'],
    'Украшения': ['10.png'],
    'Цветы': ['4.png','5.png',"6.png"]
}

data = {
    "ID": ".",
    "UserName": ".",
    "country": ".",
    "name": ".",
    "budget": ".",
    "section" : ".",
    "number_gift": ".",
    "number": "."
}
5589501552
@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(None)

    async with state.proxy() as data:
        data["ID"] = message.from_user.id
        data["UserName"] = message.from_user.full_name
        data["country"] = "."
        data["name"] = "."
        data["budget"] = "."
        data["section"] = "."
        data["number_gift"] = "."
        data["number"] = "."

        await message.answer("""Вас приветствует Doro Eco Marketplace🎁🎈 - Ваш помощник в выборе идеальных подарков. Давайте начнем!""", reply_markup=keyboard1)

        x = [[i for i in data.values()]]
        wks_person.append_table(x, start='A2', end=None,   
                            dimension='ROWS', overwrite=False)



@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Казахстан', 'Узбекистан'])
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
        data["country"]=callback_query.data
        await Form.number.set()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите, пожалуйста, свое имя")
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 3), data['country'])

@dp.message_handler(state=Form.number)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Form.sam_podarok.set()
        await message.answer(f"""Благодарю❤️ Укажите, пожалуйста, свой номер телефона""")
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 4), data['name'])

@dp.message_handler(state=Form.sam_podarok)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await Form.sam_podarok1.set()
        await message.answer(f"""Отлично, {data['name']}🎉 Укажите сумму, которую Вы готовы потратить на подарок😊""",reply_markup=keyboard)
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 8), data['number'])

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['budget_<5000', 'budget_5000-10000','budget_>10000'],state=Form.sam_podarok1)
async def process_name(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['budget'] = callback_query.data
        await bot.send_message(callback_query.from_user.id,f"Какой подарок Вы бы хотели подарить?",reply_markup=keyboard3)
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 5), data['budget'])
        await Form.inline1.set()


#КНИГИ КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Книги'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Книги"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите жанр, который Вас интересует…",reply_markup=keyboard_genre)
        await Form.book_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Саморазвитие'], state=Form.book_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if product_photos['Книги'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard) 
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
            file_name = product_photos['Книги'][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(callback_query.from_user.id, media=media)  
            await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)


#МЫЛО КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Мыло'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Мыло"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите аромат, который Вам по душе…",reply_markup=keyboard_aromat)
        await Form.soap_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Цветочный','Кофейный','Цитрус','Кокос'], state=Form.soap_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if data["country"]=="Узбекистан"or"Казахстан":
            if product_photos['Мыло'][data['budget']]=='нету':
                await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
                await Form.sam_podarok1.set()
            else:
                await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
                file_name = product_photos['Мыло'][data['budget']]
                photo_groups = list(split_list(file_name, 10))
                for group in photo_groups:
                    media = types.MediaGroup()
                    for photo_url in group:
                        photo = open(photo_url, 'rb')
                        media.attach_photo(photo) 
                    await bot.send_media_group(callback_query.from_user.id, media=media)  
                await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)


#БЕЛЬЕ КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Белье'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Пижамы"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите размер пижамы, который Вас интересует…",reply_markup=keyboard_sizepizhama)
        await Form.belbe_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])


@dp.callback_query_handler(lambda callback_query: callback_query.data in ['S','M','L','XL'], state=Form.belbe_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(callback_query.from_user.id,f"Благодарю❤️ Укажите цвет пижамы, который Вы предпочитаете…",reply_markup=keyboard_colorpizhama)
        await Form.belbe1_company.set()


@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Чёрный','Синий','Белый','Фуксия'], state=Form.belbe1_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if product_photos['Пижамы'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
    
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
            file_name = product_photos['Пижамы'][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(callback_query.from_user.id, media=media)  
            await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)

#ШОКОЛАД КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Шоколад'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Шоколад"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите вид шоколада, который Вас интересует…",reply_markup=keyboard_chocolate)
        await Form.chocolate_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])



@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Горький','Белый','Молочный','Тёмный'], state=Form.chocolate_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if product_photos['Шоколад'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id, "Благодарю❤️ Взгляните на мои рекомендации🎁")
            file_name = product_photos['Шоколад'][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(callback_query.from_user.id, media=media)  
            await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)


#УКРАШЕНИЯ КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Украшения'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Украшения"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите вид украшений, который Вас интересует…")
        await Form.jewelery_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])
    
@dp.message_handler(state=Form.jewelery_company)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if product_photos['Украшения'][data['budget']]=='нету':
            await message.answer(f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await message.answer(f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
            file_name = product_photos['Украшения'][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(chat_id=message.chat.id, media=media)  
            await message.answer(f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4) 


#ЦВЕТЫ КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Цветы'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Цветы"
        await Form.asd.set()
        if product_photos['Цветы'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id, "Благодарю❤️ Взгляните на мои рекомендации🎁")
            file_name = product_photos['Цветы'][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(callback_query.from_user.id, media=media)  
            await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['zakaz'], state=Form.asd)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(callback_query.from_user.id, f"Введите номер товара, который Вы хотите приобрести…")
        await Form.zakaz1.set()

@dp.message_handler(state=Form.zakaz1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_gift'] = message.text
        await message.answer(f"Благодарю за выбор🎁")
        await message.answer(f"С Вами свяжется наш менеджер для уточнения деталей по доставке и оплате. До встречи❤️")
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 7), data['number_gift'])
        print(data)
        await state.finish()
        await bot.send_message(CONSTANT_USER_ID, f"""
ID - {data['ID']}
Имя пользователя - {data['UserName']}
Страна - {data['country']}
Имя - {data['name']}
Раздел - {data['section']}
Бюджет - {data['budget']}
Номер подарка - {data['number_gift']}
Номер телефона - {data['number']}
""")

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['eche'], state=Form.asd)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(callback_query.from_user.id,f"Выберите бюджет",reply_markup=keyboard)
        await Form.sam_podarok1.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)