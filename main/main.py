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
import phonenumbers

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

# Функция для проверки номера телефона
def asd(my_string_number):
    if my_string_number.startswith('8'):
        my_string_number = '+7' + my_string_number[1:]
   
    try:
        my_number = phonenumbers.parse(my_string_number)
        return phonenumbers.is_valid_number(my_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


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

keyboard_chocolate2 = InlineKeyboardMarkup(row_width=3)
button_chocolategorki = InlineKeyboardButton("Горький", callback_data="Горький")
button_chocolateblack = InlineKeyboardButton("Тёмный", callback_data="Тёмный")
button_chocolatemilk = InlineKeyboardButton("Молочный", callback_data="Молочный")
button_chocolatewhite = InlineKeyboardButton("Белый", callback_data="Белый")
keyboard_chocolate2.add(button_chocolategorki,button_chocolateblack,button_chocolatemilk,button_chocolatewhite)

keyboard_chocolate1 = InlineKeyboardMarkup(row_width=3)
button_chocolate1 = InlineKeyboardButton("Шоколад", callback_data="Шоколад")
button_strawberry_in_chocolate = InlineKeyboardButton("Клубника в шоколаде", callback_data="Клубника в шоколаде")
keyboard_chocolate1.add(button_chocolate1,button_strawberry_in_chocolate)

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

keyboard_jewelery = InlineKeyboardMarkup(row_width=3)
button_colbe = InlineKeyboardButton("Колье/чокеры", callback_data="Колье")
button_jewelery_sets = InlineKeyboardButton("Комплекты", callback_data="Комплекты")
keyboard_jewelery.add(button_colbe,button_jewelery_sets)

keyboard3 = InlineKeyboardMarkup(row_width=3)
button_skidki = InlineKeyboardButton("Книги", callback_data='Книги')
# button_soap = InlineKeyboardButton("Мыло", callback_data='Мыло')
button_bele = InlineKeyboardButton("Пижамы", callback_data='Белье')
button_sache = InlineKeyboardButton("Аромасаше", callback_data='Аромасаше')
button_chocolate = InlineKeyboardButton("Сладости", callback_data='Сладости')
button_beauty = InlineKeyboardButton("Украшения", callback_data='Украшения')
# button_flower = InlineKeyboardButton("Цветы", callback_data='Цветы')
keyboard3.add(button_skidki, button_bele,button_chocolate,button_beauty,button_sache)
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
    chocolate_company1 = State()
    zakaz = State()
    zakaz1 = State()
    sam_podarok = State()
    sam_podarok1 = State()
    asd = State()
    number = State()
    next1 = State()

product_photos = {
    'Книги': {
        'budget_<5000': ['50.png', '52.png', '53.png', '54.png', '55.png', '57.png', '58.png', '510.png', '511.png','512.png','513.png','516.png','517.png','518.png','519.png','520.png','521.png','522.png','524.png','525.png'],
        'budget_5000-10000': ['51.png', '56.png', '59.png','514.png','515.png','523.png'],
        'budget_>10000': 'нету',
    },
    # 'Мыло': {
    #     'budget_<5000': 'нету',
    #     'budget_5000-10000': ['2.png','3.png','1.png'],
    #     'budget_>10000': 'нету',
    # },
    'Пижамы': {
        'budget_<5000': 'нету',
        'budget_5000-10000': 'нету',
        'budget_>10000': ['60.png','61.png','62.png','63.png'],
    },
    'Шоколад': {
        'budget_<5000': ['1001.png','1002.png','1003.png'],
        'budget_5000-10000': 'нету',
        'budget_>10000': ['1004.png','1007.png','1009.png','1011.png'],
    },
    'Клубника в шоколаде': {
        'budget_<5000': ['1008.png','1012.png'],
        'budget_5000-10000': ['1005.png','1006.png','1010.png'],
        'budget_>10000': ['1004.png','1007.png','1009.png','1011.png'],
    },
    'Украшения': {
        'Колье' : {
            'budget_<5000': 'нету',
            'budget_5000-10000': ['4003.png','4004.png','4005.png','4006.png','4007.png','4015.png','4016.png','4018.png','4020.png','4021.png','4022.png','4023.png','4024.png','4025.png','4026.png','4027.png','4028.png','4032.png','4033.png'],
            'budget_>10000': ['4001.png','4002.png','4008.png','4009.png','4010.png','4011.png','4012.png','4013.png','4014.png','4017.png','4019.png','4029.png','4030.png','4031.png','4034.png','4035.png','4036.png'],
        },
        'Комплекты' : {
            'budget_<5000': 'нету',
            'budget_5000-10000': 'нету',
            'budget_>10000': ['4037.png','4038.png'],
        }
        
    },

    # 'Цветы': {
    #     'budget_<5000': 'нету',
    #     'budget_5000-10000': ['6.png'],
    #     'budget_>10000': ['4.png','5.png'],
    # }
    'Аромасаше': {
        'budget_<5000': ['70.png','71.png','72.png'],
        'budget_5000-10000': 'нету',
        'budget_>10000': 'нету',
    }
    
}
 
product_photos_company = {
    'Книги': ['50.png', '52.png', '53.png', '54.png', '55.png', '57.png', '58.png', '510.png', '511.png','512.png','513.png','516.png','517.png','518.png','519.png','520.png','521.png','522.png','524.png','525.png','51.png', '56.png', '59.png','514.png','515.png','523.png'],
    # 'Мыло': ['2.png','3.png','1.png'],
    'Пижамы': ['60.png','61.png','62.png','63.png'],
    'Сладости': ['1001.png','1002.png','1003.png','1008.png','1012.png','1005.png','1006.png','1010.png'],
    'Украшения': ['4003.png','4004.png','4005.png','4006.png','4007.png','4015.png','4016.png','4018.png','4020.png','4021.png','4022.png','4023.png','4024.png','4025.png','4026.png','4027.png','4028.png','4032.png','4033.png','4001.png','4002.png','4008.png','4009.png','4010.png','4011.png','4012.png','4013.png','4014.png','4017.png','4019.png','4029.png','4030.png','4031.png','4034.png','4035.png','4036.png','4037.png','4038.png'],
    # 'Цветы': ['4.png','5.png',"6.png"]
}

data = {
    "ID": ".",
    "UserName": ".",
    "country": ".",
    "name": ".",
    "budget": ".",
    "section" : ".",
    "number_gift": ".",
    "number": ".",
    "size_pizhama": "."
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
        data["size_pizhama"] = "."

        await message.answer("""Вас приветствует Doro Eco Marketplace🎁🎈 - Ваш помощник в выборе идеальных подарков. Давайте начнем!""", reply_markup=keyboard1)
        await Form.next1.set()

        x = [[i for i in data.values()]]
        wks_person.append_table(x, start='A2', end=None,   
                            dimension='ROWS', overwrite=False)



@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Казахстан', 'Узбекистан'], state=Form.next1)
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
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

# @dp.message_handler(state=Form.sam_podarok)
# async def process_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['number'] = message.text
#         await Form.sam_podarok1.set()
#         await message.answer(f"""Отлично, {data['name']}🎉 Укажите сумму, которую Вы готовы потратить на подарок😊""",reply_markup=keyboard)
#         row_number_person = find_last_row_with_id(wks_person, data["ID"])
#         if row_number_person:
#             wks_person.update_value((row_number_person, 8), data['number'])
            
@dp.message_handler(state=Form.sam_podarok)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if asd(message.text) == True:
            data['number'] = message.text
            await Form.sam_podarok1.set()
            await message.answer(f"""Отлично, {data['name']}🎉 Укажите сумму, которую Вы готовы потратить на подарок😊""", reply_markup=keyboard)
            row_number_person = find_last_row_with_id(wks_person, data["ID"])
            if row_number_person:
                wks_person.update_value((row_number_person, 8), data['number'])
        else:
            await message.answer("Некорректный номер телефона. Пожалуйста, введите корректный номер.")

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
# @dp.callback_query_handler(lambda callback_query: callback_query.data in ['Мыло'], state=Form.inline1)
# async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data["section"] = "Мыло"
#         await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите аромат, который Вам по душе…",reply_markup=keyboard_aromat)
#         await Form.soap_company.set()
#         row_number_person = find_last_row_with_id(wks_person, data["ID"])
#         if row_number_person:
#             wks_person.update_value((row_number_person, 6), data['section'])

# @dp.callback_query_handler(lambda callback_query: callback_query.data in ['Цветочный','Кофейный','Цитрус','Кокос'], state=Form.soap_company)
# async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         await Form.asd.set()
#         if data["country"]=="Узбекистан"or"Казахстан":
#             if product_photos['Мыло'][data['budget']]=='нету':
#                 await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
#                 await Form.sam_podarok1.set()
#             else:
#                 await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
#                 file_name = product_photos['Мыло'][data['budget']]
#                 photo_groups = list(split_list(file_name, 10))
#                 for group in photo_groups:
#                     media = types.MediaGroup()
#                     for photo_url in group:
#                         photo = open(photo_url, 'rb')
#                         media.attach_photo(photo) 
#                     await bot.send_media_group(callback_query.from_user.id, media=media)  
#                 await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)


#ПИЖАМЫ КОМПАНИИ
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
        data["size_pizhama"] = "Пижамы"
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
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 7), data['size_pizhama'])


