"""     Шифр Цезаря с циклическим сдвигом на длину этого слова     """


def code():
    ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' * 2
    en_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
    rotation = 'ш'
    language = 'en'
    message = str(input())
    new_message = []


    def ru_letter_right(letter, where):
        return ru_alphabet[ru_alphabet.find(j[letter].lower()) + where]


    def ru_letter_left(letter, where):
        return ru_alphabet[ru_alphabet.rfind(j[letter].lower()) - where]


    def en_letter_right(letter, where):
        return en_alphabet[en_alphabet.find(j[letter].lower()) + where]


    def en_letter_left(letter, where):
        return en_alphabet[en_alphabet.rfind(j[letter].lower()) - where]


    message = message.split(' ')
    for j in message:
        step = 0
        for k in j:
            if k.isalpha():
                step += 1
        for i in range(len(j)):
            if j[i].lower() in ru_alphabet or j[i].lower() in en_alphabet:
                if j[i].isupper():
                    if rotation == 'ш':
                        if language == 'ru':
                            new_message.append(ru_letter_right(i, step).upper())
                        elif language == 'en':
                            new_message.append(en_letter_right(i, step).upper())
                    elif rotation == 'д':
                        if language == 'ru':
                            new_message.append(ru_letter_left(i, step).upper())
                        elif language == 'en':
                            new_message.append(en_letter_left(i, step).upper())
                else:
                    if rotation == 'ш':
                        if language == 'ru':
                            new_message.append(ru_letter_right(i, step))
                        elif language == 'en':
                            new_message.append(en_letter_right(i, step))
                    elif rotation == 'д':
                        if language == 'ru':
                            new_message.append(ru_letter_left(i, step))
                        elif language == 'en':
                            new_message.append(en_letter_left(i, step))
            else:
                new_message.append(j[i])
        new_message.append(' ')
    return new_message[:-1]


print(*code(), sep='')
