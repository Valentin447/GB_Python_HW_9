'''
6) Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(word):
    return word.capitalize()


#string = input("Введите строку из слов разделенных пробелом "
#               "в нижнем регистре: ")

#res_string = ""
#for el in string.split(" "):
#   res_string += int_func(el) + " "

#print(res_string)