# @dp.callback_query_handler(lambda callback_query: callback_query.data in ['Чёрный','Синий','Белый','Фуксия'], state=Form.belbe1_company)
# async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         await Form.asd.set()
#         if product_photos['Пижамы'][data['budget']]=='нету':
#             await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
    
#             await Form.sam_podarok1.set()
#         else:
#             await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
#             file_name = product_photos['Пижамы'][data['budget']]
#             photo_groups = list(split_list(file_name, 10))
#             for group in photo_groups:
#                 media = types.MediaGroup()
#                 for photo_url in group:
#                     photo = open(photo_url, 'rb')
#                     media.attach_photo(photo) 
#                 await bot.send_media_group(callback_query.from_user.id, media=media)  
#             await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)

#ШОКОЛАД КОМПАНИИ
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Сладости'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Сладости"
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите вид сладостей, который Вас интересует…",reply_markup=keyboard_chocolate1)
        await Form.chocolate_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Клубника в шоколаде'], state=Form.chocolate_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Клубника в шоколаде"
        await Form.asd.set()
        if product_photos['Клубника в шоколаде'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id, "Благодарю❤️ Взгляните на мои рекомендации🎁")
            file_name = product_photos['Клубника в шоколаде'][data['budget']]
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

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Шоколад'], state=Form.chocolate_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Шоколад" 
        await bot.send_message(callback_query.from_user.id,f"Благодарю❤️ Укажите вид шоколада, который Вас интересует…",reply_markup=keyboard_chocolate2)
        await Form.chocolate_company1.set()

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Горький','Белый','Молочный','Тёмный'], state=Form.chocolate_company1)
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
        await bot.send_message(callback_query.from_user.id, f"Благодарю❤️ Укажите вид украшений, который Вас интересует…",reply_markup=keyboard_jewelery)
        await Form.jewelery_company.set()
        row_number_person = find_last_row_with_id(wks_person, data["ID"])
        if row_number_person:
            wks_person.update_value((row_number_person, 6), data['section'])
    
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Колье','Комплекты'], state=Form.jewelery_company)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await Form.asd.set()
        if product_photos['Украшения'][callback_query.data][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id,f"Благодарю, {data['name']}❤️ Взгляните на мои рекомендации")
            file_name = product_photos['Украшения'][callback_query.data][data['budget']]
            photo_groups = list(split_list(file_name, 10))
            for group in photo_groups:
                media = types.MediaGroup()
                for photo_url in group:
                    photo = open(photo_url, 'rb')
                    media.attach_photo(photo) 
                await bot.send_media_group(callback_query.from_user.id, media=media)  
            await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4) 


