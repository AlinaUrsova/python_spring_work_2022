#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
#prices = {
#  "banana": 4,
#  "apple": 2,
#  "orange": 1.5,
#  "pear": 3
#}

def compute_bill():

  bill = {
    "banana": int(input("Сколько бананов вы хотите купить?")),
    "apple": int(input("Сколько яблок вы хотите купить?")),
    "orange": int(input("Сколько апельсинов вы хотите купить?")),
    "pear": int(input("Сколько груш вы хотите купить?"))
  }

  prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
  }

  quantity = {k: bill[k]*prices[k] for k in bill}
  print("всего фруктов в чеке:", quantity)

  quantity_l = quantity.values()

  total_price = 0
  for i in quantity_l:
    total_price += i

  print("Итоговая сумма в чеке:", total_price)


compute_bill()
















