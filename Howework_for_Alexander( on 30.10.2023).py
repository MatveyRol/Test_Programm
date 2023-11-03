from translate import Translator

#Задача №1
"""
def dob():
    a = ""
    lang = input("Укажите язык перевода: русский или английский: ")
    if lang.lower() == "английский":
        print("Выбран режим перевода с английского")
        while a != "stop":
            a = input("Введите переводимое слово. Если хотите завершить, введите stop: ")
            n[a] = perevod.translate(a)
        del n["stop"]
        print(n)
    elif lang.lower() == "русский":
        print("Выбран режим перевода с русского")
        while a != "stop":
            a = input("Введите переводимое слово. Если хотите завершить, введите stop: ")
            n[a] = perevod1.translate(a)
        del n["stop"]
        print(n)
def ud():
    print(*n.keys(),sep="\n")
    n3 = input("Введите ключ, который нужно удалить: ")
    del n[n3]
    print(n)
n = {}
perevod = Translator(from_lang="en", to_lang="ru")
perevod1 = Translator(from_lang="ru", to_lang="en")
while True:
    op = input("Введите название операции: добавление или удаление ")
    if op.lower() == "добавление":
        dob()
    elif op.lower() == "удаление":
        ud()
"""

#Задача №2
"""
perevod = Translator(from_lang="ru", to_lang="en")
perevod1 = Translator(from_lang="ru", to_lang="hi")
perevod2 = Translator(from_lang="ru", to_lang="el")
perevod3 = Translator(from_lang="ru", to_lang="de")
perevod4 = Translator(from_lang="ru", to_lang="fr")
def perevodchik(a):
    return"На английском: ",perevod.translate(a),"На языке хинди: ",perevod1.translate(a),"На греческом: ",perevod2.translate(a),"На немецком: ",perevod3.translate(a),"На французском: ",perevod4.translate(a)
n = input()
print(*perevodchik(n), sep="\n")
"""