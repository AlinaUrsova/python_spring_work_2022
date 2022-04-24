#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
#"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.

file = open('algoritm.csv', 'w', encoding='utf-8')
algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]
id = 0
for i in algoritm:
    id = id + 1
    print(id, " ", i)

file.close()
