#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.


import random
questions_main = {
    "Это слово обозначает наименьшую автономную часть языка программирования": "оператор",
    "Последовательность команд алгоритма": "конструкция",
    "Это совокупность данных и методов работы с ними": "объект"
}
question_main = random.choice(list(questions_main.keys()))
answer_main = questions_main[question_main]

star_answer = []
for i in range(len(answer_main)):
    star_answer.append("*")
print("Вопрос:", question_main)
print("Количество букв в слове:", *star_answer)


print("Добро пожаловать на игру Поле чудес.Вам необходимо ответить на вопрос. У вас есть 10 попыток")


def round_():
    counter = 0
    while True:
        user = input("Ведите букву или слово: ")
        if user == answer_main:
            print("Вы правильно назвали слово!", answer_main)
            break
        if (user in answer_main):
            print("Такая буква есть!")
            for i in range(len(answer_main)):
                if answer_main[i] == user:
                    star_answer[i] = user
                    user_answer = "".join(star_answer)
                    print(user_answer)
        else:
            print("Такой буквы нет")
            counter = counter + 1
            if counter == 10:
                print("вы не угадали")
                break
        if user_answer == answer_main:
            print("Вы правильно назвали все буквы!правильное слово ", answer_main )
            break

round_()


