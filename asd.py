import phonenumbers

def asd(my_string_number):
    if my_string_number.startswith('8'):
        my_string_number = '+7' + my_string_number[1:]
    
    try:
        my_number = phonenumbers.parse(my_string_number)
        return phonenumbers.is_valid_number(my_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# Примеры вызова функции:
result1 = asd("87054087528")  # Валидный номер
print(result1)  # Выведет True


