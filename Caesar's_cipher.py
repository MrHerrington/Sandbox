"""     Шифр Цезаря     """
ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' * 2
en_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
rotation = str(input('Шифрование или дешифрование (ш / д): '))
language = str(input('Русский или английский (ru / en): '))
step = int(input('Шаг сдвига: '))
message = str(input('Введите сообщение:\n'))
new_message = ''


def ru_letter_right(letter, where):
    return ru_alphabet[ru_alphabet.find(message[letter].lower()) + where]


def ru_letter_left(letter, where):
    return ru_alphabet[ru_alphabet.rfind(message[letter].lower()) - where]


def en_letter_right(letter, where):
    return en_alphabet[en_alphabet.find(message[letter].lower()) + where]


def en_letter_left(letter, where):
    return en_alphabet[en_alphabet.rfind(message[letter].lower()) - where]


for i in range(len(message)):
    if message[i].lower() in ru_alphabet or message[i].lower() in en_alphabet:
        if message[i].isupper():
            if rotation == 'ш':
                if language == 'ru':
                    new_message += ru_letter_right(i, step).upper()
                elif language == 'en':
                    new_message += en_letter_right(i, step).upper()
            elif rotation == 'д':
                if language == 'ru':
                    new_message += ru_letter_left(i, step).upper()
                elif language == 'en':
                    new_message += en_letter_left(i, step).upper()
        else:
            if rotation == 'ш':
                if language == 'ru':
                    new_message += ru_letter_right(i, step)
                elif language == 'en':
                    new_message += en_letter_right(i, step)
            elif rotation == 'д':
                if language == 'ru':
                    new_message += ru_letter_left(i, step)
                elif language == 'en':
                    new_message += en_letter_left(i, step)
    else:
        new_message += message[i]
print(new_message)