#ЦВЕТЫ КОМПАНИИ
# @dp.callback_query_handler(lambda callback_query: callback_query.data in ['Цветы'], state=Form.inline1)
# async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data["section"] = "Цветы"
#         await Form.asd.set()
#         if product_photos['Цветы'][data['budget']]=='нету':
#             await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
#             await Form.sam_podarok1.set()
#         else:
#             await bot.send_message(callback_query.from_user.id, "Благодарю❤️ Взгляните на мои рекомендации🎁")
#             file_name = product_photos['Цветы'][data['budget']]
#             photo_groups = list(split_list(file_name, 10))
#             for group in photo_groups:
#                 media = types.MediaGroup()
#                 for photo_url in group:
#                     photo = open(photo_url, 'rb')
#                     media.attach_photo(photo) 
#                 await bot.send_media_group(callback_query.from_user.id, media=media)  
#             await bot.send_message(callback_query.from_user.id,f"Хотите заказать или посмотреть еще?",reply_markup=keyboard_4)
#         row_number_person = find_last_row_with_id(wks_person, data["ID"])
#         if row_number_person:
#             wks_person.update_value((row_number_person, 6), data['section'])

#Аромасаше
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['Аромасаше'], state=Form.inline1)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["section"] = "Аромасаше"
        await Form.asd.set()
        if product_photos['Аромасаше'][data['budget']]=='нету':
            await bot.send_message(callback_query.from_user.id,f"Прошу прощения, в данный момент выбранный Вами подарок приобрести невозможно😔 Я делаю всё возможное, чтобы предоставить Вам больше вариантов🫶",reply_markup=keyboard)
            await Form.sam_podarok1.set()
        else:
            await bot.send_message(callback_query.from_user.id, "Благодарю❤️ Взгляните на мои рекомендации🎁")
            file_name = product_photos['Аромасаше'][data['budget']]
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
        if message.text.isdigit():
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
    Размер пижамы - {data['size_pizhama']}
    Номер подарка - {data['number_gift']}
    Номер телефона - {data['number']}
    """)
        else:
            await message.answer(f"Пожалуйста введите номер товара, который Вы хотите приобрести…")

@dp.callback_query_handler(lambda callback_query: callback_query.data in ['eche'], state=Form.asd)
async def handle_product_selection(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(callback_query.from_user.id,f"Выберите бюджет",reply_markup=keyboard)
        await Form.sam_podarok1.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)