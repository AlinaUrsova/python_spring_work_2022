import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Страна': ['Россия', 'Казахстан', 'Украина', 'Белоруссия', 'Узбекистан'],
    '2017 год': [1665, 179, 131, 60, 50],
    '2018 год': [1702, 182, 154, 63, 58],
})

print(df)


vet_csv = pd.read_csv("vetpet.csv")
print(vet_csv)

df.plot(kind='barh', y='2017 год', color='red')
plt.show()