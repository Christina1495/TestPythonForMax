mediasoft = dict(python = dict(framework = ('django', 'flask'), db = ('postgres', 'mysql'), experience = 5),
                 java = dict(framework = ('spring', 'spark'), db = ('oracle', 'mssql'), experience = 5))
fio = input("Введите ФИО: ").lower()
lang = input("Введите Язык программирования: ").lower()
if lang in mediasoft:
    framework = input("Введите Фреймворк: ").lower()
    if framework in mediasoft[lang].get('framework'):
        db = input("Введите СУБД: ").lower()
        if db in mediasoft[lang].get('db'):
            experience = input("Введите Опыт: ")
            if int(experience) >= 5:
                print("{0}, вы подходите на вакансию {1} в компанию Медиасофт".format(fio, lang))
            else:
                print("{0}, к сожалению вы не подходите на вакансию {1} в компанию Медиасофт".format(fio, lang))
        else:
            print("{0}, к сожалению вы не подходите на вакансию {1} в компанию Медиасофт".format(fio, lang))
    else:
        print("{0}, к сожалению вы не подходите на вакансию {1} в компанию Медиасофт".format(fio, lang))
else:
    print("{0}, к сожалению вы не подходите на вакансию {1} в компанию Медиасофт".format(fio, lang))







