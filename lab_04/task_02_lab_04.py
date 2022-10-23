# Определить, как часто встречается определенная буква в строке.
# TODO посчитать количество каждой буквы в строке в аргументе str_
slowar = {

}


def get_count_char(str_):
    # str_ = sorted(str_) если требуется сортировка
    str_ = "".join(c for c in str_ if c.isalpha()).lower()  # нижний регистр, зачистка
    for letter in str_:
        if letter not in slowar:
            slowar[letter] = 1  # внесение каждой буквы в словарь
        else:
            slowar[letter] += 1 # счетчик
    return slowar


def get_persent_char(dict_):
    counter = sum(dict_.values())  # количество всех букв
    for i in dict_:
        dict_[i] = round(dict_[i] * 100 / counter, 2)  # округление до 2 знаков
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
# print(get_persent_char(slowar))
